import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import torch
from transformers import AutoTokenizer, AutoModel

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
_model = AutoModel.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)

def get_embedding(text: str):
    inputs = _tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():
        outputs = _model(**inputs)

    # Mean pooling
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings[0].numpy()
