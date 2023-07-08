from sqlalchemy import func

from source.db.db import Base
import sqlalchemy as sa
from sqlalchemy_fields.types import ImageType, URLType
from sqlalchemy_fields.storages import FileSystemStorage
import os


class GalleryTitle(Base):
    __tablename__ = 'gallery_title'

    id = sa.Column(sa.Integer, primary_key=True)
    image = sa.Column(ImageType(storage=FileSystemStorage(path=f'{os.getcwd()}/static/gallery_images')))
    image_url = sa.Column(sa.String)

    page_title_ru = sa.Column(sa.String)
    page_title_en = sa.Column(sa.String)
    page_title_kg = sa.Column(sa.String)

    upper_title_en = sa.Column(sa.String)
    upper_title_ru = sa.Column(sa.String)
    upper_title_kg = sa.Column(sa.String)

    lower_title_ru = sa.Column(sa.String)
    lower_title_en = sa.Column(sa.String)
    lower_title_kg = sa.Column(sa.String)

    def __str__(self):
        return str(self.page_title_kg)

    def __repr__(self):
        return str(self.page_title_kg)


class GalleryImage(Base):
    __tablename__ = 'gallery_images'

    id = sa.Column(sa.Integer, primary_key=True)
    image = sa.Column(ImageType(storage=FileSystemStorage(path=f'{os.getcwd()}/static/gallery_images')))
    image_url = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, server_default=func.now())

    scroll = sa.Column(sa.Boolean)
    upper_part = sa.Column(sa.Boolean)
    lower_part = sa.Column(sa.Boolean)

    def __str__(self):
        return str(self.image_title)

    def __repr__(self):
        return str(self.image_title)
