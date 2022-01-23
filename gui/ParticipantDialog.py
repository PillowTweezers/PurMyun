from PySide6.QtWidgets import QDialog

from gui.ui.ui_participantdialog import Ui_ParticipantDialog
from src.participant import Participant, MAX_SCORE


class ParticipantDialog(QDialog):
    def __init__(self, participant: Participant):
        super(ParticipantDialog, self).__init__()
        self.ui = Ui_ParticipantDialog()
        self.ui.setupUi(self)

        self.setWindowTitle(participant.name)
        self.ui.nameLbl.setText(participant.name)
        self.ui.gradeLbl.setText(participant.grade)
        self.ui.progressBarWidget.setMaximum(MAX_SCORE)
        self.ui.progressBarWidget.setValue(participant.score)
        if participant.team is not None:
            self.ui.teamLbl.setText(participant.team.name)
