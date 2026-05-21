import pandas as pd

# YOUR SCRAPED DATA
custom_df = pd.read_csv(
    "bollywood_movies_reviews_2024_2026.csv"
)

# KAGGLE DATA
kaggle_df = pd.read_csv(
    "IMDB Dataset.csv"
)

# Rename columns
kaggle_df = kaggle_df.rename(columns={
    "review": "Review",
    "sentiment": "Sentiment"
})

# Keep only needed columns
kaggle_df = kaggle_df[["Review", "Sentiment"]]

# Add sentiment column to your dataset
custom_df["Sentiment"] = "positive"

# Keep same columns
custom_df = custom_df[["Review", "Sentiment"]]

# Combine
final_df = pd.concat(
    [custom_df, kaggle_df],
    ignore_index=True
)

# Save
final_df.to_csv(
    "final_dataset.csv",
    index=False
)

print(final_df.head())

print(final_df.shape)

print("FINAL DATASET READY")