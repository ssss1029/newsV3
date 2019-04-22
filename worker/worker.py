"""
See README.md for complete guide
"""

import argparse
import logging

parser = argparse.ArgumentParser(description='Process some integers.')

# General settings
parser.add_argument('--mode', default='local', choices=['local'],
                    help='Choose mode to run worker.')
parser.add_argument('--max-loops', default=None, type=int,
                    help='Maximum number of update loops to run.')

# Logging settings
parser.add_argument('--log-level', type=str, default="DEBUG",
                    choices=["DEBUG", "INFO", "WARNING", "CRITICAL"],
                    help='sum the integers (default: find the max)')
parser.add_argument('--log-file', type=str, default=None,
                    help='File to write to. If not set, will log to STDOUT.')

# This can get passed all over the place, but will never be changed.
# Need to enforce this requirment.
ARGS = parser.parse_args()

def main():

    curr_loop = 0
    while True:
        curr_loop += 1

        # Update our sources

        # For each source, get the top headlines. Store top headlines somewhere.

        # For each top headline, check if it is already processed.

        # For each unprocessed top headline, process it and store results.

        if curr_loop == ARGS.max_loops:
            logger.debug("Finished {0} loops. Stopping now.".format(curr_loop))
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
