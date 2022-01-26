from PySide6 import QtWidgets
from PySide6.QtWidgets import QTabWidget, QToolButton

from gui.teamwidget import TeamWidget
from src import client


class TeamsTabWidget(QTabWidget):
    def __init__(self, parent=None, update_ui_callback=None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.setMovable(True)
        self.update_ui_callback = update_ui_callback
        self.tabCloseRequested.connect(lambda i: self.close_team_tab(i))
        self.create_new_tab_button()

    def create_new_tab_button(self):
        tb = QToolButton()
        # TODO: uncomment this when the icon is ready and can be centered
        # tb.setIcon(QtGui.QIcon(QtGui.QPixmap(u":/assets/add.png")))
        # tb.setIconSize(QtCore.QSize(16, 16))
        tb.setText("+")
        tb.setToolTip("צור צוות חדש")
        tb.clicked.connect(self.create_team)
        self.setCornerWidget(tb)

    def create_team(self):
        self.parent().parent().create_team()

    def close_team_tab(self, index: int):
        tab = self.widget(index)
        confirm_dialog = QtWidgets.QMessageBox()
        confirm_dialog.setWindowTitle("אישור מחיקת צוות")
        confirm_dialog.setText(f"האם אתה בטוח שברצונך למחוק את צוות {tab.team.name}?")
        confirm_dialog.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirm_dialog.setDefaultButton(QtWidgets.QMessageBox.No)
        confirm_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        if confirm_dialog.exec() == QtWidgets.QMessageBox.Yes:
            client.delete_team(tab.team)
            self.update_ui_callback()

    def update_ui(self):
        current_teams = []
        for i in range(self.count() - 1, -1, -1):
            tab = self.widget(i)
            if tab.team not in client.teams:
                self.removeTab(i)
                continue
            current_teams.append(tab.team)
            tab.update_ui()
        for i, team in enumerate(client.teams):
            if team not in current_teams:
                team_widget = TeamWidget(team, update_ui_callback=self.update_ui_callback)
                self.insertTab(i, team_widget, team.name)

    def resize_headers(self):
        for i in range(self.count()):
            tab = self.widget(i)
            tab.resize_table_header()
