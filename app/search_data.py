import psycopg2
from sentence_transformers import SentenceTransformer
from pgvector.psycopg2 import register_vector

def search_answer(query: str) -> str:

    #Conexão com PostgreSQL
    conn = psycopg2.connect("dbname=DB_cinebot user=user_application password=123 host=localhost")
    register_vector(conn)
    cur = conn.cursor()

    #Carrega o modelo de embeddings
    model = SentenceTransformer('BAAI/bge-base-en-v1.5', device='cpu')

    #Gera o embedding da consulta
    query_embedding = model.encode(query, normalize_embeddings=True)

    #Faz a busca semântica
    cur.execute('''
        SELECT
            movie,
            release_year,
            overview,
            genres,
            keywords,
            movie_data,
            embedding <=> %s AS distance
        FROM movies
        ORDER BY embedding <=> %s
        LIMIT 1
    ''', (query_embedding, query_embedding))

    #Mostra os resultados
    result = cur.fetchone()

    movie = f"""
    Movie: {result[0]}
    Release year: {result[1]}
    Overview: {result[2]}
    Genres: {result[3]}
    """
    #Fecha a conexão
    cur.close()
    conn.close()

    return movie