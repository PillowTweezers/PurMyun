from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings, Slot

from gui.ParticipantCreationDialog import ParticipantCreationDialog
from gui.ParticipantDialog import ParticipantDialog
from gui.TeamCreationDialog import TeamCreationDialog
from gui.ui.ui_mainwindow import Ui_MainWindow
from src import Client as client
from src.Participant import Participant


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.createTeamBtn.clicked.connect(self.create_team)
        self.ui.loadParticipantsBtn.clicked.connect(self.load_participants)
        self.ui.createParticipantsBtn.clicked.connect(self.create_participant)

        self.ui.participantsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.participantsTableWidget.setColumnCount(4)
        self.ui.participantsTableWidget.setHorizontalHeaderLabels(["שם", "ממוצע", "מחויבות", "צוות"])
        self.ui.participantsTableWidget.setColumnWidth(0, 80)
        self.ui.participantsTableWidget.setColumnWidth(1, 55)
        self.ui.participantsTableWidget.setColumnWidth(2, 55)
        self.ui.participantsTableWidget.setColumnWidth(3, 64)
        self.ui.participantsTableWidget.doubleClicked.connect(self.participants_double_clicked)
        self.ui.participantsTableWidget.setAlternatingRowColors(True)
        self.ui.participantsTableWidget.setSortingEnabled(True)

        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.restoreGeometry(self.settings.value("geometry"))
        self.restoreState(self.settings.value("windowState"))

        self.statusBar().showMessage("מוכן")

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        event.accept()

    @Slot()
    def create_participant(self):
        self.statusBar().showMessage("יוצר משתתף...")
        participantCreationDialog = ParticipantCreationDialog()
        if participantCreationDialog.exec() == QtWidgets.QDialog.Accepted:
            participant = Participant()
            participant.name = participantCreationDialog.ui.nameLineEdt.text()
            participant.presence = participantCreationDialog.ui.presenceSlider.value()
            participant.motivation = participantCreationDialog.ui.motivationSlider.value()
            participant.square = participantCreationDialog.ui.squareSlider.value()
            participant.cross = participantCreationDialog.ui.crossSlider.value()
            participant.parallel = participantCreationDialog.ui.parallelSlider.value()
            participant.tripod = participantCreationDialog.ui.tripodSlider.value()
            participant.anchoring = participantCreationDialog.ui.anchoringSlider.value()
            participant.macrame = participantCreationDialog.ui.macrameSlider.value()
            client.add_participant(participant)
        self.statusBar().showMessage("משתתף נוצר")
        self.render_participants_table()

    @Slot()
    def participants_double_clicked(self):
        row = self.ui.participantsTableWidget.currentRow()
        participant_id = self.ui.participantsTableWidget.item(row, 0).data(QtCore.Qt.UserRole)

        def find_by_id(p): return p.id == participant_id

        participant = next(filter(find_by_id, client.participants), None)
        self.statusBar().showMessage("פותח תפריט עבור משתתף: " + participant.name)
        participantDialog = ParticipantDialog(participant)
        participantDialog.exec()

    @Slot()
    def create_team(self):
        self.statusBar().showMessage("יוצר צוות...")
        teamCreationDialog = TeamCreationDialog()
        teamCreationDialog.exec()
        self.statusBar().showMessage("צוות נוצר")

    @Slot()
    def load_participants(self):
        self.statusBar().showMessage("טוען משתתפים...")
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, str("Choose File"), "", str("*.csv"))
        _, exit_code = client.load_participants(filePath)
        if exit_code == 1:
            self.error_text('בבקשה בחר קובץ')
            return
        elif exit_code == -1:
            self.error_text('אין גישה לקובץ')
            return

        self.render_participants_table()
        self.statusBar().showMessage("משתתפים נטענו")

    def render_participants_table(self):
        self.ui.participantsTableWidget.setRowCount(len(client.participants))
        for participant in client.participants:
            item = QtWidgets.QTableWidgetItem(participant.name)
            item.setData(QtCore.Qt.UserRole, participant.id)
            self.ui.participantsTableWidget.setItem(client.participants.index(participant), 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, float("{:g}".format(round(participant.average(), 1))))
            self.ui.participantsTableWidget.setItem(client.participants.index(participant), 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setData(QtCore.Qt.DisplayRole, participant.presence)
            self.ui.participantsTableWidget.setItem(client.participants.index(participant), 2, item)
            if participant.team is not None:
                item = QtWidgets.QTableWidgetItem(participant.team.name)
                self.ui.participantsTableWidget.setItem(client.participants.index(participant), 3, item)

    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)

    def error_text(self, text: str):
        QtWidgets.QMessageBox.critical(self, "Alert", text)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
