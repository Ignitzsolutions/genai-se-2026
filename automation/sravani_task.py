import logging
from datetime import datetime

logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_log():
    logging.info("Script started")

    try:
        current_time = datetime.now()
        logging.info(f"Log generated at {current_time}")

        print("Log written successfully!")

        logging.info("Script completed successfully")

    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error occurred")

if __name__ == "__main__":
    generate_log()