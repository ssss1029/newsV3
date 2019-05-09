"""
Handle text extraction from webpages
"""

from boilerpipe.extract import Extractor
import unicodedata

def extract_article_from_url(url):
    """
    Returns the text from a given url. Works best on URLs that point to actual news articles.
    This function also cleans the text.
    """
    extractor = Extractor(extractor='ArticleExtractor', url=url)
    extracted_text = extractor.getText()

    # For now, just do a simple unicode normalization.
    # TODO: Come back to this after working more with BERT.
    extracted_text = unicodedata.normalize('NFKD', extracted_text).encode('ascii','ignore')

    return extracted_text
