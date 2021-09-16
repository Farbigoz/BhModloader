import os
import sys
import time
import py7zr
import urllib
import rarfile
import zipfile
import threading
import webbrowser
import subprocess
import multiprocessing

# (https://stackoverflow.com/questions/9144724/unknown-encoding-idna-in-python-requests)
import encodings.idna

import core
from core import NotificationType, Environment

from PySide6.QtCore import QSize, QTranslator, QLocale, QTimer, Signal
from PySide6.QtGui import QIcon, QFontDatabase
from PySide6.QtWidgets import QMainWindow, QApplication

from ui.ui_handler.window import Window
from ui.ui_handler.header import HeaderFrame
from ui.ui_handler.loading import Loading
from ui.ui_handler.mods import Mods
from ui.ui_handler.progressdialog import ProgressDialog
from ui.ui_handler.buttonsdialog import ButtonsDialog
from ui.ui_handler.acceptdialog import AcceptDialog

from ui.utils.layout import ClearFrame, AddToFrame
from ui.utils.version import GetLatest, GITHUB, REPO
from ui.utils.textformater import TextFormatter

import ui.ui_sources.translate as translate


def InitWindowSetText(text):
    if getattr(sys, "frozen", False):
        try:
            import pyi_splash
            pyi_splash.update_text(text)
        except:
            pass


def InitWindowClose():
    if getattr(sys, "frozen", False):
        try:
            import pyi_splash
            pyi_splash.update_text("application")
            pyi_splash.close()
        except:
            pass


class Queue:
    def __init__(self):
        self.urlQueue = []
        self.signalUrl = None
        self._readUrlQueue = False

        self.fileQueue = []
        self.signalFile = None
        self._readFileQueue = False

    def setUrlSignal(self, signalUrl):
        self.signalUrl = signalUrl

    def _emitUrl(self):
        while True:
            try:
                if self.signalUrl is None:
                    time.sleep(0.1)
                else:
                    self.signalUrl.emit()
                    break
            except:
                time.sleep(0.1)

    def addUrl(self, url):
        self.urlQueue.append(url)

        if not self._readUrlQueue:
            threading.Thread(target=self._emitUrl).start()

    def iterUrl(self):
        self._readUrlQueue = True

        while self.urlQueue:
            yield self.urlQueue.pop(0)

        self._readUrlQueue = False

    def setFileSignal(self, signalFile):
        self.signalFile = signalFile

    def _emitFile(self):
        while True:
            try:
                if self.signalFile is None:
                    time.sleep(0.1)
                else:
                    self.signalFile.emit()
                    break
            except:
                time.sleep(0.1)

    def addFile(self, file):
        self.fileQueue.append(file)

        if not self._readFileQueue:
            threading.Thread(target=self._emitFile).start()

    def iterFile(self):
        self._readFileQueue = True

        while self.fileQueue:
            yield self.fileQueue.pop(0)

        self._readFileQueue = False


class ModLoader(QMainWindow):
    importQueue = Queue()

    modsPath = os.path.join(os.getcwd(), "Mods")

    def __init__(self):
        super().__init__()
        self.ui = Window()
        self.ui.setupUi(self)

        self.setWindowTitle("Brawlhalla ModLoader")
        self.setWindowIcon(QIcon(':/icons/resources/icons/App.ico'))

        InitWindowSetText("core libs")
        self.controller = core.Controller()
        self.controller.setModsPath(self.modsPath)
        self.controller.reloadMods()
        self.controller.getModsData()
        InitWindowClose()

        self.loading = Loading()
        self.header = HeaderFrame(githubMethod=lambda: webbrowser.open(f"{GITHUB}/{REPO}"))
        self.mods = Mods(installMethod=self.installMod,
                         uninstallMethod=self.uninstallMod,
                         reinstallMethod=self.reinstallMod,
                         deleteMethod=self.deleteMod,
                         reloadMethod=self.reloadMods,
                         openFolderMethod=self.openModsFolder)
        self.progressDialog = ProgressDialog(self)
        self.buttonsDialog = ButtonsDialog(self)
        self.acceptDialog = AcceptDialog(self)

        self.setLoadingScreen()

        self.controllerGetterTimer = QTimer()
        self.controllerGetterTimer.timeout.connect(self.controllerGet)  # connect it to your update function
        self.controllerGetterTimer.start(10)

        # self.resize(QSize(977, 550))
        self.setMinimumSize(QSize(850, 550))

        self.versionSignal.connect(self.newVersion)
        threading.Thread(target=self.checkNewVersion).start()

        self.queueUrlSignal.connect(self.queueUrl)
        self.queueFileSignal.connect(self.queueFile)

        self.importQueue.setUrlSignal(self.queueUrlSignal)
        self.importQueue.setFileSignal(self.queueFileSignal)

        self.setForeground()

    def controllerGet(self):
        data = self.controller.getData()
        if data is None:
            return

        cmd = data[0]

        if cmd == Environment.Notification:
            notification: core.notifications.Notification = data[1]
            ntype = notification.notificationType

            if ntype == NotificationType.LoadingMod:
                modPath = notification.args[0]
                self.loading.setText(f"Loading mod '{modPath}'")

            elif ntype == NotificationType.ModElementsCount:
                modHash, count = notification.args
                self.progressDialog.setMaximum(count)

            # Check conflicts
            elif ntype == NotificationType.ModConflictSearchInSwf:
                modHash, swfName = notification.args
                self.progressDialog.setContent(f"Searching in: {swfName}")
                self.progressDialog.addValue()
            elif ntype == NotificationType.ModConflictNotFound:
                modHash, = notification.args
                self.progressDialog.setValue(0)
                self.controller.installMod(modHash)
            elif ntype == NotificationType.ModConflict:
                modHash, modConflictHashes = notification.args
                self.acceptDialog.setTitle("Conflict mods!")
                content = "Mods:"

                for modConflictHash in modConflictHashes:
                    if modConflictHash in self.mods.mods:
                        mod = self.mods.mods[modConflictHash]
                        content += f"\n- {mod.name}"

                    else:
                        content += f"\n- UNKNOWN MOD: {modConflictHash}"
                        print("ERROR Один из установленных модов не найден в модлодере!")

                self.acceptDialog.setContent(content)
                self.acceptDialog.setAccept(lambda: [self.acceptDialog.hide(), self.controller.installMod(modHash)])
                self.acceptDialog.setCancel(self.acceptDialog.hide)

                self.progressDialog.hide()
                self.acceptDialog.show()


            # Installing
            elif ntype == NotificationType.InstallingModSwf:
                modHash, swfName = notification.args
                self.progressDialog.setContent(f"Open game file: {swfName}")
            elif ntype == NotificationType.InstallingModSwfSprite:
                modHash, sprite = notification.args
                self.progressDialog.setContent(f"Installing sprite: {sprite}")
                self.progressDialog.addValue()
            elif ntype == NotificationType.InstallingModSwfSound:
                modHash, sound = notification.args
                self.progressDialog.setContent(f"Installing sound: {sound}")
                self.progressDialog.addValue()
            elif ntype == NotificationType.InstallingModFile:
                modHash, fileName = notification.args
                self.progressDialog.setContent(f"Installing file: {fileName}")
                self.progressDialog.addValue()
            elif ntype == NotificationType.InstallingModFileCache:
                modHash, fileName = notification.args
                self.progressDialog.setContent(fileName)
                self.progressDialog.addValue()
            elif ntype == NotificationType.InstallingModFinished:
                modHash = notification.args[0]
                modClass = self.mods.mods[modHash]
                modClass.installed = True
                self.mods.updateData()
                self.mods.selectedModButton.updateData()
                self.progressDialog.hide()

            # Uninstalling
            elif ntype == NotificationType.UninstallingModSwf:
                modHash, swfName = notification.args
                self.progressDialog.setContent(swfName)
            elif ntype == NotificationType.UninstallingModSwfSprite:
                modHash, sprite = notification.args
                self.progressDialog.setContent(sprite)
                self.progressDialog.addValue()
            elif ntype == NotificationType.UninstallingModSwfSound:
                modHash, sprite = notification.args
                self.progressDialog.setContent(sprite)
                self.progressDialog.addValue()
            elif ntype == NotificationType.UninstallingModFile:
                modHash, fileName = notification.args
                self.progressDialog.setContent(fileName)
                self.progressDialog.addValue()
            elif ntype == NotificationType.UninstallingModFinished:
                modHash = notification.args[0]
                modClass = self.mods.mods[modHash]
                modClass.installed = False
                self.mods.updateData()
                self.mods.selectedModButton.updateData()

                self.progressDialog.hide()

        elif cmd == Environment.ReloadMods:
            self.mods.removeAllMods()

        elif cmd == Environment.GetModsData:
            for modData in data[1]:
                self.mods.addMod(gameVersion=modData.get("gameVersion", ""),
                                 name=modData.get("name", ""),
                                 author=modData.get("author", ""),
                                 version=modData.get("version", ""),
                                 description=modData.get("description", ""),
                                 tags=modData.get("tags", []),
                                 previewsPaths=modData.get("previewsPaths", []),
                                 hash=modData.get("hash", ""),
                                 platform=modData.get("platform", ""),
                                 installed=modData.get("installed", False),
                                 currentVersion=modData.get("currentVersion", False),
                                 modFileExist=modData.get("modFileExist", False))

            self.setModsScreen()

        elif cmd == Environment.GetModConflict:
            searching, modHash = data[1]
            if searching:
                modClass = self.mods.mods[modHash]
                self.progressDialog.setTitle(f"Searching conflicts '{modClass.name}'...")
                self.progressDialog.setContent("Searching...")
                self.progressDialog.show()

        elif cmd == Environment.InstallMod:
            installing, modHash = data[1]
            if installing:
                modClass = self.mods.mods[modHash]
                self.progressDialog.setTitle(f"Installing mod '{modClass.name}'...")
                self.progressDialog.setContent("Loading mod...")
                self.progressDialog.show()

        elif data[0] == Environment.UninstallMod:
            uninstalling, modHash = data[1]
            if uninstalling:
                modClass = self.mods.mods[modHash]
                self.progressDialog.setTitle(f"Uninstalling mod '{modClass.name}'...")
                self.progressDialog.setContent("")
                self.progressDialog.show()

        else:
            print(f"Controller <- {str(data)}\n", end="")

    def setLoadingScreen(self):
        ClearFrame(self.ui.mainFrame)
        AddToFrame(self.ui.mainFrame, self.loading)
        self.loading.setText("Loading mods sources...")

    def setModsScreen(self):
        ClearFrame(self.ui.mainFrame)

        AddToFrame(self.ui.mainFrame, self.header)
        AddToFrame(self.ui.mainFrame, self.mods)

    def installMod(self):
        if self.mods.selectedModButton is not None:
            modClass = self.mods.selectedModButton.modClass
            self.controller.getModConflict(modClass.hash)

    def uninstallMod(self):
        if self.mods.selectedModButton is not None:
            modClass = self.mods.selectedModButton.modClass
            self.controller.uninstallMod(modClass.hash)

    def reinstallMod(self):
        if self.mods.selectedModButton is not None:
            modClass = self.mods.selectedModButton.modClass
            self.controller.uninstallMod(modClass.hash)
            self.controller.getModConflict(modClass.hash)

    def deleteMod(self):
        if self.mods.selectedModButton is not None:
            modClass = self.mods.selectedModButton.modClass

            self.buttonsDialog.deleteButtons()
            self.buttonsDialog.setTitle(f"Delete mod '{modClass.name}'")

            if modClass.installed:
                self.buttonsDialog.setContent("To delete mod, you need to uninstall it")
            else:
                self.buttonsDialog.setContent("")
                self.buttonsDialog.addButton("Delete", self._deleteMod)

            self.buttonsDialog.addButton("Cancel", self.buttonsDialog.hide)

            self.buttonsDialog.show()

    def reloadMods(self):
        self.setLoadingScreen()
        #self.mods.removeAllMods()
        self.controller.reloadMods()
        self.controller.getModsData()

    def openModsFolder(self):
        os.startfile(self.modsPath)

    def _deleteMod(self):
        modClass = self.mods.selectedModButton.modClass
        modClass.modFileExist = False
        self.controller.deleteMod(modClass.hash)
        self.reloadMods()
        self.buttonsDialog.hide()

    def resizeEvent(self, event):
        self.progressDialog.onResize()
        self.acceptDialog.onResize()
        self.buttonsDialog.onResize()
        super().resizeEvent(event)

    versionSignal = Signal(str, str, str, str)

    def newVersion(self, url: str, fileUrl: str, version: str, body: str):
        self.buttonsDialog.setTitle(f"New version available '{version}'")
        self.buttonsDialog.setContent(TextFormatter.format(body))
        self.buttonsDialog.deleteButtons()
        self.buttonsDialog.addButton("GO TO SITE", lambda: webbrowser.open(url))
        self.buttonsDialog.addButton("UPDATE", lambda: [self.buttonsDialog.hide(),
                                                        self.updateApp(fileUrl, version)])
        self.buttonsDialog.addButton("CANCEL", self.buttonsDialog.hide)
        self.buttonsDialog.show()

    def handleUpdateApp(self, blocknum, blocksize, totalsize):
        readedData = blocknum * blocksize

        if totalsize > 0:
            downloadPercentage = int(readedData * 100 / totalsize)
            self.progressDialog.setValue(downloadPercentage)
            QApplication.processEvents()

    def updateApp(self, fileUrl: str, version: str):
        filePath = os.path.join(os.getcwd(), "temp.exe")
        fileName = os.path.split(fileUrl)[1]

        self.progressDialog.setMaximum(100)
        self.progressDialog.setTitle(f"Update ModLoader to '{version}'")
        self.progressDialog.setContent(f"Download '{fileName}'")
        self.progressDialog.show()
        urllib.request.urlretrieve(fileUrl, filePath, self.handleUpdateApp)
        self.progressDialog.hide()

        subprocess.Popen([os.environ["CLIENT_PATH"], "-update",
                         os.path.abspath(sys.argv[0]),
                         filePath])
        QApplication.exit(0)

    def checkNewVersion(self):
        latest = GetLatest()

        if latest is not None:
            newVersion, fileUrl, version, body = latest
            self.versionSignal.emit(newVersion, fileUrl, version, body)

    def setForeground(self):
        if sys.platform.startswith("win"):
            import win32gui, win32com.client

            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(self.winId())

    queueFileSignal = Signal()

    def queueFile(self):
        for file in self.importQueue.iterFile():
            self.fileImport(file)

    def fileImport(self, filePath: str):
        self.setForeground()

        if os.path.abspath(filePath).startswith(os.path.abspath(self.modsPath)):
            return

        fileName = os.path.split(filePath)[1]
        fileNameSplit = os.path.splitext(fileName)

        if os.path.exists(os.path.join(self.modsPath, fileName)):
            i = 1
            while os.path.exists(os.path.join(self.modsPath, f"{fileNameSplit[0]} ({i}){fileNameSplit[1]}")):
                i += 1
            fileName = f"{fileNameSplit[0]} ({i}){fileNameSplit[1]}"

        with open(filePath, "rb") as outsideMod:
            with open(os.path.join(self.modsPath, fileName), "wb") as insideMod:
                insideMod.write(outsideMod.read())

        self.reloadMods()

    queueUrlSignal = Signal()

    def queueUrl(self):
        for url in self.importQueue.iterUrl():
            self.urlImport(url)

    def urlImport(self, url: str):
        self.setForeground()

        data = url.split(":", 1)[1].strip("/")
        splitData = data.split(",")

        if len(splitData) == 3:
            tag, modId, dlId = data.split(",")
            zipUrl = f"http://gamebanana.com/dl/{dlId}"
        else:
            zipUrl = ""
            return

        archivePath = os.path.join(self.modsPath, "_mod.archive")

        self.progressDialog.setMaximum(100)
        self.progressDialog.setTitle("Download mod")
        self.progressDialog.setContent("")
        self.progressDialog.show()
        QApplication.processEvents()
        try:
            urllib.request.urlretrieve(zipUrl, archivePath, self.handleUpdateApp)

            with open(archivePath, "rb") as file:
                _signature = file.read(3)

            if _signature.startswith(b"7z"):
                with py7zr.SevenZipFile(archivePath) as mod7z:
                    for file in mod7z.getnames():
                        if file.endswith(f".{core.MOD_FILE_FORMAT}"):
                            self.progressDialog.setContent(f"Extract: '{file}'")
                            QApplication.processEvents()
                            mod7z.extract(self.modsPath, [file])

            elif _signature.startswith(b"Rar"):
                with rarfile.RarFile(archivePath) as modRar:
                    for file in modRar.namelist():
                        if file.endswith(f".{core.MOD_FILE_FORMAT}"):
                            self.progressDialog.setContent(f"Extract: '{file}'")
                            QApplication.processEvents()
                            modRar.extract(file, self.modsPath)

            elif _signature.startswith(b"PK"):
                with zipfile.ZipFile(archivePath) as modZip:
                    for file in modZip.namelist():
                        if file.endswith(f".{core.MOD_FILE_FORMAT}"):
                            self.progressDialog.setContent(f"Extract: '{file}'")
                            QApplication.processEvents()
                            modZip.extract(file, self.modsPath)

            os.remove(archivePath)

            self.reloadMods()
        except Exception as e:
            print("Error unpack mod zip\n", e)

        finally:
            self.progressDialog.hide()

        print("Url:", url)

        #bmod://Mod,321718,658341


# pyrcc5 -o ui/ui_sources/icons_rc.py ui/ui_sources/icons.qrc
# venv\Lib\site-packages\PySide6\lupdate.exe @ui/ui_sources/ui_files.txt -ts ui/ui_sources/translate/header/ru_RU.ts
# venv\Lib\site-packages\PySide6\lupdate.exe ui/ui_sources/header.ui -locations ui/ui_sources/translate/header
# venv\Lib\site-packages\PySide6\lrelease.exe E:\BrawlhallaModloaderApp_0.3\ui\ui_sources\translate\header\ru_RU.ts


def RunApp(mlserver=None):
    app = QApplication(sys.argv)

    font_db = QFontDatabase()
    font_db.addApplicationFont(":/fonts/resources/fonts/Exo 2/Exo2-SemiBold.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-Black.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-BlackItalic.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-Bold.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-BoldItalic.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-Italic.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-Medium.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-MediumItalic.ttf")
    font_db.addApplicationFont(":/fonts/resources/fonts/Roboto/Roboto-Regular.ttf")

    """
    translator = QTranslator()
    lang = QLocale.system().name()
    supportedLangs = translate.GetLangs()
    if lang in supportedLangs:
        translator.load(supportedLangs[lang])
    app.installTranslator(translator)
    """

    window = ModLoader()
    window.show()
    os.kill(multiprocessing.current_process().pid, app.exec())
    if mlserver is not None:
        mlserver.close()


if __name__ == "__main__":
    RunApp()
