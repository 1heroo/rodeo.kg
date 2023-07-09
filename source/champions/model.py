import os

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy_fields.storages import FileSystemStorage
from sqlalchemy_fields.types import ImageType
from source.db.db import Base
from source.tournament.models import Tournament


class Participants(Base):
    __tablename__ = 'participants'

    id = sa.Column(sa.Integer, primary_key=True)

    image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/participant_images')))
    image_url = sa.Column(sa.String)

    name = sa.Column(sa.String)
    description = sa.Column(sa.String)

    first_champ = relationship('Champion', back_populates='first_place', foreign_keys='Champion.first_place_id')
    second_champ = relationship('Champion', back_populates='second_place', foreign_keys='Champion.second_place_id')
    third_champ = relationship('Champion', back_populates='third_place', foreign_keys='Champion.third_place_id')

    def to_dict(self):
        return {'image_url': self.image_url, 'name': self.name, 'description': self.description}

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Champion(Base):
    __tablename__ = 'champions'

    id = sa.Column(sa.Integer, primary_key=True)

    tournament_id = sa.Column(sa.Integer, sa.ForeignKey('tournaments.id'))
    tournament = relationship('Tournament', back_populates='champions')

    first_place_id = sa.Column(sa.Integer, sa.ForeignKey('participants.id'))
    first_place = relationship('Participants', back_populates='first_champ', foreign_keys='Champion.first_place_id')

    second_place_id = sa.Column(sa.Integer, sa.ForeignKey('participants.id'))
    second_place = relationship('Participants', back_populates='second_champ', foreign_keys='Champion.second_place_id')

    third_place_id = sa.Column(sa.Integer, sa.ForeignKey('participants.id'))
    third_place = relationship('Participants', back_populates='third_champ', foreign_keys='Champion.third_place_id')
