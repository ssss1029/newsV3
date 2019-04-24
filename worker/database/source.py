"""
A class that will house a news source. (e.g. CNN, BBC, etc.)
"""

from dbobject import DBObject
from news_api import news_api_categories, news_api_languages, news_api_countries

newssource_required_features = [
    "id", "name", "description",
    "url", "category", "langauge",
    "country"
]

class NewsSource(DBObject):
	"""
	Hold a news source object.
	This assumes that the object is from the News API
	"""
    def __init__(self, features):

        # Check features:
        for required_feature in newssource_required_features:
            assert required_feature in features.keys()

        super().__init__(features)

    def __str__(self):
        """
        Return a readble representaion of self
        """
        return "<NewsSource {0}:{1}>".format(
            self.id,
            self.name
        )
