from typing import Optional

from PySide6.QtWidgets import QDialog

from gui.ui.ui_participantcreationdialog import Ui_ParticipantCreationDialog
from src import client as client
from src.participant import MAX_SCORE, Participant, MIN_SCORE


class ParticipantCreationDialog(QDialog):
    def __init__(self, parent=None, participant: Optional[Participant] = None):
        super().__init__(parent)
        self.ui = Ui_ParticipantCreationDialog()
        self.ui.setupUi(self)

        self.participant = participant

        self.set_default_values()
        self.create_grades_combobox()
        if participant is not None:
            self.setWindowTitle(f"עריכת משתתף {participant.name}")
            self.ui.nameLineEdt.setText(participant.name)
            self.ui.gradeComboBox.setCurrentText(participant.grade)

    def accept(self) -> None:
        if not self.can_accept():
            self.ui.nameLineEdt.setFocus()
            return
        name = self.ui.nameLineEdt.text()
        grade = self.ui.gradeComboBox.currentText()
        score = self.ui.scoreSliderWidget.get_value()
        if self.participant is None:
            client.create_participant(name, grade, score)
        else:
            client.update_participant(self.participant, name, grade, score)
        self.done(QDialog.Accepted)

    def can_accept(self):
        return self.ui.nameLineEdt.text() != ""

    def create_grades_combobox(self):
        for grade in client.grades:
            self.ui.gradeComboBox.addItem(grade)

    def set_default_values(self):
        self.ui.scoreSliderWidget.set_value(MIN_SCORE if self.participant is None else self.participant.score)
        self.ui.scoreSliderWidget.set_min(MIN_SCORE)
        self.ui.scoreSliderWidget.set_max(MAX_SCORE)

    def set_participant_name(self, name):
        self.ui.nameLineEdt.setText(name)
        pass
