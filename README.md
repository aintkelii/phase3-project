# Sports CLI Project

A simple command-line sports team management application written in Python. This tool allows users to manage teams and players through terminal commands and stores the data in a local JSON file.

## Features

- Add new teams
- Add players to teams
- List all teams and their players
- Delete teams
- Data persistence using a local JSON file (`sports_data.json`)

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script.
2. Make sure `sports_cli_project.py` is in your working directory.
3. (Optional) Create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate


Usage
Add a Team
bash
Copy
Edit
python sports_cli_project.py add_team --team "name"
Add a Player to a Team
bash
Copy
Edit
python sports_cli_project.py add_player --team "name" --player "John"
List All Teams and Players
bash
Copy
Edit
python sports_cli_project.py list_teams
Delete a Team
bash
Copy
Edit
python sports_cli_project.py delete_team --team "Lions"
Project Structure
graphql
Copy
Edit
sports_cli_project.py      # Main CLI application
sports_data.json           # JSON file to store teams and players (auto-created)
README.md                  # Project documentation
License
This project is open-source and available under the MIT License.

Author
[George Keli Kivinda]