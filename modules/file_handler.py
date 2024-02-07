import pandas as pd
from pprint import pprint

""" Returns rows containing search value in any column for any file
    Labeled FileHandler, but can be expanded to many more types. For
    now it explicitly processes CSV files.
 """


class FileHandler:
    def __init__(self, files):
        self._file_list = [
            items
            for items in files
            if isinstance(items, str) and items.endswith(".csv")
        ]

    def find_shared_value(self, value):
        VALUE = value
        tmp_store = []
        for file in self._file_list:
            df = pd.read_csv(file)
            if (df == VALUE).any().any():
                tmp_store.append(df[df.isin([VALUE]).any(axis=1)])
            else:
                print("Value does not exist in the CSV...")
                break

        DF_LIST = tmp_store
        return DF_LIST


if __name__ == "__main__":
    t_lst = [
        "websol/tmp_file/uploads/black_white_wage_gap.csv",
        "websol/tmp_file/uploads/MOCK_DATA.csv",
        "websol/tmp_file/uploads/MOCK_DATA_copy.csv",
    ]
    T = FileHandler(files=t_lst).find_shared_value("test")
    pprint(T)
