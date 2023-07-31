import os

from sqlalchemy_fields.storages import FileSystemStorage
from sqlalchemy_fields.types import ImageType

from source.db.db import Base
import sqlalchemy as sa


class AboutUs(Base):
    __tablename__ = 'about_us'

    id = sa.Column(sa.Integer, primary_key=True)
    title_en = sa.Column(sa.String)
    title_ru = sa.Column(sa.String)
    title_kg = sa.Column(sa.String)

    preview_image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/participant_images')))
    preview_image_url = sa.Column(sa.String)

    appeal_en = sa.Column(sa.String)
    appeal_ru = sa.Column(sa.String)
    appeal_kg = sa.Column(sa.String)

    founder_info_en = sa.Column(sa.String)
    founder_info_ru = sa.Column(sa.String)
    founder_info_kg = sa.Column(sa.String)
    founder_image = sa.Column(ImageType(storage=FileSystemStorage(
        path=f'{os.getcwd()}/static/participant_images')))
    founder_image_url = sa.Column(sa.String)

    regulation_en = sa.Column(sa.String)
    regulation_ru = sa.Column(sa.String)
    regulation_kg = sa.Column(sa.String)

    def __str__(self):
        return str(self.upper_title)

    def __repr__(self):
        return str(self.upper_title)
