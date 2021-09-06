from PySide6.QtWidgets import QWidget, QFrame
from PySide6.QtCore import QSize, QPropertyAnimation, QEasingCurve

from ..ui_sources.ui_header import Ui_Header
from ..utils.buttongroup import ButtonGroup
from ..utils.buttons import ButtonTextSize


class HeaderButton(ButtonGroup):
    duration = 150
    easingCurve = QEasingCurve.OutBack

    def __init__(self, button, line, frame, isDefault=False, method=None):
        self.line: QFrame = line
        self.frame: QFrame = frame

        self.animPlus: QPropertyAnimation = None
        self.animMinus: QPropertyAnimation = None

        #self.button.setCursor(QCursor(Qt.PointingHandCursor))

        super().__init__("headerTabs", button, method=method)

        width = self.resizeFrame()
        if isDefault:
            self.button.setChecked(True)
            self.line.setMinimumWidth(width)
            self.pressedMethod()

    def resizeFrame(self):
        width = ButtonTextSize(self.button).width()
        self.frame.setMinimumWidth(width + 30)
        return width + 30

    def enter(self):
        if not self.button.isChecked():
            if self.animMinus is None:
                default = 0
            else:
                default = self.animMinus.currentValue()

            self.animPlus = QPropertyAnimation(self.line, b"minimumWidth")
            self.animPlus.setDuration(self.duration)
            self.animPlus.setStartValue(default)
            self.animPlus.setEndValue(self.frame.width()//2)
            self.animPlus.setEasingCurve(self.easingCurve)
            self.animPlus.start()

    def leave(self):
        if not self.button.isChecked():
            if self.animPlus is None:
                default = self.frame.width()
            else:
                default = self.animPlus.currentValue()

                if default == self.frame.width():
                    default = self.frame.width()//2

            self.animMinus = QPropertyAnimation(self.line, b"minimumWidth")
            self.animMinus.setDuration(self.duration)
            self.animMinus.setStartValue(default)
            self.animMinus.setEndValue(0)
            self.animMinus.setEasingCurve(self.easingCurve)
            self.animMinus.start()

    def released(self):
        self.button.setAutoExclusive(False)
        self.button.setChecked(True)
        self.button.setAutoExclusive(True)

        return True

    def pressed(self):
        if self.button.isChecked():
            return True

        else:
            if self.animPlus is None:
                oldWidth = 0
            else:
                oldWidth = self.animPlus.currentValue()
                if oldWidth == self.frame.width():
                    oldWidth = self.frame.width() // 2

            self.animPlus = QPropertyAnimation(self.line, b"minimumWidth")
            self.animPlus.setDuration(self.duration)
            self.animPlus.setStartValue(oldWidth)
            self.animPlus.setEndValue(self.frame.width())
            self.animPlus.setEasingCurve(QEasingCurve.InCubic)
            self.animPlus.start()

            for headerButton in self.getSelfGroup():
                if headerButton.button.isChecked():
                    headerButton.button.setAutoExclusive(False)
                    headerButton.button.setChecked(False)
                    headerButton.leave()
                    headerButton.button.setAutoExclusive(True)
                    break

            self.pressedMethod()

            return False


class HeaderIconButton(ButtonGroup):
    duration = 100
    easingCurve = QEasingCurve.OutBack

    baseSize = 26
    hoverSize = 28
    pressSize = 24

    def __init__(self, button, method=None):
        super().__init__("headerButtons", button, method=method)

        self.animPlus: QPropertyAnimation = QPropertyAnimation(self.button, b"iconSize")
        self.animPlus.setDuration(self.duration)
        self.animPlus.setEasingCurve(self.easingCurve)
        self.animPlus.setStartValue(QSize(self.baseSize, self.baseSize))

        self.animMinus: QPropertyAnimation = QPropertyAnimation(self.button, b"iconSize")
        self.animMinus.setDuration(self.duration)
        self.animMinus.setEasingCurve(self.easingCurve)
        self.animMinus.setStartValue(QSize(self.baseSize, self.baseSize))

    def enter(self):
        self.animPlus.setStartValue(self.animPlus.currentValue())
        self.animPlus.setEndValue(QSize(self.hoverSize, self.hoverSize))
        self.animPlus.start()

    def leave(self):
        self.animMinus.setStartValue(self.animPlus.currentValue())
        self.animMinus.setEndValue(QSize(self.baseSize, self.baseSize))
        self.animMinus.start()

    def pressed(self):
        self.animMinus.setStartValue(self.animPlus.currentValue())
        self.animMinus.setEndValue(QSize(self.pressSize, self.pressSize))
        self.animMinus.start()

        self.pressedMethod()
        return False

    def released(self):
        self.animPlus.setStartValue(self.animPlus.currentValue())
        self.animPlus.setEndValue(QSize(self.hoverSize, self.hoverSize))
        self.animPlus.start()
        return False


class HeaderFrame(QWidget):
    buttonAnimPlus = None
    buttonAnimMinus = None

    def __init__(self):
        super().__init__()

        self.ui = Ui_Header()
        self.ui.setupUi(self)

        self.headerModsButton = HeaderButton(self.ui.modsButton,
                                             self.ui.modsLine,
                                             self.ui.modsButtonFrame,
                                             isDefault=True, method=lambda: print("Mods"))
        self.headerGamebananaButton = HeaderButton(self.ui.gamebananaButton,
                                                   self.ui.gamebananaLine,
                                                   self.ui.gamebananaButtonFrame)
        self.headerSettingsButton = HeaderButton(self.ui.settingsButton,
                                                 self.ui.settingsLine,
                                                 self.ui.settingsButtonFrame)

        self.headerGithubButton = HeaderIconButton(self.ui.githubButton)
        self.headerSupportButton = HeaderIconButton(self.ui.supportButton)
        self.headerLanguageButton = HeaderIconButton(self.ui.languageButton)
        self.headerInfoButton = HeaderIconButton(self.ui.infoButton)


    def setModsButtonPressed(self, method):
        self.headerModsButton.setPressed(method)

    def setGamebananaButtonPressed(self, method):
        self.headerGamebananaButton.setPressed(method)

    def setSettingsButtonPressed(self, method):
        self.headerSettingsButton.setPressed(method)

    def resizeEvent(self, event):
        size = self.size()
        new_size = event.size()
        self.resize(QSize(new_size.width(), size.height()))

