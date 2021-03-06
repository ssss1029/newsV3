"""
Base class that all database objects should inherit from.

THIS IS NOT USED NOW.
"""

import collections

class DBObject(object):
    """
    Generic database object. All Databases must know how to interact with this.
    """

    def __init__(self, features):
        """
        features: dict(): { feature: value, feature: value }
        """
        for feat in features.keys():
            value = features[feat]

            # Only allow hashable values in the DBObject
            hashable = isinstance(value, collections.Hashable)
            if not hashable:
                raise ValueError("Unable to create DBObject with value {0}".format(value))

            setattr(self, feat, value)

        # Save a COPY of features
        self.features = dict()
        for feat in features.keys():
            self.features[feat] = features[feat]

    def get_save_data(self):
        data = dict()
        for feat in self.features:
            data[feat] = self.features[feat]
        return data
