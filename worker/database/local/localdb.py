"""
This file houses a local db object. This allows us to develop without having an actual database
instance running. This is only for testing purposes

Note that all data storage is in memory, so do not run on this mode for too long.
Also note that this is news application specific, and hence contains articles and sources
"""
import logging

from tinydb import TinyDB, Query
from ..dbobject import DBObject
from ...utils.general import copy_dict_shallow

class LocalDatabase(object):
    """
    Based on tinydb.
    Currently only supports articles and sources
    """

    def __init__(self, articles=None, sources=None):

        self.db = TinyDB('database.json')
        self.articles = db.table('articles')
        self.sources = db.table('sources')

        for idx, article in enumerate(self.articles):
            self.articles.insert(copy_dict_shallow(article))

        for idx, source in enumerate(self.sources):
            self.sources.insert(copy_dict_shallow(source))

        self.tables = { 'articles', 'sources' }


    def save_object(obj_type, obj):
        """
        Save the object to the database
        """
        assert isinstance(obj, DBObject)
        assert obj_type in self.tables

        table = getattr(self, obj_type)
        table.insert(obj.get_save_data())


    def get(obj_type, query):
        assert obj_type in self.tables
        table = getattr(self, obj_type)

        ret = list()
        for obj in table:
            is_match = True
            for key, value in query:
                if obj.get(key, None) != value:
                    is_match = False
                    break

            if is_match:
                ret.append(copy_dict_shallow(obj))

        return ret
