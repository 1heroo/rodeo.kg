from fastapi import UploadFile
from sqladmin import ModelView

from source.core.settings import settings
from source.tournament.models import TournamentTitle, Tournament, TournamentEvent


class TournamentTitleAdmin(ModelView, model=TournamentTitle):
    column_list = ['title_ru', 'image_url']

    async def on_model_change(self, data: dict, model: TournamentTitle, is_created: bool) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/tournament_images/{image.filename}'


class TournamentAdmin(ModelView, model=Tournament):
    column_list = ['tournament_title_ru', 'location_ru', 'date', 'time', 'image_url']

    async def on_model_change(self, data: dict, model: Tournament, is_created: bool) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/tournament_images/{image.filename}'


class TournamentEventAdmin(ModelView, model=TournamentEvent):
    column_list = ['title_ru', 'image_url', 'scroll']

    async def on_model_change(self, data: dict, model: TournamentEvent, is_created: bool) -> None:
        image: UploadFile = data.get('image')
        filename = image.filename

        image.filename = filename.replace(' ', '_')
        data['image_url'] = f'{settings.HOST}/static/tournament_event_images/{image.filename}'
