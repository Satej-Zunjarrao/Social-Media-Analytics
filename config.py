"""
config.py

This script contains configuration variables and constants used across the project, 
such as API keys, database credentials, and file paths.

Author: Satej
"""

# Twitter API credentials
TWITTER_API_KEY = "your_api_key"
TWITTER_API_SECRET_KEY = "your_api_secret_key"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Database configuration
DATABASE_PATH = "./database/tweets_database.db"

# Directory paths
RAW_TWEETS_DIR = "./raw_tweets/"
PROCESSED_TWEETS_DIR = "./processed_tweets/"
VISUALIZATION_DIR = "./visualizations/"

# Keywords for streaming tweets (customizable)
DEFAULT_KEYWORDS = ["#AI", "#MachineLearning", "#DataScience"]

# Visualization settings
TRENDING_TOPICS_IMAGE = "./visualizations/trending_topics.png"

# Ensure directories exist
import os
os.makedirs(RAW_TWEETS_DIR, exist_ok=True)
os.makedirs(PROCESSED_TWEETS_DIR, exist_ok=True)
os.makedirs(VISUALIZATION_DIR, exist_ok=True)
