from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    players = relationship("Player", back_populates="team")

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="players")
    stats = relationship("PlayerStats", back_populates="player")

class PlayerStats(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True)
    goals = Column(Integer)
    assists = Column(Integer)
    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship("Player", back_populates="stats")
