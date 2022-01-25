from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

from gui.GradesDialog import GradesDialog
from gui.ParticipantCreationDialog import ParticipantCreationDialog
from gui.ParticipantDialog import ParticipantDialog
from gui.ui.ui_participanttablewidget import Ui_ParticipantTableWidget
from src import client as client
from src.team import Team

COLUMN_RATIOS = [0.5, 0.2, 0.3]


class ParticipantTableWidget(QWidget):
    """
    This class represents the participant table widget.
    It has two modes: global and team view, the latter accessible via passing a team object.
    """

    def __init__(self, parent=None, team: Team = None, update_ui_callback=None):
        super(ParticipantTableWidget, self).__init__(parent)
        self.ui = Ui_ParticipantTableWidget()
        self.ui.setupUi(self)

        self.update_ui_callback = update_ui_callback
        self.team = team

        if team is not None:
            self.ui.addParticipantBtn.hide()
        else:
            self.ui.assignParticipantBtn.hide()

        self.ui.addParticipantBtn.clicked.connect(self.create_participant)
        self.ui.removeParticipantBtn.clicked.connect(self.remove_participants)
        self.ui.assignParticipantBtn.clicked.connect(self.assign_participant)

        self.ui.participantsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.ui.participantsTableWidget.setColumnCount(3)
        self.ui.participantsTableWidget.setHorizontalHeaderLabels(["שם", "ציון", "צוות"])

        self.ui.participantsTableWidget.doubleClicked.connect(self.participants_double_clicked)
        self.ui.participantsTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.participantsTableWidget.customContextMenuRequested.connect(self.participants_right_clicked)
        self.ui.participantsTableWidget.setSortingEnabled(True)
        self.ui.participantsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.participantsFilterLineEdt.textChanged.connect(self.filter_participants)

    def assign_participant(self):
        pass

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        super(ParticipantTableWidget, self).showEvent(event)
        self.resize_header()
        header = self.ui.participantsTableWidget.horizontalHeader()
        # header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        header.setStretchLastSection(True)

    def resize_header(self):
        width = self.ui.participantsTableWidget.width()
        for (i, column_ratio) in enumerate(COLUMN_RATIOS):
            self.ui.participantsTableWidget.setColumnWidth(i, int(width * column_ratio))

    @Slot()
    def participants_double_clicked(self):
        row = self.ui.participantsTableWidget.currentRow()
        participant_id = self.ui.participantsTableWidget.item(row, 0).data(QtCore.Qt.UserRole)
        participant = client.find_participant(participant_id)
        # self.statusBar().showMessage("פותח תפריט עבור משתתף: " + participant.name)
        participantDialog = ParticipantDialog(participant)
        participantDialog.exec()

    @Slot()
    def participants_right_clicked(self):
        menu = QtWidgets.QMenu()
        remove_action = menu.addAction("הסר משתתפים" if self.team is None else "הסר מצוות")
        remove_action.triggered.connect(self.remove_participants)
        if self.ui.participantsTableWidget.rowCount() == 0:
            remove_action.setEnabled(False)

        menu.addSeparator()

        move_menu = QtWidgets.QMenu("העבר לצוות")
        for team in client.teams:
            if team is self.team:
                continue
            move_action = move_menu.addAction(team.name)
            # What in the name of god is this fuckery? I have 0 idea why [bool] is needed here.
            move_action.triggered[bool].connect(lambda checked, team_=team: self.move_participants(team_))
        menu.addMenu(move_menu)
        if self.ui.participantsTableWidget.rowCount() == 0 or len(client.teams) == 0:
            move_menu.setEnabled(False)
        if len(client.teams) == 1 and self.team is not None:
            move_menu.setEnabled(False)

        menu.exec_(QtGui.QCursor.pos())
        pass

    @Slot()
    def remove_participants(self):
        selected_rows = self.ui.participantsTableWidget.selectionModel().selectedRows()
        if len(selected_rows) == 0:
            self.alert_text("לא נבחרו משתתפים")
            return
        confirmation_box = QtWidgets.QMessageBox()
        if Team:
            confirmation_box.setText("האם אתה בטוח שברצונך להסיר את חברי הצוות שנבחרו?")
        else:
            confirmation_box.setText("האם אתה בטוח שברצונך למחוק את המשתתפים שנבחרו?")
        confirmation_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirmation_box.setDefaultButton(QtWidgets.QMessageBox.No)
        confirmation_box.setIcon(QtWidgets.QMessageBox.Question)
        confirmation_box.setWindowTitle("אישור מחיקה")
        if confirmation_box.exec() == QtWidgets.QMessageBox.Yes:
            for row in sorted(selected_rows, reverse=True):
                participant_id = row.item(0).data(QtCore.Qt.UserRole)
                self.remove_participant(participant_id)
            self.update_ui_callback()
            self.ui.participantsTableWidget.clearSelection()

    @Slot()
    def move_participants(self, team: Team):
        selected_items = self.ui.participantsTableWidget.selectedItems()
        selected_rows = set()
        for item in selected_items:
            selected_rows.add(item.row())
        if len(selected_rows) == 0:
            self.alert_text("לא נבחרו משתתפים")
            return
        confirmation_box = QtWidgets.QMessageBox()
        confirmation_box.setText("האם אתה בטוח שברצונך להעביר את חברי הצוות שנבחרו?")
        confirmation_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirmation_box.setDefaultButton(QtWidgets.QMessageBox.No)
        confirmation_box.setIcon(QtWidgets.QMessageBox.Question)
        confirmation_box.setWindowTitle("אישור העברה")
        if confirmation_box.exec() == QtWidgets.QMessageBox.Yes:
            for row in selected_rows:
                participant_id = row
                client.move_participant_by_id(participant_id, team)
            self.update_ui_callback()
            self.ui.participantsTableWidget.clearSelection()

    @Slot()
    def create_participant(self):
        if not client.has_grades():
            self.open_grades_dialog()
        participantCreationDialog = ParticipantCreationDialog()
        if participantCreationDialog.exec() == QtWidgets.QDialog.Accepted:
            self.render_participants_table()
            if self.ui.participantsFilterLineEdt.text() != "":
                self.filter_participants()

    def open_grades_dialog(self):
        dialog = GradesDialog(self)
        dialog.exec_()

    @Slot()
    def filter_participants(self):
        filter_str = self.ui.participantsFilterLineEdt.text()
        if filter_str == "":
            self.render_participants_table()
            return
        for row in range(self.ui.participantsTableWidget.rowCount()):
            participant_name = self.ui.participantsTableWidget.item(row, 0).text()
            if filter_str.lower() in participant_name.lower():
                self.ui.participantsTableWidget.showRow(row)
            else:
                self.ui.participantsTableWidget.hideRow(row)
        self.ui.participantsTableWidget.clearSelection()

    def remove_participant(self, participant_id):
        if self.team is None:
            client.remove_participant(participant_id)
        else:
            client.remove_participant_from_team(participant_id, self.team)

    def clean_table(self):
        self.ui.participantsTableWidget.clearContents()
        self.ui.participantsTableWidget.setRowCount(0)

    def render_participants_table(self):
        self.clean_table()
        self.ui.participantsTableWidget.setSortingEnabled(False)

        participants = self.team.participants if self.team else client.participants
        for (i, participant) in enumerate(participants):
            self.ui.participantsTableWidget.setRowCount(i + 1)
            self.create_participant_row(participant)

        self.ui.participantsTableWidget.setSortingEnabled(True)

    def create_participant_row(self, participant):
        name_item = QtWidgets.QTableWidgetItem(participant.name)
        name_item.setData(QtCore.Qt.UserRole, participant.participant_id)
        color = name_item.background() if participant.team is None else QColor.fromRgb(participant.team.color.r,
                                                                                       participant.team.color.g,
                                                                                       participant.team.color.b)
        name_item.setBackground(color)
        self.ui.participantsTableWidget.setItem(self.ui.participantsTableWidget.rowCount() - 1, 0, name_item)

        score_item = QtWidgets.QTableWidgetItem()
        score_item.setData(QtCore.Qt.DisplayRole, participant.score)
        score_item.setBackground(color)
        self.ui.participantsTableWidget.setItem(self.ui.participantsTableWidget.rowCount() - 1, 1, score_item)

        if participant.team is not None:
            team_item = QtWidgets.QTableWidgetItem(participant.team.name)
            team_item.setBackground(color)
            self.ui.participantsTableWidget.setItem(self.ui.participantsTableWidget.rowCount() - 1, 2, team_item)

    def set_team(self, team: Team):
        self.team = team
        self.ui.addParticipantBtn.hide()
        self.ui.assignParticipantBtn.show()
        self.ui.participantsTableWidget.setColumnCount(3)
        self.ui.participantsTableWidget.setHorizontalHeaderLabels(["שם", "ממוצע", "מחויבות"])
        self.update_ui()

    def update_ui(self):
        self.render_participants_table()

    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)

    def error_text(self, text: str):
        QtWidgets.QMessageBox.critical(self, "Error", text)
