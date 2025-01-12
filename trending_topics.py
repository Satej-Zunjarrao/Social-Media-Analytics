"""
trending_topics.py

This script identifies trending topics and hashtags from tweet data using the TF-IDF algorithm. 
It extracts keywords and visualizes their frequency for highlighting dominant themes in social media discussions.

Author: Satej
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """
    Loads cleaned tweet data from a CSV file.

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

def extract_trending_topics(texts, top_n=10):
    """
    Extracts trending topics using TF-IDF.

    Args:
        texts (list): List of preprocessed tweet texts.
        top_n (int): Number of top keywords to extract.

    Returns:
        dict: Dictionary of keywords and their TF-IDF scores.
    """
    vectorizer = TfidfVectorizer(max_features=top_n, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    keywords = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.sum(axis=0).A1  # Sum scores across all documents
    trending_topics = dict(zip(keywords, scores))
    return trending_topics

def visualize_trending_topics(trending_topics, output_file):
    """
    Visualizes trending topics using a bar chart and saves the visualization as an image.

    Args:
        trending_topics (dict): Dictionary of keywords and their scores.
        output_file (str): Path to save the bar chart image.
    """
    keywords = list(trending_topics.keys())
    scores = list(trending_topics.values())

    plt.figure(figsize=(10, 6))
    plt.barh(keywords, scores, color='skyblue')
    plt.xlabel("TF-IDF Score")
    plt.ylabel("Keywords")
    plt.title("Trending Topics")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
    print(f"Trending topics visualization saved to {output_file}")

def identify_and_visualize_trends(input_file, output_image):
    """
    Identifies and visualizes trending topics from cleaned tweet data.

    Args:
        input_file (str): Path to the CSV file containing cleaned tweet data.
        output_image (str): Path to save the trending topics visualization.
    """
    data = load_data(input_file)
    if data is not None:
        trending_topics = extract_trending_topics(data["cleaned_text"].tolist())
        print("Trending Topics Identified:", trending_topics)
        visualize_trending_topics(trending_topics, output_image)

if __name__ == "__main__":
    # Example usage with file paths (replace with your own)
    input_path = "./processed_tweets/cleaned_tweets.csv"
    output_image_path = "./visualizations/trending_topics.png"
    os.makedirs("./visualizations/", exist_ok=True)
    identify_and_visualize_trends(input_path, output_image_path)
