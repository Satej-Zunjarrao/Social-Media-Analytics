\\
# Visualization Dashboard

This Jupyter Notebook creates additional visualizations for the social media analytics project. It provides detailed insights into sentiment distribution, tweet trends, and geographic distribution.

**Author**: Satej
\\
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load sentiment analysis results
sentiment_file = "./processed_tweets/sentiment_results.csv"
data = pd.read_csv(sentiment_file)

# Quick overview of the data
print("Data Overview:")
print(data.head())
print(f"Total records: {data.shape[0]}")
# Sentiment distribution plot
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x="sentiment", palette="viridis")
plt.title("Sentiment Distribution", fontsize=16)
plt.xlabel("Sentiment", fontsize=12)
plt.ylabel("Tweet Count", fontsize=12)
plt.tight_layout()
plt.savefig("./visualizations/sentiment_distribution.png")
plt.show()
# Convert 'created_at' column to datetime if necessary
if not pd.api.types.is_datetime64_any_dtype(data["created_at"]):
    data["created_at"] = pd.to_datetime(data["created_at"])

# Plot tweet volume over time
data["date"] = data["created_at"].dt.date
tweet_volume = data.groupby("date").size()

plt.figure(figsize=(10, 6))
tweet_volume.plot(kind="line", marker="o", color="blue")
plt.title("Tweet Volume Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Tweets", fontsize=12)
plt.grid()
plt.tight_layout()
plt.savefig("./visualizations/tweet_volume.png")
plt.show()

# Geographic distribution (top 10 locations)
top_locations = data["location"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y=top_locations.index, x=top_locations.values, palette="magma")
plt.title("Top 10 Tweet Locations", fontsize=16)
plt.xlabel("Tweet Count", fontsize=12)
plt.ylabel("Location", fontsize=12)
plt.tight_layout()
plt.savefig("./visualizations/top_locations.png")
plt.show()

# Display trending topics image
from IPython.display import Image, display

trending_topics_image_path = "./visualizations/trending_topics.png"
display(Image(filename=trending_topics_image_path))

\\\

---

### Key Features:
1. **`config.py`**:
   - Centralized configuration for all project settings.
   - Ensures consistency and ease of updates.

2. **`visualization_dashboard.ipynb`**:
   - Provides in-depth visualizations.
   - Well-documented with explanations and visual examples.
   - Automatically saves visual outputs to the project folder for reuse.

Let me know if you'd like additional features or further adjustments!

\\\

