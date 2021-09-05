# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modsUNiHUf.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Mods(object):
    def setupUi(self, Mods):
        if not Mods.objectName():
            Mods.setObjectName(u"Mods")
        Mods.resize(850, 514)
        Mods.setMinimumSize(QSize(0, 0))
        Mods.setStyleSheet(u"border: none;")
        self.horizontalLayout = QHBoxLayout(Mods)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(Mods)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(False)
        self.modsList = QFrame(self.splitter)
        self.modsList.setObjectName(u"modsList")
        self.modsList.setMinimumSize(QSize(200, 0))
        self.modsList.setMaximumSize(QSize(400, 16777215))
        self.modsList.setStyleSheet(u"background-color: #242529;")
        self.modsList.setFrameShape(QFrame.StyledPanel)
        self.modsList.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.modsList)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchFrame = QFrame(self.modsList)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(0, 30))
        self.searchFrame.setMaximumSize(QSize(16777215, 30))
        self.searchFrame.setCursor(QCursor(Qt.IBeamCursor))
        self.searchFrame.setStyleSheet(u"background-color: #1D1E20;")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.searchButton = QPushButton(self.searchFrame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(25, 0))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/Search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QSize(14, 14))

        self.horizontalLayout_2.addWidget(self.searchButton)

        self.searchArea = QLineEdit(self.searchFrame)
        self.searchArea.setObjectName(u"searchArea")
        self.searchArea.setMinimumSize(QSize(0, 0))
        self.searchArea.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.searchArea.setFont(font)
        self.searchArea.setStyleSheet(u"color: #eeeeee;")

        self.horizontalLayout_2.addWidget(self.searchArea)


        self.verticalLayout.addWidget(self.searchFrame, 0, Qt.AlignTop)

        self.scrollModsListFrame = QFrame(self.modsList)
        self.scrollModsListFrame.setObjectName(u"scrollModsListFrame")
        self.scrollModsListFrame.setFrameShape(QFrame.StyledPanel)
        self.scrollModsListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.scrollModsListFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollModsList = QScrollArea(self.scrollModsListFrame)
        self.scrollModsList.setObjectName(u"scrollModsList")
        self.scrollModsList.setStyleSheet(u"QScrollBar:vertical {         \n"
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
        self.scrollModsList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollModsList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 400, 444))
        self.scrollModsList.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollModsList)


        self.verticalLayout.addWidget(self.scrollModsListFrame)

        self.createModFrame = QFrame(self.modsList)
        self.createModFrame.setObjectName(u"createModFrame")
        self.createModFrame.setMaximumSize(QSize(16777215, 0))
        self.createModFrame.setStyleSheet(u"QPushButton{\n"
"color: #eeeeee;\n"
"background-color: #43C15F;\n"
"}")
        self.createModFrame.setFrameShape(QFrame.StyledPanel)
        self.createModFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.createModFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.createMod = QPushButton(self.createModFrame)
        self.createMod.setObjectName(u"createMod")
        self.createMod.setMinimumSize(QSize(0, 30))
        self.createMod.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.createMod)


        self.verticalLayout.addWidget(self.createModFrame)

        self.modsListActions = QFrame(self.modsList)
        self.modsListActions.setObjectName(u"modsListActions")
        self.modsListActions.setMinimumSize(QSize(0, 40))
        self.modsListActions.setMaximumSize(QSize(16777215, 40))
        self.modsListActions.setStyleSheet(u"background-color: #1C1C1F;")
        self.modsListActions.setFrameShape(QFrame.StyledPanel)
        self.modsListActions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.modsListActions)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.leftButtons = QFrame(self.modsListActions)
        self.leftButtons.setObjectName(u"leftButtons")
        self.leftButtons.setStyleSheet(u"background-color: #767676;\n"
"border-radius: 5px;")
        self.leftButtons.setFrameShape(QFrame.StyledPanel)
        self.leftButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.leftButtons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.deleteAllMods = QPushButton(self.leftButtons)
        self.deleteAllMods.setObjectName(u"deleteAllMods")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteAllMods.sizePolicy().hasHeightForWidth())
        self.deleteAllMods.setSizePolicy(sizePolicy)
        self.deleteAllMods.setMinimumSize(QSize(30, 30))
        self.deleteAllMods.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteAllMods.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/UninstallAllMods.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteAllMods.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.deleteAllMods)

        self.reloadModsList = QPushButton(self.leftButtons)
        self.reloadModsList.setObjectName(u"reloadModsList")
        self.reloadModsList.setMinimumSize(QSize(30, 30))
        self.reloadModsList.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/UpdateModsTable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadModsList.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.reloadModsList)

        self.installAllMods = QPushButton(self.leftButtons)
        self.installAllMods.setObjectName(u"installAllMods")
        self.installAllMods.setMinimumSize(QSize(30, 30))
        self.installAllMods.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/resources/icons/InstallAllMods.png", QSize(), QIcon.Normal, QIcon.Off)
        self.installAllMods.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.installAllMods)


        self.horizontalLayout_3.addWidget(self.leftButtons, 0, Qt.AlignLeft)

        self.rightButtons = QFrame(self.modsListActions)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setStyleSheet(u"background-color: #767676;\n"
"border-radius: 5px;")
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.modsSortButton = QPushButton(self.rightButtons)
        self.modsSortButton.setObjectName(u"modsSortButton")
        sizePolicy.setHeightForWidth(self.modsSortButton.sizePolicy().hasHeightForWidth())
        self.modsSortButton.setSizePolicy(sizePolicy)
        self.modsSortButton.setMinimumSize(QSize(30, 30))
        self.modsSortButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/resources/icons/SortModsList.png", QSize(), QIcon.Normal, QIcon.Off)
        self.modsSortButton.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.modsSortButton)

        self.updateAllMods = QPushButton(self.rightButtons)
        self.updateAllMods.setObjectName(u"updateAllMods")
        self.updateAllMods.setMinimumSize(QSize(30, 30))
        self.updateAllMods.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/resources/icons/UpdateAllMods.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateAllMods.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.updateAllMods)

        self.openModsFolderButton = QPushButton(self.rightButtons)
        self.openModsFolderButton.setObjectName(u"openModsFolderButton")
        self.openModsFolderButton.setMinimumSize(QSize(30, 30))
        self.openModsFolderButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/resources/icons/OpenModsFolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openModsFolderButton.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.openModsFolderButton)


        self.horizontalLayout_3.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.modsListActions, 0, Qt.AlignBottom)

        self.splitter.addWidget(self.modsList)
        self.modBody = QFrame(self.splitter)
        self.modBody.setObjectName(u"modBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.modBody.sizePolicy().hasHeightForWidth())
        self.modBody.setSizePolicy(sizePolicy1)
        self.modBody.setMinimumSize(QSize(0, 0))
        self.modBody.setStyleSheet(u"QFrame{\n"
"background-color: #303136;\n"
"}")
        self.modBody.setFrameShape(QFrame.StyledPanel)
        self.modBody.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.modBody)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollBody = QScrollArea(self.modBody)
        self.scrollBody.setObjectName(u"scrollBody")
        self.scrollBody.setStyleSheet(u"QScrollBar:vertical {         \n"
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
        self.scrollBody.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 450, 514))
        self.scrollBody.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollBody)

        self.modsBuildActions = QFrame(self.modBody)
        self.modsBuildActions.setObjectName(u"modsBuildActions")
        self.modsBuildActions.setMaximumSize(QSize(16777215, 0))
        self.modsBuildActions.setFrameShape(QFrame.StyledPanel)
        self.modsBuildActions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.modsBuildActions)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_4.addWidget(self.modsBuildActions)

        self.splitter.addWidget(self.modBody)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(Mods)

        QMetaObject.connectSlotsByName(Mods)
    # setupUi

    def retranslateUi(self, Mods):
        Mods.setWindowTitle(QCoreApplication.translate("Mods", u"Form", None))
        self.searchButton.setText("")
        self.searchArea.setInputMask("")
        self.searchArea.setText("")
        self.searchArea.setPlaceholderText(QCoreApplication.translate("Mods", u"Search", None))
        self.createMod.setText(QCoreApplication.translate("Mods", u"Create mod", None))
#if QT_CONFIG(tooltip)
        self.deleteAllMods.setToolTip(QCoreApplication.translate("Mods", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Delete all mods</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.deleteAllMods.setText("")
#if QT_CONFIG(tooltip)
        self.reloadModsList.setToolTip(QCoreApplication.translate("Mods", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Reload mods list</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.reloadModsList.setText("")
#if QT_CONFIG(tooltip)
        self.installAllMods.setToolTip(QCoreApplication.translate("Mods", u"<html><head/><body><p><span style=\" color:#eeeeee;\">Install all mods</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.installAllMods.setText("")
        self.modsSortButton.setText("")
        self.updateAllMods.setText("")
        self.openModsFolderButton.setText("")
    # retranslateUi

