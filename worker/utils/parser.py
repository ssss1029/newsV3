"""
Command line argument parser
"""

import argparse

def generate_parser():
    """
    Generate a parser for use by all modules.
    """

    parser = argparse.ArgumentParser(description='News Worker.')

    # General settings
    parser.add_argument('--mode', default='local', choices=['local'],
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
