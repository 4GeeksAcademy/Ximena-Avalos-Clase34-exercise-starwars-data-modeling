import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
user_favorite_character = Table('user_favorite_character', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), primary_key=True)
)

user_favorite_planet = Table('user_favorite_planet', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    firstname = Column(String(50))
    lastname = Column(String(50))
    subscription_date = Column(String(50))

    favorite_characters = relationship('Character', secondary=user_favorite_character, back_populates='users')
    favorite_planets = relationship('Planet', secondary=user_favorite_planet, back_populates='users')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(50))
    gender = Column(String(50))
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))

    users = relationship('User', secondary=user_favorite_character, back_populates='favorite_characters')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))
    population = Column(String(50))

    users = relationship('User', secondary=user_favorite_planet, back_populates='favorite_planets')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e