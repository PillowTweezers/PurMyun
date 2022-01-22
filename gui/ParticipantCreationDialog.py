from PySide6.QtWidgets import QDialog

from gui.ui.ui_participantcreationdialog import Ui_ParticipantCreationDialog
from src import Client as client
from src.Participant import Participant


class ParticipantCreationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ParticipantCreationDialog()
        self.ui.setupUi(self)

        self.set_default_values()
        self.create_grades_combobox()
        self.create_preferences_comboboxes()

    def accept(self) -> None:
        if not self.can_accept():
            self.ui.nameLineEdt.setFocus()
            return
        participant = Participant()
        participant.name = self.ui.nameLineEdt.text()
        participant.grade = self.ui.gradesComboBox.currentText()
        participant.presence = self.ui.presenceWidget.get_value()
        participant.motivation = self.ui.motivationWidget.get_value()
        participant.square = self.ui.statsWidget.ui.squareSlider.get_value()
        participant.cross = self.ui.statsWidget.ui.crossSlider.get_value()
        participant.parallel = self.ui.statsWidget.ui.parallelSlider.get_value()
        participant.tripod = self.ui.statsWidget.ui.tripodSlider.get_value()
        participant.anchoring = self.ui.statsWidget.ui.anchoringSlider.get_value()
        participant.macrame = self.ui.statsWidget.ui.macrameSlider.get_value()
        participant.preference_a = self.ui.preferenceAComboBox.currentText()
        participant.preference_b = self.ui.preferenceBComboBox.currentText()
        participant.preference_c = self.ui.preferenceCComboBox.currentText()
        client.add_participant(participant)
        self.done(QDialog.Accepted)

    def can_accept(self):
        return self.ui.nameLineEdt.text() != ""

    def create_grades_combobox(self):
        for grade in client.grades:
            self.ui.gradesComboBox.addItem(grade)

    def create_preferences_comboboxes(self):
        for team in client.teams:
            self.ui.preferenceAComboBox.addItem(team.name)
            self.ui.preferenceBComboBox.addItem(team.name)
            self.ui.preferenceCComboBox.addItem(team.name)

    def set_default_values(self):
        self.ui.motivationWidget.set_min(1)
        self.ui.motivationWidget.set_max(10)
        self.ui.motivationWidget.set_value(1)
        self.ui.presenceWidget.set_min(1)
        self.ui.presenceWidget.set_max(10)
        self.ui.presenceWidget.set_value(1)
