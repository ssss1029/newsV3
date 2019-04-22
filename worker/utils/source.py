"""
A class that will house a news source. (e.g. CNN, BBC, etc.)
"""

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
	"za
}

class NewsSource(object):
    def __init__(self, _id, name, description, url, category, language, country):
        # Do sanity checks
        category_check = category in news_api_categories
        lang_check     = language in news_api_languages
        country_check  = country in news_api_countries

        if not category_check:
            raise ValueError("Unrecognized category: {0}".format(category))
        if not lang_check:
            raise ValueError("Unrecognized language: {0}".format(language))
        if not country_check:
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

