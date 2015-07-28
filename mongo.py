import time
from trueskill import Rating
import player as p
from settings import Settings
import pymongo

__author__ = 'mocsar'

### Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

class Mongo(object):
    def __init__(self):
        db_uri = Settings.get('db-uri', '---')
        db_collection = Settings.get('mongo-db-collection', 'players')
        self.client = pymongo.MongoClient(db_uri)

        db = self.client.get_default_database()
        self.collection = db[db_collection]
        self.log_collection = db['logs_' + db_collection]

    def _get_rating(self, name):
        if self.collection:
            query = {'name': name}
            player = self.collection.find_one(query)
            if player:
                return player
            return None

    def _set_rating(self, name, mu, sigma):
        if self.collection:
            query = {'name': name}
            self.collection.update_one(query, {'$set': {'mu': float(mu), 'sigma': float(sigma)}}, upsert=True)

    def get_all_players(self):
        """
        :rtype : list[Player]
        """
        res = []
        if self.collection:
            all_data = self.collection.find()
            for values in all_data:
                res.append(p.Player(values['name'], Rating(float(values['mu']), float(values['sigma']))))
        return res

    def get_player(self, name):
        """
        :rtype : Player
        """
        values = self._get_rating(name)
        if not values: return None
        return p.Player(name, Rating(float(values['mu']), float(values['sigma'])))

    def set_player(self, player):
        """
        :type player: Player
        """
        self._set_rating(player.name, player.rating.mu, player.rating.sigma)

    def log_results(self, names):
        if self.log_collection:
            self.log_collection.insert_one({'time': time.time(), 'names': names})

    def close(self):
        if self.client:
            self.client.close()



def test1():
    db_uri = Settings.get('mongo-db-uri', '---')
    db_collection = Settings.get('mongo-db-collection', '---')

    client = pymongo.MongoClient(db_uri)

    db = client.get_default_database()
    print 'collections', db.collection_names()

    collection = db[db_collection]
    print 'count', collection.count()

    players = collection.find()
    for player in players:
        print 'find', player

    # # Note that the insert method can take either an array or a single dict.
    # SEED_DATA = [
    #     {'player': 'miki', 'score': 1.0},
    #     {'player': 'tomi', 'score': 1.1}
    # ]
    # collection.insert_many(SEED_DATA)

    # query = {'player': 'maki'}

    # player = collection.find_one(query)
    # print 'find_one', player
    # players = collection.find(query)
    # for player in players:
    #     print 'find', player

    # print 'update...'
    # collection.update_one(query, {'$set': {'score': 2.0}}, upsert=True)
    #
    # player = collection.find_one(query)
    # print 'find_one', player
    # players = collection.find(query)
    # for player in players:
    #     print 'find', player

    # db.drop_collection(db_collection)

    client.close()
