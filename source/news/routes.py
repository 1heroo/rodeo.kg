from fastapi import APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from source.news.services import NewsServices

router = APIRouter(prefix='/news')
news_services = NewsServices()


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
        status_code=status.HTTP_200_OK, headers={})
