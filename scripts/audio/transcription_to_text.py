import os
import json
import glob


def extract_transcriptions(transcription_dir):
    """
    Extracts and prints transcriptions from JSON files in a directory.

    Args:
        transcription_dir (str): The directory containing the transcription JSON files.
    """
    json_files = glob.glob(os.path.join(transcription_dir, "*.json"))
    if not json_files:
        print(f"No JSON files found in '{transcription_dir}'.")
        return

    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for result in data.get("results", []):
                    for alternative in result.get("alternatives", []):
                        transcript = alternative.get("transcript")
                        if transcript:
                            print(f"{transcript}\n")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    transcription_directory = "assets/transcriptions"
    extract_transcriptions(transcription_directory)
