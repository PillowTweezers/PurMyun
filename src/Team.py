from src.Participant import Participant
from src.Weights import Weights

MAX_WEIGHT = 5


class Team:
    def __init__(self, name="", weights=Weights(), color=None):
        self.name = name
        self.weights = weights
        self.participants = []
        self.color = color

    def remove_participant_by_id(self, participant_id):
        particpant = self.find_participant(participant_id)
        self.remove_participant(particpant)

    def remove_participant(self, participant: Participant):
        self.participants.remove(participant)
        participant.team = None

    def find_participant(self, participant_id):
        for participant in self.participants:
            if participant.id == participant_id:
                return participant

    def add_participant(self, participant: Participant):
        self.participants.append(participant)

    def clearParticipants(self):
        self.participants = []

    def __str__(self):
        output = f"Team {self.name}:\n"
        for i in range(len(self.participants)):
            output += f"\t{i + 1}. {self.participants[i].name}\n"
        return output
