from fastapi import UploadFile
from sqladmin import ModelView

from source.champions.model import Participants, Champion
from source.core.settings import settings


class ParticipantsAdmin(ModelView, model=Participants):
    column_list = ['id', 'name', 'image_url']

    async def on_model_change(self, data: dict, model: Participants, is_created: bool) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/participant_images/{image.filename}'


class ChampionAdmin(ModelView, model=Champion):
    column_list = ['tournament']
