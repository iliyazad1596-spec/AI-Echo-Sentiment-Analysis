import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/processed/final_reviews.csv")

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(df["clean_review"])

encoder = LabelEncoder()

y = encoder.fit_transform(df["sentiment"])

model = LogisticRegression(max_iter=1000)

model.fit(X, y)

joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")

print("Model saved successfully!")