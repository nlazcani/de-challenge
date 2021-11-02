import os

from utils.extractor import Extractor
from utils.report import generate_reports


CONSOLES_FILE_PATH = os.getenv("CONSOLES_FILE_PATH", "data/consoles.csv")
RESULT_FILE_PATH = os.getenv("RESULT_FILE_PATH", "data/result.csv")
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "data/")


def main():
    # Extract the data from the files
    extractor = Extractor(
        console_file_path=CONSOLES_FILE_PATH, result_file_path=RESULT_FILE_PATH
    )
    consoles_df, result_df = extractor.get_data()

    data = result_df.merge(consoles_df, how="inner", on="console")

    generate_reports(data, OUTPUT_FOLDER)


if __name__ == "__main__":
    main()
