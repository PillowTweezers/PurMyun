from PySide6 import QtWidgets

from gui.ui.ui_teamcreationdialog import Ui_TeamCreationDialog
from src import Client as client
from src.Weights import Weights


class TeamCreationDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TeamCreationDialog()
        self.ui.setupUi(self)
        self.ui.colorPickerBtn.clicked.connect(self.color_button_clicked)
        self.ui.buttonBox.accepted.connect(self.accept_button_clicked)
        self.color = None

    def color_button_clicked(self):
        colorPicker = QtWidgets.QColorDialog()
        self.color = colorPicker.getColor()
        self.ui.colorPickerBtn.setStyleSheet(
            "background-color: rgb({}, {}, {});".format(self.color.red(), self.color.green(), self.color.blue()))

    def accept_button_clicked(self):
        weights = Weights()
        weights.square = self.ui.squareSlider.value()
        weights.cross = self.ui.crossSlider.value()
        weights.parallel = self.ui.parallelSlider.value()
        weights.tripod = self.ui.tripodSlider.value()
        weights.anchoring = self.ui.anchoringSlider.value()
        weights.macrame = self.ui.macrameSlider.value()
        weights.size = -1
        client.create_team(self.ui.teamNameEdt.text(), weights, self.color)
