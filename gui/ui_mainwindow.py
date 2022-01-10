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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDockWidget, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 570)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(139, 139, 139)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
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
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.createTeamBtn = QPushButton(self.dockWidgetContents)
        self.createTeamBtn.setObjectName(u"createTeamBtn")

        self.verticalLayout.addWidget(self.createTeamBtn)

        self.createParticipantsBtn = QPushButton(self.dockWidgetContents)
        self.createParticipantsBtn.setObjectName(u"createParticipantsBtn")

        self.verticalLayout.addWidget(self.createParticipantsBtn)

        self.loadParticipantsBtn = QPushButton(self.dockWidgetContents)
        self.loadParticipantsBtn.setObjectName(u"loadParticipantsBtn")

        self.verticalLayout.addWidget(self.loadParticipantsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.controlsDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.controlsDock)
        self.participantsDock = QDockWidget(MainWindow)
        self.participantsDock.setObjectName(u"participantsDock")
        self.participantsDock.setMinimumSize(QSize(228, 524))
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameFilterEdt = QLineEdit(self.dockWidgetContents_2)
        self.nameFilterEdt.setObjectName(u"nameFilterEdt")

        self.verticalLayout_2.addWidget(self.nameFilterEdt)

        self.listView = QListView(self.dockWidgetContents_2)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(0, 454))
        self.listView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_2.addWidget(self.listView)

        self.participantsDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.participantsDock)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEfit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

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
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEfit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.controlsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.createTeamBtn.setText(QCoreApplication.translate("MainWindow", u"Create \n"
"Team", None))
        self.createParticipantsBtn.setText(QCoreApplication.translate("MainWindow", u"Create \n"
"Participant", None))
        self.loadParticipantsBtn.setText(QCoreApplication.translate("MainWindow", u"Load \n"
"Participants File", None))
        self.participantsDock.setWindowTitle(QCoreApplication.translate("MainWindow", u"Participants", None))
        self.nameFilterEdt.setText("")
        self.nameFilterEdt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter", None))
    # retranslateUi

