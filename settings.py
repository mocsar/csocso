import json

__author__ = 'mocsar'

import os

class Settings(object):
    _data = None

    @staticmethod
    def get_all_keys():
        return ['db-uri', 'mongo-db-collection', ]

    @staticmethod
    def get(key, default=None):
        if Settings._data is None: Settings._read_data()
        return Settings._data.get(key, default)

    @staticmethod
    def set(key, value):
        if Settings._data is None:
            try:
                Settings._read_data()
            except:
                pass
        if Settings._data is None:
            Settings._data = {}
        Settings._data[key] = value
        Settings._write_data()

    @staticmethod
    def _create_sfile_name():
        home_dir = os.path.expanduser("~")
        sfile = os.path.join(home_dir, '.config', 'csocso', 'ini.json')
        return sfile

    @staticmethod
    def _read_data():
        sfile = Settings._create_sfile_name()
        with open(sfile) as json_file:
            Settings._data = json.load(json_file)
        if Settings._data is None:
            Settings._data = {}

    @staticmethod
    def _write_data():
        sfile = Settings._create_sfile_name()
        if not os.path.exists(os.path.dirname(sfile)):
            os.makedirs(os.path.dirname(sfile))
        with open(sfile, 'w') as json_file:
            json.dump(Settings._data, json_file, sort_keys=True, indent=4)

