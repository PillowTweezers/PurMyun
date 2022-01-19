# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teamcreationdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QFormLayout, QGridLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSlider, QSpacerItem,
                               QVBoxLayout)


class Ui_TeamCreationDialog(object):
    def setupUi(self, TeamCreationDialog):
        if not TeamCreationDialog.objectName():
            TeamCreationDialog.setObjectName(u"TeamCreationDialog")
        TeamCreationDialog.resize(700, 440)
        TeamCreationDialog.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout = QVBoxLayout(TeamCreationDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(TeamCreationDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.teamNameEdt = QLineEdit(TeamCreationDialog)
        self.teamNameEdt.setObjectName(u"teamNameEdt")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.teamNameEdt)

        self.label_2 = QLabel(TeamCreationDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.colorPickerBtn = QPushButton(TeamCreationDialog)
        self.colorPickerBtn.setObjectName(u"colorPickerBtn")
        self.colorPickerBtn.setFlat(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.colorPickerBtn)

        self.label_9 = QLabel(TeamCreationDialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(2)
        self.crossSlider = QSlider(TeamCreationDialog)
        self.crossSlider.setObjectName(u"crossSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crossSlider.sizePolicy().hasHeightForWidth())
        self.crossSlider.setSizePolicy(sizePolicy)
        self.crossSlider.setMinimumSize(QSize(0, 140))
        self.crossSlider.setMinimum(1)
        self.crossSlider.setMaximum(5)
        self.crossSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.crossSlider, 0, 5, 1, 1)

        self.anchoringSlider = QSlider(TeamCreationDialog)
        self.anchoringSlider.setObjectName(u"anchoringSlider")
        sizePolicy.setHeightForWidth(self.anchoringSlider.sizePolicy().hasHeightForWidth())
        self.anchoringSlider.setSizePolicy(sizePolicy)
        self.anchoringSlider.setMinimumSize(QSize(0, 140))
        self.anchoringSlider.setMinimum(1)
        self.anchoringSlider.setMaximum(5)
        self.anchoringSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.anchoringSlider, 0, 1, 1, 1)

        self.squareSlider = QSlider(TeamCreationDialog)
        self.squareSlider.setObjectName(u"squareSlider")
        sizePolicy.setHeightForWidth(self.squareSlider.sizePolicy().hasHeightForWidth())
        self.squareSlider.setSizePolicy(sizePolicy)
        self.squareSlider.setMinimumSize(QSize(0, 140))
        self.squareSlider.setMinimum(1)
        self.squareSlider.setMaximum(5)
        self.squareSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.squareSlider, 0, 6, 1, 1)

        self.tripodSlider = QSlider(TeamCreationDialog)
        self.tripodSlider.setObjectName(u"tripodSlider")
        sizePolicy.setHeightForWidth(self.tripodSlider.sizePolicy().hasHeightForWidth())
        self.tripodSlider.setSizePolicy(sizePolicy)
        self.tripodSlider.setMinimumSize(QSize(0, 140))
        self.tripodSlider.setMinimum(1)
        self.tripodSlider.setMaximum(5)
        self.tripodSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.tripodSlider, 0, 2, 1, 1)

        self.parallelSlider = QSlider(TeamCreationDialog)
        self.parallelSlider.setObjectName(u"parallelSlider")
        sizePolicy.setHeightForWidth(self.parallelSlider.sizePolicy().hasHeightForWidth())
        self.parallelSlider.setSizePolicy(sizePolicy)
        self.parallelSlider.setMinimumSize(QSize(0, 140))
        self.parallelSlider.setMinimum(1)
        self.parallelSlider.setMaximum(5)
        self.parallelSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.parallelSlider, 0, 4, 1, 1)

        self.label_6 = QLabel(TeamCreationDialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_6.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.macrameSlider = QSlider(TeamCreationDialog)
        self.macrameSlider.setObjectName(u"macrameSlider")
        sizePolicy.setHeightForWidth(self.macrameSlider.sizePolicy().hasHeightForWidth())
        self.macrameSlider.setSizePolicy(sizePolicy)
        self.macrameSlider.setMinimumSize(QSize(0, 140))
        self.macrameSlider.setMinimum(1)
        self.macrameSlider.setMaximum(5)
        self.macrameSlider.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.macrameSlider, 0, 0, 1, 1)

        self.label_8 = QLabel(TeamCreationDialog)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_8.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_8, 1, 6, 1, 1)

        self.label_5 = QLabel(TeamCreationDialog)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_5.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)

        self.label_4 = QLabel(TeamCreationDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_4.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_4, 1, 5, 1, 1)

        self.label_3 = QLabel(TeamCreationDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_3.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_7 = QLabel(TeamCreationDialog)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setStyleSheet(u"margin-left:4;margin-right:4;font-size:16px;")
        self.label_7.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.gridLayout)

        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(TeamCreationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TeamCreationDialog)
        self.buttonBox.accepted.connect(TeamCreationDialog.accept)
        self.buttonBox.rejected.connect(TeamCreationDialog.reject)

        QMetaObject.connectSlotsByName(TeamCreationDialog)

    # setupUi

    def retranslateUi(self, TeamCreationDialog):
        TeamCreationDialog.setWindowTitle(
            QCoreApplication.translate("TeamCreationDialog", u"\u05d9\u05e6\u05d9\u05e8\u05ea \u05e6\u05d5\u05d5\u05ea",
                                       None))
        self.label.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05e9\u05dd:", None))
        self.teamNameEdt.setPlaceholderText(
            QCoreApplication.translate("TeamCreationDialog", u"\u05e9\u05dd \u05d4\u05e7\u05d1\u05d5\u05e6\u05d4",
                                       None))
        self.label_2.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05e6\u05d1\u05e2:", None))
        self.colorPickerBtn.setText(
            QCoreApplication.translate("TeamCreationDialog", u"\u05d1\u05d7\u05e8 \u05e6\u05d1\u05e2", None))
        self.label_9.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05de\u05d3\u05d3\u05d9\n"
                                                                              "\u05d7\u05e9\u05d9\u05d1\u05d5\u05ea:",
                                                        None))
        self.label_6.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05e2\u05d9\u05d2\u05d5\u05df\n"
                                                                              "\u05d9\u05ea\u05e8\u05d9\u05dd", None))
        self.label_8.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
                                                                              "\u05de\u05e8\u05d5\u05d1\u05e2\u05ea",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
                                                                              "\u05de\u05e7\u05d1\u05d9\u05dc\u05d4",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05d4\n"
                                                                              "\u05de\u05d5\u05e6\u05dc\u05d1\u05ea",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05db\u05e4\u05d9\u05ea\u05ea\n"
                                                                              "\u05d7\u05e6\u05d5\u05d1\u05d4", None))
        self.label_7.setText(QCoreApplication.translate("TeamCreationDialog", u"\u05de\u05e7\u05e8\u05de\u05d4", None))
    # retranslateUi
