from source.champions.model import Participants
from source.champions.queries import ParticipantQueries, ChampionQueries
from source.tournament.models import Tournament
from source.tournament.queries import TournamentQueries


class ChampionServices:

    def __init__(self):
        self.participant_queries = ParticipantQueries()
        self.champion_queries = ChampionQueries()

        self.tournament_queries = TournamentQueries()

    async def prepare_champion_data(self, tournaments: list[Tournament], lang):
        output_data = []
        participants = await self.participant_queries.fetch_all()
        participant_dict_by_id = dict()

        for participant in participants:
            participant_dict_by_id[participant.id] = participant

        for tournament in tournaments:
            champion = await self.champion_queries.get_champion_by_tournament_id(tournament_id=tournament.id)
            obj = {}

            match lang:
                case 'en':
                    obj = {
                        'image_url': tournament.image_url,
                        'title': tournament.tournament_title_ru
                    }
                case 'ru':
                    obj = {
                        'image_url': tournament.image_url,
                        'title': tournament.tournament_title_ru
                    }
                case 'kg':
                    obj = {
                        'image_url': tournament.image_url,
                        'title': tournament.tournament_title_kg
                    }
            obj.update({
                'first_place': participant_dict_by_id.get(champion.first_place_id, Participants()).to_dict(),
                'second_place': participant_dict_by_id.get(champion.second_place_id, Participants()).to_dict(),
                'third_place': participant_dict_by_id.get(champion.third_place_id, Participants()).to_dict()
            })
            output_data.append(obj)
        return output_data
