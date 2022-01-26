from PySide6.QtWidgets import QDialog

from gui.ui.ui_aboutdialog import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.ui.dataLabel.setOpenExternalLinks(True)
        self.ui.creditsTextBrowser.setOpenExternalLinks(True)