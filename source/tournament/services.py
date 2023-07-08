from source.tournament.models import TournamentTitle, Tournament, TournamentEvent
from source.tournament.queries import TournamentTitleQueries, TournamentQueries, TournamentEventQueries


class TournamentServices:

    def __init__(self):
        self.tournament_title_queries = TournamentTitleQueries()
        self.tournament_queries = TournamentQueries()
        self.event_queries = TournamentEventQueries()

    @staticmethod
    async def prepare_tournament_title_data(title: TournamentTitle, lang):
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
    async def prepare_tournaments_data(tournaments: list[Tournament], lang):
        output_tournaments = []

        for tournament in tournaments:
            match lang:
                case 'en':
                    output_tournaments.append({
                        'title': tournament.tournament_title_en,
                        'location': tournament.location_en,
                        'date': tournament.date.strftime('%m/%d/%Y'),
                        'tile': tournament.time,
                        'image_url': tournament.image_url
                    })
                case 'ru':
                    output_tournaments.append({
                        'title': tournament.tournament_title_ru,
                        'location': tournament.location_ru,
                        'date': tournament.date.strftime('%m/%d/%Y'),
                        'tile': tournament.time,
                        'image_url': tournament.image_url
                    })
                case 'kg':
                    output_tournaments.append({
                        'title': tournament.tournament_title_kg,
                        'location': tournament.location_kg,
                        'date': tournament.date.strftime('%m/%d/%Y'),
                        'tile': tournament.time,
                        'image_url': tournament.image_url
                    })
        return output_tournaments

    @staticmethod
    async def prepare_tournament_events(events: list[TournamentEvent], lang):
        scroll_events = []
        default_events = []

        for event in events:
            match lang:
                case 'en':
                    obj = {'title': event.title_en, 'description': event.description_en, 'image_url': event.image_url}
                case 'ru':
                    obj = {'title': event.title_ru, 'description': event.description_ru, 'image_url': event.image_url}
                case 'kg':
                    obj = {'title': event.title_kg, 'description': event.description_kg, 'image_url': event.image_url}
                case other:
                    obj = {}

            if event.scroll:
                scroll_events.append(obj)
            else:
                default_events.append(obj)
        return {
            'scroll_events': scroll_events,
            'default_events': default_events
        }


