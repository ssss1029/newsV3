
import logging

from worker.utils.news_api import get_top_articles
from worker.utils.parser import generate_parser

ARGS = generate_parser().parse_args()
logger = logging.getLogger(__name__)

def update_articles(db, source, news_api_key, strict=True):
    """
    Update all the articles in our database by querying the NewsAPI as appropriate
    This function will kill the program on errors if strict is True.
    """
    try:
        top_articles = get_top_articles(source_id=source["id"], news_api_key=ARGS.news_api_key)
        logger.debug("Got top articles for source {0}: {1}".format(
            source["id"],
            top_articles
        ))
    except Exception as e:
        logger.exception(e)
        logger.info("Unable to pull new top articles for source {0} from news API".format(source['id']))

        if strict:
            # Kill the program
            logger.critical("--strict used. Killing program")
            exit(-1)
        else:
            # Don't kill the program, but since there aren't any new sources, just go to the
            # next step
            logger.warning("--strict NOT used, so continuing without updating top articles for source {0}".format(source['id']))
            return
    
    for article in top_articles:
        try:
            db.updateOrInsertOne(
                tableName="articles",
                query={"url": article["url"]},
                fields=article
            )
        except Exception as e:
            logger.exception(e)
            logger.exception("Unable to insert/update {0} into DB".format(pulled_source))
            if strict:
                # Kill the program
                logger.critical("--strict used. Killing program")
                exit(-1)
            else:
                # Continue
                logger.warning("--strict NOT used, so continuing without updating this source.")
                return

    logger.info("Processed {0} articles for source {1}".format(
        len(top_articles),
        source['id']
    ))
