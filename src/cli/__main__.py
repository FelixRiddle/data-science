from .cli import get_parser
from dataset import download_dataset
from dataset import download_dataset_from_url

def main():
	"""Run CLI"""
	args = get_parser()

	if args.command == "example":
		if args.one:
			print("Example 1")

	if args.command == "dataset":
		print("Dataset downloader")
		if args.id and args.filename:
			download_dataset(args.id, args.filename)
		if args.url:
			download_dataset_from_url(args.url)

	print("Verbose: ", args.verbose)


if __name__ == "__main__":
    main()
