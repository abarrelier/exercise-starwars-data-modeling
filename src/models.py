import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(64), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    favorites = relationship('Favorites', back_populates='planets')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    favorites = relationship('Favorites', back_populates='characters')


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

    user = relationship(User)
    planet = relationship(Planets)
    character = relationship(Characters)


    def to_dict(self):
        return {}
class StarWars ( ):
## Draw from SQLAlchemy base
    render_er(Base, 'diagram.png')
