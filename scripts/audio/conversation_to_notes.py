import json
import os

CONVERSATION_DIR = "scripts/conversation"
NOTES_DIR = "notes"

def convert_conversation_to_notes():
    print("Starting conversation to notes conversion...")
    os.makedirs(NOTES_DIR, exist_ok=True)
    print(f"Created or verified notes directory: {NOTES_DIR}")
    for filename in os.listdir(CONVERSATION_DIR):
        if filename.endswith(".json"):
            print(f"Processing file: {filename}")
            filepath = os.path.join(CONVERSATION_DIR, filename)
            with open(filepath, 'r') as f:
                try:
                    conversation = json.load(f)
                    print(f"Successfully loaded JSON from {filename}")
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {filename}. Skipping.")
                    continue

            notes_filename = os.path.splitext(filename)[0] + "-conv-en.md"
            notes_filepath = os.path.join(NOTES_DIR, notes_filename)
            title = os.path.splitext(filename)[0].replace("-", " ").title() + " - Conversation"
            print(f"Creating notes file: {notes_filepath} with title: {title}")

            with open(notes_filepath, 'w') as outfile:
                outfile.write(f"---\nlayout: post\ntitle: \"{title}\"\naudio: true\n---\n\n")
                for item in conversation:
                    speaker = item.get("speaker")
                    line = item.get("line")
                    if speaker and line:
                        outfile.write(f"{speaker}: {line}\n\n")
                    else:
                        print(f"Skipping item with missing speaker or line in {filename}: {item}")
            print(f"Successfully wrote notes to {notes_filepath}")
    print("Finished conversation to notes conversion.")

if __name__ == "__main__":
    convert_conversation_to_notes()
