from PySide6.QtWidgets import QWidget

from gui.ui.ui_teamwidget import Ui_TeamWidget
from src.Team import MAX_WEIGHT


class TeamWidget(QWidget):
    def __init__(self, team, parent=None, update_ui_callback=None):
        super().__init__(parent)
        self.ui = Ui_TeamWidget()
        self.ui.setupUi(self)
        self.ui.teamNameLbl.setText(team.name)

        self.ui.squareBar.setValue(team.weights.square)
        self.ui.squareBar.setMaximum(MAX_WEIGHT)
        self.ui.squareLbl.setText(f"{team.weights.square}/{MAX_WEIGHT}")

        self.ui.crossBar.setValue(team.weights.cross)
        self.ui.crossBar.setMaximum(MAX_WEIGHT)
        self.ui.crossLbl.setText(f"{team.weights.cross}/{MAX_WEIGHT}")

        self.ui.parallelBar.setValue(team.weights.parallel)
        self.ui.parallelBar.setMaximum(MAX_WEIGHT)
        self.ui.parallelLbl.setText(f"{team.weights.parallel}/{MAX_WEIGHT}")

        self.ui.tripodBar.setValue(team.weights.tripod)
        self.ui.tripodBar.setMaximum(MAX_WEIGHT)
        self.ui.tripodLbl.setText(f"{team.weights.tripod}/{MAX_WEIGHT}")

        self.ui.anchoringBar.setValue(team.weights.anchoring)
        self.ui.anchoringBar.setMaximum(MAX_WEIGHT)
        self.ui.anchoringLbl.setText(f"{team.weights.anchoring}/{MAX_WEIGHT}")

        self.ui.macrameBar.setValue(team.weights.macrame)
        self.ui.macrameBar.setMaximum(MAX_WEIGHT)
        self.ui.macrameLbl.setText(f"{team.weights.macrame}/{MAX_WEIGHT}")

        self.ui.applyEditBtn.hide()
        self.ui.cancelEditBtn.hide()

        self.team = team
        self.ui.participantTableWidget.update_ui_callback = update_ui_callback

        self.ui.participantTableWidget.set_team(team)

    def resize_table_header(self):
        self.ui.participantTableWidget.resize_header()

    def update_ui(self):
        self.ui.participantTableWidget.update_ui()
