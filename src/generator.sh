#!/bin/bash

# Set your Python interpreter (e.g., python or python3)
PYTHON=python

# Run the main.py script with command-line arguments
$PYTHON main.py --jsonl_folder "data" --output_excel_folder "../outputs/data_excel" \
    --input_folder "../outputs/data_excel" --output_folder "../outputs/combined_languages" \
    --en_us_code "en-US" --generate_translations
