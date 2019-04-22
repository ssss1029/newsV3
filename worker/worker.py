"""
See README.md for complete guide
"""

import argparse
import logging

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--mode', default='local', choices=['local'],
                    help='Choose mode to run worker.')
parser.add_argument('--log-level', type=str, default="DEBUG",
                    choices=["DEBUG", "INFO", "WARNING", "CRITICAL"],
                    help='sum the integers (default: find the max)')
parser.add_argument('--log-file', type=str, default=None,
                    help='File to write to. If not set, will log to STDOUT.')
# This can get passed all over the place, but will never be changed.
# Need to enforce this requirment.
ARGS = parser.parse_args()

def main():
    pass

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
