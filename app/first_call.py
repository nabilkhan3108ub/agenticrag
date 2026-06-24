from app.llm import llm


def main():
    prompt = "Explain what a vector embedding is in two simple sentences."
    print("PROMPT:", prompt)
    print("\nRESPONSE:")
    print(llm.generate(prompt))


if __name__ == "__main__":
    main()
