"""
utils.py

This script contains utility functions that are commonly used across different modules 
of the project. These include logging, exception handling, and helper methods for file 
management and data validation.

Author: Satej
"""

import os
import logging
from datetime import datetime

# Configure logging
LOG_FILE = "./logs/project_log.log"
os.makedirs("./logs/", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_message(level, message):
    """
    Logs a message to the project log file.

    Args:
        level (str): The severity level of the log ('info', 'warning', 'error').
        message (str): The message to log.
    """
    if level.lower() == "info":
        logging.info(message)
    elif level.lower() == "warning":
        logging.warning(message)
    elif level.lower() == "error":
        logging.error(message)
    else:
        logging.debug(message)
    print(f"{level.upper()}: {message}")

def validate_file_path(file_path):
    """
    Validates whether a given file path exists.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    if os.path.exists(file_path):
        log_message("info", f"File validated: {file_path}")
        return True
    else:
        log_message("error", f"File not found: {file_path}")
        return False

def create_directory(directory_path):
    """
    Ensures that a given directory exists, creating it if necessary.

    Args:
        directory_path (str): Path to the directory to validate or create.
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
        log_message("info", f"Directory ensured: {directory_path}")
    except Exception as e:
        log_message("error", f"Error creating directory {directory_path}: {e}")

def get_latest_file(directory, extension=".csv"):
    """
    Retrieves the latest file in a directory based on modification time.

    Args:
        directory (str): Directory to search for files.
        extension (str): File extension to filter by (default is '.csv').

    Returns:
        str: Path to the latest file, or None if no files are found.
    """
    try:
        files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith(extension)
        ]
        if files:
            latest_file = max(files, key=os.path.getmtime)
            log_message("info", f"Latest file retrieved: {latest_file}")
            return latest_file
        else:
            log_message("warning", f"No files with extension '{extension}' found in {directory}")
            return None
    except Exception as e:
        log_message("error", f"Error retrieving latest file: {e}")
        return None

def handle_exception(func):
    """
    Decorator for handling exceptions in functions.

    Args:
        func (function): The function to wrap.

    Returns:
        function: The wrapped function with exception handling.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_message("error", f"Exception in {func.__name__}: {e}")
            return None
    return wrapper

if __name__ == "__main__":
    # Example usage of utility functions
    log_message("info", "Utility script executed for testing.")

    # Test file path validation
    test_file = "./processed_tweets/cleaned_tweets.csv"
    validate_file_path(test_file)

    # Test directory creation
    test_directory = "./test_directory/"
    create_directory(test_directory)

    # Test latest file retrieval
    latest_csv = get_latest_file("./raw_tweets/", ".csv")
    if latest_csv:
        print(f"Latest file: {latest_csv}")
