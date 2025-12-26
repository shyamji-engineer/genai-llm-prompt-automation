from llm.hf_client import hf_local_generate

prompt = (
    "Explain in detail (5-6 sentences) why cyber security "
    "is a good career choice for the future."
)
print(hf_local_generate(prompt))
