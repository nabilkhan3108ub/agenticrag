from sentence_transformers import SentenceTransformer


class Embedder:
    """Turns text into vectors using a local model (no API, fully free).

    The model is downloaded once on first use and cached locally. We wrap it
    in a class for the same reason as the LLM client: the rest of the app
    depends on our interface, not on sentence-transformers directly.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, text: str):
        return self.model.encode(text)

    def embed_many(self, texts: list):
        return self.model.encode(texts)


embedder = Embedder()
