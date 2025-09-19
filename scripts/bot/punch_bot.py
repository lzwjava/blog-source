import os
import requests
import datetime
import pytz
from supabase import create_client
import argparse

# Load environment variables
TELEGRAM_PUNCH_BOT_API_KEY = os.environ.get("TELEGRAM_PUNCH_BOT_API_KEY")
TELEGRAM_CHAT_ID = "610574272"  # Your chat ID


def send_telegram_message(bot_token, chat_id, message):
    """Sends a message to a Telegram chat using the Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print(
            f"Error sending Telegram message: {response.status_code} - {response.text}"
        )


def send_reminder(action):
    """Sends a punch reminder message."""
    # Updated message to specify punch_in or punch_out command
    command = action  # e.g., 'punch_in' or 'punch_out'
    message = f"⏰ *Reminder:* Please {action.replace('_', ' ')} by sending '{command}' to this bot."
    send_telegram_message(TELEGRAM_PUNCH_BOT_API_KEY, TELEGRAM_CHAT_ID, message)


def send_confirmation(action):
    """Sends a confirmation message for completed punch."""
    message = f"✅ You have already {action.replace('_', ' ')} today. No further reminders will be sent."
    send_telegram_message(TELEGRAM_PUNCH_BOT_API_KEY, TELEGRAM_CHAT_ID, message)


def parse_time(hour_str):
    """Parses HH string into datetime.time object with zero minutes."""
    try:
        hour = int(hour_str)
        if not 0 <= hour <= 23:
            raise ValueError
        return datetime.time(hour, 0)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Hour '{hour_str}' must be an integer between 00 and 23"
        )


def main():
    parser = argparse.ArgumentParser(description="Telegram Punch Reminder Bot")
    parser.add_argument(
        "--job",
        choices=["punch_reminder", "send_message"],
        required=True,
        help="Job to perform",
    )
    parser.add_argument(
        "--message", type=str, help="Message to send for 'send_message' job"
    )
    parser.add_argument(
        "--punch_in_start",
        type=parse_time,
        default="12",
        help="Punch in start hour (HH, default 12)",
    )
    parser.add_argument(
        "--punch_in_end",
        type=parse_time,
        default="15",
        help="Punch in end hour (HH, default 15)",
    )
    parser.add_argument(
        "--punch_out_start",
        type=parse_time,
        default="18",
        help="Punch out start hour (HH, default 18)",
    )
    parser.add_argument(
        "--punch_out_end",
        type=parse_time,
        default="21",
        help="Punch out end hour (HH, default 21)",
    )
    args = parser.parse_args()

    if args.job == "send_message":
        if TELEGRAM_PUNCH_BOT_API_KEY and TELEGRAM_CHAT_ID:
            message = (
                args.message if args.message else "Default test message from your bot!"
            )
            send_telegram_message(TELEGRAM_PUNCH_BOT_API_KEY, TELEGRAM_CHAT_ID, message)
            print(f"Message sent: {message}")
        else:
            print("TELEGRAM_PUNCH_BOT_API_KEY and TELEGRAM_CHAT_ID are not set.")
        return

    elif args.job == "punch_reminder":
        # Initialize Supabase
        supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

        # Get current time in SGT (UTC+8)
        sgt = pytz.timezone("Asia/Singapore")
        now_utc = datetime.datetime.utcnow()
        now_sgt = now_utc.replace(tzinfo=pytz.utc).astimezone(sgt)
        today_sgt = now_sgt.date()

        # Define time windows from arguments
        punch_in_start = args.punch_in_start
        punch_in_end = args.punch_in_end
        punch_out_start = args.punch_out_start
        punch_out_end = args.punch_out_end

        current_time = now_sgt.time()

        # Determine current window
        if punch_in_start <= current_time <= punch_in_end:
            window = "punch_in"
        elif punch_out_start <= current_time <= punch_out_end:
            window = "punch_out"
        else:
            window = None

        if not window:
            print("Outside punch reminder windows.")
            return

        # Fetch today's punch record
        response = (
            supabase.table("punch_records")
            .select("*")
            .eq("date", str(today_sgt))
            .execute()
        )
        punch_record = response.data[0] if response.data else None

        # Check if punch is already done
        if window == "punch_in" and punch_record and punch_record["punch_in_time"]:
            print("Already punched in today.")
            send_confirmation("punch_in")
            return
        if window == "punch_out" and punch_record and punch_record["punch_out_time"]:
            print("Already punched out today.")
            send_confirmation("punch_out")
            return

        # Fetch last processed Telegram update ID
        state_response = (
            supabase.table("telegram_state")
            .select("last_update_id")
            .eq("id", 1)
            .execute()
        )
        last_update_id = (
            state_response.data[0]["last_update_id"] if state_response.data else 0
        )

        # Get new Telegram updates
        url = f"https://api.telegram.org/bot{TELEGRAM_PUNCH_BOT_API_KEY}/getUpdates"
        params = {"offset": last_update_id + 1, "timeout": 0}
        response = requests.get(url, params=params)
        updates = response.json().get("result", [])

        max_update_id = last_update_id
        for update in updates:
            if update["update_id"] > max_update_id:
                max_update_id = update["update_id"]
            if (
                "message" in update
                and str(update["message"]["chat"]["id"]) == TELEGRAM_CHAT_ID
            ):
                message_text = update["message"].get("text", "").lower()
                # Check for specific commands based on the current window
                if window == "punch_in" and message_text == "punch_in":
                    if not punch_record:
                        supabase.table("punch_records").insert(
                            {
                                "date": str(today_sgt),
                                "punch_in_time": now_utc.isoformat(),
                            }
                        ).execute()
                    else:
                        supabase.table("punch_records").update(
                            {"punch_in_time": now_utc.isoformat()}
                        ).eq("date", str(today_sgt)).execute()
                elif window == "punch_out" and message_text == "punch_out":
                    if not punch_record:
                        supabase.table("punch_records").insert(
                            {
                                "date": str(today_sgt),
                                "punch_out_time": now_utc.isoformat(),
                            }
                        ).execute()
                    else:
                        supabase.table("punch_records").update(
                            {"punch_out_time": now_utc.isoformat()}
                        ).eq("date", str(today_sgt)).execute()

        # Update last_update_id
        if max_update_id > last_update_id:
            supabase.table("telegram_state").update(
                {"last_update_id": max_update_id}
            ).eq("id", 1).execute()

        # Refetch punch record to check latest state
        response = (
            supabase.table("punch_records")
            .select("*")
            .eq("date", str(today_sgt))
            .execute()
        )
        punch_record = response.data[0] if response.data else None

        # Send reminder if punch not recorded
        if window == "punch_in" and (
            not punch_record or not punch_record["punch_in_time"]
        ):
            send_reminder("punch_in")
        elif window == "punch_out" and (
            not punch_record or not punch_record["punch_out_time"]
        ):
            send_reminder("punch_out")


if __name__ == "__main__":
    main()
