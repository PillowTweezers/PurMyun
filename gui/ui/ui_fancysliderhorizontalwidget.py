# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fancysliderhorizontalwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_FancySliderHorizontalWidget(object):
    def setupUi(self, FancySliderHorizontalWidget):
        if not FancySliderHorizontalWidget.objectName():
            FancySliderHorizontalWidget.setObjectName(u"FancySliderHorizontalWidget")
        FancySliderHorizontalWidget.resize(400, 80)
        FancySliderHorizontalWidget.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout = QHBoxLayout(FancySliderHorizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.spinBox = QSpinBox(FancySliderHorizontalWidget)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_2.addWidget(self.spinBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.slider = QSlider(FancySliderHorizontalWidget)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.slider)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(FancySliderHorizontalWidget)

        QMetaObject.connectSlotsByName(FancySliderHorizontalWidget)
    # setupUi

    def retranslateUi(self, FancySliderHorizontalWidget):
        FancySliderHorizontalWidget.setWindowTitle(QCoreApplication.translate("FancySliderHorizontalWidget", u"Form", None))
    # retranslateUi

