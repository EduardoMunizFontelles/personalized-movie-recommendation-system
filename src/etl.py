# Extract, Transform and Load
import os
import pandas as pd
from tmdbv3api import TMDb, Movie
from dotenv import load_dotenv

# 🔐 Carrega API Key
load_dotenv()
tmdb = TMDb()
tmdb.api_key = os.getenv("TMDB_API_KEY")
tmdb.language = "en"
tmdb.debug = True

movie_api = Movie()

# 🔍 Função para buscar metadados da TMDb (ajustada)
def get_tmdb_metadata(row):
    title = row['Name']
    year = int(row['Year'])

    try:
        results = movie_api.search(title)
        if results:
            # 🔎 Busca filme com ano exato
            movie = next(
                (m for m in results if m.release_date and m.release_date.startswith(str(year))),
                results[0]  # fallback
            )
            details = movie_api.details(movie.id)
            credits = movie_api.credits(movie.id)

            genres = ', '.join([genre['name'] for genre in details.get('genres', [])])
            director = next((p['name'] for p in credits.get('crew', []) if p['job'] == 'Director'), None)
            lead_actor = credits.get('cast', [{}])[0].get('name')

            return {
                'duration_min': details.get('runtime'),
                'genres': genres,
                'director': director,
                'lead_actor': lead_actor,
                'vote_average': details.get('vote_average'),
                'budget': details.get('budget'),
                'revenue': details.get('revenue'),
                'release_date': details.get('release_date')
            }

    except Exception as e:
        print(f"[Erro] {title} ({year}): {e}")
    return {}

# 📥 Lê os CSVs do Letterboxd
watched_df = pd.read_csv("data/raw/watched.csv")[['Name', 'Year', 'Rating']]
watchlist_df = pd.read_csv("data/raw/watchlist.csv")[['Name', 'Year']]

# 🔗 Enriquecimento com checagem por ano
print("🔎 Enriquecendo filmes assistidos...")
watched_meta = watched_df.apply(get_tmdb_metadata, axis=1).apply(pd.Series)
watched_enriched = pd.concat([watched_df, watched_meta], axis=1)

print("🔎 Enriquecendo filmes da watchlist...")
watchlist_meta = watchlist_df.apply(get_tmdb_metadata, axis=1).apply(pd.Series)
watchlist_enriched = pd.concat([watchlist_df, watchlist_meta], axis=1)

# 💾 Salva os novos arquivos
watched_enriched.to_csv("data/processed/watched_enriched.csv", index=False)
watchlist_enriched.to_csv("data/processed/watchlist_enriched.csv", index=False)

print("✅ Enriquecimento concluído com sucesso!")

