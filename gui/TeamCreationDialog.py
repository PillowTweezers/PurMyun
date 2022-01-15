from PySide6 import QtWidgets

from src.Weights import Weights
from ui_teamcreationdialog import Ui_TeamCreationDialog
from src import Client as client


class TeamCreationDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TeamCreationDialog()
        self.ui.setupUi(self)
        self.ui.colorPickerBtn.clicked.connect(self.color_button_clicked)
        self.ui.buttonBox.accepted.connect(self.accept_button_clicked)

    def color_button_clicked(self):
        colorPicker = QtWidgets.QColorDialog()
        color = colorPicker.getColor()
        self.ui.colorPickerBtn.setStyleSheet(
            "background-color: rgb({}, {}, {});".format(color.red(), color.green(), color.blue()))

    def accept_button_clicked(self):
        weights = Weights()
        weights.square = self.ui.squareSlider.value()
        weights.cross = self.ui.squareSlider.value()
        weights.parallel = self.ui.squareSlider.value()
        weights.tripod = self.ui.squareSlider.value()
        weights.anchoring = self.ui.squareSlider.value()
        weights.macrame = self.ui.squareSlider.value()
        weights.size = self.ui.squareSlider.value()
        client.create_team(self.ui.teamNameEdt.text(), weights)
        client.print_all_teams()

