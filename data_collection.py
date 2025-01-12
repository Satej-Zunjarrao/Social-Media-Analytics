"""
data_collection.py

This script is responsible for connecting to the Twitter API using Tweepy,
streaming tweets in real-time based on specified hashtags or keywords, and
storing the raw tweet data in a structured format for further processing.

Author: Satej
"""

import tweepy
import pandas as pd
import os
from datetime import datetime

# Configuration: Replace with your Twitter API credentials
API_KEY = "your_api_key"
API_SECRET_KEY = "your_api_secret_key"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Set up output directory for storing raw tweet data
OUTPUT_DIR = "./raw_tweets/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def authenticate_twitter_api():
    """
    Authenticates to the Twitter API using Tweepy and returns the API object.

    Returns:
        tweepy.API: Authenticated Tweepy API object.
    """
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    print("Twitter API authentication successful.")
    return api

class StreamListener(tweepy.StreamListener):
    """
    Custom StreamListener class for processing incoming tweets in real time.
    """
    def __init__(self):
        super().__init__()
        self.tweets = []
        self.max_tweets = 1000  # Set limit for the number of tweets per session
        self.start_time = datetime.now()

    def on_status(self, status):
        """
        Handles incoming tweet data.

        Args:
            status (tweepy.Status): The tweet object provided by the API.
        """
        try:
            tweet = {
                "id": status.id,
                "created_at": status.created_at,
                "text": status.text,
                "user": status.user.screen_name,
                "location": status.user.location
            }
            self.tweets.append(tweet)

            # Save tweets periodically or if the limit is reached
            if len(self.tweets) >= self.max_tweets:
                self.save_tweets_to_csv()

        except Exception as e:
            print(f"Error processing tweet: {e}")

    def save_tweets_to_csv(self):
        """
        Saves collected tweets to a CSV file in the output directory.
        """
        filename = os.path.join(OUTPUT_DIR, f"tweets_{self.start_time.strftime('%Y%m%d_%H%M%S')}.csv")
        pd.DataFrame(self.tweets).to_csv(filename, index=False)
        print(f"Saved {len(self.tweets)} tweets to {filename}")
        self.tweets = []  # Reset the tweet list for the next batch

    def on_error(self, status_code):
        """
        Handles errors from the Twitter API.

        Args:
            status_code (int): The error code received from the API.
        """
        if status_code == 420:
            # Rate limit exceeded
            print("Rate limit exceeded. Disconnecting stream.")
            return False

def stream_tweets(keywords):
    """
    Streams tweets in real time based on specified keywords or hashtags.

    Args:
        keywords (list): List of keywords or hashtags to filter the tweets.
    """
    api = authenticate_twitter_api()
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

    print(f"Starting tweet stream for keywords: {keywords}")
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    # Example keywords: Replace with your own
    keywords = ["#technology", "#AI", "#DataScience"]
    stream_tweets(keywords)
