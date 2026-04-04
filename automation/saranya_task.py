import argparse
import datetime
import logging
from pathlib import Path


def setup_logging(log_file: Path) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def get_current_time() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print the current date and time and log the execution."
    )
    parser.add_argument(
        "--log", "-l",
        type=Path,
        default=Path("automation/saranya_task.log"),
        help="Path to the log file.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    setup_logging(args.log)
    logging.info("Saranya automation task started")

    try:
        current_time = get_current_time()
        message = f"Current date and time: {current_time}"
        print(message)
        logging.info("Task completed successfully: %s", current_time)
    except Exception as exc:
        logging.exception("Task failed")
        print(f"An error occurred: {exc}")
        raise


if __name__ == "__main__":
    main()
