from pipelines import summarization_chain
from utils.file_utils import read_file, write_file



def auto_summarize(input_path: str, output_path: str):
    text = read_file(input_path)

    chain = summarization_chain()
    summary = chain.invoke({"text": text})

    write_file(output_path, summary)
    print("✅ Summary saved to:", output_path)


if __name__ == "__main__":
    auto_summarize(
        input_path="data/sample_text.txt",
        output_path="outputs/summaries/summary.txt"
    )
