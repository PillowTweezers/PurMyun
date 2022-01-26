# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from gui.ParticipantTableWidget import ParticipantTableWidget
import mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 579)
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
        self.saveAsAction = QAction(MainWindow)
        self.saveAsAction.setObjectName(u"saveAsAction")
        icon1 = QIcon()
        icon1.addFile(u":/assets/saveAs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveAsAction.setIcon(icon1)
        self.saveAction = QAction(MainWindow)
        self.saveAction.setObjectName(u"saveAction")
        icon2 = QIcon()
        icon2.addFile(u":/assets/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveAction.setIcon(icon2)
        self.openAction = QAction(MainWindow)
        self.openAction.setObjectName(u"openAction")
        icon3 = QIcon()
        icon3.addFile(u":/assets/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openAction.setIcon(icon3)
        self.quitAction = QAction(MainWindow)
        self.quitAction.setObjectName(u"quitAction")
        icon4 = QIcon()
        icon4.addFile(u":/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.quitAction.setIcon(icon4)
        self.newAction = QAction(MainWindow)
        self.newAction.setObjectName(u"newAction")
        icon5 = QIcon()
        icon5.addFile(u":/assets/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newAction.setIcon(icon5)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.recentAction1 = QAction(MainWindow)
        self.recentAction1.setObjectName(u"recentAction1")
        self.recentAction1.setVisible(True)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_2.setVisible(True)
        self.recentAction3 = QAction(MainWindow)
        self.recentAction3.setObjectName(u"recentAction3")
        self.recentAction3.setVisible(True)
        self.recentAction4 = QAction(MainWindow)
        self.recentAction4.setObjectName(u"recentAction4")
        self.recentAction4.setVisible(True)
        self.exportExcelAction = QAction(MainWindow)
        self.exportExcelAction.setObjectName(u"exportExcelAction")
        icon6 = QIcon()
        icon6.addFile(u":/assets/export_excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportExcelAction.setIcon(icon6)
        self.resetUiAction = QAction(MainWindow)
        self.resetUiAction.setObjectName(u"resetUiAction")
        icon7 = QIcon()
        icon7.addFile(u":/assets/reset_view.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetUiAction.setIcon(icon7)
        self.resizeTablesAction = QAction(MainWindow)
        self.resizeTablesAction.setObjectName(u"resizeTablesAction")
        icon8 = QIcon()
        icon8.addFile(u":/assets/resize_tables.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resizeTablesAction.setIcon(icon8)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.teamsTabWidget = QTabWidget(self.centralwidget)
        self.teamsTabWidget.setObjectName(u"teamsTabWidget")
        self.teamsTabWidget.setTabsClosable(True)
        self.teamsTabWidget.setMovable(True)

        self.verticalLayout_3.addWidget(self.teamsTabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setLayoutDirection(Qt.RightToLeft)
        self.menuFile.setStyleSheet(u"")
        self.recentFilesMenu = QMenu(self.menuFile)
        self.recentFilesMenu.setObjectName(u"recentFilesMenu")
        icon9 = QIcon()
        icon9.addFile(u":/assets/recent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recentFilesMenu.setIcon(icon9)
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
        self.controlsDock.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.createTeamBtn = QPushButton(self.dockWidgetContents)
        self.createTeamBtn.setObjectName(u"createTeamBtn")
        self.createTeamBtn.setStyleSheet(u"text-align: center;")
        icon10 = QIcon()
        icon10.addFile(u":/assets/create_team.png", QSize(), QIcon.Normal, QIcon.Off)
        self.createTeamBtn.setIcon(icon10)

        self.verticalLayout.addWidget(self.createTeamBtn)

        self.line = QFrame(self.dockWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.assignTeamsBtn = QPushButton(self.dockWidgetContents)
        self.assignTeamsBtn.setObjectName(u"assignTeamsBtn")
        self.assignTeamsBtn.setStyleSheet(u"text-align: center;")
        icon11 = QIcon()
        icon11.addFile(u":/assets/sorting_hat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.assignTeamsBtn.setIcon(icon11)

        self.verticalLayout.addWidget(self.assignTeamsBtn)

        self.line_2 = QFrame(self.dockWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gradesBtn = QPushButton(self.dockWidgetContents)
        self.gradesBtn.setObjectName(u"gradesBtn")
        self.gradesBtn.setStyleSheet(u"text-align: center;")
        icon12 = QIcon()
        icon12.addFile(u":/assets/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gradesBtn.setIcon(icon12)

        self.verticalLayout.addWidget(self.gradesBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.controlsDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.controlsDock)
        self.participantsDock = QDockWidget(MainWindow)
        self.participantsDock.setObjectName(u"participantsDock")
        self.participantsDock.setEnabled(True)
        self.participantsDock.setMinimumSize(QSize(253, 532))
        self.participantsDock.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.participantDockLayout = QWidget()
        self.participantDockLayout.setObjectName(u"participantDockLayout")
        self.verticalLayout_2 = QVBoxLayout(self.participantDockLayout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.participantsTableWidget = ParticipantTableWidget(self.participantDockLayout)
        self.participantsTableWidget.setObjectName(u"participantsTableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.participantsTableWidget.sizePolicy().hasHeightForWidth())
        self.participantsTableWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.participantsTableWidget)

        self.participantsDock.setWidget(self.participantDockLayout)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.participantsDock)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEfit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.newAction)
        self.menuFile.addAction(self.openAction)
        self.menuFile.addAction(self.recentFilesMenu.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.saveAsAction)
        self.menuFile.addAction(self.saveAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.loadParticipantsFileAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exportExcelAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quitAction)
        self.menuView.addAction(self.resetUiAction)
        self.menuView.addSeparator()
        self.menuView.addAction(self.resizeTablesAction)

        self.retranslateUi(MainWindow)

        self.teamsTabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u05e4\u05d5\u05e8\u05de\u05d9\u05d5\u05df", None))
        self.actionCreate_Team.setText(QCoreApplication.translate("MainWindow", u"Create Team", None))
#if QT_CONFIG(shortcut)
        self.actionCreate_Team.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreate_Participant.setText(QCoreApplication.translate("MainWindow", u"Create Participant", None))
        self.actionLoad_Participants_File.setText(QCoreApplication.translate("MainWindow", u"Load Participants File", None))
#if QT_CONFIG(tooltip)
        self.actionLoad_Participants_File.setToolTip(QCoreApplication.translate("MainWindow", u"Load Participants File", None))
#endif // QT_CONFIG(tooltip)
        self.loadParticipantsFileAction.setText(QCoreApplication.translate("MainWindow", u"\u05e4\u05ea\u05d7 \u05e7\u05d5\u05d1\u05e5 \u05de\u05e9\u05ea\u05de\u05e9\u05d9\u05dd...", None))
        self.saveAsAction.setText(QCoreApplication.translate("MainWindow", u"\u05e9\u05de\u05d5\u05e8 \u05e4\u05e8\u05d5\u05d9\u05e7\u05d8 \u05d1\u05e9\u05dd...", None))
#if QT_CONFIG(shortcut)
        self.saveAsAction.setShortcut(QCoreApplication.translate("MainWindow", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.saveAction.setText(QCoreApplication.translate("MainWindow", u"\u05e9\u05de\u05d5\u05e8 \u05e4\u05e8\u05d5\u05d9\u05e7\u05d8", None))
#if QT_CONFIG(shortcut)
        self.saveAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.openAction.setText(QCoreApplication.translate("MainWindow", u"\u05e4\u05ea\u05d7 \u05e4\u05e8\u05d5\u05d9\u05e7\u05d8...", None))
#if QT_CONFIG(shortcut)
        self.openAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.quitAction.setText(QCoreApplication.translate("MainWindow", u"\u05e6\u05d0", None))
#if QT_CONFIG(shortcut)
        self.quitAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.newAction.setText(QCoreApplication.translate("MainWindow", u"\u05e6\u05d5\u05e8 \u05e4\u05e8\u05d5\u05d9\u05e7\u05d8 \u05d7\u05d3\u05e9...", None))
#if QT_CONFIG(shortcut)
        self.newAction.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u05d1\u05d3\u05d9\u05e7\u05d4", None))
        self.recentAction1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.recentAction3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.recentAction4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.exportExcelAction.setText(QCoreApplication.translate("MainWindow", u"\u05d9\u05e6\u05d0 \u05dc\u05d0\u05e7\u05e1\u05dc...", None))
        self.resetUiAction.setText(QCoreApplication.translate("MainWindow", u"\u05d0\u05e4\u05e1 \u05de\u05de\u05e9\u05e7", None))
        self.resizeTablesAction.setText(QCoreApplication.translate("MainWindow", u"\u05d0\u05e4\u05e1 \u05d8\u05d1\u05dc\u05d0\u05d5\u05ea", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u05e7\u05d5\u05d1\u05e5", None))
        self.recentFilesMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u05e4\u05e8\u05d5\u05d9\u05e7\u05d8\u05d9\u05dd \u05d0\u05d7\u05e8\u05d5\u05e0\u05d9\u05dd", None))
        self.menuEfit.setTitle(QCoreApplication.translate("MainWindow", u"\u05e2\u05e8\u05d9\u05db\u05d4", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"\u05ea\u05e6\u05d5\u05d2\u05d4", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u05e2\u05d6\u05e8\u05d4", None))
        self.controlsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u05e4\u05e2\u05d5\u05dc\u05d5\u05ea", None))
        self.createTeamBtn.setText(QCoreApplication.translate("MainWindow", u"\u05e6\u05d5\u05e8 \u05e6\u05d5\u05d5\u05ea", None))
        self.assignTeamsBtn.setText(QCoreApplication.translate("MainWindow", u"\u05de\u05e6\u05e0\u05e4\u05ea \u05d4\u05de\u05d9\u05d5\u05df", None))
        self.gradesBtn.setText(QCoreApplication.translate("MainWindow", u"\u05e1\u05d3\u05e8  \u05e9\u05db\u05d1\u05d5\u05ea", None))
        self.participantsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u05de\u05e9\u05ea\u05ea\u05e4\u05d9\u05dd", None))
    # retranslateUi

