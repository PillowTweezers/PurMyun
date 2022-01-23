from PySide6.QtGui import QColor


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def to_hex(self) -> str:
        return "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)

    @staticmethod
    def from_qcolor(qcolor: QColor) -> 'Color':
        return Color(qcolor.red(), qcolor.green(), qcolor.blue())

    def to_JSON(self) -> str:
        color_dict = {
            "r": self.r,
            "g": self.g,
            "b": self.b,
        }
        return color_dict
