# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_bodytmznKp.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ModBody(object):
    def setupUi(self, ModBody):
        if not ModBody.objectName():
            ModBody.setObjectName(u"ModBody")
        ModBody.resize(547, 481)
        ModBody.setStyleSheet(u"border: none;")
        self.verticalLayout = QVBoxLayout(ModBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.modPreviewFrame = QFrame(ModBody)
        self.modPreviewFrame.setObjectName(u"modPreviewFrame")
        self.modPreviewFrame.setStyleSheet(u"background-color:transparent;")
        self.modPreviewFrame.setFrameShape(QFrame.StyledPanel)
        self.modPreviewFrame.setFrameShadow(QFrame.Raised)
        self.modPreviewInfo = QFrame(self.modPreviewFrame)
        self.modPreviewInfo.setObjectName(u"modPreviewInfo")
        self.modPreviewInfo.setGeometry(QRect(0, 0, 519, 216))
        self.modPreviewInfo.setStyleSheet(u"QFrame{\n"
"border-image: url(:/images/resources/images/PreviewShadow.png);\n"
"background-color: #00000000;\n"
"}")
        self.modPreviewInfo.setFrameShape(QFrame.StyledPanel)
        self.modPreviewInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.modPreviewInfo)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(15, -1, 15, -1)
        self.spacer = QFrame(self.modPreviewInfo)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setStyleSheet(u"border-image: none;")
        self.spacer.setFrameShape(QFrame.StyledPanel)
        self.spacer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.spacer, 0, Qt.AlignTop)

        self.previewSwitcher = QFrame(self.modPreviewInfo)
        self.previewSwitcher.setObjectName(u"previewSwitcher")
        self.previewSwitcher.setMaximumSize(QSize(16777215, 48))
        self.previewSwitcher.setStyleSheet(u"border-image: none;")
        self.previewSwitcher.setFrameShape(QFrame.StyledPanel)
        self.previewSwitcher.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.previewSwitcher)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftPreview = QPushButton(self.previewSwitcher)
        self.leftPreview.setObjectName(u"leftPreview")
        self.leftPreview.setMaximumSize(QSize(30, 16777215))
        self.leftPreview.setCursor(QCursor(Qt.PointingHandCursor))
        self.leftPreview.setStyleSheet(u"QPushButton {\n"
"    qproperty-icon: url(\" \"); /* empty image */\n"
"    qproperty-iconSize: 48px 48px; /* space for the background image */\n"
"    background-image: url(\":/icons/resources/icons/BackTransparent.png\");\n"
"	background-color: #00000000;\n"
"    background-repeat: no-repeat;\n"
"	margin-left: -10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-image: url(\":/icons/resources/icons/Back.png\");\n"
"    background-repeat: no-repeat;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/Back.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/resources/icons/GhostInstalled.png", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/icons/resources/icons/Back.png", QSize(), QIcon.Selected, QIcon.On)
        self.leftPreview.setIcon(icon)
        self.leftPreview.setIconSize(QSize(48, 48))

        self.horizontalLayout_2.addWidget(self.leftPreview, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.rightPreview = QPushButton(self.previewSwitcher)
        self.rightPreview.setObjectName(u"rightPreview")
        self.rightPreview.setMaximumSize(QSize(30, 16777215))
        self.rightPreview.setCursor(QCursor(Qt.PointingHandCursor))
        self.rightPreview.setStyleSheet(u"QPushButton {\n"
"    qproperty-icon: url(\" \"); /* empty image */\n"
"    qproperty-iconSize: 48px 48px; /* space for the background image */\n"
"    background-image: url(\":/icons/resources/icons/ForwardTransparent.png\");\n"
"	background-color: #00000000;\n"
"    background-repeat: no-repeat;\n"
"	margin-left: -10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-image: url(\":/icons/resources/icons/Forward.png\");\n"
"    background-repeat: no-repeat;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/Forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightPreview.setIcon(icon1)
        self.rightPreview.setIconSize(QSize(48, 48))
        self.rightPreview.setFlat(False)

        self.horizontalLayout_2.addWidget(self.rightPreview, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_11.addWidget(self.previewSwitcher, 0, Qt.AlignVCenter)

        self.modInfoFrame = QFrame(self.modPreviewInfo)
        self.modInfoFrame.setObjectName(u"modInfoFrame")
        self.modInfoFrame.setLayoutDirection(Qt.LeftToRight)
        self.modInfoFrame.setStyleSheet(u"border-image: none;")
        self.modInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.modInfoFrame.setFrameShadow(QFrame.Plain)
        self.modInfoFrame.setLineWidth(0)
        self.verticalLayout_12 = QVBoxLayout(self.modInfoFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.modName = QLabel(self.modInfoFrame)
        self.modName.setObjectName(u"modName")
        font = QFont()
        font.setFamilies([u"Exo 2 SemiBold"])
        font.setPointSize(24)
        font.setBold(True)
        self.modName.setFont(font)
        self.modName.setStyleSheet(u"color: #eeeeee;")
        self.modName.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.modName)

        self.bottomModInfoFrame = QFrame(self.modInfoFrame)
        self.bottomModInfoFrame.setObjectName(u"bottomModInfoFrame")
        self.bottomModInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomModInfoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.bottomModInfoFrame)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.modSource = QLabel(self.bottomModInfoFrame)
        self.modSource.setObjectName(u"modSource")
        font1 = QFont()
        font1.setFamilies([u"Roboto Medium"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.modSource.setFont(font1)
        self.modSource.setStyleSheet(u"color: #eeeeee;")

        self.horizontalLayout_9.addWidget(self.modSource, 0, Qt.AlignLeft)

        self.previewsNavigateFrame = QFrame(self.bottomModInfoFrame)
        self.previewsNavigateFrame.setObjectName(u"previewsNavigateFrame")
        self.previewsNavigateFrame.setFrameShape(QFrame.StyledPanel)
        self.previewsNavigateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.previewsNavigateFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.previewsNavigateFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.modVersion = QLabel(self.bottomModInfoFrame)
        self.modVersion.setObjectName(u"modVersion")
        self.modVersion.setFont(font1)
        self.modVersion.setStyleSheet(u"color: #eeeeee;")

        self.horizontalLayout_9.addWidget(self.modVersion, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.bottomModInfoFrame, 0, Qt.AlignBottom)


        self.verticalLayout_11.addWidget(self.modInfoFrame, 0, Qt.AlignBottom)

        self.modPreview = QLabel(self.modPreviewFrame)
        self.modPreview.setObjectName(u"modPreview")
        self.modPreview.setGeometry(QRect(0, 0, 551, 201))
        self.modPreview.setPixmap(QPixmap(u":/images/resources/images/DefaultPreview.png"))
        self.modPreview.setScaledContents(True)
        self.modPreview.raise_()
        self.modPreviewInfo.raise_()

        self.verticalLayout.addWidget(self.modPreviewFrame)

        self.modDescriptionsAndActions = QFrame(ModBody)
        self.modDescriptionsAndActions.setObjectName(u"modDescriptionsAndActions")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modDescriptionsAndActions.sizePolicy().hasHeightForWidth())
        self.modDescriptionsAndActions.setSizePolicy(sizePolicy)
        self.modDescriptionsAndActions.setMinimumSize(QSize(0, 0))
        self.modDescriptionsAndActions.setMaximumSize(QSize(16777215, 16777215))
        self.modDescriptionsAndActions.setStyleSheet(u"QFrame{\n"
"}")
        self.modDescriptionsAndActions.setFrameShape(QFrame.StyledPanel)
        self.modDescriptionsAndActions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.modDescriptionsAndActions)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_13.setContentsMargins(15, 10, 15, -1)
        self.modTags = QLabel(self.modDescriptionsAndActions)
        self.modTags.setObjectName(u"modTags")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.modTags.setFont(font2)
        self.modTags.setStyleSheet(u"QLabel{\n"
"	color: #eeeeee;\n"
"}")
        self.modTags.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.modTags, 0, Qt.AlignTop)

        self.modActions = QFrame(self.modDescriptionsAndActions)
        self.modActions.setObjectName(u"modActions")
        self.modActions.setMinimumSize(QSize(40, 40))
        self.modActions.setStyleSheet(u"QFrame{\n"
"}")
        self.modActions.setFrameShape(QFrame.StyledPanel)
        self.modActions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.modActions)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.modActions, 0, Qt.AlignLeft|Qt.AlignTop)

        self.modDescription = QTextBrowser(self.modDescriptionsAndActions)
        self.modDescription.setObjectName(u"modDescription")
        self.modDescription.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Roboto Medium"])
        self.modDescription.setFont(font3)
        self.modDescription.setStyleSheet(u"QToolTip { \n"
"                           background-color: black; \n"
"                           color: white; \n"
"                           border: black solid 1px\n"
"}")
        self.modDescription.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.modDescription.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.modDescription.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.modDescription.setLineWrapMode(QTextEdit.WidgetWidth)
        self.modDescription.setOpenExternalLinks(True)

        self.verticalLayout_13.addWidget(self.modDescription, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.modDescriptionsAndActions, 0, Qt.AlignTop)


        self.retranslateUi(ModBody)

        QMetaObject.connectSlotsByName(ModBody)
    # setupUi

    def retranslateUi(self, ModBody):
        ModBody.setWindowTitle(QCoreApplication.translate("ModBody", u"Form", None))
        self.leftPreview.setText("")
        self.rightPreview.setText("")
        self.modName.setText(QCoreApplication.translate("ModBody", u"Brawlhalla Modloader", None))
        self.modSource.setText(QCoreApplication.translate("ModBody", u"Source:", None))
        self.modVersion.setText(QCoreApplication.translate("ModBody", u"Version:", None))
        self.modPreview.setText("")
        self.modTags.setText(QCoreApplication.translate("ModBody", u"Tags:", None))
        self.modDescription.setHtml(QCoreApplication.translate("ModBody", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto Medium'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

