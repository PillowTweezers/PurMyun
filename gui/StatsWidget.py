from PySide6.QtWidgets import QWidget

from gui.ui.ui_statsWidget import Ui_StatsWidget


class StatsWidget(QWidget):
    def __init__(self, parent=None):
        super(StatsWidget, self).__init__(parent)
        self.ui = Ui_StatsWidget()
        self.ui.setupUi(self)

        self.sliders = [self.ui.squareSlider, self.ui.crossSlider, self.ui.parallelSlider, self.ui.tripodSlider,
                        self.ui.anchoringSlider, self.ui.macrameSlider]

        for slider in self.sliders:
            slider.set_value(1)
            slider.set_min(1)
            slider.set_max(5)
