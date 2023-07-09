from fastapi import UploadFile
from sqladmin import ModelView

from source.core.settings import settings
from source.news.models import New, NewsTitle, ParticipationApplication


class NewsTitleAdmin(ModelView, model=NewsTitle):
    column_list = ['title_ru', 'image_url']

    async def on_model_change(self, data: dict, model: New, is_created: bool) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/news_images/{image.filename}'


class NewAdmin(ModelView, model=New):
    column_list = ['id', 'title_ru', 'created_at', 'image_url']
    column_default_sort = [('created_at', True)]

    async def on_model_change(self, data: dict, model: New, is_created: bool) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/news_images/{image.filename}'


class ParticipationApplicationAdmin(ModelView, model=ParticipationApplication):
    column_list = ['application_owner_name', 'amount_of_participants', 'phone_numbers']

