import pandas as pd
import magic
import os
import json
from pprint import pprint

""" Returns rows containing search value in any column for any file
    Labeled FileHandler, but can be expanded to many more types. For
    now it explicitly processes CSV files.
 """


class FileHandler:

    os.makedirs("temp_files", exist_ok=True)

    def csv_df(self, csv_path):
        return pd.read_csv(csv_path)

    def sql_df(self, query, conn):
        return pd.read_sql(query, conn)

    # Get a list of files from file input through web
    def get_files(self, files):
        self._file_list = [
            self.validate_files(items)
            for items in files
            if isinstance(items, str) and items.endswith(".csv")
        ]
        return self._file_list

    # Given csv file input on web, validate files are .csv
    def validate_files(self, file):
        try:
            _mime = magic.Magic(mime=True).from_buffer(file.read())
            if not _mime == "text/csv":
                print("Invalid file type.\n")
            return file
        except Exception as e:
            return e

    # Given a value, return a df list of df rows containing value
    def csv_find_shared_value(self, value):
        VALUE = value
        tmp_store = []
        for file in self._file_list:
            df = pd.read_csv(file)
            if (df == VALUE).any().any():
                tmp_store.append(df[df.isin([VALUE]).any(axis=1)])
            else:
                print(f"Value does not exist in {file}...\n")
                break
        DF_LIST = tmp_store
        return DF_LIST

    # Generates CSV/Returns DF of rows containing a KEY in any row
    def get_rows_for_key(self, key, csv):
        KEY, CSV = key, self.csv_df(csv)
        NEW_DF = CSV[CSV.isin([KEY]).any(axis=1)]
        NEW_DF.to_csv("temp_files/test.csv")
        return NEW_DF

    def parse_csv_to_json(self, csv):
        CSV = self.csv_df(csv)
        JSON_OUT = CSV.to_json("json_test.json")
        return JSON_OUT

    def serialize_csv_to_object(self, csv):
        CSV = self.csv_df(csv)
        JSON_F = CSV.to_json(default_handler=dict)
        with open("json_test.json", "r") as file:
            json_f = json.load(file)
            # pprint(json_f)
            NEW_DICT = {
                {
                    "country_code": json_f["code"]["0"],
                    "continent": json_f["code"]["1"],
                    "name": json_f["code"]["2"],
                },
            }

            pprint(NEW_DICT)

    def pivot_csv_to_object(self, csv):
        CSV = self.csv_df(csv)


if __name__ == "__main__":
    t_lst = [
        "test_files/countries.csv",
        "test_files/persons.csv",
    ]
    t = FileHandler()
    t.get_rows_for_key("north america", t_lst[0])
    t.parse_csv_to_json(t_lst[0])
    t.serialize_csv_to_object(t_lst[0])
