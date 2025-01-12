"""
data_storage.py

This script handles the storage of processed tweet data into a relational database. 
It uses SQLite for local storage but can be adapted for cloud-based databases.

Author: Satej
"""

import sqlite3
import pandas as pd
import os

# Database file path (can be replaced with a cloud-based database connection string)
DATABASE_PATH = "./database/tweets_database.db"
os.makedirs("./database/", exist_ok=True)

def create_database():
    """
    Creates the SQLite database and initializes the required table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tweets (
                id INTEGER PRIMARY KEY,
                created_at TEXT,
                text TEXT,
                user TEXT,
                location TEXT,
                sentiment TEXT
            )
        """)
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error creating database: {e}")

def store_data_to_db(data, table_name="tweets"):
    """
    Stores the processed tweet data into the database.

    Args:
        data (pd.DataFrame): DataFrame containing the data to store.
        table_name (str): Name of the database table.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        data.to_sql(table_name, conn, if_exists='append', index=False)
        conn.close()
        print(f"Data successfully stored in the '{table_name}' table.")
    except Exception as e:
        print(f"Error storing data to database: {e}")

if __name__ == "__main__":
    # Example usage
    create_database()
    
    # Replace with your actual CSV path
    sample_data_path = "./processed_tweets/sentiment_results.csv"
    if os.path.exists(sample_data_path):
        tweet_data = pd.read_csv(sample_data_path)
        store_data_to_db(tweet_data)
    else:
        print(f"File {sample_data_path} not found.")
