import os
import re
import argparse
import shutil


def clean_code(input_file, backup):
    if not input_file.endswith(".py"):
        print("Error: Input file must have a '.py' extension.")
        return

    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    filename, file_extension = os.path.splitext(input_file)

    if backup:
        backup_file = f"{filename}_original{file_extension}"
        shutil.copy(input_file, backup_file)

    with open(input_file, "r") as file:
        code = file.read()

    cleaned_code = re.sub(r'(?:^|\n)\s*""".*?"""', "", code, flags=re.DOTALL)
    cleaned_code = re.sub(r"^\s*#.*", "", cleaned_code, flags=re.MULTILINE)
    cleaned_code = re.sub(
        r"(\'\'\'|\s*\#\s*\'.*?\'\')", "", cleaned_code, flags=re.DOTALL
    )
    cleaned_code = re.sub(r"'''.*?'''", "", cleaned_code, flags=re.DOTALL)

    with open(input_file, "w") as file:
        file.write(cleaned_code)

    print(f"Cleaned code saved to {input_file}")

    if backup:
        print(f"Original code backed up to {backup_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Clean Python code by removing comments."
    )
    parser.add_argument(
        "input_files",
        nargs="+",
        help="Input Python file(s) to clean (must have a '.py' extension).",
    )
    parser.add_argument("--backup", action="store_true", help="skip backup if present")
    args = parser.parse_args()

    for input_file in args.input_files:
        clean_code(input_file, args.backup)


if __name__ == "__main__":
    main()
