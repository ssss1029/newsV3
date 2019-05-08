"""
This file hold functions and constants that are specific to the
News API at http://newsapi.org
"""

import logging

from newsapi import NewsApiClient

logger = logging.getLogger(__name__)

news_api_categories = {
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology"
}

news_api_languages = {
    "ar",
    "de",
    "en"
    "es",
    "fr",
    "he",
    "it",
    "nl",
    "no",
    "pt",
    "ru",
    "se",
    "ud",
    "zh"
}

news_api_countries = {
    "ae",
	"ar",
	"at",
	"au",
	"be",
	"bg",
	"br",
	"ca",
	"ch",
	"cn",
	"co",
	"cu",
	"cz",
	"de",
	"eg",
	"fr",
	"gb",
	"gr",
	"hk",
	"hu",
	"id",
	"ie",
	"il",
	"in",
	"it",
	"jp",
	"kr",
	"lt",
	"lv",
	"ma",
	"mx",
	"my",
	"ng",
	"nl",
	"no",
	"nz",
	"ph",
	"pl",
	"pt",
	"ro",
	"rs",
	"ru",
	"sa",
	"se",
	"sg",
	"si",
	"sk",
	"th",
	"tr",
	"tw",
	"ua",
	"us",
	"ve",
	"za"
}

def get_all_sources(news_api_key):
	"""
	Return all the sources from the NewsAPI.

	Return format:
		If no error:
			[
				{
					'id': 'abc-news',
					'name': 'ABC News',
					'description': 'Your trusted source for breaking blah blah.',
					'url': 'https://abcnews.go.com',
					'category': 'general',
					'language': 'en',
					'country': 'us'
				}
			]
		If error:
			Rasies exception.
	"""
	news_api_client = NewsApiClient(api_key=news_api_key)

	# This can also raise an excption
	sources = news_api_client.get_sources()

	if sources["status"] == "ok":
		# We're all good
		return sources["sources"]
	else:
		logger.exception("Error getting sources. Got the following return object: {0}".format(
			sources
		), exc_info=True)

		raise Exception("There was an error getting sources. See log.")
