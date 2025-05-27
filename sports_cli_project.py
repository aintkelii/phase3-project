import json
import os
import argparse

DATA_FILE = 'sports_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_team(data, team_name):
    if team_name in data:
        print(f"Team '{team_name}' already exists.")
    else:
        data[team_name] = {"players": []}
        print(f"Team '{team_name}' added.")

def add_player(data, team_name, player_name):
    if team_name not in data:
        print(f"Team '{team_name}' does not exist.")
    else:
        if player_name in data[team_name]['players']:
            print(f"Player '{player_name}' already in team '{team_name}'.")
        else:
            data[team_name]['players'].append(player_name)
            print(f"Player '{player_name}' added to team '{team_name}'.")

def list_teams(data):
    if not data:
        print("No teams available.")
    else:
        for team, info in data.items():
            print(f"Team: {team}, Players: {', '.join(info['players'])}")

def delete_team(data, team_name):
    if team_name in data:
        del data[team_name]
        print(f"Team '{team_name}' deleted.")
    else:
        print(f"Team '{team_name}' does not exist.")

def main():
    parser = argparse.ArgumentParser(description='Sports CLI Project')
    parser.add_argument('action', choices=['add_team', 'add_player', 'list_teams', 'delete_team'])
    parser.add_argument('--team', help='Team name')
    parser.add_argument('--player', help='Player name')
    args = parser.parse_args()

    data = load_data()

    if args.action == 'add_team' and args.team:
        add_team(data, args.team)
    elif args.action == 'add_player' and args.team and args.player:
        add_player(data, args.team, args.player)
    elif args.action == 'list_teams':
        list_teams(data)
    elif args.action == 'delete_team' and args.team:
        delete_team(data, args.team)
    else:
        print("Invalid arguments provided.")

    save_data(data)

if __name__ == '__main__':
    main()