import os

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings, Slot
from PySide6.QtGui import QAction

from gui.TeamCreationDialog import TeamCreationDialog
from gui.TeamWidget import TeamWidget
from gui.ui.ui_mainwindow import Ui_MainWindow
from src import Client as client


class MainWindow(QtWidgets.QMainWindow):
    MAX_RECENT_FILES = 4

    def __init__(self):
        super(MainWindow, self).__init__()
        # Load UI from compiled .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.recent_actions = []
        self.settings = QSettings("settings.ini", QSettings.IniFormat)

        self.ui.participantsTableWidget.update_ui_callback = self.update_ui

        self.assign_buttons()
        self.assign_actions()
        self.create_recent_menu()
        self.restore_state()
        self.statusBar().showMessage("מוכן")

    def restore_state(self):
        self.restoreGeometry(self.settings.value("geometry"))
        self.restoreState(self.settings.value("windowState"))

    def assign_buttons(self):
        self.ui.createTeamBtn.clicked.connect(self.create_team)
        self.ui.assignTeamsBtn.clicked.connect(self.assign_teams)

    def assign_actions(self):
        self.ui.loadParticipantsFileAction.triggered.connect(self.load_participants_file)
        self.ui.saveAsAction.triggered.connect(self.save_as)
        self.ui.saveAction.triggered.connect(self.save)
        self.ui.quitAction.triggered.connect(self.quit)
        self.ui.openAction.triggered.connect(self.open_project)
        self.ui.newAction.triggered.connect(self.new_project)
        self.ui.exportExcelAction.triggered.connect(self.exportExcel)

    def create_recent_menu(self):
        for i in range(self.MAX_RECENT_FILES):
            self.recent_actions.append(
                QAction(self, visible=False, triggered=self.open_recent_file))
            self.ui.recentFilesMenu.insertAction(self.ui.quitAction, self.recent_actions[i])
        self.update_recent_files_menu()

    def update_ui(self):
        self.render_participants_table()
        self.render_teams_widget()

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
            self.update_ui()
            self.statusBar().showMessage("פרויקט נוצר")
            return True
        else:
            self.statusBar().showMessage("יצירת פרויקט בוטלה")
            return False

    def open_recent_file(self):
        if self.can_exit():
            self.statusBar().showMessage("פותח פרויקט...")
            if client.open_project(self.sender().data()) == 0:
                self.update_ui()
                self.statusBar().showMessage("פרויקט נטען")
                self.update_current_file()
                return True
            else:
                self.statusBar().showMessage("טעינת פרויקט נכשלה")
        else:
            self.statusBar().showMessage("פתיחת פרויקט בוטלה")
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
                        self.update_ui()
                        self.update_current_file()
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
                    self.update_current_file()
                    return True
                else:
                    self.error_text("שגיאה בשמירת קובץ")
        self.statusBar().showMessage("שמירה בוטלה")
        return False

    def save(self):
        self.statusBar().showMessage("שמירת קובץ...")
        if client.current_file is None:
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
    def create_team(self):
        self.statusBar().showMessage("יוצר צוות...")
        teamCreationDialog = TeamCreationDialog()
        if teamCreationDialog.exec() == QtWidgets.QDialog.Accepted:
            self.statusBar().showMessage("צוות נוצר")
            self.render_teams_widget()
        else:
            self.statusBar().showMessage("צוות לא נוצר")

    @Slot()
    def assign_teams(self):
        self.statusBar().showMessage("מקצה צוותים...")
        client.assign_to_teams()
        self.update_ui()

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
        self.ui.participantsTableWidget.update_ui()

    def render_teams_widget(self):
        current_teams = []
        for i in range(self.ui.teamsTabWidget.count() - 1, -1, -1):
            tab = self.ui.teamsTabWidget.widget(i)
            if tab.team not in client.teams:
                self.ui.teamsTabWidget.removeTab(i)
                continue
            current_teams.append(tab.team)
            tab.update_ui()
        for i, team in enumerate(client.teams):
            if team not in current_teams:
                team_widget = TeamWidget(team, update_ui_callback=self.update_ui)
                self.ui.teamsTabWidget.insertTab(i, team_widget, team.name)

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

    def update_current_file(self):
        settings = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
        files = settings.value('recentFileList', [])
        if isinstance(files, str):
            files = [files]

        try:
            files.remove(client.current_file)
        except ValueError:
            pass

        files.insert(0, client.current_file)
        del files[self.MAX_RECENT_FILES:]

        settings.setValue('recentFileList', files)

        self.update_recent_files_menu()

    def update_recent_files_menu(self):
        settings = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
        files = settings.value('recentFileList', [])
        if isinstance(files, str):
            files = [files]

        files_no = 0
        if files:
            files_no = len(files)

        num_recent_files = min(files_no, self.MAX_RECENT_FILES)

        for i in range(num_recent_files):
            text = "&{}. {}".format(i + 1, os.path.basename(files[i]))
            self.recent_actions[i].setText(text)
            self.recent_actions[i].setData(files[i])
            self.recent_actions[i].setVisible(True)

        for i in range(num_recent_files, self.MAX_RECENT_FILES):
            self.recent_actions[i].setVisible(False)


    def exportExcel(self):
        saveDialog = QtWidgets.QFileDialog()
        saveDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        saveDialog.setNameFilter("")
        saveDialog.setNameFilter("excel file (*.xlsx)")
        saveDialog.setWindowTitle("ייצא לקובץ")
        saveDialog.exec()
        if saveDialog.result() == QtWidgets.QDialog.Accepted:
            filename = saveDialog.selectedFiles()[0]
            if filename:
                if client.export_to_excel(filename=filename):
                    self.statusBar().showMessage("קובץ ייוצא בהצלחה")
                    self.alert_text("קובץ ייוצא בהצלחה")
                    self.update_current_file()
                    return True
                else:
                    self.error_text("שגיאה בייצוא קובץ")
        self.statusBar().showMessage("שמירה בוטלה")
        return False

    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)

    def error_text(self, text: str):
        QtWidgets.QMessageBox.critical(self, "Error", text)
