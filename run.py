import os
import sys
import core
import json
import socket
import hashlib
import traceback
import threading
import multiprocessing

from client import Arguments, Commands, CONFIG_FILE, CONFIG, SOCKET_PORT, MODLOADER_CLIENT

from ui.utils.systemdialog import Error


FROZEN = getattr(sys, 'frozen', False)

MOD_FILE_FORMAT = core.MOD_FILE_FORMAT
FILE_DESCRIPTION = "Brawlhalla Mod"
FILE_ICON = "file_icon.ico"


os.environ["CLIENT_PATH"] = os.path.join(core.MODLOADER_CACHE_PATH, MODLOADER_CLIENT)
os.environ["FILE_ICON"] = os.path.join(core.MODLOADER_CACHE_PATH, FILE_ICON)


def _bootstrap(self, parent_sentinel=None):
    import itertools
    from multiprocessing.process import _ParentProcess
    from multiprocessing import util, context
    global _current_process, _parent_process, _process_counter, _children

    try:
        if self._start_method is not None:
            context._force_start_method(self._start_method)
        _process_counter = itertools.count(1)
        _children = set()
        util._close_stdin()
        old_process = multiprocessing.current_process()
        _current_process = self
        _parent_process = _ParentProcess(
            self._parent_name, self._parent_pid, parent_sentinel)
        if threading._HAVE_THREAD_NATIVE_ID:
            threading.main_thread()._set_native_id()
        try:
            util._finalizer_registry.clear()
            util._run_after_forkers()
        finally:
            # delay finalization of the old process object until after
            # _run_after_forkers() is executed
            del old_process
        util.info('child process calling self.run()')
        try:
            self.run()
            exitcode = 0
        finally:
            util._exit_function()
    except SystemExit as e:
        if not e.args:
            exitcode = 1
        elif isinstance(e.args[0], int):
            exitcode = e.args[0]
        else:
            sys.stderr.write(str(e.args[0]) + '\n')
            exitcode = 1
    except:
        exitcode = 1
        sys.excepthook(*sys.exc_info())
    finally:
        threading._shutdown()
        util.info('process exiting with exitcode %d' % exitcode)
        util._flush_std_streams()

    return exitcode


multiprocessing.Process._bootstrap = _bootstrap


def handle_exception(exc_type, exc_value, exc_traceback):
    try:
        import pyi_splash
        pyi_splash.close()
    except:
        pass

    callError = lambda: sys.__excepthook__(exc_type, exc_value, exc_traceback)
    errorText = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    from main import ModLoader, PRODUCT
    if ModLoader.app is not None:
        ModLoader.app.showError("Fatal Error:", errorText, lambda: [callError(), terminateApp()])
    else:
        Error(PRODUCT, errorText)
        callError()


sys.excepthook = handle_exception
threading.excepthook = lambda hook: handle_exception(hook.exc_type, hook.exc_value, hook.exc_traceback)


def terminateApp():
    if mlserver is not None:
        mlserver.close()
    for proc in multiprocessing.active_children():
        proc.kill()
    os.kill(multiprocessing.current_process().pid, 0)
    sys.exit(0)


def GetLocalPath():
    if FROZEN:
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return base_path


def InstallClient():
    configPath = os.path.join(core.MODLOADER_CACHE_PATH, CONFIG_FILE)
    if os.path.exists(configPath):
        with open(configPath, "r") as file:
            config = json.loads(file.read())
    else:
        config = CONFIG

    clientPath = os.path.join(core.MODLOADER_CACHE_PATH, MODLOADER_CLIENT)

    if FROZEN:
        origClientPath = os.path.join(GetLocalPath(), MODLOADER_CLIENT)
    else:
        origClientPath = os.path.join("dist", MODLOADER_CLIENT)

    with open(origClientPath, "rb") as file:
        originalClientContent = file.read()
        clientHash = hashlib.sha256(originalClientContent).hexdigest()

    if config["clientHash"] != clientHash:
        with open(clientPath, "wb") as file:
            file.write(originalClientContent)

    config["clientHash"] = clientHash
    if FROZEN and sys.argv[0] != config["modLoaderPath"]:
        config["modLoaderPath"] = sys.argv[0]
    with open(configPath, "w") as file:
        file.write(json.dumps(config))

    iconPath = os.path.join(core.MODLOADER_CACHE_PATH, FILE_ICON)
    if not os.path.exists(iconPath):
        with open(iconPath, "wb") as icon:
            with open(os.path.join(GetLocalPath(), FILE_ICON), "rb") as file:
                icon.write(file.read())


def RunAsAdmin():
    import win32com.shell.shell

    if sys.argv[0].endswith(".exe"):
        argv = sys.argv[1:]
    else:
        argv = sys.argv

    params = ' '.join([*argv, Arguments.AS_ADMIN])
    win32com.shell.shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)


# File association
def CheckFileRegistry():
    import winreg
    try:
        _format = f"file{MOD_FILE_FORMAT}"
        fileformat = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f".{MOD_FILE_FORMAT}")
        shell_open_command = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f"{_format}\shell\open\command")
        if (
                winreg.QueryValueEx(fileformat, None)[0] != _format
                or
                winreg.QueryValueEx(shell_open_command, None)[0] !=
                f"{os.path.join(core.MODLOADER_CACHE_PATH, MODLOADER_CLIENT)} {Arguments.FILE} \"%1\""
        ):
            winreg.CloseKey(shell_open_command)
            winreg.CloseKey(fileformat)
            return False

        winreg.CloseKey(shell_open_command)
        winreg.CloseKey(fileformat)
        return True
    except FileNotFoundError:
        return False


def InstallFileRegistry():
    import winreg
    _format = f"file{MOD_FILE_FORMAT}"
    fileformat = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f".{MOD_FILE_FORMAT}")
    winreg.SetValueEx(fileformat, None, 0, winreg.REG_SZ, _format)

    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, _format)

    main = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, _format, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(main, None, 0, winreg.REG_SZ, FILE_DESCRIPTION)

    default_icon = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{_format}\DefaultIcon")
    winreg.SetValueEx(default_icon, None, 0, winreg.REG_EXPAND_SZ,
                      f'"{os.environ["FILE_ICON"]}",0')

    shell = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{_format}\shell")
    shell_open = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{_format}\shell\open")
    shell_open_command = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{_format}\shell\open\command")
    winreg.SetValueEx(shell_open_command, None, 0, winreg.REG_SZ,
                      f"{os.path.join(core.MODLOADER_CACHE_PATH, MODLOADER_CLIENT)} {Arguments.FILE} \"%1\"")

    winreg.CloseKey(fileformat)
    winreg.CloseKey(main)
    winreg.CloseKey(default_icon)
    winreg.CloseKey(shell)
    winreg.CloseKey(shell_open)
    winreg.CloseKey(shell_open_command)


# Url association
def CheckUrlRegistry():
    import winreg
    try:
        shell_open_command = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f"{MOD_FILE_FORMAT}\shell\open\command")

        if winreg.QueryValueEx(shell_open_command, None)[0] != \
                f"{os.path.join(core.MODLOADER_CACHE_PATH, MODLOADER_CLIENT)} {Arguments.URL} \"%1\"":
            winreg.CloseKey(shell_open_command)
            return False

        winreg.CloseKey(shell_open_command)
        return True
    except FileNotFoundError:
        return False


def InstallUrlRegistry():
    import winreg
    winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, MOD_FILE_FORMAT)

    main = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, MOD_FILE_FORMAT, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(main, None, 0, winreg.REG_SZ, f"URL:{MOD_FILE_FORMAT} Protocol")
    winreg.SetValueEx(main, "URL Protocol", 0, winreg.REG_SZ, "")

    default_icon = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{MOD_FILE_FORMAT}\DefaultIcon")
    winreg.SetValueEx(default_icon, None, 0, winreg.REG_SZ, f'"{os.environ["FILE_ICON"]}",0')

    shell = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{MOD_FILE_FORMAT}\shell")
    shell_open = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{MOD_FILE_FORMAT}\shell\open")
    shell_open_command = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, f"{MOD_FILE_FORMAT}\shell\open\command")
    winreg.SetValueEx(shell_open_command, None, 0, winreg.REG_SZ,
                      f"{os.path.join(core.MODLOADER_CACHE_PATH, MODLOADER_CLIENT)} {Arguments.URL} \"%1\"")

    winreg.CloseKey(main)
    winreg.CloseKey(default_icon)
    winreg.CloseKey(shell)
    winreg.CloseKey(shell_open)
    winreg.CloseKey(shell_open_command)


# Server for ModloaderClient.exe
def MLServer(mlserver: socket, app):
    def handle(_mlclient: socket, app):
        data = _mlclient.recv(3)
        command = data[:1]
        size = int.from_bytes(data[1:], "big")
        if command == Commands.NONE:
            pass
        elif command == Commands.JUST_OPEN:
            app.setForeground()
        elif command == Commands.OPEN_FILE:
            file = _mlclient.recv(size).decode("UTF-8")
            if file.endswith(MOD_FILE_FORMAT):
                print(file)
                app.importQueue.addFile(file)
        elif command == Commands.OPEN_URL:
            url = _mlclient.recv(size).decode("UTF-8")
            app.importQueue.addUrl(url)
        _mlclient.send(b"\x01")
        _mlclient.close()

    while True:
        try:
            mlclient, _ = mlserver.accept()
            threading.Thread(target=handle, args=(mlclient, app)).start()
        except OSError:
            break


if __name__ == "__main__" and "--multiprocessing-fork" not in sys.argv:
    os.chdir(os.path.split(sys.argv[0])[0])

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(Arguments.AS_ADMIN, dest='asadmin', action='store_const', const=True, default=False)
    args = parser.parse_args()

    if sys.platform.startswith("win"):
        InstallClient()
        fileRegistered = CheckFileRegistry()
        urlRegistered = CheckUrlRegistry()

        if not fileRegistered or not urlRegistered:
            if args.asadmin:
                if not fileRegistered:
                    InstallFileRegistry()

                if not urlRegistered:
                    InstallUrlRegistry()

            elif FROZEN:
                RunAsAdmin()
    try:
        mlclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mlclient.settimeout(0.1)
        mlclient.connect(("127.0.0.1", SOCKET_PORT))
        dataSize = 0
        mlclient.send(Commands.JUST_OPEN + dataSize.to_bytes(2, byteorder='big'))
        mlclient.close()
    except (ConnectionRefusedError, socket.timeout):
        mlclient.close()

        mlserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mlserver.bind(('', SOCKET_PORT))
        mlserver.listen(5)
        from main import ModLoader, RunApp
        threading.Thread(target=MLServer, args=(mlserver, ModLoader)).start()
        RunApp(mlserver)

elif "--multiprocessing-fork" in sys.argv:
    from main import RunApp
    RunApp()
