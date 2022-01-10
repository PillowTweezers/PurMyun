from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QToolBar
from Team import Team
from Participant import Participant
from Weights import Weights
from ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().showMessage("Ready")


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
