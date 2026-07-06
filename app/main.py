from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import RAG

app = FastAPI(title="AgenticRAG API")
rag = RAG()


class Query(BaseModel):
    question: str
    top_k: int = 3


@app.get("/")
def health():
    return {"status": "ok", "service": "AgenticRAG"}


@app.post("/ask")
def ask(query: Query):
    answer, chunks = rag.answer(query.question, top_k=query.top_k)
    return {
        "question": query.question,
        "answer": answer,
        "sources": chunks,
    }
