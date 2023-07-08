from source.gallery.models import GalleryImage, GalleryTitle
from source.gallery.queries import GalleryImageQueries, GalleryTitleQueries


class GalleryServices:
    def __init__(self):
        self.gallery_title_queries = GalleryTitleQueries()
        self.gallery_image_queries = GalleryImageQueries()

    @staticmethod
    async def prepare_gallery_page_title(title: GalleryTitle, lang):
        obj = {}

        match lang:
            case 'en':
                obj = {
                    'page_title': title.page_title_en,
                    'upper_title': title.upper_title_en,
                    'lower_title': title.lower_title_en,
                    'image_url': title.image_url
                }
            case 'ru':
                obj = {
                    'page_title': title.page_title_ru,
                    'upper_title': title.upper_title_ru,
                    'lower_title': title.lower_title_ru,
                    'image_url': title.image_url
                }
            case 'kg':
                obj = {
                    'page_title': title.page_title_kg,
                    'upper_title': title.upper_title_kg,
                    'lower_title': title.lower_title_kg,
                    'image_url': title.image_url
                }
        return obj

    @staticmethod
    async def prepare_gallery_page(images: list[GalleryImage]):
        scroll_images = []
        upper_images = []
        lower_images = []

        for image in images:
            obj = {'image_url': image.image_url}

            if image.scroll:
                scroll_images.append(obj)
            if image.upper_part:
                upper_images.append(obj)
            if image.lower_part:
                lower_images.append(obj)
        return {
            'scroll_images': scroll_images,
            'upper_images': upper_images,
            'lower_images': lower_images
        }

