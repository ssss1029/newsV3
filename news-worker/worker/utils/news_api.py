"""
This file hold functions and constants that are specific to the
News API at http://newsapi.org
"""

import logging

from newsapi import NewsApiClient

logger = logging.getLogger(__name__)

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

def get_top_articles(source_id, news_api_key):
	"""
	Return all the current top articles from the given source.
	If there is any error whatsoever, this will throw an exception. So, if articles are returned
	and the fuunc exits successfully, there have been no errors.

	Return format:
		If error:
			raises Exception
		If no error:
			[
				{
					'source': {
						'id': 'abc-news', 
						'name': 'ABC News'
					}, 
					'author': 'John Parkinson', 
					'title': "Florida Bar looking at GOP ...", 
					'description': 'Florida Republican Rep. ...', 
					'url': 'https://abcnews.go.com/Politics/florida-bar-gop-lawmakers-tweet-targeting-michael-cohen/story?id=62910364', 
					'urlToImage': 'https://s.abcnews.com/images/Politics/matt-gaetz-epa-jef-190508_hpMain_16x9_992.jpg', 
					'publishedAt': '2019-05-08T21:49:58Z', 
					'content': 'Florida Republican Rep. Matt Gaetz is facing continued ... … [+3846 chars]'
				}, 
				{
					...
				}
			]
	"""
	news_api_client = NewsApiClient(api_key=news_api_key)

	response = news_api_client.get_top_headlines(
		sources=source_id,
		page_size=100,
		page=1 # This is 1-indexed
	)

	if response["status"] != "ok":
		logger.exception("Error getting articles for {0}. Got the following return object: {1}".format(
			source_id,
			response
		), exc_info=True)

		raise Exception("There was an error getting sources. See log.")
	
	# Now, we need to check if we actually got all the top articles from this one request
	# response will contain a 'totalResults' field, which we can use to figure out if there are more we need to get

	curr_articles = response["articles"]
	num_total_articles = int(response['totalResults'])
	curr_page = 2
	while num_total_articles < len(curr_articles):
		response = news_api_client.get_top_headlines(
			sources=source_id,
			page_size=100,
			page=2 # This is 1-indexed
		)

		if response["status"] != "ok":
			logger.exception("Error getting articles for {0}. Got the following return object: {1}".format(
				source_id,
				response
			), exc_info=True)

			raise Exception("There was an error getting sources. See log.")
		else:
			curr_articles.extend(response['articles'])
			curr_page += 1

	return curr_articles


###############################
# CONSTANTS
###############################

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

