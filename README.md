#  Sports CLI Manager

A terminal-based sports management application built using Python, SQLAlchemy, and Pipenv. This project allows users to manage teams, players, and player statistics using a clean CLI interface. Designed for Phase 3 to demonstrate ORM, CLI development, and best practices in Python.

---

##  Features

-  Add, delete, and edit **Teams**, **Players**, and **Player Statistics**
-  SQLAlchemy ORM with 3+ related tables
-  Persistent storage using SQLite
-  Interactive CLI menus
-  Organized project structure
-  Virtual environment managed with Pipenv

---

## 🛠 Technologies Used

- Python 3.12+
- SQLAlchemy
- Pipenv
- SQLite
- Python standard libraries (`os`, `sys`)

---

## Learning Goals

This project demonstrates the following Phase 3 curriculum concepts:

- Use of **SQLAlchemy ORM** for model relationships
- Creation and modification of a database schema
- Building a **CLI** application using menus and user input
- Use of **lists**, **dictionaries**, and **tuples**
- Applying **coding best practices** (modular structure, readable code)
- Managing a **virtual environment** with Pipenv

---

##  Project Structure

phase3-project/
│
├── app/
│ ├── init.py
│ ├── cli.py # CLI menu and input handling
│ ├── models.py # SQLAlchemy models (Team, Player, PlayerStats)
│ ├── database.py # Engine, session, and Base config
│ └── seed.py # Creates tables and optionally seeds data
│
├── main.py # App entry point
├── Pipfile # Pipenv dependency file
├── Pipfile.lock # Pipenv lock file
└── README.md # Project documentation

yaml
Copy
Edit

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd phase3-project
2. Set Up the Virtual Environment
bash
Copy
Edit
pipenv install
pipenv shell
3. Create the Database and Tables
bash
Copy
Edit
python -m app.seed
This creates the SQLite database and initializes all required tables.

4. Run the Application #(first run {pipenv install sqlalchemy} secondly run {pipenv shell
#} thirdly run {python main.py}) [ON THE TERMINAL] 
bash 
Copy
Edit



Follow the CLI prompts to add/edit/delete teams, players, and stats.

 Example Usage
bash
Copy
Edit
Welcome to Sports CLI Manager!
1. Add Team
2. Add Player
3. View Teams
4. Edit Player
5. Delete Team
6. Quit
Enter choice: 
 Data Model Overview
Team has many Players

Player belongs to one Team

Player has one PlayerStats record

 Best Practices Followed
Clear function names and comments

Modular code separated by responsibility

Reusable CLI input handlers

Proper error handling

Pipenv for isolated dependencies

 Grading Rubric Alignment
Criteria	Status
Proficiency with Learning Goals	Fully demonstrated
Technical Communication	Clear, structured, and commented
Coding Best Practices	Modular, readable, and reusable code

 Feedback
Open to suggestions and improvements. Feel free to fork, modify, and submit PRs!

 License
MIT License. Free for educational use.