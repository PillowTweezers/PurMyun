from PySide6.QtWidgets import QWidget

from gui.ui.ui_fancyprogressbarwidget import Ui_FancyProgressBarWidget


class FancyProgressBarWidget(QWidget):
    def __init__(self, parent=None, min_value: int = 0, max_value: int = 100, value: int = 0):
        super().__init__(parent)
        self.ui = Ui_FancyProgressBarWidget()
        self.ui.setupUi(self)

        self.ui.progressBar.setMinimum(min_value)
        self.ui.progressBar.setMaximum(max_value)
        self.ui.progressBar.setValue(value)

    def set_maximum(self, value: int):
        self.ui.progressBar.setMaximum(value)

    def set_minimum(self, value: int):
        self.ui.progressBar.setMinimum(value)

    def set_value(self, value: int):
        self.ui.progressBar.setValue(value)
        self.ui.label.setText(f"{value}/{self.ui.progressBar.maximum()}")

    def get_value(self):
        return self.ui.progressBar.value()
