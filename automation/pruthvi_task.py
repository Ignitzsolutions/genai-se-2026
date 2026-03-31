import logging

# Setup logging - logs will be saved to app.log file
logging.basicConfig(
    filename='automation/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def count_words(filepath):
    """Reads a text file and counts the total number of words."""
    logging.info('Script started')

    try:
        # Open and read the file
        with open(filepath, 'r') as file:
            content = file.read()

        # Count words by splitting on whitespace
        words = content.split()
        word_count = len(words)

        print(f"File: {filepath}")
        print(f"Total words: {word_count}")

        logging.info(f'Successfully counted {word_count} words in {filepath}')
        return word_count

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        logging.error(f'File not found: {filepath}')
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f'Unexpected error: {e}')

if __name__ == '__main__':
    count_words('automation/sample.txt')