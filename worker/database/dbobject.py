"""
Base class that all database objects should inherit from.
"""

class DBObject(object):
    """
    Generic database object. All Databases must know how to interact with this.
    """

    def __init__(self, features, **kwargs):
        """
        features: dict(): { feature: value, feature: value }
        """
        for feat in features.keys():
            value = features[feat]
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
