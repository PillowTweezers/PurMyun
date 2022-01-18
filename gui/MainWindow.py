from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QSettings, Slot
from gui.TeamCreationDialog import TeamCreationDialog
from src import Client as client
from gui.ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.controlsDock.setWindowTitle()

        self.ui.createTeamBtn.clicked.connect(self.create_team)
        self.ui.loadParticipantsBtn.clicked.connect(self.load_participants)

        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.restoreGeometry(self.settings.value("geometry"))
        self.restoreState(self.settings.value("windowState"))

        self.statusBar().showMessage("Ready")

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        event.accept()

    @Slot()
    def create_team(self):
        self.statusBar().showMessage("Creating team...")
        teamCreationDialog = TeamCreationDialog()
        teamCreationDialog.exec()
        self.statusBar().showMessage("Team created")

    @Slot()
    def load_participants(self):
        self.statusBar().showMessage("Loading participants...")
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, str("Choose File"), "", str("*.csv"))
        participants, exit_code = client.load_participants(filePath)
        if exit_code == 1:
            self.error_text('Please choose a file')
            return
        elif exit_code == -1:
            self.error_text('Cannot read file')
            return

        model = QtGui.QStandardItemModel()
        self.ui.participantsListView.setModel(model)
        for participant in client.participants:
            item = QtGui.QStandardItem()
            item.setText(participant.name)
            item.setEditable(False)
            model.appendRow(item)
        self.statusBar().showMessage("Participants loaded")

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
