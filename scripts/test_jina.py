import os
import requests
from dotenv import load_dotenv
import argparse
import base64

load_dotenv()

api_key = os.environ.get("JINA_API_KEY")
if not api_key:
    raise ValueError("JINA_API_KEY environment variable not set.")

parser = argparse.ArgumentParser()
parser.add_argument("--job", type=int, choices=[1, 2], help="Job to execute (1 or 2)", required=True)
parser.add_argument("--input", type=str, help="Input for the job", required=True)
args = parser.parse_args()

if args.job == 1:
    url = base64.b64decode(args.input).decode('utf-8', errors='ignore')
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    print(response.text)

elif args.job == 2:
    question = base64.b64decode(args.input).decode('utf-8', errors='ignore')
    url = f'https://s.jina.ai/{question}'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'X-Engine': 'direct',
        'X-Retain-Images': 'none'
    }
    response = requests.get(url, headers=headers)
    print(response.text)

else:
    print("Please specify --job 1 or --job 2")
