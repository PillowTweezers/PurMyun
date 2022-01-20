from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from gui.ParticipantCreationDialog import ParticipantCreationDialog
from gui.ParticipantDialog import ParticipantDialog
from gui.ui.ui_participanttablewidget import Ui_ParticipantTableWidget
from src import Client as client
from src.Team import Team

COLUMN_RATIOS = [0.315, 0.2165, 0.2165, 0.252]


class ParticipantTableWidget(QWidget):
    """
    This class represents the participant table widget.
    It has two modes: global and team view, the latter accessible via passing a team object.
    """

    def __init__(self, parent=None, team: Team = None):
        super(ParticipantTableWidget, self).__init__(parent)
        self.ui = Ui_ParticipantTableWidget()
        self.ui.setupUi(self)

        if team is not None:
            self.ui.addParticipantBtn.hide()
        else:
            self.ui.assignParticipantBtn.hide()

        self.team = team

        self.ui.addParticipantBtn.clicked.connect(self.create_participant)
        self.ui.removeParticipantBtn.clicked.connect(self.remove_participants)
        self.ui.assignParticipantBtn.clicked.connect(self.assign_participant)

        self.ui.participantsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.participantsTableWidget.setColumnCount(4)
        self.ui.participantsTableWidget.setHorizontalHeaderLabels(["שם", "ממוצע", "מחויבות", "צוות"])

        self.ui.participantsTableWidget.doubleClicked.connect(self.participants_double_clicked)
        self.ui.participantsTableWidget.setAlternatingRowColors(True)
        self.ui.participantsTableWidget.setSortingEnabled(True)
        self.ui.participantsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.participantsFilterLineEdt.textChanged.connect(self.filter_participants)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        super(ParticipantTableWidget, self).showEvent(event)
        width = self.ui.participantsTableWidget.width()
        self.ui.participantsTableWidget.setColumnWidth(0, width * COLUMN_RATIOS[0])
        self.ui.participantsTableWidget.setColumnWidth(1, width * COLUMN_RATIOS[1])
        self.ui.participantsTableWidget.setColumnWidth(2, width * COLUMN_RATIOS[2])
        self.ui.participantsTableWidget.setColumnWidth(3, width * COLUMN_RATIOS[3] - 1)

    @Slot()
    def participants_double_clicked(self):
        row = self.ui.participantsTableWidget.currentRow()
        participant_id = self.ui.participantsTableWidget.item(row, 0).data(QtCore.Qt.UserRole)

        def find_by_id(p): return p.id == participant_id

        participants = self.team.participants if self.team else client.participants
        participant = next(filter(find_by_id, participants), None)
        # self.statusBar().showMessage("פותח תפריט עבור משתתף: " + participant.name)
        participantDialog = ParticipantDialog(participant)
        participantDialog.exec()

    @Slot()
    def remove_participants(self):
        selected_items = self.ui.participantsTableWidget.selectedItems()
        selected_rows = set()
        for item in selected_items:
            selected_rows.add(item.row())
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
                participant_id = self.ui.participantsTableWidget.item(row, 0).data(QtCore.Qt.UserRole)
                self.remove_participant(participant_id)
                self.ui.participantsTableWidget.removeRow(row)
            self.ui.participantsTableWidget.clearSelection()

    @Slot()
    def create_participant(self):
        participantCreationDialog = ParticipantCreationDialog()
        if participantCreationDialog.exec() == QtWidgets.QDialog.Accepted:
            self.render_participants_table()

    def load_participants(self):
        if self.team is None:
            self.participants = client.participants
            return
        self.participants = []
        for participant in client.participants:
            if participant.team == self.team:
                self.participants.append(participant)
        self.render_participants_table()

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
        participants = self.team.participants if self.team else client.participants
        for participant in participants:
            if participant.id == participant_id:
                participants.remove(participant)
                break

    def render_participants_table(self):
        participants = self.team.participants if self.team else client.participants
        self.ui.participantsTableWidget.setRowCount(len(participants))
        for participant in participants:
            item = QtWidgets.QTableWidgetItem(participant.name)
            item.setData(QtCore.Qt.UserRole, participant.id)
            # if participant.team is not None:
            #     item.setBackground(participant.team.)
            # item.setBackground(QtGui.QColor(participant.team))
            self.ui.participantsTableWidget.setItem(participants.index(participant), 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, float("{:g}".format(round(participant.average(), 1))))
            self.ui.participantsTableWidget.setItem(participants.index(participant), 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, participant.presence)
            self.ui.participantsTableWidget.setItem(participants.index(participant), 2, item)
            if participant.team is not None:
                item = QtWidgets.QTableWidgetItem(participant.team.name)
                self.ui.participantsTableWidget.setItem(participants.index(participant), 3, item)
            self.ui.participantsTableWidget.showRow(participants.index(participant))

    def set_team(self, team: Team):
        self.team = team
        self.ui.addParticipantBtn.hide()
        self.ui.assignParticipantBtn.show()
        self.update_ui()

    def update_ui(self):
        self.render_participants_table()

    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)

    def error_text(self, text: str):
        QtWidgets.QMessageBox.critical(self, "Error", text)
