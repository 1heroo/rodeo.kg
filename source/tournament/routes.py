from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from source.tournament.services import TournamentServices

router = APIRouter(prefix='/tournaments', tags=['Tournament'])


tournament_services = TournamentServices()


@router.get('/get-tournament-page/{language}/')
async def get_tournament_page(language: str):

    if language not in ['en', 'ru', 'kg']:
        return JSONResponse(
            content={'message': 'language is not supported'}, status_code=status.HTTP_400_BAD_REQUEST)

    tournament_title = await tournament_services.tournament_title_queries.fetch_one()
    tournament_title_data = await tournament_services.prepare_tournament_title_data(title=tournament_title, lang=language)

    tournaments = await tournament_services.tournament_queries.fetch_all(datetime_sorted=True)
    tournaments_data = await tournament_services.prepare_tournaments_data(tournaments=tournaments, lang=language)

    events = await tournament_services.event_queries.fetch_all(datetime_sorted=True)
    events_data = await tournament_services.prepare_tournament_events(events=events, lang=language)

    return JSONResponse(
        content={
            'title': tournament_title_data,
            'tournaments': tournaments_data,
            'events': events_data
        },
        status_code=status.HTTP_200_OK)
