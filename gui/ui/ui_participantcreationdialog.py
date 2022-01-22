# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'participantcreationdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from gui.FancySliderHorizontalWidget import FancySliderHorizontalWidget
from gui.StatsWidget import StatsWidget

class Ui_ParticipantCreationDialog(object):
    def setupUi(self, ParticipantCreationDialog):
        if not ParticipantCreationDialog.objectName():
            ParticipantCreationDialog.setObjectName(u"ParticipantCreationDialog")
        ParticipantCreationDialog.resize(607, 584)
        ParticipantCreationDialog.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(ParticipantCreationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(ParticipantCreationDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nameLineEdt = QLineEdit(ParticipantCreationDialog)
        self.nameLineEdt.setObjectName(u"nameLineEdt")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdt.sizePolicy().hasHeightForWidth())
        self.nameLineEdt.setSizePolicy(sizePolicy)
        self.nameLineEdt.setMinimumSize(QSize(180, 0))
        self.nameLineEdt.setDragEnabled(False)
        self.nameLineEdt.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.nameLineEdt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_3 = QLabel(ParticipantCreationDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gradesComboBox = QComboBox(ParticipantCreationDialog)
        self.gradesComboBox.setObjectName(u"gradesComboBox")

        self.horizontalLayout.addWidget(self.gradesComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QLabel(ParticipantCreationDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(ParticipantCreationDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.presenceWidget = FancySliderHorizontalWidget(self.groupBox)
        self.presenceWidget.setObjectName(u"presenceWidget")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.presenceWidget)

        self.motivationWidget = FancySliderHorizontalWidget(self.groupBox)
        self.motivationWidget.setObjectName(u"motivationWidget")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.motivationWidget)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.statsWidget = StatsWidget(self.groupBox)
        self.statsWidget.setObjectName(u"statsWidget")

        self.verticalLayout_3.addWidget(self.statsWidget)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.verticalLayout_2)

        self.label_4 = QLabel(ParticipantCreationDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.groupBox_2 = QGroupBox(ParticipantCreationDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font-size:16px;")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-size:16px;")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font-size:16px;")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.preferenceCComboBox = QComboBox(self.groupBox_2)
        self.preferenceCComboBox.setObjectName(u"preferenceCComboBox")

        self.horizontalLayout_6.addWidget(self.preferenceCComboBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.preferenceBComboBox = QComboBox(self.groupBox_2)
        self.preferenceBComboBox.setObjectName(u"preferenceBComboBox")

        self.horizontalLayout_5.addWidget(self.preferenceBComboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.preferenceAComboBox = QComboBox(self.groupBox_2)
        self.preferenceAComboBox.setObjectName(u"preferenceAComboBox")

        self.horizontalLayout_4.addWidget(self.preferenceAComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.groupBox_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(ParticipantCreationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ParticipantCreationDialog)
        self.buttonBox.accepted.connect(ParticipantCreationDialog.accept)
        self.buttonBox.rejected.connect(ParticipantCreationDialog.reject)

        QMetaObject.connectSlotsByName(ParticipantCreationDialog)
    # setupUi

    def retranslateUi(self, ParticipantCreationDialog):
        ParticipantCreationDialog.setWindowTitle(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d9\u05e6\u05d9\u05e8\u05ea \u05de\u05e9\u05ea\u05ea\u05e3", None))
        self.label.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05e9\u05dd:", None))
        self.nameLineEdt.setPlaceholderText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05e9\u05dd \u05de\u05dc\u05d0", None))
        self.label_3.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05e9\u05db\u05d1\u05d4:", None))
        self.label_2.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05de\u05d3\u05d3\u05d9\u05dd:", None))
        self.groupBox.setTitle("")
        self.label_11.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05de\u05d7\u05d5\u05d9\u05d1\u05d5\u05ea:", None))
        self.label_12.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05de\u05d5\u05d8\u05d9\u05d1\u05e6\u05d9\u05d4:", None))
        self.label_4.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d4\u05e2\u05d3\u05e4\u05d5\u05ea:", None))
        self.groupBox_2.setTitle("")
        self.label_19.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d0':", None))
        self.label_21.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d1':", None))
        self.label_20.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d2':", None))
    # retranslateUi

