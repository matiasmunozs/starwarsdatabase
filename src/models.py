import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#Ejemplo clases:

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


#testeo 1:


# class User(Base):
#     __tablename__ = 'user'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)


# class Planets(Base):
#     __tablename__ = 'planets'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     population = Column(String(250))
#     terrain = Column(String(250))
#     name = Column(String(250), nullable=False)
#     planet_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)


# class People(Base):
#     __tablename__ = 'people'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     hair_color = Column(String(250))
#     eye_color = Column(String(250))
#     name = Column(String(250), nullable=False)
#     people_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)

# class Vehicle(Base):
#     __tablename__ = 'vehicle'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     model = Column(String(250))
#     capacity = Column(String(250))
#     name = Column(String(250), nullable=False)
#     vehicle_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)

# class Favorites(Base):
#     __tablename__ = 'favorites'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

#     def to_dict(self):
#         return {}



#Testeo 2:

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)
    user_name = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)


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
    id = Column(Integer, ForeignKey('fav_people.id'), primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    capacity = Column(String, nullable=False)
    person = relationship(Fav_People)

    def to_dict(self):
        return {}











## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


