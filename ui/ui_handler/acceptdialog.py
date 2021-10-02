from PySide6.QtWidgets import QWidget
from ..ui_sources.ui_accept_dialog import Ui_AcceptDialog


class AcceptDialog(QWidget):
    def __init__(self, window):
        super().__init__()

        self.ui = Ui_AcceptDialog()
        self.ui.setupUi(self)

        self.mainWindow = window

        self.acceptMethod = lambda: None
        self.cancelMethod = lambda: None

        self.ui.accept.clicked.connect(self.clickAccept)
        self.ui.cancel.clicked.connect(self.clickCancel)

    def clickAccept(self):
        self.acceptMethod()

    def clickCancel(self):
        self.cancelMethod()

    def onResize(self):
        self.setGeometry(0, 0, self.mainWindow.width(), self.mainWindow.height())

    def isShown(self):
        return self.parent() is not None

    def show(self):
        if self.parent() is None:
            self.setParent(self.mainWindow)
            self.parent().layout().addWidget(self)
            self.onResize()

    def hide(self):
        if self.parent() is not None:
            self.parent().layout().removeWidget(self)
            self.setParent(None)

    def removeContent(self):
        self.ui.content.setParent(None)

    def addContent(self):
        self.ui.content.setParent(self.ui.dialogBackground)

    def setContent(self, content: str):
        if self.ui.content.parent() is None:
            self.addContent()

        self.ui.content.setText(content)

    def setTitle(self, title: str):
        self.ui.title.setText(title)

    def setAccept(self, method):
        self.acceptMethod = method

    def setCancel(self, method):
        self.cancelMethod = method
