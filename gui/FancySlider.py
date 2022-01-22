from PySide6.QtWidgets import QWidget

from gui.ui.ui_fancyslider import Ui_FancySliderWidget


class FancySlider(QWidget):
    def __init__(self, parent=None, min_value=0, max_value=100, value=0):
        super().__init__(parent)
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
