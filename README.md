# Social-Media-Analytics
Built a real-time system to analyze social media data for sentiment, trends, and actionable insights.

# Social Media Analytics System

## Overview
The **Social Media Analytics System** is a Python-based solution designed to analyze social media data (tweets) in real time. The system integrates API-based data collection, sentiment analysis, trend identification, and visualization to provide actionable insights for brands, enabling improved customer engagement and campaign effectiveness.

This project includes a modular and scalable pipeline for data collection, cleaning, sentiment analysis, trending topic identification, visualization, and automation.

---

## Key Features
- **Data Collection**: Streams live tweets using the Twitter API.
- **Data Cleaning**: Preprocesses text by removing noise, stop words, and URLs.
- **Sentiment Analysis**: Classifies tweets into positive, negative, or neutral sentiments using pre-trained models.
- **Trending Topics**: Identifies trending hashtags and keywords using TF-IDF.
- **Visualization**: Generates real-time dashboards and insights for stakeholders.
- **Automation**: Automates the pipeline to ensure continuous processing and updates.

## Directory Structure
```
project/
│
├── data_collection.py          # Streams live tweets using Twitter API
├── data_preprocessing.py       # Cleans and preprocesses raw tweet data
├── sentiment_analysis.py       # Performs sentiment classification on tweets
├── trending_topics.py          # Identifies trending topics and hashtags
├── data_storage.py             # Stores processed data in a relational database
├── automation_pipeline.py      # Orchestrates the entire analytics pipeline
├── visualization_dashboard.ipynb # Generates advanced visualizations
├── config.py                   # Stores reusable configurations and constants
├── utils.py                    # Provides helper functions for logging, file management, etc.
├── README.md                   # Project documentation
```

# Modules

1. **data_collection.py**  
   - Streams live tweets based on keywords or hashtags using the Twitter API.  
   - Saves collected tweets in a structured CSV format.

2. **data_preprocessing.py**  
   - Cleans tweet text by removing noise, URLs, and special characters.  
   - Tokenizes and normalizes text for downstream analysis.

3. **sentiment_analysis.py**  
   - Classifies tweets into positive, neutral, or negative sentiments using Vader or fine-tuned Transformer models.  
   - Outputs a sentiment-labeled dataset.

4. **trending_topics.py**  
   - Identifies trending keywords and hashtags using TF-IDF.  
   - Visualizes keyword frequency using bar charts.

5. **data_storage.py**  
   - Stores processed tweets into an SQLite database.  
   - Supports extensibility for cloud-based storage solutions.

6. **automation_pipeline.py**  
   - Orchestrates the complete social media analytics workflow.  
   - Ensures modular and automated execution of all components.

7. **visualization_dashboard.ipynb**  
   - Provides advanced visualizations such as sentiment distribution, tweet trends, and geographic insights.  
   - Saves visualizations as images for reporting.

8. **config.py**  
   - Centralized configuration file for API credentials, database paths, and constants.  
   - Ensures consistency and ease of updates.

9. **utils.py**  
   - Helper functions for logging, file management, and exception handling.  
   - Includes decorators for enhanced debugging.

---

# Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com
