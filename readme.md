## `README.md`

```markdown
# Movie Recommendation Pipeline

This project implements a **Movie Recommendation System** using the [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/).  
It demonstrates how to design a machine learning workflow: **ingestion → preprocessing → training → recommendation → orchestration** with Prefect.

---

## Project Structure
```

movie_recommendation_pipeline/
│── data/
│ ├── raw/ # original MovieLens files + converted CSVs
│ │ ├── ml-100k/ # original dataset
│ │ ├── ratings.csv # converted ratings
│ │ └── movies.csv # converted movies
│ └── processed/ # cleaned dataset (ratings_clean.csv)
│── models/ # trained recommender model (recommender.pkl)
│── notebooks/ # Jupyter notebooks for EDA
│── src/ # source code
│ ├── conversion.py # convert u.data/u.item → ratings.csv/movies.csv
│ ├── ingest.py # load ratings + movies
│ ├── transform.py # preprocess (filter users/movies)
│ ├── train.py # train User-User CF model
│ ├── recommend.py # generate recommendations
│ └── flow\.py # orchestrate pipeline with Prefect
│── db/ # (optional) database for storing recs
│── requirements.txt # dependencies
│── README.md # documentation
│── .gitignore # git ignore rules

````

---

##  Pipeline Workflow

1. **Convert Data**
   - Run `convert_ml100k.py` to generate `ratings.csv` and `movies.csv` from the raw `ml-100k` dataset.

2. **Ingest**
   - Loads `ratings.csv` and `movies.csv` → merges into one dataset.

3. **Transform**
   - Removes users with <5 ratings.
   - Removes movies with <20 ratings.
   - Saves clean dataset → `data/processed/ratings_clean.csv`.

4. **Train**
   - Builds a **User-User Collaborative Filtering** model using cosine similarity.
   - Saves trained model → `models/recommender.pkl`.

5. **Recommend**
   - Generates Top-N movie recommendations for a given `userId`.
   - Example: Top 5 movies for `userId=1`.

6. **Orchestration**
   - Prefect flow (`flow.py`) automates:
     ```
     convert → ingest → transform → train → recommend
     ```

---

##  Installation

```bash
git clone <your-repo-url>
cd movie_recommendation_pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt
````

---

## Usage

### Convert raw MovieLens data

```bash
python src/convert_ml100k.py
```

### Run full pipeline

```bash
python src/flow.py
```

### Run individual steps

```bash
python src/ingest.py
python src/transform.py
python src/train.py
python src/recommend.py
```

---

## Dataset

- **Name:** MovieLens 100k
- **Records:** 100,000 ratings
- **Users:** 943
- **Movies:** 1,682
- **Rating Scale:** 1–5

---

## Features

- End-to-end modular ML pipeline
- User-User Collaborative Filtering (cosine similarity)
- Prefect orchestration for automation
- Easily extendable to Item-Item CF, Matrix Factorization, or Deep Learning

---

## Future Work

- Implement Item-Item CF and Matrix Factorization (ALS, SVD++)
- Add content-based filtering (genres, release year)
- Hybrid recommender (collaborative + content-based)
- Store recommendations in SQLite/PostgreSQL
- Deploy with a simple Flask/FastAPI API

---
