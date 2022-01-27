import json
from random import shuffle
from typing import Optional

import xlsxwriter
from xlsxwriter import Workbook

from src.clientjsonencoder import ClientJSONEncoder
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


def create_mixed_worksheet(workbook: Workbook):
    worksheet = workbook.add_worksheet(name="משולב")
    worksheet.right_to_left()

    row = 1
    col = 0
    sorted_participants = sorted(participants, key=lambda x: grades.index(x.grade), reverse=False)
    for participant in sorted_participants:
        cell_format = workbook.add_format()
        if participant.team is not None:
            cell_format.set_bg_color(participant.team.color.to_hex())
        else:
            cell_format.set_bg_color('#FFFFFF')
        worksheet.write(row, col, participant.name, cell_format)
        worksheet.write(row, col + 1, participant.team.name if participant.team is not None else "", cell_format)
        worksheet.write(row, col + 2, participant.grade, cell_format)
        row += 1
    worksheet.add_table('A1:C' + str(row),
                        {'autofilter': True, 'columns': [{'header': 'שם'}, {'header': 'צוות'}, {'header': 'שכבה'}]})
    # Resize the columns to fit the data in the cells
    max_name = max([len(p.name) for p in participants])
    max_team = max([len(p.team.name) for p in participants if p.team is not None])
    max_grade = max([len(p.grade) for p in participants])
    worksheet.set_column('A:A', max_name + 1)
    worksheet.set_column('B:B', max_team + 1)
    worksheet.set_column('C:C', max_grade + 1)


def create_teams_worksheet(workbook: Workbook):
    worksheet = workbook.add_worksheet(name="צוותים")
    worksheet.right_to_left()

    def sort_participants(participants_list: list[Participant]) -> list[Participant]:
        return sorted(participants_list, key=lambda par: (grades.index(par.grade), par.name), reverse=False)

    def draw_team_table(row: int, col: int, team: Team = None) -> (int, int):
        cell_format = workbook.add_format()
        display_participants = [p for p in participants if p.team is team]
        bold = workbook.add_format({'bold': True})

        display_name = team.name if team is not None else "מחוסרי צוות"
        worksheet.write(row, col, display_name, bold)
        row += 1

        worksheet.add_table(row, col, row + len(display_participants), col + 1,
                            {'autofilter': True,
                             'columns': [{'header': 'שם', 'format': bold}, {'header': 'שכבה', 'format': bold}]})
        row += 1

        if team is not None:
            cell_format.set_bg_color(team.color.to_hex())
        else:
            cell_format.set_bg_color('#FFFFFF')
        for participant in sort_participants(display_participants):
            worksheet.write(row, col, participant.name, cell_format)
            worksheet.write(row, col + 1, participant.grade, cell_format)
            row += 1

        # Resize the columns to fit the data in the cells
        if len(display_participants) > 0:
            max_name = max([len(p.name) for p in display_participants])
            max_grade = max([len(p.grade) for p in display_participants])
            worksheet.set_column(col, col, max_name + 1)
            worksheet.set_column(col + 1, col + 1, max_grade + 1)
        return row - len(display_participants) - 2, col + 4

    start_row = 0
    start_col = 0
    for team in teams:
        start_row, start_col = draw_team_table(start_row, start_col, team)
    draw_team_table(start_row, start_col)
    workbook.close()


def export_to_excel(filename: str) -> int:
    try:
        workbook = xlsxwriter.Workbook(filename)
        create_mixed_worksheet(workbook)
        create_teams_worksheet(workbook)
    except PermissionError as e:
        return 1
    return 0
