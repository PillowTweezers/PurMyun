from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QToolBar
from Team import Team
from Participant import Participant
from Weights import Weights


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("פורמיון")
        self.setWindowIcon(QtGui.QIcon("../assets/icon.png"))
        self.setGeometry(100, 100, 800, 500)
        self.statusBar().showMessage("Ready")

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        helpMenu = mainMenu.addMenu("Help")
        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut("Ctrl+O")

        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut("Ctrl+S")

        exitAction = QAction(QIcon('../assets/exit.png'), "Exit", self)
        exitAction.setShortcut("Ctrl+X")
        exitAction.triggered.connect(self.exit_app)

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        # root_layout = QtWidgets.QHBoxLayout()
        # self.setLayout(root_layout)

        # Side bar
        # side_bar_layout = QtWidgets.QVBoxLayout()
        #
        # load_participants_btn = QtWidgets.QPushButton("Load participants")
        # load_participants_btn.clicked.connect(self.load_participants)
        # side_bar_layout.addWidget(load_participants_btn)
        # root_layout.addLayout(side_bar_layout)
        toolbarFont = QtGui.QFont("Helvetica [Cronyx]", 10, QtGui.QFont.Bold)
        load_participants_action = QAction(QIcon("../assets/load.jpg"), "Load Participants", self)
        load_participants_action.triggered.connect(self.load_participants)
        load_participants_action.setFont(toolbarFont)
        load_participants_action.setShortcut("Ctrl+L")

        create_team_action = QAction(QIcon("../assets/team.png"), "Create Team", self)
        create_team_action.triggered.connect(self.add_team)
        create_team_action.setFont(toolbarFont)
        create_team_action.setShortcut("Ctrl+T")

        toolbar = QToolBar("Toolbar", self)
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)
        toolbar.addAction(load_participants_action)
        toolbar.addAction(create_team_action)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbar)

    def exit_app(self):
        self.close()
        exit(0)

    def add_team(self):
        # team_name = input("Enter new team's name:\n")
        # team_weights = create_weights_object()
        # team = Team(name=team_name, weights=team_weights)
        # teams.append(team)
        self.alert_text("Not implemented yet")

    def load_participants(self):
        self.alert_text("Not implemented yet")
        pass
    
    def alert_text(self, text: str):
        QtWidgets.QMessageBox.about(self, "Alert", text)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
