from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from source.about_us.queries import AboutUsQueries

router = APIRouter(prefix='/about-us', tags=['About Us'])


about_us_queries = AboutUsQueries()


@router.get('/get-about-us-page/{language}')
async def get_about_us_page(language: str):

    if language not in ['en', 'ru', 'kg']:
        return JSONResponse(
            content={'message': 'language is not supported'},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    about_us_page = await about_us_queries.fetch_one()

    obj = {}
    match language:
        case 'en':
            obj = {
                'title': about_us_page.title_en,
                'appeal': about_us_page.appeal_en,
                'founder_info': about_us_page.founder_info_en,
                'regulation': about_us_page.regulation_en
            }
        case 'ru':
            obj = {
                'title': about_us_page.title_ru,
                'appeal': about_us_page.appeal_ru,
                'founder_info': about_us_page.founder_info_ru,
                'regulation': about_us_page.regulation_ru
            }
        case 'kg':
            obj = {
                'title': about_us_page.title_kg,
                'appeal': about_us_page.appeal_kg,
                'founder_info': about_us_page.founder_info_kg,
                'regulation': about_us_page.regulation_kg
            }
    obj.update({
        'preview_image_url': about_us_page.preview_image_url,
        'founder_image_url': about_us_page.founder_image_url
    })

    return JSONResponse(content=obj, status_code=status.HTTP_200_OK)

