"""
See README.md for complete guide
"""

import logging
import os
import sys

from worker.database.local.localdb import LocalDatabase
from worker.utils.news_api import get_all_sources, get_top_articles
from worker.utils.parser import generate_parser

ARGS = generate_parser().parse_args()

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

def main():
    finished_loops = 0

    # Initialize run mode.
    if ARGS.mode == 'local':
        db = LocalDatabase(
            articles=[],
            sources=[],
            json_save_file="news-worker/database.json"
        )
    else:
        raise NotImplementedError("Mode {0} not supported yet".format(ARGS.mode))

    logger.info("Starting main worker loop")
    while True:

        # Update our sources
        update_sources(
            db=db,
            news_api_key=ARGS.news_api_key,
            strict=ARGS.strict
        )

        # For each source, get the top headlines. Store top headlines in db.
        saved_sources = db.get(
            tableName='sources',
            fields=['id'],
            query={}
        )
        logger.info("Beginning updating top articles for each source")
        for source in saved_sources:
            update_articles(
                db=db,
                source=source,
                news_api_key=ARGS.news_api_key,
                strict=ARGS.strict
            )

        logger.info("Finished updating top articles for each source.")

        # For each top headline, check if it is already processed.

        # For each unprocessed top headline, process it and store results.

        finished_loops += 1
        if finished_loops == ARGS.max_loops:
            logger.debug("Finished {0} loops. Stopping now.".format(finished_loops))
            break

    logger.debug("Bye-bye")



if __name__ == "__main__":
    # Set up logging
    numeric_log_level = getattr(logging, ARGS.log_level.upper(), None)
    if ARGS.log_file is not None:
        logging.basicConfig(filename=ARGS.log_file, filemode='a+', level=numeric_log_level)
    else:
        logging.basicConfig(level=numeric_log_level)
    logger = logging.getLogger(__name__)

    logger.info("Starting worker with mode = {0}".format(ARGS.mode))
    logger.info("Settings = {0}".format(vars(ARGS)))

    main()
