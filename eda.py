import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/cleaned_reviews.csv")

print(df.head())

# Sentiment Distribution
df["sentiment"].value_counts().plot(kind="bar")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()

# Rating Distribution

df["rating"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()

df.groupby("platform")["rating"].mean().plot(
    kind="bar"
)

plt.title("Average Rating by Platform")
plt.ylabel("Average Rating")

plt.show()

df.groupby("verified_purchase")["rating"].mean().plot(
    kind="bar"
)

plt.title("Verified vs Non-Verified Users")
plt.ylabel("Average Rating")

plt.show()