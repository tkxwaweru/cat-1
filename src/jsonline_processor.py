# A class to convert the jsonl files from the dataset to excel files

import os
import jsonlines
import pandas as pd
import data


class JsonlProcessor:
    def __init__(self, jsonl_folder, output_excel_folder):
        self.jsonl_folder = jsonl_folder
        self.output_excel_folder = output_excel_folder

    def convert_jsonl_to_excel(self, jsonl_file):
        data = []
        with jsonlines.open(jsonl_file) as reader:
            for item in reader:
                data.append(
                    {
                        "id": item.get("id", ""),
                        "utt": item.get("utt", ""),
                        "annot_utt": item.get("annot_utt", ""),
                    }
                )

        df = pd.DataFrame(data)

        file_name = os.path.splitext(os.path.basename(jsonl_file))[0]
        excel_file_path = os.path.join(self.output_excel_folder, f"{file_name}.xlsx")

        df.to_excel(excel_file_path, index=False, engine="openpyxl")

    def process_jsonl_files(self):
        os.makedirs(self.output_excel_folder, exist_ok=True)
        for root, _, files in os.walk(self.jsonl_folder):
            for file in files:
                if file.endswith(".jsonl"):
                    jsonl_file_path = os.path.join(root, file)
                    self.convert_jsonl_to_excel(jsonl_file_path)
