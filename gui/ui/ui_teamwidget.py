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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.squareLbl = QLabel(self.groupBox)
        self.squareLbl.setObjectName(u"squareLbl")
        self.squareLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.squareLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.squareLbl, 1, 2, 1, 1)

        self.macrameLbl = QLabel(self.groupBox)
        self.macrameLbl.setObjectName(u"macrameLbl")
        self.macrameLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.macrameLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.macrameLbl, 11, 2, 1, 1)

        self.squareBar = QProgressBar(self.groupBox)
        self.squareBar.setObjectName(u"squareBar")
        self.squareBar.setValue(0)

        self.gridLayout.addWidget(self.squareBar, 1, 1, 1, 1)

        self.anchoringLbl = QLabel(self.groupBox)
        self.anchoringLbl.setObjectName(u"anchoringLbl")
        self.anchoringLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.anchoringLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.anchoringLbl, 9, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)

        self.anchoringBar = QProgressBar(self.groupBox)
        self.anchoringBar.setObjectName(u"anchoringBar")
        self.anchoringBar.setValue(0)

        self.gridLayout.addWidget(self.anchoringBar, 9, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.tripodLbl = QLabel(self.groupBox)
        self.tripodLbl.setObjectName(u"tripodLbl")
        self.tripodLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.tripodLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tripodLbl, 7, 2, 1, 1)

        self.crossLbl = QLabel(self.groupBox)
        self.crossLbl.setObjectName(u"crossLbl")
        self.crossLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.crossLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.crossLbl, 3, 2, 1, 1)

        self.crossBar = QProgressBar(self.groupBox)
        self.crossBar.setObjectName(u"crossBar")
        self.crossBar.setValue(0)

        self.gridLayout.addWidget(self.crossBar, 3, 1, 1, 1)

        self.parallelBar = QProgressBar(self.groupBox)
        self.parallelBar.setObjectName(u"parallelBar")
        self.parallelBar.setValue(0)

        self.gridLayout.addWidget(self.parallelBar, 5, 1, 1, 1)

        self.parallelLbl = QLabel(self.groupBox)
        self.parallelLbl.setObjectName(u"parallelLbl")
        self.parallelLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.parallelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.parallelLbl, 5, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.macrameBar = QProgressBar(self.groupBox)
        self.macrameBar.setObjectName(u"macrameBar")
        self.macrameBar.setValue(0)

        self.gridLayout.addWidget(self.macrameBar, 11, 1, 1, 1)

        self.tripodBar = QProgressBar(self.groupBox)
        self.tripodBar.setObjectName(u"tripodBar")
        self.tripodBar.setValue(0)

        self.gridLayout.addWidget(self.tripodBar, 7, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

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
        self.verticalLayout_2.setContentsMargins(80, 0, 80, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.participantTableWidget = ParticipantTableWidget(self.widget)
        self.participantTableWidget.setObjectName(u"participantTableWidget")

        self.horizontalLayout_2.addWidget(self.participantTableWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.widget)

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
        self.label_3.setText(QCoreApplication.translate("TeamWidget", u"\u05de\u05d3\u05d3\u05d9 \u05d7\u05e9\u05d9\u05d1\u05d5\u05ea:", None))
        self.groupBox.setTitle("")
        self.squareLbl.setText("")
        self.macrameLbl.setText("")
        self.squareBar.setFormat("")
        self.anchoringLbl.setText("")
        self.label_11.setText(QCoreApplication.translate("TeamWidget", u"\u05de\u05e7\u05e8\u05de\u05d4", None))
        self.anchoringBar.setFormat("")
        self.label_8.setText(QCoreApplication.translate("TeamWidget", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e7\u05d1\u05d9\u05dc\u05d4", None))
        self.label_9.setText(QCoreApplication.translate("TeamWidget", u"\u05db\u05e4\u05d9\u05ea\u05ea\n"
"\u05d7\u05e6\u05d5\u05d1\u05d4", None))
        self.label_7.setText(QCoreApplication.translate("TeamWidget", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05d5\u05e6\u05dc\u05d1\u05ea", None))
        self.tripodLbl.setText("")
        self.crossLbl.setText("")
        self.crossBar.setFormat("")
        self.parallelBar.setFormat("")
        self.parallelLbl.setText("")
        self.label_6.setText(QCoreApplication.translate("TeamWidget", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e8\u05d5\u05d1\u05e2\u05ea", None))
        self.label_10.setText(QCoreApplication.translate("TeamWidget", u"\u05e2\u05d9\u05d2\u05d5\u05df\n"
"\u05d9\u05ea\u05e8\u05d9\u05dd", None))
        self.macrameBar.setFormat("")
        self.tripodBar.setFormat("")
        self.editBtn.setText(QCoreApplication.translate("TeamWidget", u"\u05e2\u05e8\u05d5\u05da", None))
        self.label_2.setText(QCoreApplication.translate("TeamWidget", u"\u05d7\u05d1\u05e8\u05d9 \u05e6\u05d5\u05d5\u05ea:", None))
    # retranslateUi

