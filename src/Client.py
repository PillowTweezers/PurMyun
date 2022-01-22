from __future__ import annotations

import csv
import os
import pickle
from random import shuffle

import xlsxwriter

from src.Participant import Participant
from src.Team import Team
from src.Weights import Weights

participants = []
teams = []
id_keeper = 0
current_file = None
is_dirty = False
grades = []


def load_participants(file_path):
    global is_dirty
    is_dirty = True
    global id_keeper
    if file_path == "":
        return [], 1
    elif not (os.path.isfile(file_path) and os.access(file_path, mode=os.R_OK)):
        return -1
    with open(file_path, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = id_keeper
            id_keeper += 1
            participants.append(Participant(row))
    return participants.copy(), 0


def create_team(team_name: str, team_weights: Weights, color=None):
    global is_dirty
    is_dirty = True
    team_weights.name = team_name
    team = Team(name=team_name, weights=team_weights, color=color)
    teams.append(team)


def assign_to_teams():
    global is_dirty
    is_dirty = True

    def remove_participant_from_list(participant, lst):
        for i in range(len(lst)):
            if lst[i] == participant:
                lst.pop(i)
                break

    if len(teams) == 0:
        return
    for team in teams:
        team.clearParticipants()
    participants_listings = dict()
    for team in teams:
        participants_listings[team.name] = participants.copy()
        participants_listings[team.name].sort(key=lambda par: par.calculateGrade(team.weights), reverse=True)
    running = True
    while running:
        teams_copy = teams.copy()
        shuffle(teams_copy)
        for team in teams_copy:
            if len(participants_listings[team.name]) == 0:
                running = False
                break
            recruit = participants_listings[team.name].pop(0)
            team.add_participant(recruit)
            recruit.team = team
            for participants_listing in participants_listings.values():
                remove_participant_from_list(recruit, participants_listing)


def find_participant(id):
    for participant in participants:
        if participant.id == id:
            return participant
    return None


def move_participant(participant_id: int, team: Team):
    global is_dirty
    is_dirty = True
    participant = find_participant(participant_id)
    if participant is None:
        return -1
    if participant.team is not None:
        participant.team.remove_participant(participant)
    team.add_participant(participant)
    participant.team = team


def save_teams_to_file():
    with open('teams.pickle', 'wb') as f:
        pickle.dump(teams, f, pickle.HIGHEST_PROTOCOL)


def load_teams_from_file():
    if os.path.exists('teams.pickle'):
        with open('teams.pickle', 'rb') as f:
            global teams
            teams = pickle.load(f)


def print_all_teams():
    for team in teams:
        print(str(team))


def save_participants_to_file(filename="participants.pickle"):
    with open(filename, 'wb') as f:
        pickle.dump(participants, f, pickle.HIGHEST_PROTOCOL)


def save_project_as(filename: str | None = "unnamed.pickle"):
    global is_dirty
    global current_file
    try:
        with open(filename, 'wb') as f:
            pickle.dump((participants, teams, grades), f, pickle.HIGHEST_PROTOCOL)
        is_dirty = False
        current_file = filename
        return 0
    except PermissionError:
        return -1


def save_project():
    if current_file is not None:
        return save_project_as(current_file)
    else:
        return -1


def set_grades(grades_list: list):
    global is_dirty
    is_dirty = True
    global grades
    grades = grades_list


def open_project(filename="unnamed.pickle"):
    global is_dirty
    global current_file
    try:
        with open(filename, 'rb') as f:
            global participants, teams, grades
            participants, teams, grades = pickle.load(f)
            max_id = 0
            for participant in participants:
                if participant.id > max_id:
                    max_id = participant.id
            global id_keeper
            id_keeper = max_id + 1
        current_file = filename
        is_dirty = False
        return 0
    except FileNotFoundError:
        return -1
    except PermissionError:
        return -2


def add_participant(participant):
    global is_dirty
    is_dirty = True
    global id_keeper
    participant.id = id_keeper
    id_keeper += 1
    participants.append(participant)


def remove_participant(participant_id):
    global is_dirty
    is_dirty = True
    for participant in participants:
        if participant.id == participant_id:
            if participant.team:
                participant.team.remove_participant(participant)
            participants.remove(participant)
            break


def remove_participant_from_team(participant_id, team: Team):
    global is_dirty
    is_dirty = True
    team.remove_participant_by_id(participant_id)


def sort_participants(participants_list: list[Participant]):
    return sorted(participants_list, key=lambda par: (grades.index(par.grade), par.name), reverse=False)


def export_to_excel(filename: str = "results.xlsx"):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    def draw_table(row: int, col: int, team: Team):
        if team.color is not None:
            background_color = workbook.add_format({'bg_color': team.color.name()})
        else:
            background_color = None
        worksheet.write(row, col + 1, team.name, bold)
        row += 1
        worksheet.write(row, col, "שכבה", bold)
        worksheet.write(row, col + 1, "שם", bold)
        row += 1
        for par in sort_participants(team.participants):
            worksheet.write(row, col, par.grade, background_color)
            worksheet.write(row, col + 1, par.name, background_color)
            row += 1
        return 0, col + 4

    def getUnassignedParticipants():
        unassigned = []
        for participant in participants:
            if participant.team is None:
                unassigned.append(participant)
        return unassigned

    start_row = 0
    start_col = 0
    for group in teams:
        start_row, start_col = draw_table(start_row, start_col, group)
    unsigned_participants = getUnassignedParticipants()
    if len(unsigned_participants) > 0:
        worksheet.write(start_row, start_col + 1, "ללא צוות", bold)
        start_row += 1
        worksheet.write(start_row, start_col, "שכבה", bold)
        worksheet.write(start_row, start_col + 1, "שם", bold)
        start_row += 1
        for par in sort_participants(getUnassignedParticipants()):
            worksheet.write(start_row, start_col, par.grade)
            worksheet.write(start_row, start_col + 1, par.name)
            start_row += 1
    try:
        workbook.close()
        return True
    except xlsxwriter.exceptions.FileCreateError or PermissionError:
        return False


def has_grades() -> bool:
    return len(grades) == 3


def new_project():
    global is_dirty
    is_dirty = False
    global participants, teams
    participants = []
    teams = []
    global id_keeper
    id_keeper = 0
    global current_file
    current_file = None


def update_team(team: Team, name, weights: Weights, color):
    global is_dirty
    is_dirty = True
    team.name = name
    team.weights = weights
    team.color = color
