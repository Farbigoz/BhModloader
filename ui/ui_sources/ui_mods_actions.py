# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mods_actionsnWYaPk.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ModsActions(object):
    def setupUi(self, ModsActions):
        if not ModsActions.objectName():
            ModsActions.setObjectName(u"ModsActions")
        ModsActions.resize(748, 40)
        ModsActions.setMinimumSize(QSize(0, 40))
        ModsActions.setMaximumSize(QSize(16777215, 40))
        ModsActions.setCursor(QCursor(Qt.ArrowCursor))
        ModsActions.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(ModsActions)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(ModsActions)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.webPage = QPushButton(self.mainFrame)
        self.webPage.setObjectName(u"webPage")
        self.webPage.setMinimumSize(QSize(90, 40))
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(11)
        self.webPage.setFont(font)
        self.webPage.setCursor(QCursor(Qt.PointingHandCursor))
        self.webPage.setStyleSheet(u"background-color: #3396CD;\n"
"border-radius: 4px;\n"
"color: #eeeeee;")
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/OpenWeb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.webPage.setIcon(icon)
        self.webPage.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.webPage)

        self.install = QPushButton(self.mainFrame)
        self.install.setObjectName(u"install")
        self.install.setMinimumSize(QSize(90, 40))
        self.install.setFont(font)
        self.install.setCursor(QCursor(Qt.PointingHandCursor))
        self.install.setStyleSheet(u"background-color: #43C15F;\n"
"border-radius: 4px;\n"
"color: #eeeeee;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/Install.png", QSize(), QIcon.Normal, QIcon.Off)
        self.install.setIcon(icon1)
        self.install.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.install)

        self.uninstall = QPushButton(self.mainFrame)
        self.uninstall.setObjectName(u"uninstall")
        self.uninstall.setMinimumSize(QSize(90, 40))
        self.uninstall.setFont(font)
        self.uninstall.setCursor(QCursor(Qt.PointingHandCursor))
        self.uninstall.setStyleSheet(u"background-color: #00B9A3;\n"
"border-radius: 4px;\n"
"color: #eeeeee;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/Uninstall.png", QSize(), QIcon.Normal, QIcon.Off)
        self.uninstall.setIcon(icon2)
        self.uninstall.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.uninstall)

        self.reinstall = QPushButton(self.mainFrame)
        self.reinstall.setObjectName(u"reinstall")
        self.reinstall.setMinimumSize(QSize(90, 40))
        self.reinstall.setFont(font)
        self.reinstall.setCursor(QCursor(Qt.PointingHandCursor))
        self.reinstall.setStyleSheet(u"background-color: #CD33C7;\n"
"border-radius: 4px;\n"
"color: #eeeeee;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/UpdateModsTable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reinstall.setIcon(icon3)
        self.reinstall.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.reinstall)

        self.update = QPushButton(self.mainFrame)
        self.update.setObjectName(u"update")
        self.update.setMinimumSize(QSize(90, 40))
        self.update.setFont(font)
        self.update.setCursor(QCursor(Qt.PointingHandCursor))
        self.update.setStyleSheet(u"background-color: #833DBB;\n"
"border-radius: 4px;\n"
"color: #eeeeee;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/icons/Update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update.setIcon(icon4)
        self.update.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.update)

        self.deleteMod = QPushButton(self.mainFrame)
        self.deleteMod.setObjectName(u"deleteMod")
        self.deleteMod.setMinimumSize(QSize(90, 40))
        self.deleteMod.setFont(font)
        self.deleteMod.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteMod.setStyleSheet(u"background-color: #FF5050;\n"
"border-radius: 4px;\n"
"color: #eeeeee;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/icons/Delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteMod.setIcon(icon5)
        self.deleteMod.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.deleteMod)


        self.horizontalLayout.addWidget(self.mainFrame, 0, Qt.AlignLeft)


        self.retranslateUi(ModsActions)

        QMetaObject.connectSlotsByName(ModsActions)
    # setupUi

    def retranslateUi(self, ModsActions):
        ModsActions.setWindowTitle(QCoreApplication.translate("ModsActions", u"Form", None))
        self.webPage.setText(QCoreApplication.translate("ModsActions", u"WebPage", None))
        self.install.setText(QCoreApplication.translate("ModsActions", u"Install", None))
        self.uninstall.setText(QCoreApplication.translate("ModsActions", u"Uninstall", None))
        self.reinstall.setText(QCoreApplication.translate("ModsActions", u"Reinstall", None))
        self.update.setText(QCoreApplication.translate("ModsActions", u"Update", None))
        self.deleteMod.setText(QCoreApplication.translate("ModsActions", u"Delete", None))
    # retranslateUi

