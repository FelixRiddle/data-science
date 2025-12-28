from .cli import get_parser


def main():
    """Run CLI"""
    parser = get_parser()
    args = parser.parse_args()

    if args.command == "example":
        if args.one:
            print("Example 1")

    print("Verbose: ", args.verbose)


if __name__ == "__main__":
    main()
