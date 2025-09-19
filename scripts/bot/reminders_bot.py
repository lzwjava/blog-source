import os
import requests
from dotenv import load_dotenv
import json
import argparse

load_dotenv()

TELEGRAM_BOT2_API_KEY = os.environ.get("TELEGRAM_BOT2_API_KEY")
TELEGRAM_CHAT_ID = "610574272"


def send_telegram_message(bot_token, chat_id, message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(
            f"Error sending Telegram message: {response.status_code} - {response.text}"
        )


def get_chat_id(bot_token):
    """Retrieves the chat ID of the last message sent to the bot."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    if response.status_code == 200:
        updates = response.json()
        print(json.dumps(updates, indent=4))
        if updates["result"]:
            chat_id = updates["result"][-1]["message"]["chat"]["id"]
            return chat_id
    return None


def send_reminder(message):
    """Sends a reminder message to Telegram."""
    if TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID:
        send_telegram_message(TELEGRAM_BOT2_API_KEY, TELEGRAM_CHAT_ID, f"{message}")
    else:
        print("TELEGRAM_BOT2_API_KEY and TELEGRAM_CHAT_ID are not set.")


def main():
    parser = argparse.ArgumentParser(description="Telegram Bot Script")
    parser.add_argument(
        "--job",
        choices=["get_chat_id", "send_message"],
        required=True,
        help="Job to perform",
    )
    parser.add_argument("--message", help="Custom message to send", default=None)
    args = parser.parse_args()

    if args.job == "get_chat_id":
        bot_token = TELEGRAM_BOT2_API_KEY
        chat_id = get_chat_id(bot_token)
        if chat_id:
            print(f"Chat ID: {chat_id}")
        else:
            print("Could not retrieve chat ID.")

    elif args.job == "send_message":
        if args.message:
            send_reminder(args.message)
        else:
            print("No message provided for send_message job.")


if __name__ == "__main__":
    main()
