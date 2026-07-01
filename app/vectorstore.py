import psycopg
from pgvector.psycopg import register_vector
from app.config import config
from app.embeddings import embedder


class VectorStore:
    def __init__(self):
        self.conn = psycopg.connect(config.db_url())
        self._setup()

    def _setup(self):
        self.conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        register_vector(self.conn)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chunks (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                embedding vector(384)
            )
            """
        )
        self.conn.commit()

    def add(self, text):
        vec = embedder.embed(text)
        self.conn.execute(
            "INSERT INTO chunks (content, embedding) VALUES (%s, %s)",
            (text, vec),
        )
        self.conn.commit()

    def search(self, query, top_k=3):
        vec = embedder.embed(query)
        result = self.conn.execute(
            "SELECT content, embedding <=> %s AS distance FROM chunks ORDER BY distance LIMIT %s",
            (vec, top_k),
        ).fetchall()
        return result

    def clear(self):
        self.conn.execute("DELETE FROM chunks")
        self.conn.commit()
