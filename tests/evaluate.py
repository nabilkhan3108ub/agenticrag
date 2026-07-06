from app.vectorstore import VectorStore
from tests.eval_data import TEST_SET


def hit_rate_at_k(store, top_k):
    """Fraction of test questions where the correct chunk (identified by its
    expected keyword) appears within the top_k retrieved results.
    """
    hits = 0
    misses = []
    for item in TEST_SET:
        question = item["question"]
        keyword = item["expected_keyword"]
        results = store.search(question, top_k=top_k)
        retrieved = [content for content, distance in results]
        hit = any(keyword.lower() in chunk.lower() for chunk in retrieved)
        if hit:
            hits += 1
        else:
            misses.append(question)
    return hits, misses


def evaluate(k_values=(1, 3, 5)):
    store = VectorStore()
    total = len(TEST_SET)

    print("Retrieval evaluation across k values")
    print("Test set size:", total)
    print("")
    print("  k    hit rate")
    print("  --   --------")

    for k in k_values:
        hits, misses = hit_rate_at_k(store, k)
        rate = hits / total
        print("  " + str(k) + "    " + str(hits) + "/" + str(total) + "  = " + str(round(rate * 100, 1)) + "%")
        if misses:
            for m in misses:
                print("         miss:", m)

    print("")
    print("Note: higher k usually raises hit rate but feeds more (and noisier)")
    print("context to the LLM. The goal is the smallest k with strong hit rate.")


if __name__ == "__main__":
    evaluate()
