-- Ativa a extensão vector
CREATE EXTENSION IF NOT EXISTS vector;

-- Cria a tabela movies
CREATE TABLE IF NOT EXISTS movies (
    id BIGSERIAL PRIMARY KEY,
    movie TEXT,
    release_year TEXT,
    genres TEXT,
    overview TEXT,
    keywords TEXT,
    movie_data TEXT,
    embedding VECTOR(768)
);