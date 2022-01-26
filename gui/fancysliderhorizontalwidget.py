from gui.fancysliderwidget import FancySliderWidget


class FancySliderHorizontalWidget(FancySliderWidget):
    def __init__(self, parent=None):
        super(FancySliderHorizontalWidget, self).__init__(parent, horizontal=True)
