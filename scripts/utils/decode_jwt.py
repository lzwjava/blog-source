# decode_jwt.py
import jwt
import argparse
from jwt.exceptions import DecodeError

def decode_jwt_token(token: str) -> dict:
    """
    Decodes a JWT token without verifying the signature.

    Args:
        token: The JWT token to decode.

    Returns:
        A dictionary containing the decoded payload, or None if the token is invalid.
    """
    try:
        decoded_payload = jwt.decode(token, options={"verify_signature": False}, algorithms=["HS256"])
        return decoded_payload
    except DecodeError:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decode a JWT token.')
    parser.add_argument('token', type=str, help='The JWT token to decode')
    args = parser.parse_args()

    decoded_token = decode_jwt_token(args.token)

    if decoded_token:
        print(decoded_token)
    else:
        print("Invalid token")