import logging
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.INFO)

try:
    logging.info("Script started")

    now = datetime.now()
    print("Current Date & Time:", now)

    logging.info("Script executed successfully")

except Exception as e:
    logging.error(f"Error: {e}")
    print(e)