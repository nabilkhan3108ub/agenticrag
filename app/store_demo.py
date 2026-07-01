from app.vectorstore import VectorStore


def main():
    store = VectorStore()
    store.clear()
    chunks = [
        "Dogs are loyal animals and popular household pets.",
        "Puppies are baby dogs that need training and care.",
        "Airplanes use jet engines to fly across long distances.",
        "The Eiffel Tower is a famous landmark located in Paris.",
        "Python is a programming language used in data science.",
    ]
    print("Storing chunks in the database...")
    for c in chunks:
        store.add(c)
    query = "Tell me about dogs"
    print("Query:", query)
    results = store.search(query, top_k=3)
    print("Top matches (lower distance = more relevant):")
    for content, distance in results:
        print("  [", round(float(distance), 3), "] ", content)


if __name__ == "__main__":
    main()
