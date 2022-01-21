from PySide6.QtWidgets import QDialog

from gui.ui.ui_gradedialog import Ui_GradesDialog
from src import Client as client


class GradesDialog(QDialog):
    def __init__(self, parent=None):
        super(GradesDialog, self).__init__(parent)
        self.ui = Ui_GradesDialog()
        self.ui.setupUi(self)

        for i, grade in enumerate(client.grades):
            if i == 0:
                self.ui.sixGradeEdit.setText(grade)
            elif i == 1:
                self.ui.sevenGradeEdit.setText(grade)
            elif i == 2:
                self.ui.eightGradeEdit.setText(grade)

    def accept(self) -> None:
        if self.can_exit():
            grades = [self.ui.sixGradeEdit.text(), self.ui.sevenGradeEdit.text(), self.ui.eightGradeEdit.text()]
            client.set_grades(grades)
            self.done(QDialog.Accepted)
        else:
            self.parent().error_text("אנא מלא את כל השדות")

    def reject(self) -> None:
        if len(client.grades) != 3:
            self.parent().error_text("לא ניתן לבטל את הטופס,\nאנא מלא את כל השדות")
        else:
            self.done(QDialog.Rejected)

    def can_exit(self) -> bool:
        return self.ui.sixGradeEdit.text() != "" and self.ui.sevenGradeEdit.text() != "" and \
               self.ui.eightGradeEdit.text() != ""
