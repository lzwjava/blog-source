#!/usr/bin/env python3
import subprocess
import sys

# Use gpg to encrypt a message
if len(sys.argv) < 3:
    print("Usage: python3 gpg_encrypt.py <recipient> <message>")
    sys.exit(1)

recipient = sys.argv[1]
message = sys.argv[2]

# Use gpg to encrypt
result = subprocess.run(['gpg', '--encrypt', '--recipient', recipient],
                       input=message, capture_output=True, text=True)
print(result.stdout)