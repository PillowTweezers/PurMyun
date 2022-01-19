import csv
import os
import pickle
from random import shuffle

from src.Participant import Participant
from src.Team import Team
from src.Weights import Weights

participants = []
teams = []
id_keeper = 0
last_project_file = None


def load_participants(file_path):
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


def create_team(team_name: str, team_weights: Weights):
    team_weights.name = team_name
    team = Team(name=team_name, weights=team_weights)
    teams.append(team)


def assign_to_teams():
    def remove_participant_from_list(participant, lst):
        for i in range(len(lst)):
            if lst[i] == participant:
                lst.pop(i)
                break

    participants_listings = dict()
    for team in teams:
        participants_listings[team.name] = participants.copy()
        participants_listings[team.name].sort(key=lambda par: par.calculateGrade(team.weights), reverse=True)
    running = True
    while running:
        shuffle(teams)
        for team in teams:
            if len(participants_listings[team.name]) == 0:
                running = False
                break
            recruit = participants_listings[team.name].pop(0)
            team.add_participant(recruit)
            recruit.team = team
            for participants_listing in participants_listings.values():
                remove_participant_from_list(recruit, participants_listing)


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
    global last_project_file
    try:
        with open(filename, 'wb') as f:
            pickle.dump((participants, teams), f, pickle.HIGHEST_PROTOCOL)
        last_project_file = filename
        return 0
    except PermissionError:
        return -1


def save_project():
    if last_project_file is not None:
        return save_project_as(last_project_file)
    else:
        return -1


def load_project(filename="unnamed.pickle"):
    with open(filename, 'rb') as f:
        global participants, teams
        participants, teams = pickle.load(f)


def add_participant(participant):
    global id_keeper
    participant.id = id_keeper
    id_keeper += 1
    participants.append(participant)


def remove_participant(participant_id):
    for participant in participants:
        if participant.id == participant_id:
            participants.remove(participant)
            break
