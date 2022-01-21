from PySide6.QtWidgets import QDialog

from gui.ui.ui_participantcreationdialog import Ui_ParticipantCreationDialog
from src import Client as client
from src.Participant import Participant


class ParticipantCreationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ParticipantCreationDialog()
        self.ui.setupUi(self)

        self.create_grades_combobox()

    def create_grades_combobox(self):
        for grade in client.grades:
            self.ui.gradesComboBox.addItem(grade)

    def accept(self) -> None:
        if not self.can_accept():
            self.ui.nameLineEdt.setFocus()
            return
        participant = Participant()
        participant.name = self.ui.nameLineEdt.text()
        participant.presence = self.ui.presenceSlider.value()
        participant.motivation = self.ui.motivationSlider.value()
        participant.square = self.ui.squareSlider.value()
        participant.cross = self.ui.crossSlider.value()
        participant.parallel = self.ui.parallelSlider.value()
        participant.tripod = self.ui.tripodSlider.value()
        participant.anchoring = self.ui.anchoringSlider.value()
        participant.macrame = self.ui.macrameSlider.value()
        client.add_participant(participant)
        self.done(QDialog.Accepted)

    def can_accept(self):
        return self.ui.nameLineEdt.text() != ""
