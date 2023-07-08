from source.core.settings import settings
from source.news.models import New, NewsTitle
from source.news.queries import NewsQueries, NewsTitleQueries
from sqlalchemy_fields.storages.base import StorageImage


class NewsServices:

    def __init__(self):
        self.news_title_queries = NewsTitleQueries()
        self.news_queries = NewsQueries()

    @staticmethod
    async def prepare_news_page_title(title: NewsTitle, lang):
        obj = {}

        match lang:
            case 'en':
                obj = {'title': title.title_en, 'image_url': title.image_url}
            case 'ru':
                obj = {'title': title.title_ru, 'image_url': title.image_url}
            case 'kg':
                obj = {'title': title.title_kg, 'image_url': title.image_url}
        return obj

    @staticmethod
    async def prepare_news_page(news: list[New], lang):
        output_news = []
        for new in news:
            match lang:
                case 'en':
                    output_news.append({
                        'upper_title': new.upper_title_en,
                        'title': new.title_en,
                        'description': new.description_en,
                        'location_n_date': new.location_n_date_en,
                        'image_url': new.image_url
                    })
                case 'ru':
                    output_news.append({
                        'upper_title': new.upper_title_ru,
                        'title': new.title_ru,
                        'description': new.description_ru,
                        'location_n_date': new.location_n_date_ru,
                        'image_url': new.image_url
                    })
                case 'kg':
                    output_news.append({
                        'upper_title': new.upper_title_kg,
                        'title': new.title_kg,
                        'description': new.description_kg,
                        'location_n_date': new.location_n_date_kg,
                        'image_url': new.image_url
                    })
        return output_news
