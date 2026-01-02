import argparse
from .examples import example1


def get_parser():
    """Parse CLI"""
    parser = argparse.ArgumentParser(
        prog="Data Science", description="Data Science", epilog=""
    )

    parser.add_argument(
        "-v", "--verbose", help="Increase output verbosity", action="store_true"
    )

    subparsers = parser.add_subparsers(dest="command", help="Run a example")

    # Example subcommand
    example_cmd = subparsers.add_parser("example", help="Run an example")
    example_cmd.add_argument("-1", "--one", help="Example 1", action="store_true")

    # Dataset downloader subcommand
    dataset_cmd = subparsers.add_parser("dataset", help="Download a dataset")
    # Positional argument
    dataset_cmd.add_argument(
        "url", help="The Google Drive share link"
    )
    # Optional Arguments
    dataset_cmd.add_argument("--id", help="File id")
    dataset_cmd.add_argument("--filename", help="Filename")

    args = parser.parse_args()

    return args
