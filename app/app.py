import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

from nltk.corpus import stopwords
from textblob import TextBlob

# Load Dataset
base_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    base_dir,
    "..",
    "data",
    "processed",
    "final_reviews.csv"
)

df = pd.read_csv(csv_path)

# Page Title
st.title("AI Echo - Sentiment Analysis Dashboard")

# ----------------------------------
# Sentiment Prediction Section
# ----------------------------------

st.header("Predict Review Sentiment")

user_review = st.text_area("Enter a Review")

if st.button("Predict Sentiment"):

    if user_review.strip() == "":
        st.warning("Please enter a review.")

    else:

        analysis = TextBlob(user_review)

        score = analysis.sentiment.polarity

        if score > 0.5:
            sentiment = "Positive"

        elif score < -0.5:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        st.success(f"Predicted Sentiment: {sentiment}")

# ----------------------------------
# Sentiment Distribution
# ----------------------------------

st.header("Sentiment Distribution")

fig1, ax1 = plt.subplots()

df["sentiment"].value_counts().plot(
    kind="bar",
    ax=ax1
)

ax1.set_xlabel("Sentiment")
ax1.set_ylabel("Count")

st.pyplot(fig1)

# ----------------------------------
# Rating Distribution
# ----------------------------------

st.header("Rating Distribution")

fig2, ax2 = plt.subplots()

df["rating"].value_counts().sort_index().plot(
    kind="bar",
    ax=ax2
)

ax2.set_xlabel("Rating")
ax2.set_ylabel("Count")

st.pyplot(fig2)

# ----------------------------------
# Average Rating by Platform
# ----------------------------------

st.header("Average Rating by Platform")

fig3, ax3 = plt.subplots()

df.groupby("platform")["rating"].mean().plot(
    kind="bar",
    ax=ax3
)

ax3.set_ylabel("Average Rating")

st.pyplot(fig3)

# ----------------------------------
# Verified vs Non-Verified Users
# ----------------------------------

st.header("Verified vs Non-Verified Users")

fig4, ax4 = plt.subplots()

df.groupby("verified_purchase")["rating"].mean().plot(
    kind="bar",
    ax=ax4
)

ax4.set_ylabel("Average Rating")

st.pyplot(fig4)
