# A class to process translations from english to the other languages of the dataset

import os
import pandas as pd


class LanguageProcessor:
    def __init__(self, input_folder, output_folder, en_us_code="en-US"):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.en_us_code = en_us_code

    def process_languages(self):
        os.makedirs(self.output_folder, exist_ok=True)
        en_us_data = pd.read_excel(
            os.path.join(self.input_folder, f"{self.en_us_code}.xlsx")
        )
        en_us_data = en_us_data[["id", "utt", "annot_utt"]]

        for root, _, files in os.walk(self.input_folder):
            for file in files:
                if file.endswith(".xlsx") and file != f"{self.en_us_code}.xlsx":
                    language_code = os.path.splitext(file)[0]
                    current_lang_data = pd.read_excel(os.path.join(root, file))
                    current_lang_data = current_lang_data.rename(
                        columns={
                            "utt": f"utt-{language_code}",
                            "annot_utt": f"annot_utt-{language_code}",
                        }
                    )
                    combined_data = pd.merge(
                        en_us_data, current_lang_data, on="id", how="inner"
                    )
                    output_file_path = os.path.join(
                        self.output_folder, f"en-US_to_{language_code}.xlsx"
                    )
                    combined_data.to_excel(
                        output_file_path, index=False, engine="openpyxl"
                    )
