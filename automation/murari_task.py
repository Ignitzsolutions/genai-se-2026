import logging
from datetime import datetime

logging.basicConfig(
    filename='automation.log',
    level=logging.INFO
)

logging.info("Script started")

try:
    now = datetime.now()
    print("Current Date and Time:", now)

    logging.info("Success")

except Exception as e:
    logging.error(str(e))
    print(e)