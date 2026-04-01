import argparse
import logging
from pathlib import Path


def setup_logging(log_file: Path):
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def count_words(file_path: Path) -> int:
    with file_path.open("r", encoding="utf-8") as f:
        text = f.read()
    # Basic word split on whitespace provides beginner-friendly behavior
    words = text.split()
    return len(words)


def main():
    parser = argparse.ArgumentParser(description="Read a text file and count words")
    parser.add_argument(
        "--file",
        "-f",
        type=Path,
        default=Path("automation/sample.txt"),
        help="Path to the input text file",
    )
    parser.add_argument(
        "--log",
        "-l",
        type=Path,
        default=Path("automation/app.log"),
        help="Path to the log file",
    )
    args = parser.parse_args()

    setup_logging(args.log)
    logging.info("Script started")

    try:
        input_file = args.file
        if not input_file.exists():
            raise FileNotFoundError(f"File not found: {input_file}")

        word_count = count_words(input_file)
        message = f"File '{input_file}' has {word_count} words."
        print(message)
        logging.info(message)

        logging.info("Script completed successfully")
    except Exception as e:
        error_message = f"Script failed: {e}"
        print(error_message)
        logging.exception(error_message)
        raise


if __name__ == "__main__":
    main()
