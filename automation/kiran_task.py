import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Script started")

try:
    now = datetime.now()
    print("Current Date & Time:", now)

    logging.info("Script executed successfully")

except Exception as e:
    print("Error:", e)
    logging.error(f"Error occurred: {e}")
    