from pathlib import Path
from .cli import get_parser
from dataset import download_dataset_by_id
from dataset import download_dataset

def main():
	"""Run CLI"""
	args = get_parser()
 
	# This creates: project_root/data/raw/filename
	data_dir = Path("data/raw")
    
	# Ensure the directory exists (like 'mkdir -p' in bash)
	data_dir.mkdir(parents=True, exist_ok=True)

	if args.command == "example":
		if args.one:
			print("Example 1")

	if args.command == "dataset":
		print("Dataset downloader")
		if args.id and args.filename:
			download_dataset_by_id(args.id, args.filename)
		if args.url:
			download_dataset(args.url)

	print("Verbose: ", args.verbose)


if __name__ == "__main__":
    main()
