"""
data_preprocessing.py

This script preprocesses raw tweet data by cleaning text, removing noise, and
preparing it for analysis. It includes functions for text tokenization, normalization,
and removal of irrelevant content like URLs and special characters.

Author: Satej
"""

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download("stopwords")
nltk.download("punkt")

STOPWORDS = set(stopwords.words("english"))

def load_data(file_path):
    """
    Loads raw tweet data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing raw tweet data.

    Returns:
        pd.DataFrame: DataFrame with loaded tweet data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}, shape: {data.shape}")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def clean_text(text):
    """
    Cleans tweet text by removing URLs, special characters, and stop words.

    Args:
        text (str): Raw tweet text.

    Returns:
        str: Cleaned text.
    """
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # Remove special characters and numbers
    text = re.sub(r"\W|\d", " ", text)
    # Tokenize and remove stop words
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in STOPWORDS]
    return " ".join(tokens)

def preprocess_data(input_file, output_file):
    """
    Processes raw tweet data and saves the cleaned data to a new CSV file.

    Args:
        input_file (str): Path to the input CSV file with raw tweet data.
        output_file (str): Path to the output CSV file for saving cleaned data.
    """
    raw_data = load_data(input_file)
    if raw_data is not None:
        raw_data["cleaned_text"] = raw_data["text"].apply(clean_text)
        raw_data.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    # Example usage with file paths (replace with your own)
    input_path = "./raw_tweets/tweets_sample.csv"
    output_path = "./processed_tweets/cleaned_tweets.csv"
    preprocess_data(input_path, output_path)
