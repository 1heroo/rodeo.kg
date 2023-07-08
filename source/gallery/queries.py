from source.db.db import async_session

from source.db.queries import BaseQueries
from source.gallery.models import GalleryImage, GalleryTitle

import sqlalchemy as sa


class GalleryTitleQueries(BaseQueries):
    model = GalleryTitle

    async def fetch_one(self) -> GalleryTitle:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().first()


class GalleryImageQueries(BaseQueries):
    model = GalleryImage

    async def fetch_all(self, datetime_sorted=False) -> list[GalleryImage]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            images = result.scalars().all()
            if datetime_sorted:
                return sorted(images, key=lambda new: new.created_at, reverse=True)

            return images

    # async def get_none_field_models(self):
    #     async with async_session() as session:
    #         result = await session.execute(
    #             sa.select(self.model)
    #             .where(self.model.image_title == None)
    #             .where(self.model.image_url == None)
    #         )
    #         return result.scalars().all()
