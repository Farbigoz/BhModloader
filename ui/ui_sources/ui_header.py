# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'headerCAFuuo.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class Ui_Header(object):
    def setupUi(self, Header):
        if not Header.objectName():
            Header.setObjectName(u"Header")
        Header.resize(850, 40)
        Header.setMaximumSize(QSize(16777215, 40))
        Header.setStyleSheet(u"border: none;")
        self.verticalLayout_2 = QVBoxLayout(Header)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.buttonsFrame = QFrame(Header)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setStyleSheet(u"background-color: #121317;")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftButtons = QFrame(self.buttonsFrame)
        self.leftButtons.setObjectName(u"leftButtons")
        self.leftButtons.setFrameShape(QFrame.StyledPanel)
        self.leftButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.leftButtons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.modsButtonFrame = QFrame(self.leftButtons)
        self.modsButtonFrame.setObjectName(u"modsButtonFrame")
        self.modsButtonFrame.setStyleSheet(u"")
        self.modsButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.modsButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.modsButtonFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.modsButton = QPushButton(self.modsButtonFrame)
        self.modsButton.setObjectName(u"modsButton")
        self.modsButton.setMinimumSize(QSize(0, 38))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.modsButton.setFont(font)
        self.modsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.modsButton.setStyleSheet(u"QPushButton {\n    color: #eeeeee;\n}")
        self.modsButton.setCheckable(True)
        self.modsButton.setChecked(False)

        self.verticalLayout.addWidget(self.modsButton)

        self.modsLine = QFrame(self.modsButtonFrame)
        self.modsLine.setObjectName(u"modsLine")
        self.modsLine.setMinimumSize(QSize(0, 2))
        self.modsLine.setMaximumSize(QSize(16777215, 2))
        self.modsLine.setStyleSheet(u"background-color: #ffffff;")
        self.modsLine.setFrameShape(QFrame.StyledPanel)
        self.modsLine.setFrameShadow(QFrame.Raised)
        self.modsLine.setLineWidth(0)

        self.verticalLayout.addWidget(self.modsLine, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.modsButtonFrame)

        self.gamebananaButtonFrame = QFrame(self.leftButtons)
        self.gamebananaButtonFrame.setObjectName(u"gamebananaButtonFrame")
        self.gamebananaButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.gamebananaButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.gamebananaButtonFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gamebananaButton = QPushButton(self.gamebananaButtonFrame)
        self.gamebananaButton.setObjectName(u"gamebananaButton")
        self.gamebananaButton.setMinimumSize(QSize(0, 38))
        self.gamebananaButton.setFont(font)
        self.gamebananaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gamebananaButton.setStyleSheet(u"QPushButton {\n    color: #eeeeee;\n}")
        self.gamebananaButton.setCheckable(True)

        self.verticalLayout_3.addWidget(self.gamebananaButton)

        self.gamebananaLine = QFrame(self.gamebananaButtonFrame)
        self.gamebananaLine.setObjectName(u"gamebananaLine")
        self.gamebananaLine.setMinimumSize(QSize(0, 2))
        self.gamebananaLine.setMaximumSize(QSize(16777215, 2))
        self.gamebananaLine.setStyleSheet(u"background-color: #ffffff;")
        self.gamebananaLine.setFrameShape(QFrame.StyledPanel)
        self.gamebananaLine.setFrameShadow(QFrame.Raised)
        self.gamebananaLine.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.gamebananaLine, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.gamebananaButtonFrame)

        self.settingsButtonFrame = QFrame(self.leftButtons)
        self.settingsButtonFrame.setObjectName(u"settingsButtonFrame")
        self.settingsButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsButtonFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.settingsButtonFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settingsButton = QPushButton(self.settingsButtonFrame)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(0, 38))
        self.settingsButton.setFont(font)
        self.settingsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsButton.setStyleSheet(u"QPushButton {\n    color: #eeeeee;\n}")
        self.settingsButton.setCheckable(True)

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.settingsLine = QFrame(self.settingsButtonFrame)
        self.settingsLine.setObjectName(u"settingsLine")
        self.settingsLine.setMinimumSize(QSize(0, 2))
        self.settingsLine.setMaximumSize(QSize(16777215, 2))
        self.settingsLine.setStyleSheet(u"background-color: #ffffff;")
        self.settingsLine.setFrameShape(QFrame.StyledPanel)
        self.settingsLine.setFrameShadow(QFrame.Raised)
        self.settingsLine.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.settingsLine, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.settingsButtonFrame)


        self.horizontalLayout.addWidget(self.leftButtons, 0, Qt.AlignLeft)

        self.rightButtons = QFrame(self.buttonsFrame)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.githubButton = QPushButton(self.rightButtons)
        self.githubButton.setObjectName(u"githubButton")
        self.githubButton.setMinimumSize(QSize(40, 40))
        self.githubButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/GitHub.png", QSize(), QIcon.Normal, QIcon.Off)
        self.githubButton.setIcon(icon)
        self.githubButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.githubButton)

        self.supportButton = QPushButton(self.rightButtons)
        self.supportButton.setObjectName(u"supportButton")
        self.supportButton.setMinimumSize(QSize(40, 40))
        self.supportButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/Donate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.supportButton.setIcon(icon1)
        self.supportButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.supportButton)

        self.languageButton = QPushButton(self.rightButtons)
        self.languageButton.setObjectName(u"languageButton")
        self.languageButton.setMinimumSize(QSize(40, 40))
        self.languageButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/Language.png", QSize(), QIcon.Normal, QIcon.Off)
        self.languageButton.setIcon(icon2)
        self.languageButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.languageButton)

        self.infoButton = QPushButton(self.rightButtons)
        self.infoButton.setObjectName(u"infoButton")
        self.infoButton.setMinimumSize(QSize(40, 40))
        self.infoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.infoButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/About.png", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon3)
        self.infoButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.infoButton)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.buttonsFrame)


        self.retranslateUi(Header)

        QMetaObject.connectSlotsByName(Header)
    # setupUi

    def retranslateUi(self, Header):
        Header.setWindowTitle(QCoreApplication.translate("Header", u"Form", None))
        self.modsButton.setText(QCoreApplication.translate("Header", u"Mods", None))
        self.gamebananaButton.setText(QCoreApplication.translate("Header", u"Gamebanana", None))
        self.settingsButton.setText(QCoreApplication.translate("Header", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.githubButton.setToolTip(QCoreApplication.translate("Header", u"<html><head/><body><p>Support project!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.githubButton.setText("")
        self.supportButton.setText("")
        self.languageButton.setText("")
        self.infoButton.setText("")
    # retranslateUi

