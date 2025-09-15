import pandas as pd
import joblib
import numpy as np

MODEL_PATH = "models/recommender.pkl"
MOVIES_PATH = "data/raw/movies.csv"
DATA_PATH = "data/processed/ratings_clean.csv"

def recommend_movies(user_id, top_n=5):
    """Recommend Top-N movies for a given user using User-User CF."""

    # Load model + data
    model_data = joblib.load(MODEL_PATH)
    user_item_matrix = model_data["user_item_matrix"]
    user_similarity = model_data["user_similarity"]

    movies = pd.read_csv(MOVIES_PATH)
    ratings = pd.read_csv(DATA_PATH)

    # Check if user exists
    if user_id not in user_item_matrix.index:
        print(f" User {user_id} not found in dataset.")
        return

    # Find similar users
    user_index = user_item_matrix.index.get_loc(user_id)
    sim_scores = list(enumerate(user_similarity[user_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top similar users (excluding self)
    top_users = [i for i, score in sim_scores[1:11]]  # top 10 similar users

    # Movies the target user has already seen
    watched_movies = set(ratings[ratings["userId"] == user_id]["movieId"].tolist())

    # Candidate movies: from similar users but not watched
    candidate_movies = set()
    for u in top_users:
        similar_user_id = user_item_matrix.index[u]
        user_movies = ratings[ratings["userId"] == similar_user_id]["movieId"].tolist()
        candidate_movies.update(user_movies)

    candidate_movies -= watched_movies

    # Score candidates: average rating among top similar users
    scores = {}
    for movie in candidate_movies:
        score = ratings[
            (ratings["movieId"] == movie) &
            (ratings["userId"].isin(user_item_matrix.index[top_users]))
        ]["rating"].mean()
        if not np.isnan(score):
            scores[movie] = score

    # Sort and pick top N
    top_recs = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Map movie IDs to titles
    recs_df = pd.DataFrame(top_recs, columns=["movieId", "predicted_rating"])
    recs_df = recs_df.merge(movies, on="movieId", how="left")

    print(f"🎬 Top {top_n} recommendations for User {user_id}:")
    print(recs_df[["movieId", "title", "predicted_rating"]])

    return recs_df

if __name__ == "__main__":
    recommend_movies(user_id=1, top_n=5)
