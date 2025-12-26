from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def gemini_generate(prompt: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-flash-latest",   # ✅ FIXED
        contents=prompt
    )
    return response.text
