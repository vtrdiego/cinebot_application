import pandas as pd

# Carregar o dataset original
df = pd.read_csv('data/datasets/TMDB_movie_dataset_v11.csv')  # Substitua pelo caminho correto do seu arquivo

# Substituir valores nulos por 'unknown'
df = df.fillna('unknown')

# Padronizar os dados: tudo em minúsculo e remover espaços em branco
df = df.map(lambda x: x.strip().lower() if isinstance(x, str) else x)

# Renomear colunas
df = df.rename(columns={
    'title': 'movie',
    'release_date': 'release_year'
})

# Extrair apenas o ano da coluna release_year
df['release_year'] = df['release_year'].str[:4]

# Filtrar apenas os filmes com release_year a partir de 1990
df = df[df['release_year'].astype(str).str.isnumeric()]  # Garantir que o ano é numérico
df = df[df['release_year'].astype(int) >= 1990]

# Criar a nova coluna 'movie_data'
df['movie_data'] = (
    df['movie'] + " is an " + df['genres'] +
    " movie released in " + df['release_year'] +
    " that features themes such as " + df['keywords'] + "."
)

# Reordenar as colunas
df_final = df[['movie', 'release_year', 'overview', 'genres', 'keywords', 'movie_data']]

# Salvar o novo dataset tratado
df_final.head(20).to_csv('data/datasets/treated_dataset.csv', index=False)