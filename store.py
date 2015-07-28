from mongo import Mongo

__author__ = 'mocsar'

class Store(object):

    store = None
    """ :type: Mongo """

    @classmethod
    def get_store(cls):
        """

        :rtype : Mongo
        """
        if not cls.store:
            cls.store = Mongo()
        return cls.store
