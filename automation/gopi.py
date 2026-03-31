import logging
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info("Script started")

        current_time = datetime.now()
        print("Current Date & Time:", current_time)

        logging.info("Script executed successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(e)

if __name__ == "__main__":
    main()