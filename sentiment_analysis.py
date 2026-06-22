import pandas as pd

df = pd.read_excel("data/raw/chatgpt_style_reviews_dataset.xlsx")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())
def sentiment_label(rating):

    if rating >= 4:
        return "Positive"

    elif rating == 3:
        return "Neutral"

    else:
        return "Negative"


df["sentiment"] = df["rating"].apply(sentiment_label)

print(df[["rating", "sentiment"]].head())
df.to_csv(
    "data/processed/cleaned_reviews.csv",
    index=False
)

print("Cleaned dataset saved successfully!")