import logging
import datetime
import requests

# Setup logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_data():
    logging.info('Script started')
    try:
        # Fetch data from public API
        response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        data = response.json()
        
        # Print current date and time
        now = datetime.datetime.now()
        print(f"Current Date & Time: {now}")
        print(f"Fetched Data: {data}")
        
        logging.info('Data fetched successfully')
        logging.info(f'Response: {data}')
        
    except Exception as e:
        print(f"Error occurred: {e}")
        logging.error(f'Error occurred: {e}')

fetch_data()


