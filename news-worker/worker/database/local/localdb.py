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

logger = logging.getLogger(__name__)

class LocalDatabase(object):
    """
    Based on tinydb.
    Currently only supports articles and sources
    """

    def __init__(self, articles=None, sources=None, json_save_file='database.json'):

        self.db = TinyDB(json_save_file)
        self.articles = self.db.table('articles')
        self.sources = self.db.table('sources')

        for article in self.articles:
            self.articles.insert(copy_dict_shallow(article))

        for source in self.sources:
            self.sources.insert(copy_dict_shallow(source))

        self.tables = { 'articles', 'sources' }

    def _insert(self, tableName, obj):
        """
        Save the object to the database
        """
        assert tableName in self.tables

        table = getattr(self, tableName)
        table.insert(obj)


    def _get(self, tableName, query):
        assert tableName in self.tables
        table = getattr(self, tableName)
        return table.search(query)

    def _updateAll(self, tableName, query, fields):
        """
        Update all records matching query to contain fields
        """
        assert tableName in self.tables
        table = getattr(self, tableName)
        table.update(fields, query)


    def updateOrInsertOne(self, tableName, query, fields):
        """
        If there are 0 records that match query, add in the entirety of fields as a new
            record into the db under tableName
        If there is exactly 1 record that matches query, update that record with fields
        If there is more than one record that matches query, error.
        """

        # Query the database with the given query
        MatchingQuery = Query()
        for key, value in query.items():
            MatchingQuery = MatchingQuery & (Query()[key] == value)
        
        existing_sources = self._get(
            tableName=tableName,
            query=MatchingQuery
        )
        
        if len(existing_sources) > 1:
            # Something has gone wrong
            logger.exception("db.updateOne failed. Found {0} in {1} that match {2}".format(
                len(existing_sources),
                tableName,
                query
            ))
            raise Exception()
        elif len(existing_sources) == 0:
            # Insert this into the DB
            logger.debug("Found 0 existing records for query {0}. Inserting {1} into db.".format(
                query,
                fields
            ))
            self._insert(
                tableName=tableName,
                obj=fields
            )
        else:
            # Update the one record that exists in the DB
            assert len(existing_sources) == 1 # Sanity check
            logger.debug("Found 1 existing record for query {0}. Updating with {1}".format(
                query, 
                fields
            ))
            self._updateAll(
                tableName=tableName,
                query=MatchingQuery,
                fields=fields
            )
        

