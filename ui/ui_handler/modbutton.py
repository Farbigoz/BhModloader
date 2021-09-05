import re

from PySide6.QtWidgets import QWidget, QScrollArea
from PySide6.QtGui import QFontMetrics, Qt, QPixmap
from PySide6.QtCore import QEvent

from .modclass import ModClass

from ..ui_sources.ui_mod_button import Ui_ModButton


class ModButton(QWidget):
    buttons = []

    def __init__(self, modClass: ModClass, method):
        self.pressed = False
        self.modClass = modClass
        self.method = method

        super().__init__()

        self.ui = Ui_ModButton()
        self.ui.setupUi(self)

        self.updateData()

        self.ui.background.installEventFilter(self)

        #if not self.buttons:
        #    self.select()

        self.buttons.append(self)

    def updateData(self):
        self.ui.modName.setText(self.modClass.name)
        self.ui.gameVersion.setText(f"[{self.modClass.gameVersion}]")
        self.ui.modAuthor.setText("Author: " + self.modClass.author)
        if self.modClass.currentVersion:
            gameVersionColor = "#43C15F"
        else:
            gameVersionColor = "#3FAED1"
        self.ui.gameVersion.setStyleSheet(f"color: {gameVersionColor}")

        if self.modClass.installed and self.modClass.modFileExist:
            self.ui.modState.setPixmap(QPixmap(u":/icons/resources/icons/Installed.png"))
        elif self.modClass.installed:
            self.ui.modState.setPixmap(QPixmap(u":/icons/resources/icons/GhostInstalled.png"))
        else:
            self.ui.modState.setPixmap(QPixmap(u":/icons/resources/icons/NotInstalled.png"))

    def onParentResize(self):
        parent = self
        while True:
            parent = parent.parent()
            if type(parent) == QScrollArea:
                break

            if parent is None:
                return False

        metrics = QFontMetrics(self.ui.modName.font())
        elided = metrics.elidedText(self.modClass.name, Qt.ElideRight, parent.width() - 100)
        self.ui.modName.setText(elided)
        self.ui.modName.setMaximumWidth(parent.width() - 100)

    def select(self):
        if self.pressed:
            pass
        else:
            for b in self.buttons:
                if b.pressed:
                    b.pressed = False
                    ss = b.ui.background.styleSheet()
                    bgColor = re.findall(r"background-color: #FF(.+);", ss)[0]
                    b.ui.background.setStyleSheet(
                        ss.replace(f"#FF{bgColor}", f"#00{bgColor}").replace(f"#FE{bgColor}", f"#77{bgColor}"))

            self.pressed = True
            ss = self.ui.background.styleSheet()
            bgColor = re.findall(r"background-color: #00(.+);", ss)[0]
            self.ui.background.setStyleSheet(
                ss.replace(f"#00{bgColor}", f"#FF{bgColor}").replace(f"#77{bgColor}", f"#FE{bgColor}"))

            self.method(self.modClass)

    def remove(self):
        self.layout().removeWidget(self)
        self.setParent(None)

    def eventFilter(self, qobject: QWidget, event):
        if event.type() == QEvent.MouseButtonPress:
            self.select()

        return False
