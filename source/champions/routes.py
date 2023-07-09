from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from source.champions.services import ChampionServices
from source.core.settings import settings

router = APIRouter(prefix='/champions', tags=['Champion'])


champion_services = ChampionServices()


@router.get('/get-champion-page/{language}/')
async def get_champion_page(language: str):

    if language not in ['en', 'ru', 'kg']:
        return JSONResponse(
            content={'message': 'language is not supported'},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    tournaments = await champion_services.tournament_queries.fetch_all(datetime_sorted=True)
    tournaments = tournaments[:5]
    tournaments_data = await champion_services.prepare_champion_data(tournaments=tournaments, lang=language)

    return JSONResponse(
        content={
            'data': tournaments_data
        },
        status_code=status.HTTP_200_OK,
        headers={
            'Access-Control-Allow-Origin': settings.HOST,
            'vary': 'Origin',
            'Access-Control-Allow-Credentials': 'true'
        }
    )
