import pathlib
import sys

from PySide6 import QtWidgets
# This is bad, yet it's the only way to get the app to work.
from PySide6.QtGui import QIcon

sys.path.insert(0, str(pathlib.Path('./gui/ui').resolve()))
from gui.MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication([])
    app.setLayoutDirection(QtWidgets.QApplication.layoutDirection().RightToLeft)
    window = MainWindow()
    window.setWindowIcon(QIcon(u":/assets/logo.png"))
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
