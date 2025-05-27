from .database import Session
from .models import Team, Player, PlayerStats

session = Session()

def main_menu():
    while True:
        print("\n--- Sports CLI ---")
        print("1. Add Team")
        print("2. Edit Team")
        print("3. Delete Team")
        print("4. View Teams")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_team()
        elif choice == '2':
            edit_team()
        elif choice == '3':
            delete_team()
        elif choice == '4':
            view_teams()
        elif choice == '5':
            break

def add_team():
    name = input("Enter team name: ")
    team = Team(name=name)
    session.add(team)
    session.commit()
    print("Team added!")

def edit_team():
    view_teams()
    team_id = input("Enter team ID to edit: ")
    team = session.query(Team).get(team_id)
    if team:
        new_name = input(f"New name for team '{team.name}': ")
        team.name = new_name
        session.commit()
        print("Team updated.")
    else:
        print("Team not found.")

def delete_team():
    view_teams()
    team_id = input("Enter team ID to delete: ")
    team = session.query(Team).get(team_id)
    if team:
        session.delete(team)
        session.commit()
        print("Team deleted.")
    else:
        print("Team not found.")

def view_teams():
    teams = session.query(Team).all()
    for team in teams:
        print(f"ID: {team.id}, Name: {team.name}")
