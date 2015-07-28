from mongo import Mongo

__author__ = 'mocsar'

class Store:

    store = None
    """ :type: Mongo """

    @classmethod
    def get_store(cls):
        if not cls.store:
            cls.store = Mongo()
        return cls.store
