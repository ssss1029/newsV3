"""
See README.md for complete guide
"""

import logging

from parser import generate_parser

ARGS = generate_parser().parse_args()

def main():
    finished_loops = 0
    while True:

        # Update our sources

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

    logger.debug("Starting worker with mode = {0}".format(ARGS.mode))
    logger.debug("Settings = {0}".format(vars(ARGS)))

    main()
