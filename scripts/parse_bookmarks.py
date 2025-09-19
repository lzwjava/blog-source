import json
import lz4.block
import sys


def decompress_jsonlz4(file_path):
    with open(file_path, "rb") as f:
        # Read the first 8 bytes - header magic
        magic = f.read(8)
        if magic != b"mozLz40\0":
            raise ValueError("Invalid file header - not a JSON-LZ4 file")

        # Read the rest of the file and decompress
        compressed_data = f.read()
        json_bytes = lz4.block.decompress(compressed_data)
        json_str = json_bytes.decode("utf-8")
        return json.loads(json_str)


# Example usage
if __name__ == "__main__":
    file_path = sys.argv[1]
    data = decompress_jsonlz4(file_path)
    print(json.dumps(data, indent=4))
