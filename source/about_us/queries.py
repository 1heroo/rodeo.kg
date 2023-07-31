import sqlalchemy as sa
from source.db.queries import BaseQueries
from source.about_us.models import AboutUs
from source.db.db import async_session


class AboutUsQueries(BaseQueries):
    model = AboutUs

    async def fetch_all(self) -> list[AboutUs]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().all()

    async def fetch_one(self) -> AboutUs:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().one()
