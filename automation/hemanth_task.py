import requests
import logging
import argparse

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_user(user_id):
    logging.info(f'Script started - fetching user ID: {user_id}')
    try:
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        user = response.json()
        print(f"✅ Name   : {user['name']}")
        print(f"📧 Email  : {user['email']}")
        print(f"🌐 Website: {user['website']}")
        logging.info(f"Success - fetched user: {user['name']}")
    except Exception as e:
        logging.error(f'Failed - {e}')
        print(f'❌ Error: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=int, default=1)
    args = parser.parse_args()
    fetch_user(args.id)