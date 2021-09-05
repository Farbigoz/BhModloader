from typing import Dict

from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import QEvent


class ButtonGroup(QWidget):
    _groups: Dict[str, list] = {}

    def __init__(self, group: str, button: QPushButton, isDefault: bool = False, method=None):
        self.group = group

        if group not in self._groups:
            self._groups[group] = []

        if button in self._groups[group]:
            raise Exception(f"This button '{button}' is already in '{group}' group")

        self.button: QPushButton = button
        self._groups[group].append(self)

        if method is None:
            self.pressedMethod = lambda: None
        else:
            self.pressedMethod = method

        if isDefault:
            self.button.setChecked(True)
            self.pressedMethod()

        super().__init__()

        self.button.installEventFilter(self)

    def remove(self):
        self._groups[self.group].pop(self)

    def setPressed(self, method):
        self.pressedMethod = method

    def pressed(self):
        if self.button.isChecked():
            return True
        else:
            self.pressedMethod()
            return False

    def released(self):
        return False

    def enter(self):
        pass

    def leave(self):
        pass

    def eventFilter(self, qobject, event):
        #if event.type() not in [QEvent.HoverMove, QEvent.PolishRequest, QEvent.Paint, QEvent.MouseMove]:
        #    print(event.type())

        if event.type() == QEvent.Enter:
            self.enter()

        elif event.type() == QEvent.Leave:
            self.leave()

        elif event.type() == QEvent.MouseButtonPress:
            return self.pressed()

        elif event.type() == QEvent.MouseButtonRelease:
            return self.released()

        elif event.type() == QEvent.MouseButtonDblClick:
            return True

        return False

    @classmethod
    def getGroup(cls, group: str) -> list:
        return cls._groups.get(group, [])

    def getSelfGroup(self) -> list:
        return self._groups.get(self.group, [])
