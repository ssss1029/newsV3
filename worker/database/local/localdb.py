"""
This file houses a local db object. This allows us to develop without having an actual database
instance running. This is only for testing purposes

Note that all data storage is in memory, so do not run on this mode for too long.
"""
import logging

class LocalDatabase(object):
    def __init__(self):
        pass
