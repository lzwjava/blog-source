import torch
from datasets import load_dataset
import requests
import json
from tqdm import tqdm

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
    
    # print(f"Input to API: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        output_text = response.json()["choices"][0]["message"]["content"]
        predicted_answer = output_text.strip()[0] if len(output_text.strip()) > 0 else ""
        # print(f"Output from API: {output_text}")
    else:
        predicted_answer = ""
        print(f"Error: {response.status_code} - {response.text}")
    
    # Compare with ground truth
    
    answer_map = {0: "A", 1: "B", 2: "C", 3: "D"}
    ground_truth_answer = answer_map.get(example["answer"], "")
    is_correct = predicted_answer.upper() == ground_truth_answer
    if is_correct:
        correct += 1
    total += 1
    
    # print(f"Question: {example['question']}")
    print(f"Choices: A. {example['choices'][0]}, B. {example['choices'][1]}, C. {example['choices'][2]}, D. {example['choices'][3]}")
    print(f"Predicted Answer: {predicted_answer}, Ground Truth: {ground_truth_answer}, Correct: {is_correct}")
    print("-" * 30)

    if (i+1) % 10 == 0:
        accuracy = correct / total
        print(f"Processed {i+1}/{len(dataset)}. Current Accuracy: {accuracy:.2%} ({correct}/{total})")


# Calculate accuracy
accuracy = correct / total
print(f"Subject: {subject}")
print(f"Accuracy: {accuracy:.2%} ({correct}/{total})")