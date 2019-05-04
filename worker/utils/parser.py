"""
Command line argument parser
"""

import argparse

def str2bool(v):
    """
    Converts a string to its appropriate boolean value.
    Useful for parsing boolean arguments.
    See https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def generate_parser():
    """
    Generate the parser for use by all modules.
    """

    parser = argparse.ArgumentParser(description='News Worker.')

    # General settings
    parser.add_argument('--mode', default='local', choices=['local'],
                        help='Choose mode to run worker.')
    parser.add_argument('--strict', default=True, type=str2bool,
                        help='Choose mode to run worker.')
    parser.add_argument('--max-loops', default=-1, type=int,
                        help='Maximum number of update loops to run. -1 = Run forever')

    # Logging settings
    parser.add_argument('--log-level', type=str, default="DEBUG",
                        choices=["DEBUG", "INFO", "WARNING", "CRITICAL"],
                        help='sum the integers (default: find the max)')
    parser.add_argument('--log-file', type=str, default=None,
                        help='File to write to. If not set, will log to STDOUT.')

    # Other config
    parser.add_argument('--news-api-key', type=str, default=None,
                        help='News API Secret. Go to newsapi.org to get one if you don\'t \
                        have one already')

    return parser
