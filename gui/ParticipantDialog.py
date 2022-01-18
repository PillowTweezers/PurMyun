from PySide6.QtGui import Qt
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

        self.ui.presenceBar.setValue(participant.presence / MAX_PRESENCE * 100)
        self.ui.presenceBar.setFormat(f"{participant.presence}/{MAX_PRESENCE}")
        self.ui.squareBar.setValue(participant.square / MAX_OTHER * 100)
        self.ui.squareBar.setFormat(f"{participant.square}/{MAX_OTHER}")
        self.ui.crossBar.setValue(participant.cross / MAX_OTHER * 100)
        self.ui.crossBar.setFormat(f"{participant.cross}/{MAX_OTHER}")
        self.ui.parallelBar.setValue(participant.parallel / MAX_OTHER * 100)
        self.ui.parallelBar.setFormat(f"{participant.parallel}/{MAX_OTHER}")
        self.ui.tripodBar.setValue(participant.tripod / MAX_OTHER * 100)
        self.ui.tripodBar.setFormat(f"{participant.tripod}/{MAX_OTHER}")
        self.ui.anchoringBar.setValue(participant.anchoring / MAX_OTHER * 100)
        self.ui.anchoringBar.setFormat(f"{participant.anchoring}/{MAX_OTHER}")
        self.ui.macrameBar.setValue(participant.macrame / MAX_OTHER * 100)
        self.ui.macrameBar.setFormat(f"{participant.macrame}/{MAX_OTHER}")
        self.ui.macrameBar.setAlignment(Qt.AlignCenter)
