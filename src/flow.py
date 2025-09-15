from prefect import flow, task
from ingest import ingest_data
from transform import transform_data
from train import train_model
from recommend import recommend_movies

@task
def ingest_task():
    return ingest_data()

@task
def transform_task():
    return transform_data()

@task
def train_task():
    return train_model()

@task
def recommend_task():
    return recommend_movies(user_id=1, top_n=5)

@flow(name="Movie Recommendation Pipeline")
def movie_pipeline():
    print(" Starting Movie Recommendation Pipeline")
    ingest_task()
    transform_task()
    train_task()
    recommend_task()
    print(" Pipeline finished!")

if __name__ == "__main__":
    movie_pipeline()
