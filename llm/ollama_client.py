import requests
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

def ollama_generate(prompt: str) -> str:
    url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    return response.json()["response"]
