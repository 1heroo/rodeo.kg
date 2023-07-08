import datetime

from fastapi import UploadFile
from sqladmin import ModelView

from source.core.settings import settings
from source.gallery.models import GalleryImage, GalleryTitle
from source.gallery.queries import GalleryImageQueries


class GalleryTitleAdmin(ModelView, model=GalleryTitle):
    column_list = ['image_url', 'page_title_ru']

    async def on_model_change(self, data, model: GalleryImage, is_created) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/gallery_images/{image.filename}'


class GalleryImageAdmin(ModelView, model=GalleryImage):
    column_list = ['image_url', 'scroll', 'upper_part', 'lower_part', 'created_at']
    column_default_sort = [('created_at', True)]

    async def on_model_change(self, data, model: GalleryImage, is_created) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/gallery_images/{image.filename}'
