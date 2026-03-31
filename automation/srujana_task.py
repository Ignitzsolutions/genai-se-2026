import logging
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Script started here")

    try:
        now = datetime.now()
        print("Current Date & Time:", now)

        logging.info("Script executed successfully..")

    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error:", e)

if __name__ == "__main__":
    main()