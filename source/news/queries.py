from source.db.db import async_session

from source.db.queries import BaseQueries
from source.news.models import New, NewsTitle
import sqlalchemy as sa


class NewsTitleQueries(BaseQueries):
    model = NewsTitle

    async def fetch_one(self) -> NewsTitle:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().first()


class NewsQueries(BaseQueries):
    model = New

    async def fetch_all(self, datetime_sorted=False) -> list[New]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            news = result.scalars().all()
            if datetime_sorted:
                return sorted(news, key=lambda new: new.created_at, reverse=True)
            return news
