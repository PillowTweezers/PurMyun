from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QDialog

from gui.TeamCreationDialog import TeamCreationDialog
from gui.ui.ui_teamwidget import Ui_TeamWidget
from src import client as client


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
