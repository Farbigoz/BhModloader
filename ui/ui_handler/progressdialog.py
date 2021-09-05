from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPaintEvent

from ..ui_sources.ui_progress_dialog import Ui_ProgressDialog


class ProgressDialog(QWidget):
    def __init__(self, window):
        super().__init__()

        self.ui = Ui_ProgressDialog()
        self.ui.setupUi(self)

        self.mainWindow = window

    def onResize(self):
        self.setGeometry(0, 0, self.mainWindow.width(), self.mainWindow.height())

    def show(self):
        if self.parent() is None:
            self.setParent(self.mainWindow)
            self.parent().layout().addWidget(self)
            self.onResize()

    def hide(self):
        if self.parent() is not None:
            self.parent().layout().removeWidget(self)
            self.setParent(None)
            self.setValue(self.ui.progressBar.minimum())

    def removeContent(self):
        self.ui.content.setParent(None)

    def addContent(self):
        self.ui.content.setParent(self.ui.dialogBackground)

    def setMinimum(self, value: int):
        self.ui.progressBar.setMinimum(value)

    def setMaximum(self, value: int):
        self.ui.progressBar.setMaximum(value)

    def setValue(self, value: int):
        self.ui.progressBar.setValue(value)

    def addValue(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

    def setTitle(self, title: str):
        self.ui.title.setText(title)

    def setContent(self, content: str):
        if self.ui.content.parent() is None:
            self.addContent()

        self.ui.content.setText(content)
