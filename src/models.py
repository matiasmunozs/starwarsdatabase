import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)
    user_name = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet_id'))
    fav_planet = relationship('Fav_Planet')
    people_id  = Column(Integer, ForeignKey('people_id '))
    fav_people = relationship('Fav_People')
    vehicle_id = Column(Integer, ForeignKey('vehicle_id'))
    fav_vehicle = relationship('Fav_Vehicle')


class Fav_Planet(Base):
    __tablename__ = 'fav_planet'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planet_id = Column(Integer, primary_key=True)  
    person = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, ForeignKey('fav_planet.id'), primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String, nullable=False)
    person = relationship(Fav_Planet)

class Fav_People(Base):
    __tablename__ = 'fav_people'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    people_id = Column(Integer, primary_key=True)  
    person = relationship(User)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, ForeignKey('fav_people.id'), primary_key=True)
    name = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    eyes_color = Column(String, nullable=False)
    person = relationship(Fav_People)

class Fav_Vehicle(Base):
    __tablename__ = 'fav_vehicle'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    vehicle_id = Column(Integer, primary_key=True)  
    person = relationship(User)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, ForeignKey('fav_vehicle.id'), primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    capacity = Column(String, nullable=False)
    person = relationship(Fav_People)

    def to_dict(self):
        return {}











## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


