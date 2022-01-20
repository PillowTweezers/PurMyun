from src.Weights import Weights
from src.Participant import Participant

MAX_WEIGHT = 5


class Team:
    def __init__(self, name="", weights=Weights(), color=None):
        self.name = name
        self.weights = weights
        self.participants = []
        self.color = color

    def add_participant(self, participant: Participant):
        self.participants.append(participant)

    def clearParticipants(self):
        self.participants = []

    def __str__(self):
        output = f"Team {self.name}:\n"
        for i in range(len(self.participants)):
            output += f"\t{i + 1}. {self.participants[i].name}\n"
        return output
