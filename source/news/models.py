import os

from sqlalchemy import func
from sqlalchemy_fields.storages import FileSystemStorage
from sqlalchemy_fields.types import FileType, ImageType

from source.db.db import Base
import sqlalchemy as sa


class NewsTitle(Base):
    __tablename__ = 'news_title'

    id = sa.Column(sa.Integer, primary_key=True)

    title_ru = sa.Column(sa.String)
    title_en = sa.Column(sa.String)
    title_kg = sa.Column(sa.String)

    image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/news_images')))
    image_url = sa.Column(sa.String)


class New(Base):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True)

    image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/news_images')))
    image_url = sa.Column(sa.String)

    upper_title_ru = sa.Column(sa.String)
    upper_title_kg = sa.Column(sa.String)
    upper_title_en = sa.Column(sa.String)

    title_ru = sa.Column(sa.String)
    title_kg = sa.Column(sa.String)
    title_en = sa.Column(sa.String)

    description_ru = sa.Column(sa.String)
    description_kg = sa.Column(sa.String)
    description_en = sa.Column(sa.String)

    location_n_date_ru = sa.Column(sa.String)
    location_n_date_kg = sa.Column(sa.String)
    location_n_date_en = sa.Column(sa.String)

    created_at = sa.Column(sa.DateTime, server_default=func.now())

    def __str__(self):
        return str(self.title_ru)

    def __repr__(self):
        return str(self.title_ru)


class ParticipationApplication(Base):
    __tablename__ = 'aplications'

    id = sa.Column(sa.Integer, primary_key=True)
    application_owner_name = sa.Column(sa.String)
    amount_of_participants = sa.Column(sa.Integer)
    participants_names = sa.Column(sa.String)
    participants_ages = sa.Column(sa.String)
    phone_numbers = sa.Column(sa.String)

    def __str__(self):
        return str(self.application_owner_name)

    def __repr__(self):
        return str(self.application_owner_name)
