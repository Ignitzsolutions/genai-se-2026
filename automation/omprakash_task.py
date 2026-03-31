import logging
from datetime import datetime

logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Script started")
    
    try:
        now = datetime.now()
        print("Current Date & Time:", now)
        
        logging.info("Script executed successfully")
        
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(e)

if __name__ == "__main__":
    main()