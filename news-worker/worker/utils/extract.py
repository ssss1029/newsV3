"""
Handle text extraction from webpages
"""

import logging
import unicodedata

from boilerpipe.extract import Extractor
from worker.utils.parser import generate_parser

ARGS = generate_parser().parse_args()
logger = logging.getLogger(__name__)


def extract_content_from_url(url):
    """
    Returns the text from a given url. Works best on URLs that point to actual news articles.
    This function also cleans the text.
    """
    try:
        extractor = Extractogr(extractor='ArticleExtractor', url=url)
        extracted_text = extractor.getText()

        # For now, just do a simple unicode normalization.
        # TODO: Come back to this later.
        extracted_text = unicodedata.normalize('NFKD', extracted_text).encode('ascii','ignore')
        print("Extracted content from {0}".format(url))
    except Exception as e:
        print("Unable to extract content from {0}".format(url))
        print(">>> ERROR:", e)
        extracted_text = e

    return extracted_text
