from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from source.gallery.queries import GalleryImageQueries
from source.gallery.services import GalleryServices

router = APIRouter(prefix='/gallery', tags=['Gallery'])


gallery_services = GalleryServices()


@router.get('/get-gallery-page/{language}/')
async def get_gallery_page(language: str):

    if language not in ['en', 'ru', 'kg']:
        return JSONResponse(
            content={'message': 'language is not supported'}, status_code=status.HTTP_400_BAD_REQUEST)

    gallery_title = await gallery_services.gallery_title_queries.fetch_one()
    gallery_title_data = await gallery_services.prepare_gallery_page_title(title=gallery_title, lang=language)

    gallery_images = await gallery_services.gallery_image_queries.fetch_all(datetime_sorted=True)
    gallery_images_data = await gallery_services.prepare_gallery_page(images=gallery_images)
    return JSONResponse(
        content={
            'title': gallery_title_data,
            'data': gallery_images_data
        }, status_code=status.HTTP_200_OK)

