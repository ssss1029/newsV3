
import logging
import time

from multiprocessing.dummy import Pool

from worker.utils.news_api import get_top_articles
from worker.utils.parser import generate_parser
from worker.utils.extract import extract_content_from_url

ARGS = generate_parser().parse_args()
logger = logging.getLogger(__name__)

def extract_content_from_all_articles(db, news_api_key, strict=True, num_threads=1):
    """
    Update all the articles in our database by querying the NewsAPI as appropriate
    This function will kill the program on errors if strict is True.
    """
    articles = db.get(
        'articles',
        query={"content": None}
    )

    logger.info("Beginning to process {0} articles.".format(
        len(articles),
    ))
    
    p = Pool(num_threads)
    contents = p.map(extract_content_from_url, [a['url'] for a in articles])

    for content, article in zip(contents, articles):
        if isinstance(content, Exception):
            continue

        # Save article content
        try:
            db.updateOrInsertOne(
                tableName="articles",
                query={"url": article["url"]},
                fields={"content": str(content)}
            )
        except Exception as e:
            logger.exception(e)
            logger.exception("Unable to insert/update article content into DB")
            if strict:
                # Kill the program
                logger.critical("--strict used. Killing program")
                exit(-1)
            else:
                # Continue
                logger.warning("--strict NOT used, so continuing without updating this article's content.")
                return

    logger.info("Processed {0} articles.".format(
        len(articles),
    ))
