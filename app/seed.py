from .database import Base, engine
from .models import Team, Player, PlayerStats

def seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database seeded: all tables created.")

if __name__ == "__main__":
    seed()
