# This class is used to generate 3 files for the languages english, swahili and german
# based on the dev, test and train partition parameters

import os
import json


class JsonlFilesProcessor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.languages = ["en-US", "sw-KE", "de-DE"]
        self.partitions = ["test", "train", "dev"]

    def process_jsonl_files(self):
        # Ensure the output directory exists, or create it
        os.makedirs(self.output_folder, exist_ok=True)

        for language in self.languages:
            for partition in self.partitions:
                input_file = os.path.join(self.input_folder, f"{language}.jsonl")
                output_file = os.path.join(
                    self.output_folder, f"{language}_{partition}.jsonl"
                )

                with open(input_file, "r") as infile, open(output_file, "w") as outfile:
                    for line in infile:
                        data = json.loads(line)
                        if data.get("partition") == partition:
                            outfile.write(json.dumps(data) + "\n")


if __name__ == "__main__":
    input_folder = "data"
    output_folder = "../outputs/partition_languages"

    jsonl_processor = JsonlFilesProcessor(input_folder, output_folder)
    jsonl_processor.process_jsonl_files()
