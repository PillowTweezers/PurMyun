from src.Weights import Weights
from src.Team import Team
from src.Participant import Participant
import csv
import os
import pickle

teams = []
participants = []


def print_options():
    print("1. Create new team")
    print("2. Load people from csv")
    print("3. Change team weights")
    print("4. Remove team")
    print("5. Print team")
    print("6. Print all teams")
    print("7. Assign to teams")
    print("8. Clear all data")
    print("9. Save")
    print("10. Exit")
    print("11. Save and exit")
    pass


def create_weights_object():
    print("Enter new team's weights:")
    weights = Weights()
    weights.square = int(input("Enter square weight:\n"))
    weights.cross = int(input("Enter cross weight:\n"))
    weights.parallel = int(input("Enter parallel weight:\n"))
    weights.tripod = int(input("Enter tripod weight:\n"))
    weights.anchoring = int(input("Enter anchoring weight:\n"))
    weights.macrame = int(input("Enter macrame weight:\n"))
    return weights


def create_new_team():
    team_name = input("Enter new team's name:\n")
    team_weights = create_weights_object()
    team = Team(name=team_name, weights=team_weights)
    teams.append(team)
    print("Team created successfully")


def load_people_from_file():
    while True:
        # file_path = input("Enter file name:\n")
        file_path = 'formsAnswers.csv'
        # Check if can read file
        if os.path.isfile(file_path) and os.access(file_path, mode=os.R_OK):
            break
        else:
            print("File not found")
    with open(file_path, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            participants.append(Participant(row))
    print_all_teams()


def change_team_weights():
    for i in range(len(teams)):
        print(f"{i + 1}. {teams[i].name}")
    team_number = int(input("Enter team number:\n"))
    team = teams[team_number - 1]
    team.weights = create_weights_object()


def remove_team():
    for i in range(len(teams)):
        print(f"{i + 1}. {teams[i].name}")
    team_number = int(input("Enter team number:\n"))
    teams.pop(team_number - 1)


def remove_participant_from_list(participant, lst):
    for i in range(len(lst)):
        if lst[i] == participant:
            lst.pop(i)
            break


def assign_to_teams():
    participants_listings = dict()
    for team in teams:
        participants_listings[team.name] = participants.copy()
        participants_listings[team.name].sort(key=lambda par: par.calculateGrade(team.weights), reverse=True)
    running = True
    while running:
        for team in teams:
            if len(participants_listings[team.name]) == 0:
                running = False
                break
            recruit = participants_listings[team.name].pop(0)
            team.add_participant(recruit)
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


def print_team():
    for i in range(len(teams)):
        print(f"{i + 1}. {teams[i].name}")
    option = input("Enter team number:\n")
    if option.isdigit():
        option = int(option)
        if 0 < option <= len(teams):
            print(str(teams[option - 1]))
        else:
            print("Wrong option")
    else:
        print("Wrong option")


def print_all_teams():
    for team in teams:
        print(str(team))


def clear():
    global teams, participants
    teams = []
    participants = []


def main():
    load_people_from_file()
    load_teams_from_file()
    option = 0
    while option != 11:
        if option == 0:
            pass
        if option == 1:
            create_new_team()
        elif option == 2:
            load_people_from_csv()
        elif option == 3:
            change_team_weights()
        elif option == 4:
            remove_team()
        elif option == 5:
            print_team()
        elif option == 6:
            print_all_teams()
        elif option == 7:
            assign_to_teams()
        elif option == 8:
            clear()
        elif option == 9:
            save_teams_to_file()
        elif option == 10:
            exit(0)
        else:
            print(f"Option {option} is not a valid option")
        print_options()
        while True:
            try:
                option = int(input())
                break
            except ValueError:
                print("Please enter a number")
    save_teams_to_file()


if __name__ == "__main__":
    main()
