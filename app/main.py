import os

from utils.extractor import Extractor


CONSOLES_FILE_PATH = os.getenv("CONSOLES_FILE_PATH", "data/consoles.csv")
RESULT_FILE_PATH = os.getenv("RESULT_FILE_PATH", "data/result.csv")
OUTPUT_FOLDER = os.getenv("CONSOLES_FILE_PATH", "results")


def main():
    # Extract the data from the files
    extractor = Extractor(
        console_file_path=CONSOLES_FILE_PATH, result_file_path=RESULT_FILE_PATH
    )
    consoles_df, result_df = extractor.get_data()

    data = result_df.merge(consoles_df, how='inner', on='console')

    data.info()

    



if __name__ == "__main__":
    main()
