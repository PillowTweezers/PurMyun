from Weights import Weights
from Participant import Participant


class Team:
    def __init__(self, name="", weights=Weights()):
        self.name = name
        self.weights = weights
        self.participants = []

    #
    # def __init__(self):
    #     self.name = ""
    #     self.weights = Weights()
    #     self.participants = []
    def add_participant(self, participant: Participant):
        self.participants.append(participant)

    def clearParticipants(self):
        self.participants = []

    def __str__(self):
        output = f"Team {self.name}:\n"
        for i in range(len(self.participants)):
            output += f"\t{i + 1}. {self.participants[i].name}\n"
        return output
