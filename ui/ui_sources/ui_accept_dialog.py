# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accept_dialogAnrhKc.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_AcceptDialog(object):
    def setupUi(self, AcceptDialog):
        if not AcceptDialog.objectName():
            AcceptDialog.setObjectName(u"AcceptDialog")
        AcceptDialog.resize(850, 550)
        AcceptDialog.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(AcceptDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(AcceptDialog)
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

        self.content = QLabel(self.dialogBackground)
        self.content.setObjectName(u"content")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(10)
        self.content.setFont(font1)

        self.verticalLayout.addWidget(self.content)

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
        self.accept = QPushButton(self.buttons)
        self.accept.setObjectName(u"accept")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.accept.setFont(font2)
        self.accept.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.accept)

        self.cancel = QPushButton(self.buttons)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setFont(font2)
        self.cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.cancel)


        self.verticalLayout.addWidget(self.buttons, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.dialogBackground, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(AcceptDialog)

        QMetaObject.connectSlotsByName(AcceptDialog)
    # setupUi

    def retranslateUi(self, AcceptDialog):
        AcceptDialog.setWindowTitle(QCoreApplication.translate("AcceptDialog", u"Form", None))
        self.title.setText(QCoreApplication.translate("AcceptDialog", u"TextLabel", None))
        self.content.setText(QCoreApplication.translate("AcceptDialog", u"TextLabel", None))
        self.accept.setText(QCoreApplication.translate("AcceptDialog", u"ACCEPT", None))
        self.cancel.setText(QCoreApplication.translate("AcceptDialog", u"CANCEL", None))
    # retranslateUi

