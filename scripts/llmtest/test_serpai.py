import json
import os
import sys
from typing import Any, Dict

import requests


def serper_search(query: str, gl: str = "us", hl: str = "en") -> Dict[str, Any]:
    """Query Serper.dev Search API using SERPER_API_KEY from env.

    - Respects HTTP(S)_PROXY envs automatically via requests.
    - Returns parsed JSON dict.
    """
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing SERPER_API_KEY. Export your Serper API key: export SERPER_API_KEY=..."
        )

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }
    payload = {
        "q": query,
        "gl": gl,
        "hl": hl,
        # Serper supports location but it's optional; uncomment if you need it.
        # "location": "Austin, Texas, United States",
    }

    resp = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    # Default query mirrors the previous example
    query = sys.argv[1] if len(sys.argv) > 1 else "Coffee"
    try:
        data = serper_search(query)
    except Exception as e:
        # Provide a concise, useful error
        print(f"Error: {e}")
        sys.exit(1)

    # Print a short summary then raw JSON for inspection
    organic = data.get("organic") or []
    if organic:
        print("Top results:")
        for item in organic[:5]:
            title = item.get("title", "<no title>")
            link = item.get("link", "<no link>")
            print(f"- {title} -> {link}")

    # Always dump full JSON so callers can parse it
    print("\nFull JSON:")
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
