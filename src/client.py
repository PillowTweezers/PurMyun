import json
from random import shuffle
from typing import Optional

from src.client_json_encoder import ClientJSONEncoder
from src.color import Color
from src.participant import Participant
from src.team import Team

participants = []
teams = []
grades = []
participant_id_keeper = 0
current_file = None
is_dirty = False


def create_participant(name: str, grade: str, score: int, team: Optional[Team] = None) -> Participant:
    __set_dirty(True)
    global participant_id_keeper
    participant = Participant(name=name, grade=grade, score=score, participant_id=participant_id_keeper)
    participant_id_keeper += 1
    if team is not None:
        team.add_participant(participant)
    participants.append(participant)
    return participant


def create_team(team_name: str, color: Color = None) -> Team:
    __set_dirty(True)
    team = Team(team_name, color)
    teams.append(team)
    return team


def add_participant_to_team(participant: Participant, team: Team) -> None:
    __set_dirty(True)
    remove_participant_from_team(participant)
    team.add_participant(participant)


def remove_participant_from_team(participant: Participant) -> int:
    if participant.team is not None:
        __set_dirty(True)
        participant.team.remove_participant(participant)
        return 0
    return -1


def update_participant(participant: Participant, name: Optional[str] = None, grade: Optional[str] = None,
                       score: Optional[int] = None) -> None:
    __set_dirty(True)
    if name is not None:
        participant.name = name
    if grade is not None:
        participant.grade = grade
    if score is not None:
        participant.score = score


def update_team(team: Team, name: Optional[str] = None, color: Optional[Color] = None) -> None:
    __set_dirty(True)
    if name is not None:
        team.name = name
    if color is not None:
        team.color = color


def delete_team(team: Team) -> None:
    __set_dirty(True)
    team.remove_all_participants()
    teams.remove(team)


def remove_participant(participant: Participant) -> None:
    __set_dirty(True)
    if participant.team is not None:
        participant.team.remove_participant(participant)
    participants.remove(participant)


def assign_to_teams() -> int:
    if len(teams) == 0:
        return -1
    __set_dirty(True)

    participants_copy = participants.copy()
    sorted(participants_copy, key=lambda x: x.score, reverse=True)
    while len(participants_copy) > 0:
        teams_copy = teams.copy()
        shuffle(teams_copy)
        for team in teams_copy:
            if len(participants_copy) == 0:
                break
            participant = participants_copy.pop()
            add_participant_to_team(participant, team)
    return 0


def find_participant(participant_id: int) -> Optional[Participant]:
    for participant in participants:
        if participant.participant_id == participant_id:
            return participant
    return None


def has_grades() -> bool:
    return len(grades) == 3


def set_grades(grades_list: list) -> None:
    __set_dirty(True)
    global grades
    grades = grades_list


def __set_dirty(_is_dirty: bool) -> None:
    global is_dirty
    is_dirty = _is_dirty


def to_JSON() -> dict:
    client_dict = {
        "participants": [p for p in participants if p.team is None],
        "teams": teams,
        "grades": grades
    }
    return client_dict


def save_project_as(filename: str) -> int:
    global current_file
    current_file = filename
    try:
        with open(filename, 'w') as f:
            json.dump(to_JSON(), f, cls=ClientJSONEncoder, indent=4, sort_keys=True)
            __set_dirty(False)
            return 0
    except PermissionError:
        return -1


def save_project() -> int:
    global current_file
    if current_file is not None:
        return save_project_as(current_file)
    else:
        return -1


def open_project(filename: str) -> int:
    global current_file
    try:
        with open(filename, 'r') as f:
            client_dict = json.load(f)
            global participants, teams, grades
            grades = client_dict["grades"]
            for participant in client_dict["participants"]:
                create_participant(participant["name"], participant["grade"], participant["score"])
            for team in client_dict["teams"]:
                t_obj = create_team(team["name"], Color(team["color"]["r"], team["color"]["g"], team["color"]["b"]))
                for participant in team["participants"]:
                    create_participant(participant["name"], participant["grade"], participant["score"], t_obj)
        current_file = filename
        __set_dirty(False)
        return 0
    except FileNotFoundError:
        return -1
    except json.decoder.JSONDecodeError:
        return -2
    except PermissionError:
        return -3


def new_project() -> None:
    __set_dirty(False)
    global participants, teams
    participants = []
    teams = []
    global participant_id_keeper
    participant_id_keeper = 0
    global current_file
    current_file = None


def export_to_excel(filename: str = "results.xlsx") -> int:
    # TODO: Implement this.
    pass
