import pandas as pd

RATINGS_PATH = "data/raw/ratings.csv"
MOVIES_PATH = "data/raw/movies.csv"

def ingest_data():
    """Load ratings and movies, merge into a single dataframe."""
    ratings = pd.read_csv(RATINGS_PATH)
    movies = pd.read_csv(MOVIES_PATH)

    df = ratings.merge(movies, on="movieId", how="left")
    print(f" Ingested data: {df.shape[0]} rows, {df.shape[1]} columns")
    print(df.head())
    return df

if __name__ == "__main__":
    ingest_data()
