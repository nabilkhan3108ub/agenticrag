import numpy as np
from app.embeddings import embedder


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def main():
    sentences = [
        "A dog is a loyal pet.",
        "Puppies are young dogs.",
        "The airplane flew across the ocean.",
    ]
    print("Embedding sentences...")
    vectors = [embedder.embed(s) for s in sentences]
    print("Each sentence became a vector of", len(vectors[0]), "numbers.")
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            sim = cosine_similarity(vectors[i], vectors[j])
            print("Similarity:", round(float(sim), 3))
            print("  ", sentences[i])
            print("  ", sentences[j])


if __name__ == "__main__":
    main()
