
import logging  
# Importing Python's built-in logging module to track events (info, errors, etc.)

# Setup logging configuration
logging.basicConfig(
    filename='automation.log',  
    # All logs will be written to a file named 'automation.log'

    level=logging.INFO,  
    # Logging level is set to INFO → it will record INFO, WARNING, ERROR, CRITICAL

    format='%(asctime)s - %(levelname)s - %(message)s'  
    # Format of each log:
    # timestamp - log level - actual message
)

def count_words(file_path):
    # Function to count number of words in a given file

    try:
        # Start of error handling block

        logging.info("Script started")  
        # Log that the script execution has started

        with open(file_path, 'r') as file:  
            # Open the file in read mode ('r')
            # 'with' ensures file is automatically closed after use

            content = file.read()  
            # Read entire file content as a string

            words = content.split()  
            # Split text into words using spaces → returns list of words

            count = len(words)  
            # Count number of words by finding length of list

        logging.info(f"Word count successful: {count}")  
        # Log successful execution with word count

        print(f"Word Count: {count}")  
        # Print result to console for user

    except Exception as e:
        # Catch any error (file not found, permission error, etc.)

        logging.error(f"Error occurred: {e}")  
        # Log error message into log file

        print("Error:", e)  
        # Print error to user


if __name__ == "__main__":
    # This ensures the code runs only when this file is executed directly

    file_path = input("Enter file path: ")  
    # Take file path input from user (e.g., sample.txt)

    count_words(file_path)  
    # Call function and pass file path