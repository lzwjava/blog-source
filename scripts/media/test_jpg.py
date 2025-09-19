import os
import struct


def read_jpg_info(filename):
    """Reads JPG file and prints basic information."""
    print(f"Attempting to read JPG info from: {filename}")
    try:
        with open(filename, "rb") as f:
            print("File opened successfully.")
            # Read the first two bytes to check for JPG header (Start of Image marker)
            header = f.read(2)
            print(f"Read header: {header}")
            if header == b"\xff\xd8":
                print("Valid JPG header found.")
            else:
                print("Not a valid JPG file.")
                return

            # Read the next marker
            marker = f.read(2)
            while marker:
                print(f"Marker: {marker}")
                if marker == b"\xff\xd9":
                    print("End of Image marker found.")
                    break

                # Check if it's an Application Segment (e.g., JFIF, EXIF)
                if marker >= b"\xff\xe0" and marker <= b"\xff\xef":
                    # Read the length of the Application Segment
                    length_bytes = f.read(2)
                    length = struct.unpack(">H", length_bytes)[0]
                    print(f"Application Segment Length: {length}")

                    # Read the Application Data
                    app_data = f.read(length - 2)
                    print(
                        f"Application Data: {app_data[:20]}..."
                    )  # Print only the first 20 bytes

                    # Example: Check for JFIF identifier
                    if marker == b"\xff\xe0" and app_data.startswith(b"JFIF"):
                        print("JFIF Application Segment found.")

                # Added check for other markers, including those between 0xffc0 and 0xfffe (excluding 0xffd0-0xffd7)
                elif marker >= b"\xff\xc0" and marker <= b"\xff\xfe":
                    # Read the length of the segment
                    length_bytes = f.read(2)
                    length = struct.unpack(">H", length_bytes)[0]
                    print(f"Segment Length: {length}")

                    # Read the Segment Data
                    segment_data = f.read(length - 2)
                    print(
                        f"Segment Data: {segment_data[:20]}..."
                    )  # Print only the first 20 bytes

                else:
                    print("Unknown marker.")
                    break  # Stop reading after encountering an unknown marker

                marker = f.read(2)

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    jpg_file = os.path.join(dir_path, "test.jpg")
    read_jpg_info(jpg_file)
