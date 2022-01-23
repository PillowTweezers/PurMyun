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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from gui.fancy_progress_bar_widget import FancyProgressBarWidget

class Ui_ParticipantDialog(object):
    def setupUi(self, ParticipantDialog):
        if not ParticipantDialog.objectName():
            ParticipantDialog.setObjectName(u"ParticipantDialog")
        ParticipantDialog.resize(417, 134)
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

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.teamLbl = QLabel(self.widget)
        self.teamLbl.setObjectName(u"teamLbl")
        self.teamLbl.setStyleSheet(u"font-size:16px;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.teamLbl)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.gradeLbl = QLabel(self.widget)
        self.gradeLbl.setObjectName(u"gradeLbl")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.gradeLbl)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:16px;font-weight:bold;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.progressBarWidget = FancyProgressBarWidget(self.widget)
        self.progressBarWidget.setObjectName(u"progressBarWidget")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.progressBarWidget)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(ParticipantDialog)

        QMetaObject.connectSlotsByName(ParticipantDialog)
    # setupUi

    def retranslateUi(self, ParticipantDialog):
        ParticipantDialog.setWindowTitle(QCoreApplication.translate("ParticipantDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e9\u05dd:", None))
        self.nameLbl.setText("")
        self.label_3.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e6\u05d5\u05d5\u05ea:", None))
        self.teamLbl.setText(QCoreApplication.translate("ParticipantDialog", u"\u05d0\u05d9\u05e0\u05d5 \u05de\u05e6\u05d5\u05d5\u05ea", None))
        self.label_12.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e9\u05db\u05d1\u05d4:", None))
        self.gradeLbl.setText("")
        self.label_2.setText(QCoreApplication.translate("ParticipantDialog", u"\u05e6\u05d9\u05d5\u05df:", None))
    # retranslateUi

