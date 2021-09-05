# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress_dialogHeKZmR.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        if not ProgressDialog.objectName():
            ProgressDialog.setObjectName(u"ProgressDialog")
        ProgressDialog.resize(850, 550)
        ProgressDialog.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(ProgressDialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(ProgressDialog)
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

        self.progressBar = QProgressBar(self.dialogBackground)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    min-height: 6;\n"
"    max-height: 6;\n"
"    border-radius: 3px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 3px;\n"
"    background-color: #4B8BF4;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.content = QLabel(self.dialogBackground)
        self.content.setObjectName(u"content")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(10)
        self.content.setFont(font1)

        self.verticalLayout.addWidget(self.content, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.dialogBackground, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(ProgressDialog)

        QMetaObject.connectSlotsByName(ProgressDialog)
    # setupUi

    def retranslateUi(self, ProgressDialog):
        ProgressDialog.setWindowTitle(QCoreApplication.translate("ProgressDialog", u"Form", None))
        self.title.setText(QCoreApplication.translate("ProgressDialog", u"TextLabel", None))
        self.content.setText(QCoreApplication.translate("ProgressDialog", u"TextLabel", None))
    # retranslateUi

