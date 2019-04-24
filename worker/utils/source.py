"""
A class that will house a news source. (e.g. CNN, BBC, etc.)
"""

from news_api import news_api_categories, news_api_languages, news_api_countries

class NewsSource(object):
	"""
	Hold a news source object.
	This assumes that the object is from the News API
	"""
    def __init__(self, _id, name, description, url, category, language, country):

        # Do sanity checks
        if category not in news_api_categories:
            raise ValueError("Unrecognized category: {0}".format(category))
        if language not in news_api_languages:
            raise ValueError("Unrecognized language: {0}".format(language))
        if language not in news_api_languages:
            raise ValueError("Unrecognized country: {0}".format(country))

        self.id = _id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

    def __str__(self):
        """
        Return a readble representaion of self
        """
        return "<NewsSource {0}: {0}>".format(self.id, self.name)