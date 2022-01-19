# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractScrollArea, QDockWidget, QHBoxLayout,
                               QLineEdit, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QStatusBar, QTableWidget, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 571)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.actionCreate_Team = QAction(MainWindow)
        self.actionCreate_Team.setObjectName(u"actionCreate_Team")
        font = QFont()
        font.setPointSize(14)
        self.actionCreate_Team.setFont(font)
        self.actionCreate_Participant = QAction(MainWindow)
        self.actionCreate_Participant.setObjectName(u"actionCreate_Participant")
        self.actionCreate_Participant.setFont(font)
        self.actionLoad_Participants_File = QAction(MainWindow)
        self.actionLoad_Participants_File.setObjectName(u"actionLoad_Participants_File")
        self.actionLoad_Participants_File.setFont(font)
        self.loadParticipantsFileAction = QAction(MainWindow)
        self.loadParticipantsFileAction.setObjectName(u"loadParticipantsFileAction")
        icon = QIcon()
        icon.addFile(u":/assets/form.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadParticipantsFileAction.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(139, 139, 139)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setLayoutDirection(Qt.RightToLeft)
        self.menuFile.setStyleSheet(u"")
        self.menuEfit = QMenu(self.menubar)
        self.menuEfit.setObjectName(u"menuEfit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.controlsDock = QDockWidget(MainWindow)
        self.controlsDock.setObjectName(u"controlsDock")
        self.controlsDock.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.createTeamBtn = QPushButton(self.dockWidgetContents)
        self.createTeamBtn.setObjectName(u"createTeamBtn")

        self.verticalLayout.addWidget(self.createTeamBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.controlsDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.controlsDock)
        self.participantsDock = QDockWidget(MainWindow)
        self.participantsDock.setObjectName(u"participantsDock")
        self.participantsDock.setMinimumSize(QSize(253, 532))
        self.participantsDock.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nameFilterEdt = QLineEdit(self.dockWidgetContents_2)
        self.nameFilterEdt.setObjectName(u"nameFilterEdt")

        self.horizontalLayout.addWidget(self.nameFilterEdt)

        self.addParticipantBtn = QPushButton(self.dockWidgetContents_2)
        self.addParticipantBtn.setObjectName(u"addParticipantBtn")
        icon1 = QIcon()
        icon1.addFile(u":/assets/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addParticipantBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.addParticipantBtn)

        self.removeParticipantBtn = QPushButton(self.dockWidgetContents_2)
        self.removeParticipantBtn.setObjectName(u"removeParticipantBtn")
        icon2 = QIcon()
        icon2.addFile(u":/assets/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeParticipantBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.removeParticipantBtn)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.participantsTableWidget = QTableWidget(self.dockWidgetContents_2)
        self.participantsTableWidget.setObjectName(u"participantsTableWidget")
        self.participantsTableWidget.setMinimumSize(QSize(0, 454))
        self.participantsTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.participantsTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.participantsTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.participantsTableWidget)

        self.participantsDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.participantsDock)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEfit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.loadParticipantsFileAction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u05e4\u05d5\u05e8\u05de\u05d9\u05d5\u05df", None))
        self.actionCreate_Team.setText(QCoreApplication.translate("MainWindow", u"Create Team", None))
        # if QT_CONFIG(shortcut)
        self.actionCreate_Team.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
        # endif // QT_CONFIG(shortcut)
        self.actionCreate_Participant.setText(QCoreApplication.translate("MainWindow", u"Create Participant", None))
        self.actionLoad_Participants_File.setText(
            QCoreApplication.translate("MainWindow", u"Load Participants File", None))
        # if QT_CONFIG(tooltip)
        self.actionLoad_Participants_File.setToolTip(
            QCoreApplication.translate("MainWindow", u"Load Participants File", None))
        # endif // QT_CONFIG(tooltip)
        self.loadParticipantsFileAction.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u05e4\u05ea\u05d7 \u05e7\u05d5\u05d1\u05e5 \u05de\u05e9\u05ea\u05de\u05e9\u05d9\u05dd...",
                                                                           None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u05e7\u05d5\u05d1\u05e5", None))
        self.menuEfit.setTitle(QCoreApplication.translate("MainWindow", u"\u05e2\u05e8\u05d9\u05db\u05d4", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"\u05ea\u05e6\u05d5\u05d2\u05d4", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u05e2\u05d6\u05e8\u05d4", None))
        self.controlsDock.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u05e4\u05e2\u05d5\u05dc\u05d5\u05ea", None))
        self.createTeamBtn.setText(
            QCoreApplication.translate("MainWindow", u"\u05e6\u05d5\u05e8 \u05e7\u05d1\u05d5\u05e6\u05d4", None))
        self.participantsDock.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u05de\u05e9\u05ea\u05ea\u05e4\u05d9\u05dd", None))
        self.nameFilterEdt.setText("")
        self.nameFilterEdt.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u05e4\u05d9\u05dc\u05d8\u05e8", None))
        self.addParticipantBtn.setText("")
        self.removeParticipantBtn.setText("")
    # retranslateUi

