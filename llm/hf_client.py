"""
Hugging Face Client

This module demonstrates Hugging Face usage in two ways:
1. Local inference using Transformers (stable, default)
2. Optional cloud inference using HF Inference API (experimental)
"""

from transformers import pipeline
from config import HF_API_TOKEN

# -----------------------------
# 1️⃣ HF LOCAL TEXT GENERATION
# -----------------------------

# Small, instruction-tuned, <1GB
_local_generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-small",
    device=-1  # CPU
)

def hf_local_generate(prompt: str) -> str:
    """
    Hugging Face local instruction-based text generation.
    Stable, small model (<1GB).
    """
    result = _local_generator(
        prompt,
        max_new_tokens=150
    )
    return result[0]["generated_text"]


# ------------------------------------------------
# 2️⃣ HF CLOUD API (OPTIONAL / UNSTABLE - NOT USED)
# ------------------------------------------------
"""
import requests

HF_API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def hf_api_generate(prompt: str) -> str:
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()[0]["generated_text"]
"""
