"""
This file hold functions and constants that are specific to the
News API at http://newsapi.org
"""

from newsapi import NewsApiClient
from .parser import generate_parser

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

ARGS = generate_parser().parse_args()

def get_all_sources():
	"""
	Return all the sources from the NewsAPI.
	Return format:
	"""
	news_api_client = NewsApiClient(api_key=ARGS.news_api_key)
	sources = news_api_client.get_sources()
	return sources
