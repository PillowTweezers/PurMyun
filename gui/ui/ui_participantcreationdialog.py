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
    QDialogButtonBox, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ParticipantCreationDialog(object):
    def setupUi(self, ParticipantCreationDialog):
        if not ParticipantCreationDialog.objectName():
            ParticipantCreationDialog.setObjectName(u"ParticipantCreationDialog")
        ParticipantCreationDialog.resize(607, 563)
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

        self.presenceSlider = QSlider(self.groupBox)
        self.presenceSlider.setObjectName(u"presenceSlider")
        self.presenceSlider.setMinimum(1)
        self.presenceSlider.setMaximum(10)
        self.presenceSlider.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.presenceSlider)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.motivationSlider = QSlider(self.groupBox)
        self.motivationSlider.setObjectName(u"motivationSlider")
        self.motivationSlider.setMinimum(1)
        self.motivationSlider.setMaximum(5)
        self.motivationSlider.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.motivationSlider)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(2)
        self.anchoringSlider = QSlider(self.groupBox)
        self.anchoringSlider.setObjectName(u"anchoringSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.anchoringSlider.sizePolicy().hasHeightForWidth())
        self.anchoringSlider.setSizePolicy(sizePolicy1)
        self.anchoringSlider.setMinimumSize(QSize(0, 140))
        self.anchoringSlider.setMinimum(1)
        self.anchoringSlider.setMaximum(5)
        self.anchoringSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.anchoringSlider, 0, 10, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_15.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_15, 1, 8, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_16.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_16, 1, 7, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_13.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_13, 1, 10, 1, 1)

        self.tripodSlider = QSlider(self.groupBox)
        self.tripodSlider.setObjectName(u"tripodSlider")
        sizePolicy1.setHeightForWidth(self.tripodSlider.sizePolicy().hasHeightForWidth())
        self.tripodSlider.setSizePolicy(sizePolicy1)
        self.tripodSlider.setMinimumSize(QSize(0, 140))
        self.tripodSlider.setMinimum(1)
        self.tripodSlider.setMaximum(5)
        self.tripodSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.tripodSlider, 0, 9, 1, 1)

        self.crossSlider = QSlider(self.groupBox)
        self.crossSlider.setObjectName(u"crossSlider")
        sizePolicy1.setHeightForWidth(self.crossSlider.sizePolicy().hasHeightForWidth())
        self.crossSlider.setSizePolicy(sizePolicy1)
        self.crossSlider.setMinimumSize(QSize(0, 140))
        self.crossSlider.setMinimum(1)
        self.crossSlider.setMaximum(5)
        self.crossSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.crossSlider, 0, 7, 1, 1)

        self.squareSlider = QSlider(self.groupBox)
        self.squareSlider.setObjectName(u"squareSlider")
        sizePolicy1.setHeightForWidth(self.squareSlider.sizePolicy().hasHeightForWidth())
        self.squareSlider.setSizePolicy(sizePolicy1)
        self.squareSlider.setMinimumSize(QSize(0, 140))
        self.squareSlider.setMinimum(1)
        self.squareSlider.setMaximum(5)
        self.squareSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.squareSlider, 0, 6, 1, 1)

        self.parallelSlider = QSlider(self.groupBox)
        self.parallelSlider.setObjectName(u"parallelSlider")
        sizePolicy1.setHeightForWidth(self.parallelSlider.sizePolicy().hasHeightForWidth())
        self.parallelSlider.setSizePolicy(sizePolicy1)
        self.parallelSlider.setMinimumSize(QSize(0, 140))
        self.parallelSlider.setMinimum(1)
        self.parallelSlider.setMaximum(5)
        self.parallelSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.parallelSlider, 0, 8, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_17.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_17, 1, 9, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_14.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_14, 1, 6, 1, 1)

        self.macrameSlider = QSlider(self.groupBox)
        self.macrameSlider.setObjectName(u"macrameSlider")
        sizePolicy1.setHeightForWidth(self.macrameSlider.sizePolicy().hasHeightForWidth())
        self.macrameSlider.setSizePolicy(sizePolicy1)
        self.macrameSlider.setMinimumSize(QSize(0, 140))
        self.macrameSlider.setMinimum(1)
        self.macrameSlider.setMaximum(5)
        self.macrameSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.macrameSlider, 0, 11, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_18.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_18, 1, 11, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


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
        self.label_15.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e7\u05d1\u05d9\u05dc\u05d4", None))
        self.label_16.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05d5\u05e6\u05dc\u05d1\u05ea", None))
        self.label_13.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05e2\u05d9\u05d2\u05d5\u05df\n"
"\u05d9\u05ea\u05e8\u05d9\u05dd", None))
        self.label_17.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05ea\n"
"\u05d7\u05e6\u05d5\u05d1\u05d4", None))
        self.label_14.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e8\u05d5\u05d1\u05e2\u05ea", None))
        self.label_18.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05de\u05e7\u05e8\u05de\u05d4", None))
        self.label_4.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d4\u05e2\u05d3\u05e4\u05d5\u05ea:", None))
        self.groupBox_2.setTitle("")
        self.label_19.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d0':", None))
        self.label_21.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d1':", None))
        self.label_20.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05d2':", None))
    # retranslateUi

