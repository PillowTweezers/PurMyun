from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QDialog

from gui.TeamCreationDialog import TeamCreationDialog
from gui.ui.ui_teamwidget import Ui_TeamWidget
from src import Client as client
from src.Team import MAX_WEIGHT


class TeamWidget(QWidget):
    def __init__(self, team, parent=None, update_ui_callback=None):
        super().__init__(parent)
        self.ui = Ui_TeamWidget()
        self.ui.setupUi(self)

        self.team = team
        self.ui.participantTableWidget.update_ui_callback = update_ui_callback
        self.update_ui_callback = update_ui_callback

        self.ui.editBtn.clicked.connect(self.edit_clicked)
        self.ui.deleteTeamBtn.clicked.connect(self.delete_team_clicked)

        self.ui.participantTableWidget.set_team(team)

        self.show_team_data()

    def show_team_data(self):
        self.ui.teamNameLbl.setText(self.team.name)

        self.ui.squareBar.setValue(self.team.weights.square)
        self.ui.squareBar.setMaximum(MAX_WEIGHT)
        self.ui.squareLbl.setText(f"{self.team.weights.square}/{MAX_WEIGHT}")

        self.ui.crossBar.setValue(self.team.weights.cross)
        self.ui.crossBar.setMaximum(MAX_WEIGHT)
        self.ui.crossLbl.setText(f"{self.team.weights.cross}/{MAX_WEIGHT}")

        self.ui.parallelBar.setValue(self.team.weights.parallel)
        self.ui.parallelBar.setMaximum(MAX_WEIGHT)
        self.ui.parallelLbl.setText(f"{self.team.weights.parallel}/{MAX_WEIGHT}")

        self.ui.tripodBar.setValue(self.team.weights.tripod)
        self.ui.tripodBar.setMaximum(MAX_WEIGHT)
        self.ui.tripodLbl.setText(f"{self.team.weights.tripod}/{MAX_WEIGHT}")

        self.ui.anchoringBar.setValue(self.team.weights.anchoring)
        self.ui.anchoringBar.setMaximum(MAX_WEIGHT)
        self.ui.anchoringLbl.setText(f"{self.team.weights.anchoring}/{MAX_WEIGHT}")

        self.ui.macrameBar.setValue(self.team.weights.macrame)
        self.ui.macrameBar.setMaximum(MAX_WEIGHT)
        self.ui.macrameLbl.setText(f"{self.team.weights.macrame}/{MAX_WEIGHT}")

    def edit_clicked(self):
        teamEditDialog = TeamCreationDialog(parent=self, team=self.team)
        teamEditDialog.exec()
        if teamEditDialog.result() == QDialog.Accepted:
            self.update_ui_callback()

    def delete_team_clicked(self):
        confirm_dialog = QtWidgets.QMessageBox()
        confirm_dialog.setWindowTitle("אישור מחיקת צוות")
        confirm_dialog.setText(f"האם אתה בטוח שברצונך למחוק את צוות {self.team.name}?")
        confirm_dialog.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirm_dialog.setDefaultButton(QtWidgets.QMessageBox.No)
        confirm_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        if confirm_dialog.exec() == QtWidgets.QMessageBox.Yes:
            client.delete_team(self.team)
            self.update_ui_callback()

    def resize_table_header(self):
        self.ui.participantTableWidget.resize_header()

    def update_ui(self):
        self.show_team_data()
        self.ui.participantTableWidget.update_ui()
