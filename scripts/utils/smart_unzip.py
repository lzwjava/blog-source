import zipfile
import os
import argparse


def smart_unzip(zip_path):
    extract_dir = os.path.splitext(zip_path)[0] + "_unzipped"
    os.makedirs(extract_dir, exist_ok=True)

    renamed_files = {}

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        file_names = zip_ref.namelist()

        for file in file_names:
            extracted_path = zip_ref.extract(file, extract_dir)  # Extract first

            # Rename files without extensions (excluding directories)
            if not os.path.splitext(os.path.basename(file))[1] and not file.endswith(
                "/"
            ):
                new_name = extracted_path + ".unknown"
                os.rename(extracted_path, new_name)
                renamed_files[new_name] = extracted_path

    # Create a new zip with renamed files
    output_zip = os.path.splitext(zip_path)[0] + "_processed.zip"
    with zipfile.ZipFile(output_zip, "w") as new_zip:
        for root, _, files in os.walk(extract_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, extract_dir)

                # Rename back the files in archive
                if full_path in renamed_files:
                    arcname = os.path.relpath(renamed_files[full_path], extract_dir)

                new_zip.write(full_path, arcname)

    print(f"Processed ZIP file created: {output_zip}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Smart unzip: Extract ZIP and rename files without extensions."
    )
    parser.add_argument("zip_path", help="Path to the input ZIP file")
    args = parser.parse_args()
    smart_unzip(args.zip_path)
