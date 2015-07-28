import trueskill
from store import Store

__author__ = 'mocsar'

class Player:

    def __init__(self, name, rating):
        """
        :type ratings: trueskill.Rating
        :type name: str
        """
        self.rating = rating
        self.name = name

    def get_score(self):
        """
        :rtype : float
        """
        return trueskill.expose(self.rating)

    @classmethod
    def create_player(cls, name):
        """
        :type name: str
        """
        if cls.get_player(name):
            raise RuntimeError('Player already exists: %s' % name)
        Store.get_store().set_player(Player(name, trueskill.Rating()))

    @classmethod
    def get_all_names(cls):
        """
        :rtype : list[str]
        """
        return [player.name for player in cls.get_all_players()]

    @classmethod
    def get_player(cls, name):
        """
        :rtype : Player
        """
        player = Store.get_store().get_player(name)
        return player

    @classmethod
    def get_all_players(cls):
        return Store.get_store().get_all_players()

    @classmethod
    def rate(cls, names):
        """
        :type names: list[str]
        """
        if not isinstance(names, list):
            raise TypeError("Argument must be a list")
        if len(names) != 4:
            raise ValueError("Please specify 4 players")

        winner1 = cls.get_player(names[0])
        winner2 = cls.get_player(names[1])
        loser1 = cls.get_player(names[2])
        loser2 = cls.get_player(names[3])

        winners = [winner1.rating, winner2.rating]
        losers = [loser1.rating, loser2.rating]

        winners, losers = trueskill.rate([winners, losers])

        winner1.rating = winners[0]
        winner2.rating = winners[1]
        loser1.rating = losers[0]
        loser2.rating = losers[1]

        Store.get_store().set_player(winner1)
        Store.get_store().set_player(winner2)
        Store.get_store().set_player(loser1)
        Store.get_store().set_player(loser2)

        Store.get_store().log_results(names)

    @classmethod
    def get_leaderboard(cls):
        """
        Returns with sorted list of the players. The best player is the first in the list.
        :rtype : list[Player]
        """
        players = cls.get_all_players()
        return sorted(players, key=lambda player: trueskill.global_env().expose(player.rating), reverse=True)


