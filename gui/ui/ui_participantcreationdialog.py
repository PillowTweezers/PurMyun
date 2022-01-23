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
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from gui.FancySliderHorizontalWidget import FancySliderHorizontalWidget

class Ui_ParticipantCreationDialog(object):
    def setupUi(self, ParticipantCreationDialog):
        if not ParticipantCreationDialog.objectName():
            ParticipantCreationDialog.setObjectName(u"ParticipantCreationDialog")
        ParticipantCreationDialog.resize(295, 155)
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
        self.nameLineEdt.setMinimumSize(QSize(220, 0))
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
        self.gradeComboBox = QComboBox(ParticipantCreationDialog)
        self.gradeComboBox.setObjectName(u"gradeComboBox")

        self.horizontalLayout.addWidget(self.gradeComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QLabel(ParticipantCreationDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.scoreSliderWidget = FancySliderHorizontalWidget(ParticipantCreationDialog)
        self.scoreSliderWidget.setObjectName(u"scoreSliderWidget")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.scoreSliderWidget)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

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
        self.label_2.setText(QCoreApplication.translate("ParticipantCreationDialog", u"\u05e6\u05d9\u05d5\u05df:", None))
    # retranslateUi

