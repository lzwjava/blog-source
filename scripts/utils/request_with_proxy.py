import requests
import argparse


def request_url_with_proxy(url, proxy):
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--proxy")

    args = parser.parse_args()

    proxy = {"http": args.proxy, "https": args.proxy} if args.proxy else {}

    response = request_url_with_proxy(args.url, proxy)

    if response:
        print(f"Status Code: {response.status_code}")
        print(f"Content: {response.text[:100]}...")
