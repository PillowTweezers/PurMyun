from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

import gui.ui.window_rc
from gui.MainWindow import MainWindow

# This is in order to block automaticly removing the import of the rc file
_ = gui.ui.window_rc.qt_resource_name


def main():
    app = QtWidgets.QApplication([])
    app.setLayoutDirection(QtWidgets.QApplication.layoutDirection().RightToLeft)
    window = MainWindow()
    window.setWindowIcon(QIcon(u":/assets/logo.png"))
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
