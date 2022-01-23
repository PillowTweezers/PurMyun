MAX_SCORE = 5


class Participant:

    def __init__(self, name: str, grade: str, score: int, participant_id: int):
        self.name = name
        self.grade = grade
        self.score = score
        self.participant_id = participant_id
        self.team = None

    def to_JSON(self) -> dict:
        dict_participant = {
            "name": self.name,
            "grade": self.grade,
            "score": self.score,
        }
        return dict_participant
