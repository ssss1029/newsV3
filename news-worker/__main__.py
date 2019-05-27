"""
See README.md for complete guide
"""

import logging
import os
import sys

from worker.database.local.localdb import LocalDatabase
from worker.steps.update_articles import update_articles
from worker.steps.update_sources import update_sources
from worker.utils.news_api import get_all_sources, get_top_articles
from worker.utils.parser import generate_parser

ARGS = generate_parser().parse_args()

# All the step names
ALL_STEPS = [
    "SOURCES",
    "TOP_HEADLINES",
    "EXTRACT_CONTENT"
]

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

        # Update our sources (step: SOURCES)
        update_sources(
            db=db,
            news_api_key=ARGS.news_api_key,
            strict=ARGS.strict
        )

        # For each source, get the top headlines. Store top headlines in db. (step: TOP_HEADLINES)
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

        # For each top headline, check if it is already processed. (step: )

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
