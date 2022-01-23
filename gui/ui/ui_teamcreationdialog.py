# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teamcreationdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TeamCreationDialog(object):
    def setupUi(self, TeamCreationDialog):
        if not TeamCreationDialog.objectName():
            TeamCreationDialog.setObjectName(u"TeamCreationDialog")
        TeamCreationDialog.resize(285, 143)
        TeamCreationDialog.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(TeamCreationDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(TeamCreationDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.teamNameEdt = QLineEdit(TeamCreationDialog)
        self.teamNameEdt.setObjectName(u"teamNameEdt")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teamNameEdt.sizePolicy().hasHeightForWidth())
        self.teamNameEdt.setSizePolicy(sizePolicy)
        self.teamNameEdt.setMinimumSize(QSize(220, 0))
        self.teamNameEdt.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.teamNameEdt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_2 = QLabel(TeamCreationDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.colorPickerBtn = QPushButton(TeamCreationDialog)
        self.colorPickerBtn.setObjectName(u"colorPickerBtn")
        self.colorPickerBtn.setMinimumSize(QSize(220, 0))
        self.colorPickerBtn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.colorPickerBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(TeamCreationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TeamCreationDialog)
        self.buttonBox.accepted.connect(TeamCreationDialog.accept)
        self.buttonBox.rejected.connect(TeamCreationDialog.reject)

        QMetaObject.connectSlotsByName(TeamCreationDialog)
    # setupUi

    def retranslateUi(self, TeamCreationDialog):
        TeamCreationDialog.setWindowTitle(QCoreApplication.translate("TeamCreationDialog", u"\u05d9\u05e6\u05d9\u05e8\u05ea \u05e6\u05d5\u05d5\u05ea", None))
        self.label.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05e9\u05dd:", None))
        self.teamNameEdt.setPlaceholderText(QCoreApplication.translate("TeamCreationDialog", u"\u05e9\u05dd \u05d4\u05e7\u05d1\u05d5\u05e6\u05d4", None))
        self.label_2.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05e6\u05d1\u05e2:", None))
        self.colorPickerBtn.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05d1\u05d7\u05e8 \u05e6\u05d1\u05e2", None))
    # retranslateUi

