from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

from gui.ui.ui_teamcreationdialog import Ui_TeamCreationDialog
from src import Client as client
from src.Weights import Weights


class TeamCreationDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, team=None):
        super().__init__(parent)
        self.ui = Ui_TeamCreationDialog()
        self.ui.setupUi(self)
        self.ui.colorPickerBtn.clicked.connect(self.color_button_clicked)
        self.color = None
        self.team = team

        if team is not None:
            self.setWindowTitle("עריכת צוות")
            self.ui.teamNameEdt.setText(team.name)
            self.ui.colorPickerBtn.setStyleSheet(
                "background-color: rgb({}, {}, {});".format(
                    team.color.red(), team.color.green(), team.color.blue()
                )
            )
            self.color = team.color
            self.ui.statsWidget.ui.squareSlider.set_value(team.weights.square)
            self.ui.statsWidget.ui.crossSlider.set_value(team.weights.cross)
            self.ui.statsWidget.ui.parallelSlider.set_value(team.weights.parallel)
            self.ui.statsWidget.ui.tripodSlider.set_value(team.weights.tripod)
            self.ui.statsWidget.ui.anchoringSlider.set_value(team.weights.anchoring)
            self.ui.statsWidget.ui.macrameSlider.set_value(team.weights.macrame)
            # self.ui.statsWidget.ui.sizeSlider.set_value(team.weights.size)

    def color_button_clicked(self):
        colorPicker = QtWidgets.QColorDialog()
        self.color = colorPicker.getColor()
        self.ui.colorPickerBtn.setStyleSheet(
            "background-color: rgb({}, {}, {});".format(self.color.red(), self.color.green(), self.color.blue()))

    def accept(self) -> None:
        if self.can_accept():
            weights = Weights()
            weights.square = self.ui.statsWidget.ui.squareSlider.get_value()
            weights.cross = self.ui.statsWidget.ui.crossSlider.get_value()
            weights.parallel = self.ui.statsWidget.ui.parallelSlider.get_value()
            weights.tripod = self.ui.statsWidget.ui.tripodSlider.get_value()
            weights.anchoring = self.ui.statsWidget.ui.anchoringSlider.get_value()
            weights.macrame = self.ui.statsWidget.ui.macrameSlider.get_value()
            weights.size = -1
            if self.team is None:
                client.create_team(self.ui.teamNameEdt.text(), weights, self.color)
            else:
                client.update_team(self.team, self.ui.teamNameEdt.text(), weights, self.color)
            self.done(QDialog.Accepted)
        else:
            self.focus_on_empty()

    def can_accept(self):
        return self.ui.teamNameEdt.text() != "" and self.color is not None

    def focus_on_empty(self):
        if self.ui.teamNameEdt.text() == "":
            self.ui.teamNameEdt.setFocus()
        elif self.color is None:
            self.ui.colorPickerBtn.setFocus()
