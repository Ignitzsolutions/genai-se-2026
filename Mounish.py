import logging
from datetime import datetime

# Logging setup
log_file = "Mounish.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="a", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logging.info("Execution started")

try:
    now = datetime.now()
    current_dt = now.strftime("%Y-%m-%d %H:%M:%S")
    message = f"Current date and time: {current_dt}"
    print(message)
    logging.info(message)

    # Your main script logic can go here

    logging.info("Execution finished successfully")
except Exception as ex:
    logging.exception("Execution failed")
    raise
