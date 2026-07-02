from app.vectorstore import VectorStore


# A small knowledge base with real, multi-sentence facts.
DOCUMENTS = [
    "The Great Wall of China is over 13,000 miles long. It was built over many centuries by different dynasties to protect against invasions from the north.",
    "Photosynthesis is the process by which plants convert sunlight into energy. It takes place in the chloroplasts and produces oxygen as a byproduct.",
    "The human heart has four chambers: two atria and two ventricles. It pumps blood throughout the body, beating about 100,000 times per day.",
    "Python is a high-level programming language known for its readable syntax. It is widely used in data science, web development, and automation.",
    "Mount Everest is the tallest mountain on Earth, standing at 8,849 meters. It is located in the Himalayas on the border between Nepal and Tibet.",
    "The Amazon rainforest produces about 20 percent of the world's oxygen. It is home to millions of species of plants, animals, and insects.",
]


def chunk_text(text, max_words=40):
    # Simple chunking: split long text into pieces of at most max_words words.
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunks.append(" ".join(words[i:i + max_words]))
    return chunks


def main():
    store = VectorStore()
    store.clear()

    print("Ingesting documents...")
    count = 0
    for doc in DOCUMENTS:
        for chunk in chunk_text(doc):
            store.add(chunk)
            count += 1

    print(f"Stored {count} chunks from {len(DOCUMENTS)} documents.")


if __name__ == "__main__":
    main()
