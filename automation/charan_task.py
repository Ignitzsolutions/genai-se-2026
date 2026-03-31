import logging

# Setup logging
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def count_words(file_path):
    try:
        logging.info("Script started")

        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            count = len(words)

        logging.info(f"Word count successful: {count}")
        print(f"Word Count: {count}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("Error:", e)


if __name__ == "__main__":
    file_path = input("Enter file path: ")
    count_words(file_path)