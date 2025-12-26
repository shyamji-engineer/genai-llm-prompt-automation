from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from config import OLLAMA_MODEL

def analysis_chain():
    llm = OllamaLLM(model=OLLAMA_MODEL)

    with open("prompts/analysis.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["text"],
        template=template
    )

    return prompt | llm
