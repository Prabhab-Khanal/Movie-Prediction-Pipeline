import pandas as pd
import os

RAW_DIR = "data/raw/ml-100k"
OUT_DIR = "data/raw"

def convert_movielens():
    # 1. Convert ratings
    ratings_path = os.path.join(RAW_DIR, "u.data")
    ratings = pd.read_csv(ratings_path, sep="\t",
                          names=["userId","movieId","rating","timestamp"])
    ratings.to_csv(os.path.join(OUT_DIR, "ratings.csv"), index=False)

    # 2. Convert movies
    movies_path = os.path.join(RAW_DIR, "u.item")
    movies = pd.read_csv(movies_path, sep="|", encoding="latin-1", header=None,
                         usecols=[0,1,2], names=["movieId","title","release_date"])
    movies.to_csv(os.path.join(OUT_DIR, "movies.csv"), index=False)

    print(" Conversion complete!")
    print(f"Ratings saved to {OUT_DIR}/ratings.csv")
    print(f"Movies saved to {OUT_DIR}/movies.csv")

if __name__ == "__main__":
    convert_movielens()
