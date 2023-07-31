from source.champions.models import Champion, Participants
from source.db.db import async_session
from source.db.queries import BaseQueries
import sqlalchemy as sa


class ParticipantQueries(BaseQueries):
    model = Participants

    async def fetch_all(self) -> list[Participants]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().all()


class ChampionQueries(BaseQueries):
    model = Champion

    async def fetch_all(self) -> list[Champion]:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
            )
            return result.scalars().all()

    async def get_champion_by_tournament_id(self, tournament_id: int) -> Champion:
        async with async_session() as session:
            result = await session.execute(
                sa.select(self.model)
                .where(self.model.tournament_id == tournament_id)
            )
            return result.scalars().first()
