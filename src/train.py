import pandas as pd
import os
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

DATA_PATH = "data/processed/ratings_clean.csv"
MODEL_PATH = "models/recommender.pkl"

def train_model():
    """Train a simple User-User Collaborative Filtering model using cosine similarity."""

    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Create User-Movie ratings matrix
    user_item_matrix = df.pivot_table(index="userId", columns="movieId", values="rating").fillna(0)

    # Convert to sparse matrix for efficiency
    sparse_matrix = csr_matrix(user_item_matrix.values)

    # Compute cosine similarity between users
    user_similarity = cosine_similarity(sparse_matrix)

    # Save everything needed for recommendation
    model_data = {
        "user_item_matrix": user_item_matrix,
        "user_similarity": user_similarity
    }

    os.makedirs("models", exist_ok=True)
    joblib.dump(model_data, MODEL_PATH)
    print(f" User-User CF model trained and saved at {MODEL_PATH}")
    print(f"Matrix shape: {user_item_matrix.shape} (users x movies)")

    return model_data

if __name__ == "__main__":
    train_model()
