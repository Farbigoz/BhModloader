# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_buttonHQkyNx.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ModButton(object):
    def setupUi(self, ModButton):
        if not ModButton.objectName():
            ModButton.setObjectName(u"ModButton")
        ModButton.resize(370, 48)
        ModButton.setMinimumSize(QSize(0, 48))
        ModButton.setMaximumSize(QSize(16777215, 48))
        ModButton.setCursor(QCursor(Qt.PointingHandCursor))
        ModButton.setStyleSheet(u"border: none;\n"
"background-color: #00000000;")
        self.horizontalLayout = QHBoxLayout(ModButton)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(ModButton)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"QFrame#background{\n"
"background-color: #0024638C;\n"
"border-radius: 5;\n"
"}\n"
"QFrame:hover#background{\n"
"background-color: #7724638C;\n"
"}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.background)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(7, 0, 7, 0)
        self.modInfo = QFrame(self.background)
        self.modInfo.setObjectName(u"modInfo")
        self.modInfo.setStyleSheet(u"")
        self.modInfo.setFrameShape(QFrame.StyledPanel)
        self.modInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.modInfo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.modInfo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.gameVersion = QLabel(self.frame_2)
        self.gameVersion.setObjectName(u"gameVersion")
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(12)
        self.gameVersion.setFont(font)
        self.gameVersion.setStyleSheet(u"color: #43C15F;\n"
"")

        self.horizontalLayout_3.addWidget(self.gameVersion, 0, Qt.AlignLeft)

        self.modName = QLabel(self.frame_2)
        self.modName.setObjectName(u"modName")
        self.modName.setFont(font)
        self.modName.setStyleSheet(u"QLabel{\n"
"color: #eeeeee;\n"
"}")
        self.modName.setTextFormat(Qt.AutoText)
        self.modName.setScaledContents(False)
        self.modName.setWordWrap(False)
        self.modName.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.modName, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.modInfo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 3)
        self.modAuthor = QLabel(self.frame)
        self.modAuthor.setObjectName(u"modAuthor")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(10)
        self.modAuthor.setFont(font1)
        self.modAuthor.setMouseTracking(True)
        self.modAuthor.setStyleSheet(u"QLabel{\n"
"color: #B1BA96;\n"
"}")
        self.modAuthor.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.modAuthor)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.modInfo)

        self.modStateFrame = QFrame(self.background)
        self.modStateFrame.setObjectName(u"modStateFrame")
        self.modStateFrame.setMinimumSize(QSize(20, 0))
        self.modStateFrame.setMaximumSize(QSize(20, 16777215))
        self.modStateFrame.setFrameShape(QFrame.StyledPanel)
        self.modStateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.modStateFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.modState = QLabel(self.modStateFrame)
        self.modState.setObjectName(u"modState")
        self.modState.setMinimumSize(QSize(20, 20))
        self.modState.setMaximumSize(QSize(20, 20))
        self.modState.setPixmap(QPixmap(u":/icons/resources/icons/Installed.png"))
        self.modState.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.modState)


        self.horizontalLayout_2.addWidget(self.modStateFrame)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(ModButton)

        QMetaObject.connectSlotsByName(ModButton)
    # setupUi

    def retranslateUi(self, ModButton):
        ModButton.setWindowTitle(QCoreApplication.translate("ModButton", u"Form", None))
        self.gameVersion.setText(QCoreApplication.translate("ModButton", u"[5.10]", None))
        self.modName.setText(QCoreApplication.translate("ModButton", u"Night Mammoth Fortress Map", None))
        self.modAuthor.setText(QCoreApplication.translate("ModButton", u"Author: I_FabrizioG_I", None))
        self.modState.setText("")
    # retranslateUi

