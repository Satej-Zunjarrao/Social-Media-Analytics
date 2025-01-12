"""
sentiment_analysis.py

This script performs sentiment analysis on preprocessed tweet data using a pre-trained sentiment analysis model.
It classifies tweets as positive, negative, or neutral and provides an aggregated sentiment score for the dataset.

Author: Satej
"""

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os

# Download the necessary NLTK resource for sentiment analysis
import nltk
nltk.download("vader_lexicon")

def load_data(file_path):
    """
    Loads preprocessed tweet data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing cleaned tweet data.

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

def analyze_sentiment(text, analyzer):
    """
    Analyzes the sentiment of a given text using the SentimentIntensityAnalyzer.

    Args:
        text (str): The text to analyze.
        analyzer (SentimentIntensityAnalyzer): The sentiment analyzer object.

    Returns:
        str: Sentiment label (positive, neutral, negative).
    """
    scores = analyzer.polarity_scores(text)
    if scores['compound'] > 0.05:
        return "positive"
    elif scores['compound'] < -0.05:
        return "negative"
    else:
        return "neutral"

def perform_sentiment_analysis(input_file, output_file):
    """
    Performs sentiment analysis on cleaned tweet data and saves the results.

    Args:
        input_file (str): Path to the input CSV file with cleaned tweet data.
        output_file (str): Path to the output CSV file for saving sentiment analysis results.
    """
    data = load_data(input_file)
    if data is not None:
        analyzer = SentimentIntensityAnalyzer()
        data["sentiment"] = data["cleaned_text"].apply(lambda x: analyze_sentiment(x, analyzer))
        data.to_csv(output_file, index=False)
        print(f"Sentiment analysis results saved to {output_file}")

if __name__ == "__main__":
    # Example usage with file paths (replace with your own)
    input_path = "./processed_tweets/cleaned_tweets.csv"
    output_path = "./processed_tweets/sentiment_results.csv"
    perform_sentiment_analysis(input_path, output_path)
