import base64

# Sample string
sample_string = "Hello, World!"

# Encode to Base64
sample_bytes = sample_string.encode("utf-8")
encoded_bytes = base64.b64encode(sample_bytes)
encoded_string = encoded_bytes.decode("utf-8")
print("Encoded string:", encoded_string)

# Decode from Base64
encoded_bytes = encoded_string.encode("utf-8")
decoded_bytes = base64.b64decode(encoded_bytes)
decoded_string = decoded_bytes.decode("utf-8")
print("Decoded string:", decoded_string)
