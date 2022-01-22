from PySide6.QtWidgets import QWidget

from gui.ui.ui_fancysliderwidget import Ui_FancySliderWidget
from gui.ui.ui_fancysliderhorizontalwidget import Ui_FancySliderHorizontalWidget


class FancySliderWidget(QWidget):
    def __init__(self, parent=None, min_value=0, max_value=100, value=0, horizontal=False):
        super().__init__(parent)
        if horizontal:
            self.ui = Ui_FancySliderHorizontalWidget()
        else:
            self.ui = Ui_FancySliderWidget()
        self.ui.setupUi(self)

        self.ui.slider.setMinimum(min_value)
        self.ui.slider.setMaximum(max_value)
        self.ui.slider.setValue(value)

        self.ui.spinBox.setMinimum(min_value)
        self.ui.spinBox.setMaximum(max_value)
        self.ui.spinBox.setValue(value)

        self.ui.slider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.slider.setValue)

    def set_min(self, min_value):
        self.ui.slider.setMinimum(min_value)
        self.ui.spinBox.setMinimum(min_value)

    def set_max(self, max_value):
        self.ui.slider.setMaximum(max_value)
        self.ui.spinBox.setMaximum(max_value)

    def set_value(self, value):
        self.ui.slider.setValue(value)
        self.ui.spinBox.setValue(value)

    def get_value(self):
        return self.ui.slider.value()
