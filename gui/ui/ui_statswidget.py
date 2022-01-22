# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from gui.FancySliderWidget import FancySliderWidget

class Ui_StatsWidget(object):
    def setupUi(self, StatsWidget):
        if not StatsWidget.objectName():
            StatsWidget.setObjectName(u"StatsWidget")
        StatsWidget.resize(616, 316)
        StatsWidget.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(StatsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(-1, 10, -1, -1)
        self.label_5 = QLabel(StatsWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_5, 1, 7, 1, 1)

        self.label_4 = QLabel(StatsWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_4, 1, 6, 1, 1)

        self.label_7 = QLabel(StatsWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_7, 1, 10, 1, 1)

        self.label_6 = QLabel(StatsWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_6, 1, 9, 1, 1)

        self.label_3 = QLabel(StatsWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_3, 1, 8, 1, 1)

        self.label_8 = QLabel(StatsWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_8, 1, 5, 1, 1)

        self.squareSlider = FancySliderWidget(StatsWidget)
        self.squareSlider.setObjectName(u"squareSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.squareSlider.sizePolicy().hasHeightForWidth())
        self.squareSlider.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.squareSlider, 0, 5, 1, 1)

        self.crossSlider = FancySliderWidget(StatsWidget)
        self.crossSlider.setObjectName(u"crossSlider")
        sizePolicy1.setHeightForWidth(self.crossSlider.sizePolicy().hasHeightForWidth())
        self.crossSlider.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.crossSlider, 0, 6, 1, 1)

        self.parallelSlider = FancySliderWidget(StatsWidget)
        self.parallelSlider.setObjectName(u"parallelSlider")
        sizePolicy1.setHeightForWidth(self.parallelSlider.sizePolicy().hasHeightForWidth())
        self.parallelSlider.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.parallelSlider, 0, 7, 1, 1)

        self.tripodSlider = FancySliderWidget(StatsWidget)
        self.tripodSlider.setObjectName(u"tripodSlider")
        sizePolicy1.setHeightForWidth(self.tripodSlider.sizePolicy().hasHeightForWidth())
        self.tripodSlider.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.tripodSlider, 0, 8, 1, 1)

        self.anchoringSlider = FancySliderWidget(StatsWidget)
        self.anchoringSlider.setObjectName(u"anchoringSlider")
        sizePolicy1.setHeightForWidth(self.anchoringSlider.sizePolicy().hasHeightForWidth())
        self.anchoringSlider.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.anchoringSlider, 0, 9, 1, 1)

        self.macrameSlider = FancySliderWidget(StatsWidget)
        self.macrameSlider.setObjectName(u"macrameSlider")
        sizePolicy1.setHeightForWidth(self.macrameSlider.sizePolicy().hasHeightForWidth())
        self.macrameSlider.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.macrameSlider, 0, 10, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(StatsWidget)

        QMetaObject.connectSlotsByName(StatsWidget)
    # setupUi

    def retranslateUi(self, StatsWidget):
        StatsWidget.setWindowTitle(QCoreApplication.translate("StatsWidget", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("StatsWidget", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e7\u05d1\u05d9\u05dc\u05d4", None))
        self.label_4.setText(QCoreApplication.translate("StatsWidget", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05d5\u05e6\u05dc\u05d1\u05ea", None))
        self.label_7.setText(QCoreApplication.translate("StatsWidget", u"\u05de\u05e7\u05e8\u05de\u05d4", None))
        self.label_6.setText(QCoreApplication.translate("StatsWidget", u"\u05e2\u05d9\u05d2\u05d5\u05df\n"
"\u05d9\u05ea\u05e8\u05d9\u05dd", None))
        self.label_3.setText(QCoreApplication.translate("StatsWidget", u"\u05db\u05e4\u05d9\u05ea\u05ea\n"
"\u05d7\u05e6\u05d5\u05d1\u05d4", None))
        self.label_8.setText(QCoreApplication.translate("StatsWidget", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
"\u05de\u05e8\u05d5\u05d1\u05e2\u05ea", None))
    # retranslateUi

