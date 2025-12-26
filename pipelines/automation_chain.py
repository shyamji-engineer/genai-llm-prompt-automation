from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from config import OLLAMA_MODEL

def automation_chain(prompt_file: str):
    llm = Ollama(model=OLLAMA_MODEL)

    with open(prompt_file) as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["input_text"],
        template=template
    )

    return prompt | llm
