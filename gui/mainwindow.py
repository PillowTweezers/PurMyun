import os

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, Slot
from PySide6.QtGui import QAction
from appdirs import AppDirs

from gui.aboutdialog import AboutDialog
from gui.gradesdialog import GradesDialog
from gui.participantcreationdialog import ParticipantCreationDialog
from gui.teamcreationdialog import TeamCreationDialog
from gui.ui.ui_mainwindow import Ui_MainWindow
from src import client as client

MAX_RECENT_FILES = 4


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # Load UI from compiled .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.recent_actions = []
        settings_path = AppDirs("PurMyun", "PillowTweezers").user_config_dir
        os.makedirs(settings_path, exist_ok=True)
        self.settings = QSettings(settings_path + "/settings.ini", QSettings.IniFormat)

        self.ui.teamsTabWidget.update_ui_callback = self.update_ui
        self.assign_buttons()
        self.assign_actions()
        self.create_recent_menu()
        self.save_default_state()
        self.restore_state()
        self.statusBar().showMessage("מוכן")

    def assign_buttons(self):
        self.ui.createTeamBtn.clicked.connect(self.create_team)
        self.ui.assignTeamsBtn.clicked.connect(self.assign_teams)
        self.ui.gradesBtn.clicked.connect(self.open_grades_dialog)

    def assign_actions(self):
        self.ui.loadParticipantsFileAction.triggered.connect(self.load_participants_file)
        self.ui.saveAsAction.triggered.connect(self.save_as)
        self.ui.saveAction.triggered.connect(self.save)
        self.ui.quitAction.triggered.connect(self.close)
        self.ui.openAction.triggered.connect(self.open_project)
        self.ui.newAction.triggered.connect(self.new_project)
        self.ui.exportExcelAction.triggered.connect(self.export_to_excel)
        self.ui.resetUiAction.triggered.connect(self.reset_ui)
        self.ui.resizeTablesAction.triggered.connect(self.resize_tables)
        self.ui.aboutAction.triggered.connect(self.about)

    def create_recent_menu(self):
        for i in range(MAX_RECENT_FILES):
            self.recent_actions.append(
                QAction(self, visible=False, triggered=self.open_recent_file))
            self.ui.recentFilesMenu.insertAction(self.ui.quitAction, self.recent_actions[i])
        self.update_recent_files_menu()

    def restore_state(self):
        self.restoreGeometry(self.settings.value("geometry"))
        self.restoreState(self.settings.value("windowState"))

    def reset_ui(self):
        # FIXME: Participant tables should resize headers.
        cur_pos = self.pos()
        self.restoreGeometry(self.settings.value("defaultGeometry"))
        self.restoreState(self.settings.value("defaultState"))
        self.move(cur_pos)

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

    def open_grades_dialog(self):
        dialog = GradesDialog(self)
        dialog.exec_()

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
        dialog = TeamCreationDialog(parent=self)
        if dialog.exec() == QtWidgets.QDialog.Accepted:
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
        if not client.has_grades():
            self.open_grades_dialog()
        self.statusBar().showMessage("טוען משתתפים...")
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, str("בחר קובץ"), "", str("*.txt"))
        if file_path:
            try:
                with (open(file_path, "r", encoding="utf-8")) as file:
                    for line in file:
                        name = line.rstrip("\n")
                        if name:
                            dialog = ParticipantCreationDialog(self)
                            dialog.set_participant_name(name)
                            if dialog.exec() == QtWidgets.QDialog.Accepted:
                                self.statusBar().showMessage(f"משתתף {name} נוצר")
                                self.update_ui()
                            else:
                                self.statusBar().showMessage("משתתף לא נוצר")
            except FileNotFoundError:
                self.error_text("קובץ לא נמצא")
            except PermissionError as e:
                self.error_text(f"קובץ לא ניתן לקרוא: {e}")
        self.statusBar().showMessage("טעינת משתתפים בוטלה")

    def render_participants_table(self):
        self.ui.participantsTableWidget.update_ui()

    def render_teams_widget(self):
        self.ui.teamsTabWidget.update_ui()

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
        files = self.settings.value('recentFileList', [])
        if isinstance(files, str):
            files = [files]

        try:
            files.remove(client.current_file)
        except ValueError:
            pass

        files.insert(0, client.current_file)
        del files[MAX_RECENT_FILES:]

        self.settings.setValue('recentFileList', files)

        self.update_recent_files_menu()

    def update_recent_files_menu(self):
        files = self.settings.value('recentFileList', [])
        # TODO: Sometimes None is added to the list. This is only a workaround. SOLVE IT!
        for file in files:
            if file is None:
                files.remove(file)
                self.settings.setValue('recentFileList', files)
        if isinstance(files, str):
            files = [files]

        files_no = 0
        if files:
            files_no = len(files)

        num_recent_files = min(files_no, MAX_RECENT_FILES)

        for i in range(num_recent_files):
            text = "&{}. {}".format(i + 1, os.path.basename(files[i]))
            self.recent_actions[i].setText(text)
            self.recent_actions[i].setData(files[i])
            self.recent_actions[i].setVisible(True)

        for i in range(num_recent_files, MAX_RECENT_FILES):
            self.recent_actions[i].setVisible(False)

    def export_to_excel(self):
        if not client.has_grades():
            self.open_grades_dialog()
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

    def about(self):
        dialog = AboutDialog(parent=self)
        dialog.exec()

    def resize_tables(self):
        self.ui.participantsTableWidget.resize_header()
        self.ui.teamsTabWidget.resize_headers()

    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)

    def error_text(self, text: str):
        QtWidgets.QMessageBox.critical(self, "Error", text)
