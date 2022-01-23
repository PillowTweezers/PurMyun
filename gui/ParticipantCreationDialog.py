from PySide6.QtWidgets import QDialog

from gui.ui.ui_participantcreationdialog import Ui_ParticipantCreationDialog
from src import client as client
from src.participant import MAX_SCORE


class ParticipantCreationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ParticipantCreationDialog()
        self.ui.setupUi(self)

        self.set_default_values()
        self.create_grades_combobox()

    def accept(self) -> None:
        if not self.can_accept():
            self.ui.nameLineEdt.setFocus()
            return
        name = self.ui.nameLineEdt.text()
        grade = self.ui.gradeComboBox.currentText()
        score = self.ui.scoreSliderWidget.get_value()
        client.create_participant(name, grade, score)
        self.done(QDialog.Accepted)

    def can_accept(self):
        return self.ui.nameLineEdt.text() != ""

    def create_grades_combobox(self):
        for grade in client.grades:
            self.ui.gradeComboBox.addItem(grade)

    def set_default_values(self):
        self.ui.scoreSliderWidget.set_value(1)
        self.ui.scoreSliderWidget.set_min(1)
        self.ui.scoreSliderWidget.set_max(MAX_SCORE)
