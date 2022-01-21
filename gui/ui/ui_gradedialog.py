# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gradedialog.ui'
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
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_GradesDialog(object):
    def setupUi(self, GradesDialog):
        if not GradesDialog.objectName():
            GradesDialog.setObjectName(u"GradesDialog")
        GradesDialog.resize(373, 274)
        GradesDialog.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(GradesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(GradesDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight:bold;font-size:16px;")

        self.verticalLayout.addWidget(self.label_2)

        self.widget = QWidget(GradesDialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(30)
        self.sixGradeEdit = QLineEdit(self.widget)
        self.sixGradeEdit.setObjectName(u"sixGradeEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sixGradeEdit)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight:bold;font-size:16px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.sevenGradeEdit = QLineEdit(self.widget)
        self.sevenGradeEdit.setObjectName(u"sevenGradeEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sevenGradeEdit)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight:bold;font-size:16px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.eightGradeEdit = QLineEdit(self.widget)
        self.eightGradeEdit.setObjectName(u"eightGradeEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.eightGradeEdit)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-weight:bold;font-size:16px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(GradesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(GradesDialog)
        self.buttonBox.accepted.connect(GradesDialog.accept)
        self.buttonBox.rejected.connect(GradesDialog.reject)

        QMetaObject.connectSlotsByName(GradesDialog)
    # setupUi

    def retranslateUi(self, GradesDialog):
        GradesDialog.setWindowTitle(QCoreApplication.translate("GradesDialog", u"\u05e1\u05d9\u05d3\u05d5\u05e8 \u05e9\u05db\u05d1\u05d5\u05ea", None))
        self.label_2.setText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05de\u05d5\u05ea \u05e9\u05db\u05d1\u05d4:", None))
        self.sixGradeEdit.setPlaceholderText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05dd \u05e9\u05db\u05d1\u05d4", None))
        self.label.setText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05d9\u05e9\u05d9\u05d5\u05ea:", None))
        self.sevenGradeEdit.setPlaceholderText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05dd \u05e9\u05db\u05d1\u05d4", None))
        self.label_3.setText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05d1\u05d9\u05e2\u05d9\u05d5\u05ea:", None))
        self.eightGradeEdit.setPlaceholderText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05dd \u05e9\u05db\u05d1\u05d4", None))
        self.label_4.setText(QCoreApplication.translate("GradesDialog", u"\u05e9\u05de\u05d9\u05e0\u05d9\u05d5\u05ea:", None))
    # retranslateUi

