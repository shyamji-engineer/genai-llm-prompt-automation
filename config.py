import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-r1:1.5b")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")