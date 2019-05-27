

import logging

from worker.utils.news_api import get_all_sources
from worker.utils.parser import generate_parser

ARGS = generate_parser().parse_args()
logger = logging.getLogger(__name__)

def update_sources(db, news_api_key, strict=True):
    """
    Update all the sources in our database by querying the NewsAPI as appropriate
    This function will kill the program on errors if strict is True.
    """

    # Get the current sources from the API
    try:
        sources_new = get_all_sources(news_api_key)
        logger.info("Acquired new sources")
        logger.debug(sources_new)
    except Exception as e:
        logger.exception(e)
        logger.info("Unable to pull new sources from news API")

        if strict:
            # Kill the program
            logger.critical("--strict used. Killing program")
            exit(-1)
        else:
            # Don't kill the program, but since there aren't any new sources, just go to the
            # next step
            logger.warning("--strict NOT used, so continuing without updating DB with sources.")
            return

    logger.info("Beginning updating sources in DB")
    for pulled_source in sources_new:
        try:
            db.updateOrInsertOne(
                tableName="sources",
                query={"id": pulled_source["id"]},
                fields=pulled_source
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

    logger.info("Finished updating sources in DB")