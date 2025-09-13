import psycopg2
import pandas as pd
from sentence_transformers import SentenceTransformer
from pgvector.psycopg2 import register_vector
from psycopg2.extras import execute_values
from tqdm import tqdm
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

start_time = time.time()

# Conexão com PostgreSQL
conn = psycopg2.connect("dbname=DB_cinebot user=user_application password=123 host=localhost")
register_vector(conn)
cur = conn.cursor()

# Carrega o modelo
model = SentenceTransformer('BAAI/bge-base-en-v1.5', device='cpu')

# Carrega o dataset
df = pd.read_csv("data/datasets/treated_dataset.csv")

# Define o tamanho do lote
batch_size = 500
data_batch = []

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    movie_data = row["movie_data"]
    embedding = model.encode(movie_data, normalize_embeddings=True)  # Gerar embedding

    data_batch.append((
        row["movie"],
        row["release_year"],
        row["overview"],
        row["genres"],
        row["keywords"],
        row["movie_data"],
        embedding
    ))

    # Executa a inserção do lote
    if len(data_batch) >= batch_size:
        execute_values(
            cur,
            """
            INSERT INTO movies (
                movie, release_year, overview,
                genres, keywords, movie_data, embedding
            ) VALUES %s
            """,
            data_batch
        )
        conn.commit()
        data_batch = []

# Insere quaisquer dados restantes
if data_batch:
    execute_values(
        cur,
        """
        INSERT INTO movies (
            movie, release_year, overview,
            genres, keywords, movie_data, embedding
        ) VALUES %s
        """,
        data_batch
    )
    conn.commit()

# Cria o índice HNSW caso não existir
cur.execute("""
    CREATE INDEX IF NOT EXISTS movies_embedding_hnsw 
    ON movies 
    USING hnsw (embedding vector_cosine_ops) 
    WITH (m = 16, ef_construction = 64);
""")

conn.commit()
cur.close()
conn.close()

end_time = time.time()
logging.info(f"\n\nTempo de execução: {end_time - start_time:.2f} segundos\n\n")