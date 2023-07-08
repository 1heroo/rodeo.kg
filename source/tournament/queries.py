from source.db.db import async_session
from source.db.queries import BaseQueries
import sqlalchemy as sa

from source.tournament.models import TournamentTitle, Tournament, TournamentEvent


class TournamentTitleQueries(BaseQueries):
    model = TournamentTitle

    async def fetch_one(self) -> TournamentTitle:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().one()


class TournamentQueries(BaseQueries):
    model = Tournament

    async def fetch_all(self, datetime_sorted=False) -> list[Tournament]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            tournaments = result.scalars().all()
            if datetime_sorted:
                return sorted(tournaments, key=lambda new: new.created_at, reverse=True)
            return tournaments


class TournamentEventQueries(BaseQueries):
    model = TournamentEvent

    async def fetch_all(self, datetime_sorted=False) -> list[Tournament]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            events = result.scalars().all()
            if datetime_sorted:
                return sorted(events, key=lambda new: new.created_at, reverse=True)
            return events
