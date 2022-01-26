# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'participanttablewidget.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from  . import participantstable_rc

class Ui_ParticipantTableWidget(object):
    def setupUi(self, ParticipantTableWidget):
        if not ParticipantTableWidget.objectName():
            ParticipantTableWidget.setObjectName(u"ParticipantTableWidget")
        ParticipantTableWidget.resize(317, 555)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ParticipantTableWidget.sizePolicy().hasHeightForWidth())
        ParticipantTableWidget.setSizePolicy(sizePolicy)
        ParticipantTableWidget.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(ParticipantTableWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.participantsFilterLineEdt = QLineEdit(ParticipantTableWidget)
        self.participantsFilterLineEdt.setObjectName(u"participantsFilterLineEdt")

        self.horizontalLayout_2.addWidget(self.participantsFilterLineEdt)

        self.addParticipantBtn = QPushButton(ParticipantTableWidget)
        self.addParticipantBtn.setObjectName(u"addParticipantBtn")
        icon = QIcon()
        icon.addFile(u":/assets/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addParticipantBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.addParticipantBtn)

        self.assignParticipantBtn = QPushButton(ParticipantTableWidget)
        self.assignParticipantBtn.setObjectName(u"assignParticipantBtn")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.assignParticipantBtn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.assignParticipantBtn)

        self.removeParticipantBtn = QPushButton(ParticipantTableWidget)
        self.removeParticipantBtn.setObjectName(u"removeParticipantBtn")
        icon2 = QIcon()
        icon2.addFile(u":/assets/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeParticipantBtn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.removeParticipantBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.participantsTableWidget = QTableWidget(ParticipantTableWidget)
        self.participantsTableWidget.setObjectName(u"participantsTableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.participantsTableWidget.sizePolicy().hasHeightForWidth())
        self.participantsTableWidget.setSizePolicy(sizePolicy1)
        self.participantsTableWidget.setMinimumSize(QSize(0, 454))
        self.participantsTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.participantsTableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.participantsTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.verticalLayout.addWidget(self.participantsTableWidget)


        self.retranslateUi(ParticipantTableWidget)

        QMetaObject.connectSlotsByName(ParticipantTableWidget)
    # setupUi

    def retranslateUi(self, ParticipantTableWidget):
        ParticipantTableWidget.setWindowTitle(QCoreApplication.translate("ParticipantTableWidget", u"Form", None))
        self.participantsFilterLineEdt.setText("")
        self.participantsFilterLineEdt.setPlaceholderText(QCoreApplication.translate("ParticipantTableWidget", u"\u05e4\u05d9\u05dc\u05d8\u05e8", None))
        self.addParticipantBtn.setText("")
        self.assignParticipantBtn.setText("")
        self.removeParticipantBtn.setText("")
    # retranslateUi

