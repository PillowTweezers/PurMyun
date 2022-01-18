from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QSettings, Slot

from gui.ParticipantDialog import ParticipantDialog
from gui.TeamCreationDialog import TeamCreationDialog
from src import Client as client
from gui.ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.createTeamBtn.clicked.connect(self.create_team)
        self.ui.loadParticipantsBtn.clicked.connect(self.load_participants)

        self.ui.participantsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.participantsTableWidget.setColumnCount(4)
        self.ui.participantsTableWidget.setHorizontalHeaderLabels(["שם", "ממוצע", "מחויבות", "צוות"])
        self.ui.participantsTableWidget.setColumnWidth(0, 80)
        self.ui.participantsTableWidget.setColumnWidth(1, 55)
        self.ui.participantsTableWidget.setColumnWidth(2, 55)
        self.ui.participantsTableWidget.setColumnWidth(3, 64)
        self.ui.participantsTableWidget.doubleClicked.connect(self.participants_double_clicked)

        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.restoreGeometry(self.settings.value("geometry"))
        self.restoreState(self.settings.value("windowState"))

        self.statusBar().showMessage("מוכן")

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        event.accept()

    @Slot()
    def participants_double_clicked(self):
        row = self.ui.participantsTableWidget.currentRow()
        participant = client.participants[row]
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
        participants, exit_code = client.load_participants(filePath)
        if exit_code == 1:
            self.error_text('בבקשה בחר קובץ')
            return
        elif exit_code == -1:
            self.error_text('אין גישה לקובץ')
            return

        self.ui.participantsTableWidget.setRowCount(len(participants))
        for participant in client.participants:
            item = QtWidgets.QTableWidgetItem(participant.name)
            self.ui.participantsTableWidget.setItem(client.participants.index(participant), 0, item)
            item = QtWidgets.QTableWidgetItem("{:g}".format(round(participant.average, 1)))
            self.ui.participantsTableWidget.setItem(client.participants.index(participant), 1, item)
            item = QtWidgets.QTableWidgetItem(str(participant.presence))
            self.ui.participantsTableWidget.setItem(client.participants.index(participant), 2, item)
            if participant.team is not None:
                item = QtWidgets.QTableWidgetItem(participant.team.name)
                self.ui.participantsTableWidget.setItem(client.participants.index(participant), 3, item)

        self.statusBar().showMessage("משתתפים נטענו")

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
