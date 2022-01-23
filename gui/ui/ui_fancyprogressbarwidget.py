# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fancyprogressbarwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FancyProgressBarWidget(object):
    def setupUi(self, FancyProgressBarWidget):
        if not FancyProgressBarWidget.objectName():
            FancyProgressBarWidget.setObjectName(u"FancyProgressBarWidget")
        FancyProgressBarWidget.resize(361, 40)
        FancyProgressBarWidget.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout = QHBoxLayout(FancyProgressBarWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.progressBar = QProgressBar(FancyProgressBarWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(FancyProgressBarWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(FancyProgressBarWidget)

        QMetaObject.connectSlotsByName(FancyProgressBarWidget)
    # setupUi

    def retranslateUi(self, FancyProgressBarWidget):
        FancyProgressBarWidget.setWindowTitle(QCoreApplication.translate("FancyProgressBarWidget", u"Form", None))
        self.progressBar.setFormat("")
        self.label.setText("")
    # retranslateUi

