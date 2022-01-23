# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teamwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from gui.ParticipantTableWidget import ParticipantTableWidget
import mainwindow_rc

class Ui_TeamWidget(object):
    def setupUi(self, TeamWidget):
        if not TeamWidget.objectName():
            TeamWidget.setObjectName(u"TeamWidget")
        TeamWidget.resize(539, 568)
        TeamWidget.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(TeamWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.scrollArea = QScrollArea(TeamWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 535, 564))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.teamNameLbl = QLabel(self.scrollAreaWidgetContents)
        self.teamNameLbl.setObjectName(u"teamNameLbl")

        self.horizontalLayout_4.addWidget(self.teamNameLbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editBtn = QPushButton(self.scrollAreaWidgetContents)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setStyleSheet(u"text-align: center;")
        icon = QIcon()
        icon.addFile(u":/assets/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.editBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(80, 0, 80, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.participantTableWidget = ParticipantTableWidget(self.widget)
        self.participantTableWidget.setObjectName(u"participantTableWidget")

        self.horizontalLayout_2.addWidget(self.participantTableWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.deleteTeamBtn = QPushButton(self.scrollAreaWidgetContents)
        self.deleteTeamBtn.setObjectName(u"deleteTeamBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteTeamBtn.sizePolicy().hasHeightForWidth())
        self.deleteTeamBtn.setSizePolicy(sizePolicy)
        self.deleteTeamBtn.setMinimumSize(QSize(180, 0))
        self.deleteTeamBtn.setStyleSheet(u"font-weight:bold;font-size:18px;background:darkred;text-align: center;")
        icon1 = QIcon()
        icon1.addFile(u":/assets/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteTeamBtn.setIcon(icon1)
        self.deleteTeamBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.deleteTeamBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(TeamWidget)

        QMetaObject.connectSlotsByName(TeamWidget)
    # setupUi

    def retranslateUi(self, TeamWidget):
        TeamWidget.setWindowTitle(QCoreApplication.translate("TeamWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("TeamWidget", u"\u05e9\u05dd:", None))
        self.teamNameLbl.setText("")
        self.editBtn.setText(QCoreApplication.translate("TeamWidget", u"\u05e2\u05e8\u05d5\u05da", None))
        self.label_2.setText(QCoreApplication.translate("TeamWidget", u"\u05d7\u05d1\u05e8\u05d9 \u05e6\u05d5\u05d5\u05ea:", None))
        self.deleteTeamBtn.setText(QCoreApplication.translate("TeamWidget", u"\u05de\u05d7\u05e7 \u05e6\u05d5\u05d5\u05ea", None))
    # retranslateUi

