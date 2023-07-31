from fastapi import UploadFile
from sqladmin import ModelView

from source.about_us.models import AboutUs
from source.core.settings import settings


class AboutUsAdmin(ModelView, model=AboutUs):
    column_list = ['title_ru', 'preview_image_url']

    async def on_model_change(self, data: dict, model: AboutUs, is_created: bool) -> None:
        preview_image: UploadFile = data.get('preview_image')
        filename = preview_image.filename
        preview_image.filename = filename.replace(' ', '_')
        data['preview_image_url'] = f'{settings.HOST}/static/participant_images/{preview_image.filename}'

        founder_image: UploadFile = data.get('preview_image')
        filename = founder_image.filename
        founder_image.filename = filename.replace(' ', '_')
        data['founder_image_url'] = f'{settings.HOST}/static/participant_images/{founder_image.filename}'

