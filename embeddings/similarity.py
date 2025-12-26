import numpy as np
from embeddings.embedding_model import get_embedding

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == "__main__":
    text1 = "Large Language Models are powerful AI systems used for natural language understanding."
    text2 = "LLMs are powerful artificial intelligence models designed for natural language processing."

    e1 = get_embedding(text1)
    e2 = get_embedding(text2)

    print("Similarity:", cosine_similarity(e1, e2))
