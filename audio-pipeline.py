import os
import markdown
from google.cloud import texttospeech
from html import unescape
from bs4 import BeautifulSoup
import re
import random
from pydub import AudioSegment
import tempfile
import json
import time
from datetime import datetime
import argparse

# Define progress files for both tasks
PROGRESS_FILES = {
    'pages': 'progress/progress_pages.json',
    'posts': 'progress/progress_posts.json'
}

# Fixed output directory
OUTPUT_DIRECTORY = "assets/audios"

def load_progress(task):
    progress_file = PROGRESS_FILES.get(task)
    if progress_file and os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            return json.load(f)
    return {}

def save_progress(task, progress):
    progress_file = PROGRESS_FILES.get(task)
    if progress_file:
        with open(progress_file, 'w') as f:
            json.dump(progress, f, indent=4)

def split_into_sentences(text):
    """
    Splits text into sentences using regex.
    Handles common sentence endings.
    """
    sentence_endings = re.compile(r'(?<=[.!?]) +')
    sentences = sentence_endings.split(text)
    return sentences

def split_text(text, max_bytes=3000):
    """
    Splits text into chunks not exceeding max_bytes.
    First splits text into sentences to ensure sentences are not split across chunks.
    If a single sentence exceeds max_bytes, it further splits the sentence.
    """
    sentences = split_into_sentences(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        # Check if the sentence itself exceeds max_bytes
        if len(sentence.encode('utf-8')) > max_bytes:
            # Further split the sentence by commas or other delimiters
            sub_sentences = re.split(r', |; |: |。|，', sentence)
            for sub_sentence in sub_sentences:
                sub_sentence = sub_sentence.strip()
                if not sub_sentence:
                    continue
                tentative_chunk = f"{current_chunk} {sub_sentence}".strip()
                if len(tentative_chunk.encode('utf-8')) > max_bytes:
                    if current_chunk:
                        chunks.append(current_chunk)
                    current_chunk = sub_sentence
                else:
                    current_chunk = tentative_chunk
        else:
            tentative_chunk = f"{current_chunk} {sentence}".strip()
            if len(tentative_chunk.encode('utf-8')) > max_bytes:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = sentence
            else:
                current_chunk = tentative_chunk

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def text_to_speech(text, output_filename, task, language_code="en-US", voice_name=None, dry_run=False, start_chunk=0, progress=None):
    if dry_run:
        print(f"Dry run: Would generate audio for file: {output_filename}")
        return
    print(f"Generating audio for: {output_filename}")
    try:
        client = texttospeech.TextToSpeechClient()
        text_chunks = split_text(text)
        if not text_chunks:
            print("No text chunks to process.")
            return

        audio_segments = []
        # If resuming, load already processed chunks
        if progress and output_filename in progress:
            processed_chunks = progress[output_filename].get('processed_chunks', [])
            temp_files = progress[output_filename].get('temp_files', [])
            for chunk_path in temp_files:
                if os.path.exists(chunk_path):
                    audio_segments.append(AudioSegment.from_mp3(chunk_path))
            start_chunk = len(processed_chunks)
            print(f"Resuming from chunk {start_chunk + 1}/{len(text_chunks)}")
        else:
            processed_chunks = []
            progress[output_filename] = {'processed_chunks': [], 'temp_files': []}

        for idx in range(start_chunk, len(text_chunks)):
            chunk = text_chunks[idx]
            synthesis_input = texttospeech.SynthesisInput(text=chunk)
            if language_code == "en-US" and not voice_name:
                voice_name = random.choice(["en-US-Journey-D", "en-US-Journey-F", "en-US-Journey-O"])
            elif language_code == "cmn-CN" and not voice_name:
                voice_name = random.choice(["cmn-CN-Wavenet-A", "cmn-CN-Wavenet-B", "cmn-CN-Wavenet-C", "cmn-CN-Wavenet-D"])
            voice = texttospeech.VoiceSelectionParams(language_code=language_code, name=voice_name)
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                effects_profile_id=["small-bluetooth-speaker-class-device"]    
            )

            try:
                response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
            except Exception as e:
                # Check if the error is due to sentences being too long
                error_message = str(e).lower()
                if 'sentences that are too long' in error_message:
                    print(f"Chunk {idx + 1} has sentences that are too long. Attempting to split further.")
                    # Split the chunk into smaller parts and process each
                    sub_sentences = split_into_sentences(chunk)
                    for sub_idx, sub_sentence in enumerate(sub_sentences):
                        sub_sentence = sub_sentence.strip()
                        if not sub_sentence:
                            continue
                        sub_synthesis_input = texttospeech.SynthesisInput(text=sub_sentence)
                        try:
                            sub_response = client.synthesize_speech(input=sub_synthesis_input, voice=voice, audio_config=audio_config)
                            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_sub_file:
                                tmp_sub_file.write(sub_response.audio_content)
                                sub_temp_filename = tmp_sub_file.name
                            sub_audio_segment = AudioSegment.from_mp3(sub_temp_filename)
                            audio_segments.append(sub_audio_segment)
                            os.remove(sub_temp_filename)
                            print(f"Sub-chunk {sub_idx + 1}/{len(sub_sentences)} of chunk {idx + 1} processed.")
                        except Exception as sub_e:
                            print(f"Failed to process sub-chunk {sub_idx + 1} of chunk {idx + 1}: {sub_e}")
                            continue
                    # After handling sub-chunks, skip adding the original chunk
                    progress[output_filename]['processed_chunks'].append(idx)
                    save_progress(task, progress)
                    continue  # Move to the next chunk
                else:
                    print(f"Error on chunk {idx + 1}: {e}")
                    # Implement retry logic or other error handling as needed
                    retries = 3
                    for attempt in range(1, retries + 1):
                        try:
                            wait_time = 2 ** attempt
                            print(f"Retrying chunk {idx + 1} in {wait_time} seconds (Attempt {attempt}/{retries})...")
                            time.sleep(wait_time)
                            response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
                            break  # Success
                        except Exception as retry_e:
                            print(f"Retry attempt {attempt} failed for chunk {idx + 1}: {retry_e}")
                            if attempt == retries:
                                print(f"Failed to process chunk {idx + 1} after {retries} attempts.")
                                raise retry_e

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_file.write(response.audio_content)
                temp_filename = tmp_file.name
            audio_segment = AudioSegment.from_mp3(temp_filename)
            audio_segments.append(audio_segment)
            os.remove(temp_filename)
            print(f"Chunk {idx + 1}/{len(text_chunks)} processed.")

            # Update progress
            progress[output_filename]['processed_chunks'].append(idx)
            progress[output_filename]['temp_files'].append(temp_filename)
            save_progress(task, progress)

        if audio_segments:
            combined = audio_segments[0]
            for segment in audio_segments[1:]:
                combined += segment
            combined.export(output_filename, format="mp3")
            print(f"Audio content written to {output_filename}")
            # Cleanup temp files
            for temp_file in progress[output_filename]['temp_files']:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            # Remove progress entry for completed file
            del progress[output_filename]
            save_progress(task, progress)
        else:
            print("No audio segments to combine.")
    except Exception as e:
        print(f"An error occurred while generating audio for {output_filename}: {e}")
        save_progress(task, progress)  # Ensure progress is saved even on error

def md_to_text(md_file):
    print(f"Reading file: {md_file}")
    try:
        with open(md_file, 'r', encoding='utf-8') as file:
            md_content = file.read()
        # Remove front matter (--- ... ---)
        md_content = re.sub(r'---\n.*?\n---', '', md_content, flags=re.DOTALL)
        html = markdown.markdown(md_content)
        text = unescape(BeautifulSoup(html, "html.parser").get_text())
        return text
    except Exception as e:
        print(f"Error reading or parsing {md_file}: {e}")
        return ""

def get_last_n_files(input_dir, n=10):
    """
    Retrieve the last n Markdown files from the input directory based on filename (descending order).
    """
    try:
        # Get all markdown files
        md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
        # Sort by filename descending
        md_files_sorted = sorted(md_files, reverse=True)
        # Get the top n files
        last_n_files = md_files_sorted[:n]
        return last_n_files
    except Exception as e:
        print(f"Error retrieving files from {input_dir}: {e}")
        return []

def process_markdown_files(task, input_dir, output_dir, n=10, max_files=100, dry_run=False):
    os.makedirs(output_dir, exist_ok=True)
    
    if task == 'pages':
        all_md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
        last_md_files = all_md_files
        total_files = len(last_md_files)
        print(f"Total Markdown files to process in 'pages': {total_files}")
    elif task == 'posts':
        last_md_files = get_last_n_files(input_dir, n)
        total_files = len(last_md_files)
        print(f"Total Markdown files to process in '_posts' (last {n}): {total_files}")
    else:
        print("Invalid task specified.")
        return

    if total_files == 0:
        print(f"No Markdown files found in '{input_dir}' directory.")
        return

    files_processed = 0

    # Load existing progress
    progress = load_progress(task)

    for filename in last_md_files:
        md_file_path = os.path.join(input_dir, filename)
        output_filename = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.mp3")
        if os.path.exists(output_filename):
            print(f"Skipping {filename}: {output_filename} already exists.")
            continue
        article_text = md_to_text(md_file_path)
        if not article_text.strip():
            print(f"Skipping {filename}: No content to convert.")
            continue
        print(f"\nProcessing {files_processed + 1}/{total_files}: {filename}")
        try:
            if '-zh' in filename:
                text_to_speech(
                    article_text, 
                    output_filename, 
                    task=task, 
                    language_code="cmn-CN", 
                    dry_run=dry_run,
                    progress=progress
                )
            else:
                text_to_speech(
                    article_text, 
                    output_filename, 
                    task=task, 
                    dry_run=dry_run,
                    progress=progress
                )
            files_processed += 1
            print(f"File {files_processed}/{total_files} processed.\n")
            if task == 'pages' and files_processed >= max_files:
                print("Processed the maximum allowed files.")
                break
            if task == 'posts' and files_processed >= max_files:
                print("Processed the maximum allowed files.")
                break
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
            continue

    print(f"Processing complete! {files_processed}/{total_files} files processed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Markdown files to generate audio.")
    parser.add_argument('--task', choices=['pages', 'posts'], required=True, help="Task to perform: 'pages' or 'posts'")
    parser.add_argument('--n', type=int, default=10, help="Number of last files to process (only for 'posts').")
    parser.add_argument('--max_files', type=int, default=100, help="Maximum number of files to process (only for 'pages').")
    parser.add_argument('--dry_run', action='store_true', help="Perform a dry run without generating audio.")
    
    args = parser.parse_args()

    # Determine input_dir based on task
    if args.task == 'pages':
        input_directory = "pages"
        max_files = args.max_files
        n = None  # Not used for 'pages'
    elif args.task == 'posts':
        input_directory = "_posts"
        n = args.n
        max_files = args.max_files  # Typically 10 for 'posts', but keeping flexibility
    else:
        print("Invalid task specified. Choose either 'pages' or 'posts'.")
        exit(1)

    # Handle 'n' and 'max_files' based on task
    if args.task == 'pages':
        process_markdown_files(
            task=args.task,
            input_dir=input_directory,
            output_dir=OUTPUT_DIRECTORY,
            n=0,  # Not used
            max_files=args.max_files,
            dry_run=args.dry_run
        )
    elif args.task == 'posts':
        process_markdown_files(
            task=args.task,
            input_dir=input_directory,
            output_dir=OUTPUT_DIRECTORY,
            n=args.n,
            max_files=args.max_files,  # Typically 10
            dry_run=args.dry_run
        )
