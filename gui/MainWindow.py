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
        # Load UI from compiled .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect All Buttons to their corresponding slots
        self.ui.createTeamBtn.clicked.connect(self.create_team)
        self.ui.addParticipantBtn.clicked.connect(self.create_participant)
        self.ui.removeParticipantBtn.clicked.connect(self.remove_participants)

        # Connect all Action signals to their corresponding slots
        self.ui.loadParticipantsFileAction.triggered.connect(self.load_participants_file)
        self.ui.saveAsAction.triggered.connect(self.save_as)
        self.ui.saveAction.triggered.connect(self.save)
        self.ui.quitAction.triggered.connect(self.quit)
        self.ui.openAction.triggered.connect(self.open_project)
        self.ui.newAction.triggered.connect(self.new_project)

        # Init participants table
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
        self.ui.participantsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # Load past window state
        self.settings = QSettings("settings.ini", QSettings.IniFormat)
        self.restoreGeometry(self.settings.value("geometry"))
        self.restoreState(self.settings.value("windowState"))

        self.statusBar().showMessage("מוכן")

    def closeEvent(self, event):
        if self.can_exit():
            self.settings.setValue("geometry", self.saveGeometry())
            self.settings.setValue("windowState", self.saveState())
            event.accept()
        else:
            event.ignore()

    @Slot()
    def new_project(self):
        if self.can_exit():
            self.statusBar().showMessage("יוצר פרויקט חדש...")
            client.new_project()
            self.render_participants_table()
            self.statusBar().showMessage("פרויקט נוצר")
            return True
        else:
            self.statusBar().showMessage("יצירת פרויקט בוטלה")
            return False

    @Slot()
    def open_project(self):
        if self.can_exit():
            self.statusBar().showMessage("טוען קובץ...")
            openDialog = QtWidgets.QFileDialog()
            openDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
            openDialog.setNameFilter("קובץ פורימון (*.pur)")
            openDialog.setWindowTitle("פתיחת קובץ")
            openDialog.exec()
            if openDialog.result() == QtWidgets.QDialog.Accepted:
                filename = openDialog.selectedFiles()[0]
                if filename:
                    if client.open_project(filename=filename) == 0:
                        self.statusBar().showMessage("קובץ נטען בהצלחה")
                        self.render_participants_table()
                        return True
                    else:
                        self.error_text("שגיאה בטעינת קובץ")
            self.statusBar().showMessage("טעינה בוטלה")
        return False

    @Slot()
    def save_as(self):
        self.statusBar().showMessage("שמירת קובץ...")
        saveDialog = QtWidgets.QFileDialog()
        saveDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        saveDialog.setNameFilter("קובץ פורימון (*.pur)")
        saveDialog.setDefaultSuffix("pur")
        saveDialog.setWindowTitle("שמירת קובץ")
        saveDialog.exec()
        if saveDialog.result() == QtWidgets.QDialog.Accepted:
            filename = saveDialog.selectedFiles()[0]
            if filename:
                if client.save_project_as(filename=filename) == 0:
                    self.statusBar().showMessage("קובץ נשמר בהצלחה")
                    return True
                else:
                    self.error_text("שגיאה בשמירת קובץ")
        self.statusBar().showMessage("שמירה בוטלה")
        return False

    def save(self):
        self.statusBar().showMessage("שמירת קובץ...")
        if client.last_project_file is None:
            return self.save_as()
        else:
            if client.save_project() == 0:
                self.statusBar().showMessage("קובץ נשמר בהצלחה")
                return True
            else:
                self.error_text("שגיאה בשמירת קובץ")
        self.statusBar().showMessage("שמירה בוטלה")
        return False

    @Slot()
    def remove_participants(self):
        self.statusBar().showMessage("מחיקת משתתפים...")
        selected_items = self.ui.participantsTableWidget.selectedItems()
        selected_rows = set()
        for item in selected_items:
            selected_rows.add(item.row())
        if len(selected_rows) == 0:
            self.alert_text("לא נבחרו משתתפים")
            return
        confirmation_box = QtWidgets.QMessageBox()
        confirmation_box.setText("האם אתה בטוח שברצונך למחוק את המשתתפים שנבחרו?")
        confirmation_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirmation_box.setDefaultButton(QtWidgets.QMessageBox.No)
        confirmation_box.setIcon(QtWidgets.QMessageBox.Question)
        confirmation_box.setWindowTitle("אישור מחיקה")
        if confirmation_box.exec() == QtWidgets.QMessageBox.Yes:
            for row in sorted(selected_rows, reverse=True):
                participant_id = self.ui.participantsTableWidget.item(row, 0).data(QtCore.Qt.UserRole)
                client.remove_participant(participant_id)
                self.ui.participantsTableWidget.removeRow(row)
            self.statusBar().showMessage("משתתפים נמחקו")
            self.ui.participantsTableWidget.clearSelection()
        else:
            self.statusBar().showMessage("מחיקת משתתפים בוטלה")

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
    def load_participants_file(self):
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

    @Slot()
    def quit(self):
        if self.can_exit():
            self.close()

    def render_participants_table(self):
        # This library seems to not work well with clearContents()
        # my guess is that it's asynchonous and the table is still rendering
        # while the clearContents() is happening.
        # You may want to figure out a way to wait for it to clear. Remember
        # that this is only a guess.
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

    def can_exit(self):
        if client.is_dirty:
            confirm_dialog = QtWidgets.QMessageBox()
            confirm_dialog.setLayout(QtWidgets.QVBoxLayout())
            confirm_dialog.setText("הנתונים שלך עדיין לא נשמרו. האם אתה בטוח שברצונך לצאת?")
            confirm_dialog.setStandardButtons(
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Save)
            yes_button = confirm_dialog.button(QtWidgets.QMessageBox.Yes)
            yes_button.setStyleSheet("text-align: left;")
            yes_button.setText("כן")
            no_button = confirm_dialog.button(QtWidgets.QMessageBox.No)
            no_button.setStyleSheet("text-align: left;")
            no_button.setText("לא")
            save_button = confirm_dialog.button(QtWidgets.QMessageBox.Save)
            save_button.setStyleSheet("text-align: left;")
            save_button.setText("שמור וצא")
            confirm_dialog.setDefaultButton(QtWidgets.QMessageBox.No)
            confirm_dialog.setIcon(QtWidgets.QMessageBox.Question)
            confirm_dialog.setWindowTitle("אישור יציאה")
            confirm_dialog.exec()
            if confirm_dialog.result() == QtWidgets.QMessageBox.Yes:
                return True
            elif confirm_dialog.result() == QtWidgets.QMessageBox.Save:
                if self.save():
                    return True
            return False
        return True

    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)

    def error_text(self, text: str):
        QtWidgets.QMessageBox.critical(self, "Error", text)
