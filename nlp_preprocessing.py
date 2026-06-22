import pandas as pd
import re
import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

df = pd.read_csv("data/processed/cleaned_reviews.csv")

stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r'[^a-zA-Z ]', '', text)

    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(words)

df["clean_review"] = df["review"].apply(clean_text)

print(df[["review","clean_review"]].head())

df.to_csv(
    "data/processed/final_reviews.csv",
    index=False
)

print("Text preprocessing completed!")