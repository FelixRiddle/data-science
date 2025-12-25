parser = argparse.ArgumentParser(
    prog="Data Science", description="Data Science", epilog=""
)

parser.add_argument(
    "-v", "--verbose", help="Increase output verbosity", action="store_true"
)

# Example subcommand
example_cmd = parser.add_subparsers(
    "example", help="Run a example", action="store_true"
)
example_cmd.add_argument("-1", "--1", help="Example 1", action="store_true")

args = parser.parse_args()
print("Verbose: ", args.verbose)
