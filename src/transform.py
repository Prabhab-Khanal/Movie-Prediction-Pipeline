import pandas as pd
import os

RATINGS_PATH = "data/raw/ratings.csv"
MOVIES_PATH = "data/raw/movies.csv"
OUT_PATH = "data/processed/ratings_clean.csv"

def transform_data():
    """Clean and filter MovieLens dataset for training recommender."""

    # Load data
    ratings = pd.read_csv(RATINGS_PATH)
    movies = pd.read_csv(MOVIES_PATH)

    # Merge ratings with movie titles
    df = ratings.merge(movies, on="movieId", how="left")

    # Drop timestamp (not needed for training)
    if "timestamp" in df.columns:
        df = df.drop(columns=["timestamp"])

    # Handle missing values in movie metadata
    df = df.dropna(subset=["title"])  # drop rows without movie title

    # Filter out movies with too few ratings (e.g., <20)
    movie_counts = df["movieId"].value_counts()
    df = df[df["movieId"].isin(movie_counts[movie_counts >= 20].index)]

    # Filter out users with too few ratings (e.g., <5)
    user_counts = df["userId"].value_counts()
    df = df[df["userId"].isin(user_counts[user_counts >= 5].index)]

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print(f"Saved processed dataset: {OUT_PATH}")
    print(f"Rows: {df.shape[0]}, Users: {df['userId'].nunique()}, Movies: {df['movieId'].nunique()}")

    return df

if __name__ == "__main__":
    transform_data()
