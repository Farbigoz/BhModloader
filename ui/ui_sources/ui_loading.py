# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingYVLieB.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Loading(object):
    def setupUi(self, Loading):
        if not Loading.objectName():
            Loading.setObjectName(u"Loading")
        Loading.resize(400, 382)
        self.verticalLayout = QVBoxLayout(Loading)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadingFrame = QFrame(Loading)
        self.loadingFrame.setObjectName(u"loadingFrame")
        self.loadingFrame.setFrameShape(QFrame.StyledPanel)
        self.loadingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.loadingFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.anim = QLabel(self.loadingFrame)
        self.anim.setObjectName(u"anim")
        self.anim.setMinimumSize(QSize(100, 100))
        self.anim.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.anim)

        self.label = QLabel(self.loadingFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFFFFF;")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.loadingFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.retranslateUi(Loading)

        QMetaObject.connectSlotsByName(Loading)
    # setupUi

    def retranslateUi(self, Loading):
        Loading.setWindowTitle(QCoreApplication.translate("Loading", u"Form", None))
        self.anim.setText("")
        self.label.setText(QCoreApplication.translate("Loading", u"Loading...", None))
    # retranslateUi

