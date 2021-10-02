# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buttons_dialogwOnGpe.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ButtonsDialog(object):
    def setupUi(self, ButtonsDialog):
        if not ButtonsDialog.objectName():
            ButtonsDialog.setObjectName(u"ButtonsDialog")
        ButtonsDialog.resize(850, 550)
        ButtonsDialog.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(ButtonsDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(ButtonsDialog)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"QFrame#background{\n"
                                      "background-color: #991E2025;\n"
                                      "}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.background)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dialogBackground = QFrame(self.background)
        self.dialogBackground.setObjectName(u"dialogBackground")
        self.dialogBackground.setMinimumSize(QSize(500, 100))
        self.dialogBackground.setStyleSheet(u"QFrame#dialogBackground{\n"
                                            "background-color: #1E2025;\n"
                                            "border-radius: 7px;\n"
                                            "}\n"
                                            "QLabel{\n"
                                            "color: #eeeeee;\n"
                                            "}")
        self.dialogBackground.setFrameShape(QFrame.StyledPanel)
        self.dialogBackground.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.dialogBackground)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.title = QLabel(self.dialogBackground)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(14)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title)

        self.scrollLabel = QScrollArea(self.dialogBackground)
        self.scrollLabel.setObjectName(u"scrollLabel")
        self.scrollLabel.setStyleSheet(u"QScrollArea{\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "QScrollBar:vertical {\n"
                                       "    border: none;\n"
                                       "    background: #2B2C32;\n"
                                       "    width: 7px;\n"
                                       "    margin: 0 0 0 0;\n"
                                       "    border-radius: 0px;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical {\n"
                                       "    background-color: #616161;\n"
                                       "    min-height: 30px;\n"
                                       "    border-radius: 7px;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:hover{\n"
                                       "    background-color: #A1A1A1;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:pressed {\n"
                                       "    background-color: #717171;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical {\n"
                                       "	border: none;\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical {\n"
                                       "	border: none;\n"
                                       "}\n"
                                       "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                       "	background: none;\n"
                                       "}\n"
                                       "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                       "	background: none;\n"
                                       "}")
        self.scrollLabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollLabel.setWidgetResizable(True)
        self.scrollLabel.setMinimumHeight(0)
        self.scrollLabel.setMaximumHeight(0)

        self.verticalLayout.addWidget(self.scrollLabel)

        self.content = QLabel()
        self.content.setObjectName(u"content")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        self.content.setFont(font1)
        self.content.setOpenExternalLinks(True)
        self.content.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse)

        self.scrollLabel.setWidget(self.content)

        self.buttons = QFrame(self.dialogBackground)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setStyleSheet(u"QPushButton{\n"
                                   "color: #4A9CEC\n"
                                   "}")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttons)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 10, 10, 10)

        self.verticalLayout.addWidget(self.buttons, 0, Qt.AlignRight)

        self.horizontalLayout_2.addWidget(self.dialogBackground, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.background)

        self.retranslateUi(ButtonsDialog)

        QMetaObject.connectSlotsByName(ButtonsDialog)

    # setupUi

    def retranslateUi(self, ButtonsDialog):
        ButtonsDialog.setWindowTitle(QCoreApplication.translate("ButtonsDialog", u"Form", None))
        self.title.setText(QCoreApplication.translate("ButtonsDialog", u"TextLabel", None))
        self.content.setText(QCoreApplication.translate("ButtonsDialog", u"TextLabel", None))
    # retranslateUi
