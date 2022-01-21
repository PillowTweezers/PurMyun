# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'participantdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QProgressBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ParticipantDialog(object):
    def setupUi(self, ParticipantDialog):
        if not ParticipantDialog.objectName():
            ParticipantDialog.setObjectName(u"ParticipantDialog")
        ParticipantDialog.resize(492, 519)
        self.verticalLayout = QVBoxLayout(ParticipantDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ParticipantDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setLayoutDirection(Qt.RightToLeft)
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nameLbl = QLabel(self.widget)
        self.nameLbl.setObjectName(u"nameLbl")
        self.nameLbl.setStyleSheet(u"font-size:16px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLbl)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.teamLbl = QLabel(self.widget)
        self.teamLbl.setObjectName(u"teamLbl")
        self.teamLbl.setStyleSheet(u"font-size:16px;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.teamLbl)


        self.verticalLayout.addWidget(self.widget)

        self.line_4 = QFrame(ParticipantDialog)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.label_2 = QLabel(ParticipantDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.verticalLayout.addWidget(self.label_2)

        self.groupBox = QGroupBox(ParticipantDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)

        self.presenceBar = QProgressBar(self.groupBox)
        self.presenceBar.setObjectName(u"presenceBar")
        self.presenceBar.setLayoutDirection(Qt.RightToLeft)
        self.presenceBar.setValue(0)

        self.gridLayout.addWidget(self.presenceBar, 0, 1, 1, 1)

        self.anchoringBar = QProgressBar(self.groupBox)
        self.anchoringBar.setObjectName(u"anchoringBar")
        self.anchoringBar.setValue(0)

        self.gridLayout.addWidget(self.anchoringBar, 6, 1, 1, 1)

        self.squareBar = QProgressBar(self.groupBox)
        self.squareBar.setObjectName(u"squareBar")
        self.squareBar.setValue(0)

        self.gridLayout.addWidget(self.squareBar, 2, 1, 1, 1)

        self.macrameBar = QProgressBar(self.groupBox)
        self.macrameBar.setObjectName(u"macrameBar")
        self.macrameBar.setValue(0)

        self.gridLayout.addWidget(self.macrameBar, 7, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.crossBar = QProgressBar(self.groupBox)
        self.crossBar.setObjectName(u"crossBar")
        self.crossBar.setValue(0)

        self.gridLayout.addWidget(self.crossBar, 3, 1, 1, 1)

        self.parallelLbl = QLabel(self.groupBox)
        self.parallelLbl.setObjectName(u"parallelLbl")
        self.parallelLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.parallelLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.parallelLbl, 4, 2, 1, 1)

        self.tripodBar = QProgressBar(self.groupBox)
        self.tripodBar.setObjectName(u"tripodBar")
        self.tripodBar.setValue(0)

        self.gridLayout.addWidget(self.tripodBar, 5, 1, 1, 1)

        self.parallelBar = QProgressBar(self.groupBox)
        self.parallelBar.setObjectName(u"parallelBar")
        self.parallelBar.setValue(0)

        self.gridLayout.addWidget(self.parallelBar, 4, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.squareLbl = QLabel(self.groupBox)
        self.squareLbl.setObjectName(u"squareLbl")
        self.squareLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.squareLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.squareLbl, 2, 2, 1, 1)

        self.crossLbl = QLabel(self.groupBox)
        self.crossLbl.setObjectName(u"crossLbl")
        self.crossLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.crossLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.crossLbl, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.tripodLbl = QLabel(self.groupBox)
        self.tripodLbl.setObjectName(u"tripodLbl")
        self.tripodLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.tripodLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.tripodLbl, 5, 2, 1, 1)

        self.presenceLbl = QLabel(self.groupBox)
        self.presenceLbl.setObjectName(u"presenceLbl")
        self.presenceLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.presenceLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.presenceLbl, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.anchoringLbl = QLabel(self.groupBox)
        self.anchoringLbl.setObjectName(u"anchoringLbl")
        self.anchoringLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.anchoringLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.anchoringLbl, 6, 2, 1, 1)

        self.macrameLbl = QLabel(self.groupBox)
        self.macrameLbl.setObjectName(u"macrameLbl")
        self.macrameLbl.setStyleSheet(u"font-weight:bold;font-size:16px;")
        self.macrameLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.macrameLbl, 7, 2, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.line_5 = QFrame(ParticipantDialog)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.widget_2 = QWidget(ParticipantDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setLayoutDirection(Qt.RightToLeft)
        self.formLayout_3 = QFormLayout(self.widget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.preferencesA = QLabel(self.widget_2)
        self.preferencesA.setObjectName(u"preferencesA")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.preferencesA)

        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.preferencesB = QLabel(self.widget_2)
        self.preferencesB.setObjectName(u"preferencesB")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.preferencesB)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.preferencesC = QLabel(self.widget_2)
        self.preferencesC.setObjectName(u"preferencesC")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.preferencesC)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(ParticipantDialog)

        QMetaObject.connectSlotsByName(ParticipantDialog)
    # setupUi

    def retranslateUi(self, ParticipantDialog):
        ParticipantDialog.setWindowTitle(QCoreApplication.translate("ParticipantDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e9\u05dd:", None))
        self.nameLbl.setText("")
        self.label_3.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e6\u05d5\u05d5\u05ea:", None))
        self.teamLbl.setText(QCoreApplication.translate("ParticipantDialog", u"\u05d0\u05d9\u05e0\u05d5 \u05de\u05e6\u05d5\u05d5\u05ea", None))
        self.label_2.setText(QCoreApplication.translate("ParticipantDialog", u"\u05de\u05d3\u05d3\u05d9\u05dd:", None))
        self.groupBox.setTitle("")
        self.label_11.setText(QCoreApplication.translate("ParticipantDialog", u"\u05de\u05e7\u05e8\u05de\u05d4", None))
        self.presenceBar.setFormat("")
        self.anchoringBar.setFormat("")
        self.squareBar.setFormat("")
        self.macrameBar.setFormat("")
        self.label_10.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e2\u05d9\u05d2\u05d5\u05df\n"
"\u05d9\u05ea\u05e8\u05d9\u05dd", None))
        self.crossBar.setFormat("")
        self.parallelLbl.setText("")
        self.tripodBar.setFormat("")
        self.parallelBar.setFormat("")
        self.label_9.setText(QCoreApplication.translate("ParticipantDialog", u"\u05db\u05e4\u05d9\u05ea\u05ea\n"
"\u05d7\u05e6\u05d5\u05d1\u05d4", None))
        self.squareLbl.setText("")
        self.crossLbl.setText("")
        self.label_8.setText(QCoreApplication.translate("ParticipantDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e7\u05d1\u05d9\u05dc\u05d4", None))
        self.tripodLbl.setText("")
        self.presenceLbl.setText("")
        self.label_5.setText(QCoreApplication.translate("ParticipantDialog", u"\u05de\u05d7\u05d5\u05d9\u05d1\u05d5\u05ea", None))
        self.label_6.setText(QCoreApplication.translate("ParticipantDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e8\u05d5\u05d1\u05e2\u05ea", None))
        self.label_7.setText(QCoreApplication.translate("ParticipantDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05d5\u05e6\u05dc\u05d1\u05ea", None))
        self.anchoringLbl.setText("")
        self.macrameLbl.setText("")
        self.preferencesA.setText("")
        self.label_14.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e2\u05d3\u05d9\u05e4\u05d5\u05ea \u05d0':", None))
        self.label_16.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e2\u05d3\u05d9\u05e4\u05d5\u05ea \u05d1':", None))
        self.preferencesB.setText("")
        self.label_13.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e2\u05d3\u05d9\u05e4\u05d5\u05ea \u05d2':", None))
        self.preferencesC.setText("")
    # retranslateUi

