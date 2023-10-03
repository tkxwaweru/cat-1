# Main function of project - main.py

import argparse
from jsonline_processor import JsonlProcessor
from jsonl_files import JsonlFilesProcessor
from languages_processor import LanguageProcessor
from jsonl_translations import JsonlTranslations  # Import the JsonlTranslations class


def main():
    parser = argparse.ArgumentParser(
        description="Process JSONL and language Excel files."
    )
    parser.add_argument(
        "--jsonl_folder", required=True, help="Path to the JSONL folder"
    )
    parser.add_argument(
        "--output_excel_folder",
        required=True,
        help="Path to the output Excel folder for JSONL files",
    )
    parser.add_argument(
        "--input_folder",
        required=True,
        help="Path to the input Excel folder for languages",
    )
    parser.add_argument(
        "--output_folder",
        required=True,
        help="Path to the output Excel folder for languages",
    )
    parser.add_argument(
        "--en_us_code", default="en-US", help="Language code for en-US (default: en-US)"
    )

    # Add the --generate_translations flag
    parser.add_argument(
        "--generate_translations",
        action="store_true",  # This makes it a boolean flag (True if present, False if absent)
        help="Generate translations from en-US to other languages",
    )

    args = parser.parse_args()

    # Create instances of the processors
    jsonl_processor = JsonlProcessor(args.jsonl_folder, args.output_excel_folder)
    lang_processor = LanguageProcessor(
        args.input_folder, args.output_folder, args.en_us_code
    )

    # Create an instance of the JsonlFilesProcessor class
    jsonl_files_processor = JsonlFilesProcessor(
        args.jsonl_folder, "../outputs/partition_languages"
    )

    # Call the JSONL processing step
    jsonl_files_processor.process_jsonl_files()  # Call the process_jsonl_files method

    # Run the JSONL processing step
    jsonl_processor.process_jsonl_files()

    # Run the language processing step
    lang_processor.process_languages()

    # Check if the --generate_translations flag is provided
    if args.generate_translations:
        # Create an instance of the JsonlTranslations class
        translations_processor = JsonlTranslations(
            args.jsonl_folder, "../outputs/translations"
        )

        # Generate the translations JSON file
        translations_processor.generate_translations_json()


if __name__ == "__main__":
    main()
