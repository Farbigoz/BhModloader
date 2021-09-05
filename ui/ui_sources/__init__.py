import os

# Fix pyside designer
path = os.path.dirname(__file__)
for file in os.listdir(path):
    if file.endswith(".py"):
        filePath = os.path.join(path, file)
        with open(filePath, "r") as fileIO:
            content = fileIO.read()

        content = content.replace("import icons_rc\n", "")
        content = content.replace("from PyQt5 import QtCore\n", "from PySide6 import QtCore\n")
        #content = content.replace('"\n"', "")

        with open(filePath, "w") as fileIO:
            fileIO.write(content)

        del filePath
        del content
    del file
del path

from .icons_rc import *

from .ui_window import Ui_Window
from .ui_header import Ui_Header
from .ui_loading import Ui_Loading
from .ui_mods import Ui_Mods
from .ui_mods_actions import Ui_ModsActions
