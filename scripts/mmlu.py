import torch
from datasets import load_dataset
import requests
import json
from tqdm import tqdm
import argparse
import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

# Set up argument parsing
parser = argparse.ArgumentParser(description="Evaluate MMLU dataset with different backends.")
parser.add_argument("--type", type=str, default="ollama", choices=["ollama", "llama", "deepseek", "gemini"], help="Backend type: ollama, llama, deepseek, or gemini")
args = parser.parse_args()

# Load MMLU dataset
subject = "college_computer_science"  # Choose your subject
dataset = load_dataset("cais/mmlu", subject, split="test")

# Format prompt without few-shot examples
def format_mmlu_prompt(example):
    prompt = "The following are multiple-choice questions about {}".format(subject.replace("_", " "))
    prompt += ". Please answer with the letter of the correct choice (A, B, C, or D) only."
    prompt += " Answer the letter only. Do not need Explanation."
    
    # Add current question
    prompt += f"Question: {example['question']}\n"
    prompt += "Choices:\nA. {}\nB. {}\nC. {}\nD. {}\n".format(*example['choices'])
    return prompt

# Initialize DeepSeek client if needed
def initialize_deepseek_client():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY environment variable not set.")
        exit()
    return OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# Initialize Gemini client if needed
def initialize_gemini_client():
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        exit()
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={gemini_api_key}"
    gemini_headers = {'Content-Type': 'application/json'}
    return gemini_url, gemini_headers

def call_gemini_api(prompt, retries=3, backoff_factor=1):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent"
    params = {"key": os.environ.get("GEMINI_API_KEY")}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    for attempt in range(retries):
        response = requests.post(url, json=payload, params=params)
        if response.status_code != 429:
            return response.json()
        time.sleep(backoff_factor * (2 ** attempt))  # Exponential backoff
    return None

def process_ollama_response(response):
    if response.status_code == 200:
        output_text = response.json()["choices"][0]["message"]["content"]
        predicted_answer = output_text.strip()[0] if len(output_text.strip()) > 0 else ""
        print(f"Output from API: {output_text}")
        return predicted_answer
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return ""

def process_llama_response(response):
    if response.status_code == 200:
        output_text = response.json()["choices"][0]["message"]["content"]
        predicted_answer = output_text.strip()[0] if len(output_text.strip()) > 0 else ""
        print(f"Output from API: {output_text}")
        return predicted_answer
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return ""

def process_deepseek_response(client, prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        if response and response.choices:
            output_text = response.choices[0].message.content.strip()
            predicted_answer = output_text.strip()[0] if len(output_text.strip()) > 0 else ""
            print(f"Output from API: {output_text}")
            return predicted_answer
        else:
            print("Error: No response from the API.")
            return ""
    except Exception as e:
        print(f"Error during API call: {e}")
        return ""

def process_gemini_response(prompt):
    json_response = call_gemini_api(prompt)
    if json_response and 'candidates' in json_response and json_response['candidates']:
        first_candidate = json_response['candidates'][0]
        if 'content' in first_candidate and 'parts' in first_candidate['content']:
            first_part = first_candidate['content']['parts'][0]
            if 'text' in first_part:
                output_text = first_part['text']
                predicted_answer = output_text.strip()[0] if len(output_text.strip()) > 0 else ""
                print(f"Output from API: {output_text}")
                return predicted_answer
            else:
                print("No text found in the response")
                return ""
        else:
            print("Unexpected response format: content or parts missing")
            return ""
    else:
        print("No candidates found in the response")
        return ""

def evaluate_model(args, dataset):
    correct = 0
    total = 0
    client = None
    if args.type == "deepseek":
        client = initialize_deepseek_client()
    elif args.type == "gemini":
        gemini_url, gemini_headers = initialize_gemini_client()

    for i, example in tqdm(enumerate(dataset), total=len(dataset), desc="Evaluating"):
        prompt = format_mmlu_prompt(example)
        predicted_answer = ""

        if args.type == "ollama":
            url = "http://localhost:11434/v1/chat/completions"
            data = {
                "messages": [{"role": "user", "content": prompt}],
                "model": "mistral:7b"
            }
            headers = {"Content-Type": "application/json"}
            print(f"Input to API: {data}")
            response = requests.post(url, headers=headers, data=json.dumps(data))
            predicted_answer = process_ollama_response(response)

        elif args.type == "llama":
            url = "http://localhost:8080/v1/chat/completions"
            data = {
                "messages": [{"role": "user", "content": prompt}]
            }
            headers = {"Content-Type": "application/json"}
            print(f"Input to API: {data}")
            response = requests.post(url, headers=headers, data=json.dumps(data))
            predicted_answer = process_llama_response(response)

        elif args.type == "deepseek":
            predicted_answer = process_deepseek_response(client, prompt)

        elif args.type == "gemini":
            predicted_answer = process_gemini_response(prompt)
        else:
            raise ValueError("Invalid backend type")
        
        answer_map = {0: "A", 1: "B", 2: "C", 3: "D"}
        ground_truth_answer = answer_map.get(example["answer"], "")
        is_correct = predicted_answer.upper() == ground_truth_answer
        if is_correct:
            correct += 1
        total += 1
        
        print(f"Question: {example['question']}")
        print(f"Choices: A. {example['choices'][0]}, B. {example['choices'][1]}, C. {example['choices'][2]}, D. {example['choices'][3]}")
        print(f"Predicted Answer: {predicted_answer}, Ground Truth: {ground_truth_answer}, Correct: {is_correct}")
        print("-" * 30)

        if (i+1) % 10 == 0:
            accuracy = correct / total
            print(f"Processed {i+1}/{len(dataset)}. Current Accuracy: {accuracy:.2%} ({correct}/{total})")
    
    return correct, total

# Evaluation loop
correct, total = evaluate_model(args, dataset)

# Calculate accuracy
accuracy = correct / total
print(f"Subject: {subject}")
print(f"Accuracy: {accuracy:.2%} ({correct}/{total})")