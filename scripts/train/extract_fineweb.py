import pandas as pd
import os

# Path to the FineWeb parquet file
parquet_file = "fineweb_test_dump/000_00000.parquet"

# Check if file exists
if not os.path.exists(parquet_file):
    print(f"Error: {parquet_file} not found!")
    exit(1)

print(f"Loading FineWeb data from {parquet_file}...")

# Load the parquet file
try:
    df = pd.read_parquet(parquet_file)
    print(f"Loaded {len(df)} rows")
    print(f"Columns: {list(df.columns)}")
    print(f"First few rows:")
    print(df.head())
except Exception as e:
    print(f"Error loading parquet file: {e}")
    exit(1)

# Extract text and save to file
output_file = "fineweb_test_dump/fineweb_extracted.txt"

print(f"Extracting text to {output_file}...")

try:
    with open(output_file, "w", encoding="utf-8") as f:
        # Iterate through rows and extract text
        for i, row in df.iterrows():
            # Try to find the text column (common names: text, content, article, etc.)
            text_content = None

            # Check common column names for text content
            for col in ['text', 'content', 'article', 'text_content', 'body']:
                if col in df.columns:
                    text_content = str(row[col])
                    break

            if text_content and text_content.strip():
                f.write(text_content + "\n")

            # Progress reporting
            if i % 10000 == 0:
                print(f"Processed {i} rows")

    print(f"Extraction complete! Output saved to {output_file}")

except Exception as e:
    print(f"Error during extraction: {e}")