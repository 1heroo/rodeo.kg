import os

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy_fields.storages import FileSystemStorage
from sqlalchemy_fields.types import ImageType
# from source.champions.model import Champion
from source.db.db import Base


class TournamentTitle(Base):
    __tablename__ = 'tournament_title'

    id = sa.Column(sa.Integer, primary_key=True)

    image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/tournament_images')))
    image_url = sa.Column(sa.String)

    title_en = sa.Column(sa.String)
    title_ru = sa.Column(sa.String)
    title_kg = sa.Column(sa.String)

    def __str__(self):
        return str(self.title_ru)

    def __repr__(self):
        return str(self.title_ru)


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = sa.Column(sa.Integer, primary_key=True)

    image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/tournament_images')))
    image_url = sa.Column(sa.String)

    tournament_title_en = sa.Column(sa.String)
    tournament_title_ru = sa.Column(sa.String)
    tournament_title_kg = sa.Column(sa.String)

    location_en = sa.Column(sa.String)
    location_ru = sa.Column(sa.String)
    location_kg = sa.Column(sa.String)

    date = sa.Column(sa.Date)
    time = sa.Column(sa.String)

    created_at = sa.Column(sa.DateTime, server_default=func.now())

    # champions = relationship('Champion', back_populates='tournament')

    def __str__(self):
        return str(self.tournament_title_ru)

    def __repr__(self):
        return str(self.tournament_title_ru)


class TournamentEvent(Base):
    __tablename__ = 'tournament_events'

    id = sa.Column(sa.Integer, primary_key=True)

    image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/tournament_event_images')))
    image_url = sa.Column(sa.String)

    title_en = sa.Column(sa.String)
    title_ru = sa.Column(sa.String)
    title_kg = sa.Column(sa.String)

    description_en = sa.Column(sa.String)
    description_ru = sa.Column(sa.String)
    description_kg = sa.Column(sa.String)

    scroll = sa.Column(sa.Boolean)
    created_at = sa.Column(sa.DateTime, server_default=func.now())

    def __str__(self):
        return str(self.title_ru)

    def __repr__(self):
        return str(self.title_ru)
