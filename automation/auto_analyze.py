from pipelines import summarization_chain
from utils.file_utils import read_file, write_file


def auto_analyze(input_path: str, output_path: str):
    text = read_file(input_path)

    chain = analysis_chain()
    analysis = chain.invoke({"text": text})

    write_file(output_path, analysis)
    print("✅ Analysis saved to:", output_path)


if __name__ == "__main__":
    auto_analyze(
        input_path="data/sample_text.txt",
        output_path="outputs/results.txt"
    )
