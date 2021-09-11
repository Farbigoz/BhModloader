from typing import List, Tuple, Callable

from PySide6.QtGui import QFont, QCursor, Qt
from PySide6.QtWidgets import QWidget, QPushButton
from ..ui_sources.ui_buttons_dialog import Ui_ButtonsDialog


class ButtonsDialog(QWidget):
    font = QFont()
    font.setFamilies([u"Roboto Medium"])
    font.setPointSize(10)
    font.setBold(False)


    def __init__(self, window):
        super().__init__()

        self.ui = Ui_ButtonsDialog()
        self.ui.setupUi(self)

        self.mainWindow = window

        #self.buttons: List[Tuple[str, Callable]] = []
        self.buttons: List[QPushButton] = []

    def deleteButtons(self):
        for button in self.buttons:
            self.ui.buttons.layout().removeWidget(button)
            button.setParent(None)
            button.deleteLater()
            del button

        self.buttons.clear()

    def addButton(self, text: str, function: Callable):
        button = QPushButton()
        button.setFont(self.font)
        button.setCursor(QCursor(Qt.PointingHandCursor))
        button.setText(text)
        button.setParent(self.ui.buttons)
        button.clicked.connect(function)
        self.ui.buttons.layout().addWidget(button)
        self.buttons.append(button)

    def setButtons(self, buttons: List[Tuple[str, Callable]]):
        self.deleteButtons()
        for button in buttons:
            self.addButton(*button)

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

    def setContent(self, content: str):
        self.ui.content.setText(content)

    def setTitle(self, title: str):
        self.ui.title.setText(title)
