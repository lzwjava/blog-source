import torch
from datasets import load_dataset
import requests
import json
from tqdm import tqdm
import re

# Load MMLU dataset
subject = "college_computer_science"  # Choose your subject
dataset = load_dataset("cais/mmlu", subject, split="test")

# Format prompt without few-shot examples
def format_mmlu_prompt(example):
    prompt = "The following are multiple-choice questions about {}".format(subject.replace("_", " "))
    prompt += ". Please answer with the number of the correct choice (0, 1, 2, or 3) only."
    prompt += " Output the number only, and do not output any other text."
    
    # Add current question
    prompt += f"Question: {example['question']}\n"
    prompt += "Choices:\n0. {}\n1. {}\n2. {}\n3. {}\n".format(*example['choices'])
    return prompt

# Evaluation loop
correct = 0
total = 0

for i, example in tqdm(enumerate(dataset), total=len(dataset), desc="Evaluating"):
    prompt = format_mmlu_prompt(example)
    
    # Send request to llama-server
    url = "http://localhost:8080/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": [{"role": "user", "content": prompt}]
    }
    
    print(f"Input to API: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        output_text = response.json()["choices"][0]["message"]["content"]
        predicted_answer = output_text.strip()[0] if len(output_text.strip()) > 0 else ""
        print(f"Output from API: {output_text}")
    else:
        predicted_answer = ""
        print(f"Error: {response.status_code} - {response.text}")
    
    # Compare with ground truth
    is_correct = predicted_answer == str(example["answer"])
    if is_correct:
        correct += 1
    total += 1
    
    print(f"Question: {example['question']}")
    print(f"Choices: 0. {example['choices'][0]}, 1. {example['choices'][1]}, 2. {example['choices'][2]}, 3. {example['choices'][3]}")
    print(f"Predicted Answer: {predicted_answer}, Ground Truth: {example['answer']}, Correct: {is_correct}")
    print("-" * 30)


# Calculate accuracy
accuracy = correct / total
print(f"Subject: {subject}")
print(f"Accuracy: {accuracy:.2%} ({correct}/{total})")