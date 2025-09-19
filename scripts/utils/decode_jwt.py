import jwt
import argparse
import json
from jwt.exceptions import PyJWTError


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Decode a JWT token.")
    parser.add_argument("token", type=str, help="The JWT token to decode")
    args = parser.parse_args()
    token = args.token

    # Decode and print the header
    try:
        header = jwt.get_unverified_header(token)
        print("Header:")
        print(json.dumps(header, indent=4))
    except PyJWTError as e:
        print(f"Header decode error: {e}")

    # Decode and print the payload
    try:
        payload = jwt.decode(
            token, options={"verify_signature": False}, algorithms=["HS256"]
        )
        print("Payload:")
        print(json.dumps(payload, indent=4))
    except PyJWTError as e:
        print(f"Payload decode error: {e}")


if __name__ == "__main__":
    main()
