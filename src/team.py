from src.color import Color
from src.participant import Participant


class Team:
    def __init__(self, name: str, color: Color):
        self.name = name
        self.color = color
        self.participants = []

    def remove_participant(self, participant: Participant) -> None:
        self.participants.remove(participant)
        participant.team = None

    def add_participant(self, participant: Participant) -> None:
        self.participants.append(participant)
        participant.team = self

    def remove_all_participants(self) -> None:
        for participant in self.participants:
            participant.team = None
        self.participants = []

    def to_JSON(self) -> dict:
        team_dict = {
            "name": self.name,
            "color": self.color.to_JSON(),
            "participants": [participant.to_JSON() for participant in self.participants],
        }
        return team_dict
