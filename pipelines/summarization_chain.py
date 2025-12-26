from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from config import OLLAMA_MODEL

def summarization_chain():
    llm = OllamaLLM(model=OLLAMA_MODEL)

    with open("prompts/summarization.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["text"],
        template=template
    )

    return prompt | llm
