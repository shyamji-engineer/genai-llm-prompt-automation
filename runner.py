"""
runner.py

Interactive runner for GenAI experiments.
Allows:
- Model selection (Ollama / Gemini / Hugging Face)
- Input selection (Manual text / File input)
"""

import sys
from utils.file_utils import read_file


# ------------------------
# Input handlers
# ------------------------

def get_manual_input():
    print("\nEnter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


def get_file_input():
    path = input("\nEnter file path: ").strip()
    try:
        return read_file(path)
    except Exception as e:
        print("Error reading file:", e)
        sys.exit(1)


def get_input_text():
    print("\nSelect Input Type:")
    print("1. Manual text")
    print("2. File input")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        return get_manual_input()
    elif choice == "2":
        return get_file_input()
    else:
        print("Invalid input choice")
        sys.exit(1)


# ------------------------
# Model runners
# ------------------------

def run_ollama(text):
    from pipelines import text_generation_chain

    chain = text_generation_chain()
    return chain.invoke({"text": text})


def run_gemini(text):
    from llm.gemini_client import gemini_generate

    return gemini_generate(text)


def run_hf(text):
    from llm.hf_client import hf_local_generate

    return hf_local_generate(text)


# ------------------------
# Main runner
# ------------------------

def main():
    print("\n=== GenAI Experiment Runner ===\n")
    print("Select LLM Model:")
    print("1. Ollama (Local)")
    print("2. Gemini (Cloud)")
    print("3. Hugging Face (Local)")

    model_choice = input("Enter choice (1/2/3): ").strip()

    text = get_input_text()

    print("\n--- Generating Output ---\n")

    if model_choice == "1":
        output = run_ollama(text)
        print("[OLLAMA OUTPUT]\n")
        print(output)

    elif model_choice == "2":
        output = run_gemini(text)
        print("[GEMINI OUTPUT]\n")
        print(output)

    elif model_choice == "3":
        output = run_hf(text)
        print("[HUGGING FACE OUTPUT]\n")
        print(output)

    else:
        print("Invalid model choice")
        sys.exit(1)


if __name__ == "__main__":
    main()
