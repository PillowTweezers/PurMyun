from PySide6.QtWidgets import QDialog

from gui.ui.ui_participantdialog import Ui_ParticipantDialog
from src.Participant import Participant, MAX_PRESENCE, MAX_OTHER


class ParticipantDialog(QDialog):
    def __init__(self, participant: Participant):
        super(ParticipantDialog, self).__init__()
        self.ui = Ui_ParticipantDialog()
        self.ui.setupUi(self)

        self.setWindowTitle(participant.name)
        self.ui.nameLbl.setText(participant.name)
        self.ui.gradeLbl.setText(participant.grade)
        if participant.team is not None:
            self.ui.teamLbl.setText(participant.team.name)

        self.ui.presenceBar.setValue(participant.presence)
        self.ui.presenceBar.setMaximum(MAX_PRESENCE)
        self.ui.presenceLbl.setText(f"{participant.presence}/{MAX_PRESENCE}")

        self.ui.squareBar.setValue(participant.square)
        self.ui.squareBar.setMaximum(MAX_OTHER)
        self.ui.squareLbl.setText(f"{participant.square}/{MAX_OTHER}")

        self.ui.crossBar.setValue(participant.cross)
        self.ui.crossBar.setMaximum(MAX_OTHER)
        self.ui.crossLbl.setText(f"{participant.cross}/{MAX_OTHER}")

        self.ui.parallelBar.setValue(participant.parallel)
        self.ui.parallelBar.setMaximum(MAX_OTHER)
        self.ui.parallelLbl.setText(f"{participant.parallel}/{MAX_OTHER}")

        self.ui.tripodBar.setValue(participant.tripod)
        self.ui.tripodBar.setMaximum(MAX_OTHER)
        self.ui.tripodLbl.setText(f"{participant.tripod}/{MAX_OTHER}")

        self.ui.anchoringBar.setValue(participant.anchoring)
        self.ui.anchoringBar.setMaximum(MAX_OTHER)
        self.ui.anchoringLbl.setText(f"{participant.anchoring}/{MAX_OTHER}")

        self.ui.macrameBar.setValue(participant.macrame)
        self.ui.macrameBar.setMaximum(MAX_OTHER)
        self.ui.macrameLbl.setText(f"{participant.macrame}/{MAX_OTHER}")

        self.ui.preferenceALbl.setText(participant.team_preference1)
        self.ui.preferenceBLbl.setText(participant.team_preference2)
        self.ui.preferenceCLbl.setText(participant.team_preference3)
