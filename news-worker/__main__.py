"""
See README.md for complete guide
"""

import logging
import os
import sys

from worker.database.local.localdb import LocalDatabase
from worker.utils.news_api import get_all_sources
from worker.utils.parser import generate_parser

ARGS = generate_parser().parse_args()

def update_sources(db):
    """
    Update all the sources in our database
    This function will exit when appropriate.
    """

    # Get the current sources from the API
    try:
        sources_new = get_all_sources(ARGS.news_api_key)
        logger.info("Acquired new sources")
        logger.debug(sources_new)
    except Exception as e:
        logger.exception(e)
        logger.info("Unable to pull new sources from news API")
        sources_new = []

        if ARGS.strict == True:
            # Kill the program
            logger.critical("--strict used. Killing program")
            exit(-1)
        else:
            # Don't kill the program, but since there aren't any new sources, just go to the
            # next step
            logger.warning("--strict NOT used, so continuing without updating DB with sources.")
            return

    logger.info("Beginning updating database ")
    for pulled_source in sources_new:
        db.updateOrInsertOne(
            tableName="sources",
            query={"id": pulled_source["id"]},
            fields=pulled_source
        )
    logger.info("Finished updating database")

    # sources_new should be a fully populated list by here.
    # logger.info("Beginning updating database ")
    # for pulled_source in sources_new:
    #     curr_id = pulled_source["id"]

    #     # Check if this ID already exists in the database.
    #     existing_source = db.get(
    #         obj_type="source",
    #         query={"id" : curr_id}
    #     )

    #     if len(existing_source) > 1:
    #         # Something has gone horribly wrong.
    #         logger.critical("ID {0} has multiple sources in database: {1}".format(
    #             curr_id,
    #             str(existing_source)
    #         ))
    #         exit(-1)

    #     if len(existing_source) == 1:
    #         # Update this item
    #         logger.debug("Updating object in {0} with id = {1} to {2}".format(
    #             "sources",
    #             curr_id,
    #             pulled_source
    #         ))

    #         db.update(
    #             obj_type="source",
    #             query={"id" : curr_id},
    #             fields=pulled_source
    #         )
    #     else:
    #         # No matching existing sources. Stick this in database.
    #         # Insert into the database
    #         logger.debug("Inserting object into {0}: {1}".format(
    #             "sources",
    #             pulled_source
    #         ))
    #         db.insert(
    #             obj_type="source",
    #             fields=pulled_source
    #         )
    # logger.info("Finished updating database")


def main():
    finished_loops = 0

    # Initialize run mode.
    if ARGS.mode == 'local':
        database = LocalDatabase(
            articles=[],
            sources=[],
            json_save_file="database.json"
        )
    else:
        raise NotImplementedError("Mode {0} not supported yet".format(ARGS.mode))

    logger.info("Starting main worker loop")
    while True:

        # Update our sources
        update_sources(database)

        # For each source, get the top headlines. Store top headlines somewhere.

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
