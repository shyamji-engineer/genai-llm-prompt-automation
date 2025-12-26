from pipelines import text_generation_chain

if __name__ == "__main__":
    chain = text_generation_chain()

    prompt = "Explain what Generative AI is in simple terms."

    result = chain.invoke({"text": prompt})
    print("\nGenerated Output:\n")
    print(result)
