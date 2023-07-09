from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from source.core.settings import settings
from source.news.models import ParticipationApplication
from source.news.services import NewsServices

from pydantic import BaseModel


router = APIRouter(prefix='/news')
news_services = NewsServices()


class ParticipationSubmitSchema(BaseModel):

    application_owner_name: str = 'ФИО заявителя'
    amount_of_participants: int = 2
    participants_names: str = 'Имена участников'
    participants_ages: str = 'Возрасты участников'
    phone_numbers: str = '+996000000000'

    class Config:
        orm_mode = True


@router.post('/submit-application', tags=['Participation Application'])
async def submit_application(data: ParticipationSubmitSchema):
    instance = ParticipationApplication(
        application_owner_name=data.application_owner_name,
        amount_of_participants=data.amount_of_participants,
        participants_names=data.participants_names,
        participants_ages=data.participants_ages,
        phone_numbers=data.phone_numbers
    )
    await news_services.news_queries.save_in_db(instances=instance)
    return Response(status_code=status.HTTP_200_OK, headers={
            'Access-Control-Allow-Origin': settings.HOST,
            'vary': 'Origin',
            'Access-Control-Allow-Credentials': 'true'
        })


@router.get('/get-news-page/{langauge}/', tags=['News Page'])
async def get_news_page(request: Request, language: str):

    if language not in ['en', 'ru', 'kg']:
        return JSONResponse(
            content={'message': 'language is not supported'}, status_code=status.HTTP_400_BAD_REQUEST)

    news_title = await news_services.news_title_queries.fetch_one()
    news_title_data = await news_services.prepare_news_page_title(title=news_title, lang=language)

    news = await news_services.news_queries.fetch_all(datetime_sorted=True)
    news_data = await news_services.prepare_news_page(news=news, lang=language)

    return JSONResponse(
        content={
            'title': news_title_data,
            'data': news_data
        },
        status_code=status.HTTP_200_OK,
        headers={
            'Access-Control-Allow-Origin': settings.HOST,
            'vary': 'Origin',
            'Access-Control-Allow-Credentials': 'true'
        })
