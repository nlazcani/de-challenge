import pandas as pd

class Extractor:
    def __init__(self, console_file_path, result_file_path):
        self.console_file_path = console_file_path
        self.result_file_path = result_file_path

    def get_data(self):
        console_df = pd.read_csv(self.console_file_path)
        console_df = console_df.dropna(axis=0, how='any')
        console_df = console_df.drop_duplicates(keep='first')
        result_df = pd.read_csv(self.result_file_path)
        result_df = result_df.dropna(axis=0, how='any')
        result_df = result_df.drop_duplicates(keep='first')
        return console_df, result_df