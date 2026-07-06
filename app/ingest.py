from app.vectorstore import VectorStore


# Harder knowledge base: many chunks on OVERLAPPING topics, so retrieval must
# distinguish between similar options instead of picking the one obvious match.
DOCUMENTS = [
    # Multiple mountains (overlapping topic)
    "Mount Everest is the tallest mountain on Earth at 8,849 meters. It sits in the Himalayas on the Nepal-Tibet border.",
    "K2 is the second-highest mountain in the world at 8,611 meters. It is considered far more dangerous to climb than Everest.",
    "Mount Kilimanjaro is the highest mountain in Africa at 5,895 meters. Unlike Everest, it is a free-standing volcano in Tanzania.",

    # Multiple programming languages (overlapping topic)
    "Python is a high-level language praised for readable syntax. It dominates data science, machine learning, and automation work.",
    "JavaScript is the language of the web browser. It powers interactive front-end websites and, via Node, back-end servers too.",
    "Rust is a systems programming language focused on memory safety without a garbage collector. It is popular for performance-critical software.",

    # Multiple body organs (overlapping topic)
    "The human heart has four chambers and pumps blood through the body. It beats around 100,000 times per day.",
    "The human liver filters toxins from the blood and produces bile for digestion. It is the largest internal organ.",
    "The lungs exchange oxygen and carbon dioxide with the blood. An adult breathes about 20,000 times a day.",

    # A few singletons with tricky phrasing
    "Photosynthesis lets plants turn sunlight into chemical energy inside chloroplasts, releasing oxygen as a byproduct.",
    "The Amazon rainforest generates roughly 20 percent of Earth's oxygen and shelters millions of species.",
    "The Great Wall of China stretches over 13,000 miles and was built across centuries to repel northern invaders.",
]


def chunk_text(text, max_words=40):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


def main():
    store = VectorStore()
    store.clear()
    print("Ingesting documents...")
    count = 0
    for doc in DOCUMENTS:
        for chunk in chunk_text(doc):
            store.add(chunk)
            count += 1
    print("Stored", count, "chunks from", len(DOCUMENTS), "documents.")


if __name__ == "__main__":
    main()
