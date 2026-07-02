from app.rag import RAG


def main():
    rag = RAG()

    question = "How tall is Mount Everest and where is it?"
    print("QUESTION:", question)

    answer, chunks = rag.answer(question)

    print("\nRETRIEVED CONTEXT:")
    for c in chunks:
        print("  -", c)

    print("\nANSWER:")
    print(answer)


if __name__ == "__main__":
    main()
