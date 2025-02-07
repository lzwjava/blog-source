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
import random


# Initialize DeepSeek client if needed
def initialize_deepseek_client():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("Error: DEEPSEEK_API_KEY environment variable not set.")
        exit()
    return OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def call_gemini_api(prompt, retries=3, backoff_factor=1):
    gemini_api_key = os.environ.get("GEMINI_API_KEY")
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        exit()    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    params = {"key": gemini_api_key}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    print(f"Input to Gemini API: {payload}")

    for attempt in range(retries):
        response = requests.post(url, json=payload, params=params)
        response_json = response.json()
        print(response_json)
        if response.status_code == 200:
            return response_json
        elif response.status_code == 429:
            time.sleep(backoff_factor * (2 ** attempt))  # Exponential backoff
        else:
            raise Exception(f"Gemini API Error: {response.status_code} - {response_json}")
    return None

def call_mistral_api(prompt, model="mistral-small-2501", process_response=True):
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    print(f"Input to Mistral API: {data}")
    print(f"Mistral API URL: {url}")
    print(f"Mistral API Headers: {headers}")
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print(response_json)
        if response_json and response_json['choices']:
            content = response_json['choices'][0]['message']['content']
            if process_response:
                return process_mistral_response(content)
            else:
                return content
        else:
            print(f"Mistral API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral API Error: {e}") 
        stre = f"{e}"
        if '429' in  stre:
            # print(f"Response status code: {e.response.status_code}")
            # print(f"Response content: {e.response.text}")
            print("Too many requests, sleeping for 10 seconds and retrying")
            time.sleep(10)
            return call_mistral_api(prompt, model, process_response)

        raise e


def _call_ollama_api(prompt, model):
    url = "http://localhost:11434/v1/chat/completions"
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": model,
        "max_tokens": 300
    }
    headers = {"Content-Type": "application/json"}
    print(f"Input to API: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return process_ollama_response(response)

def _call_llama_api(prompt):
    url = "http://localhost:8080/v1/chat/completions"
    data = {
        "messages": [{"role": "user", "content": prompt}]
    }
    headers = {"Content-Type": "application/json"}
    print(f"Input to API: {data}")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return process_llama_response(response)

def _call_grok_api(prompt):
    api_key = os.environ.get("GROK_API_KEY")
    if not api_key:
        print("Error: GROK_API_KEY environment variable not set.")
        return None

    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "grok-2-latest",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    print(f"Input to Grok API: {data}")
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        json_response = response.json()
        if 'choices' in json_response and json_response['choices']:
            first_choice = json_response['choices'][0]
            if 'message' in first_choice and 'content' in first_choice['message']:
                return process_grok_response(first_choice['message']['content'])
            else:
                print("Unexpected response format: message or content missing")
                return ""
        else:
            print("No choices found in the response")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return ""
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return ""

