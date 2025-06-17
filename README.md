# 🎬 Personalized Movie Recommendation System

This is a personalized recommendation system that ranks my Letterboxd watchlist based on my preferences, using machine learning and external metadata from TMDb.

## 🎯 Objective
Build a complete end-to-end data science project that demonstrates skills in data collection, cleaning, analysis, modeling, and deployment.

## ⚙️ Features
- Parses data from Letterboxd (`watched.csv` and `watchlist.csv`)
- Enriches metadata using the TMDb API (genres, popularity, ratings, etc.)
- Trains machine learning models to predict personal ratings
- Ranks watchlist films by predicted personal preference
- Optional deployment as an interactive web app (Streamlit)

## 🧰 Tech Stack
Python · Pandas · Scikit-Learn · XGBoost · Matplotlib · TMDb API · Streamlit

## 🗂️ Project Structure
```personalized-movie-recommendation-system/
├── data/
│ ├── raw/ <- Raw data from Letterboxd and TMDb
│ └── processed/ <- Cleaned and enriched data
├── notebooks/ <- Jupyter notebooks for analysis and modeling
├── src/ <- Core Python scripts (ETL, modeling, etc.)
│ ├── etl.py
│ ├── features.py
│ ├── model.py
│ └── recommend.py
├── app/ <- Streamlit or Gradio interface
│ └── app.py
├── requirements.txt
├── .env ← minha chave da TMDb
├── README.md
├── .venv
└── .gitignore```