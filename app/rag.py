from app.vectorstore import VectorStore
from app.llm import llm


class RAG:
    """The core RAG pipeline: retrieve relevant chunks, then generate an
    answer grounded in them. Ties together the vector store and the LLM.
    """

    def __init__(self):
        self.store = VectorStore()

    def build_prompt(self, question, chunks):
        # Assemble retrieved chunks into context, then instruct the model to
        # answer using ONLY that context. This is what makes the answer grounded.
        context = "\n".join(f"- {c}" for c in chunks)
        return (
            "You are a helpful assistant. Answer the question using ONLY the "
            "context below. If the context does not contain the answer, say "
            "you do not have enough information.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\n\n"
            "Answer:"
        )

    def answer(self, question, top_k=3):
        # 1. Retrieve the most relevant chunks
        results = self.store.search(question, top_k=top_k)
        chunks = [content for content, distance in results]

        # 2. Build a prompt that includes them
        prompt = self.build_prompt(question, chunks)

        # 3. Ask the LLM to generate a grounded answer
        response = llm.generate(prompt)

        return response, chunks
