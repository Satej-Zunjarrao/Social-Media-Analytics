"""
automation_pipeline.py

This script orchestrates the entire pipeline: from data collection to storage.
It integrates modules for data collection, preprocessing, sentiment analysis, 
trending topics identification, and storage, ensuring seamless automation.

Author: Satej
"""

import os
from data_collection import stream_tweets
from data_preprocessing import preprocess_data
from sentiment_analysis import perform_sentiment_analysis
from trending_topics import identify_and_visualize_trends
from data_storage import create_database, store_data_to_db

# Configuration paths
RAW_TWEETS_DIR = "./raw_tweets/"
PROCESSED_TWEETS_DIR = "./processed_tweets/"
VISUALIZATION_DIR = "./visualizations/"
os.makedirs(RAW_TWEETS_DIR, exist_ok=True)
os.makedirs(PROCESSED_TWEETS_DIR, exist_ok=True)
os.makedirs(VISUALIZATION_DIR, exist_ok=True)

def run_pipeline(keywords):
    """
    Executes the entire social media analytics pipeline.

    Args:
        keywords (list): List of keywords or hashtags to filter tweets.
    """
    print("Starting the automation pipeline...")
    
    # Step 1: Data Collection
    print("Step 1: Collecting tweets...")
    stream_tweets(keywords)
    latest_file = sorted(os.listdir(RAW_TWEETS_DIR), reverse=True)[0]
    raw_file_path = os.path.join(RAW_TWEETS_DIR, latest_file)

    # Step 2: Data Preprocessing
    print("Step 2: Preprocessing data...")
    preprocessed_file = os.path.join(PROCESSED_TWEETS_DIR, "cleaned_tweets.csv")
    preprocess_data(raw_file_path, preprocessed_file)

    # Step 3: Sentiment Analysis
    print("Step 3: Performing sentiment analysis...")
    sentiment_file = os.path.join(PROCESSED_TWEETS_DIR, "sentiment_results.csv")
    perform_sentiment_analysis(preprocessed_file, sentiment_file)

    # Step 4: Trending Topics Identification
    print("Step 4: Identifying trending topics...")
    trending_image_path = os.path.join(VISUALIZATION_DIR, "trending_topics.png")
    identify_and_visualize_trends(preprocessed_file, trending_image_path)

    # Step 5: Data Storage
    print("Step 5: Storing data into the database...")
    create_database()
    processed_data = pd.read_csv(sentiment_file)
    store_data_to_db(processed_data)

    print("Automation pipeline executed successfully!")

if __name__ == "__main__":
    # Example usage with hashtags or keywords
    hashtags = ["#AI", "#MachineLearning", "#DataScience"]
    run_pipeline(hashtags)
