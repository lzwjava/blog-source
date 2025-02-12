import os
import requests
from dotenv import load_dotenv
import json
import subprocess
import argparse

load_dotenv()

TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
TELEGRAM_CHAT_ID = "-4714712674"

def send_telegram_message(bot_token, chat_id, message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(f"Error sending Telegram message: {response.status_code} - {response.text}")

def get_chat_id(bot_token):
    """Retrieves the chat ID of the last message sent to the bot."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        updates = response.json()
        print(json.dumps(updates, indent=4))
        if updates['result']:
            chat_id = updates['result'][-1]['message']['chat']['id']
            return chat_id
    return None

def get_latest_commit_message():
    """Fetches the latest commit message from the Git repository."""
    try:
        result = subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching latest commit message: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Telegram Bot Script")
    parser.add_argument('--job', choices=['get_chat_id', 'send_message'], required=True, help="Job to perform")
    args = parser.parse_args()

    if args.job == 'get_chat_id':
        bot_token = TELEGRAM_BOT_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"Chat ID: {chat_id}")
        else:
            print("Could not retrieve chat ID.")

    elif args.job == 'send_message':
        if TELEGRAM_BOT_API_KEY and TELEGRAM_CHAT_ID:
            commit_message = get_latest_commit_message()
            if commit_message:
                message = f"Blog Updated. Commit message: {commit_message}"
                send_telegram_message(TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            else:
                print("Could not retrieve the latest commit message.")
        else:
            print("TELEGRAM_BOT_API_KEY and TELEGRAM_CHAT_ID are not set.")

if __name__ == '__main__':
    main()
