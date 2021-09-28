#! python3

"""
Main entry point to extract Confluence pages.
"""

import argparse
import logging
import subprocess
import sys
from .config import load_config
from .confluenceclient import ConfluenceClient
from .export import export_all_pages


def _input_password() -> str:
    """
    Get password input by masking characters.
    Similar to getpass() but works with cygwin.
    """
    sys.stdout.write("Password :\n")
    sys.stdout.flush()
    subprocess.check_call(["stty", "-echo"])
    password = input()
    subprocess.check_call(["stty", "echo"])
    return password


def _create_argument_parser() -> argparse.ArgumentParser:
    """
    Create the list of arguments supported and return the parser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose mode",
        dest="verbose",
    )
    parser.add_argument(
        "config",
        action="store",
        help="Configuration file",
        nargs="?",
        metavar="config.yaml",
    )
    parser.add_argument(
        "--user",
        action="store",
        help="Define the user to connect to Atlassian server",
        dest="atlassian_user",
    )
    parser.add_argument(
        "--password",
        action="store",
        help="Define the password to connect to Atlassian server",
        dest="atlassian_password",
    )
    return parser


def main() -> None:
    """
    Entry point of Confluence extractor script.
    """
    # Parse command line
    parser = _create_argument_parser()
    args = parser.parse_args()

    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    # Create logger
    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=log_level,
    )

    if not args.config:
        parser.print_usage()
        return

    # Get configuration from JSON/YAML file
    config = load_config(args.config)
    if args.verbose:
        config.dump()

    if args.atlassian_user is None:
        args.atlassian_user = str(input("Enter login for Atlassian :\n"))
    if args.atlassian_password is None:
        args.atlassian_password = _input_password()

    confluence_client = ConfluenceClient(
        config.confluence,
        args.atlassian_user,
        args.atlassian_password,
    )

    export_all_pages(confluence_client, config)
