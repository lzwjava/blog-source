import os
import struct


def read_mp3_info(filename):
    """Reads MP3 file and prints media info using os and struct."""
    print(f"Attempting to read MP3 info from: {filename}")
    try:
        with open(filename, "rb") as f:
            print("File opened successfully.")
            # Read the first 10 bytes to check for ID3 tag
            header = f.read(10)
            print(f"Read header: {header}")
            if header[:3] == b"ID3":
                # ID3 tag found, skip it
                print("ID3 tag found.")
                id3_version = header[3:5]
                id3_flags = header[5]
                id3_size_bytes = header[6:10]
                id3_size = struct.unpack(">I", id3_size_bytes)[0]
                # The size is encoded with synchsafe integers, so we need to decode it
                id3_size = (
                    (id3_size & 0x7F)
                    | ((id3_size >> 8) & 0x3F80)
                    | ((id3_size >> 16) & 0x1FC000)
                    | ((id3_size >> 24) & 0xFE00000)
                )
                print(
                    f"ID3 version: {id3_version}, flags: {id3_flags}, size: {id3_size}"
                )
                f.seek(id3_size, os.SEEK_CUR)  # Skip the ID3 tag
                print(f"Skipped ID3 tag, current position: {f.tell()}")

            # Now, read the MP3 frame header
            frame_header = f.read(4)
            print(f"Read frame header: {frame_header}")
            if len(frame_header) < 4:
                print("Not a valid MP3 file or reached end of file.")
                return

            # Parse the frame header
            syncword = frame_header[0:2]
            print(f"Syncword: {syncword}")
            if syncword != b"\xff\xfb" and syncword != b"\xff\xfa":
                print("Not a valid MP3 frame.")
                return

            # Extract information from the frame header
            version_layer_byte = frame_header[1]
            bitrate_sampling_byte = frame_header[2]
            other_bits_byte = frame_header[3]

            version = (version_layer_byte >> 3) & 0x03
            layer = (version_layer_byte >> 1) & 0x03
            protection_bit = (version_layer_byte >> 0) & 0x01

            bitrate_index = (bitrate_sampling_byte >> 4) & 0x0F
            sampling_rate_index = (bitrate_sampling_byte >> 2) & 0x03
            padding_bit = (bitrate_sampling_byte >> 1) & 0x01
            private_bit = (bitrate_sampling_byte >> 0) & 0x01

            channel_mode = (other_bits_byte >> 6) & 0x03
            mode_extension = (other_bits_byte >> 4) & 0x03
            copyright_bit = (other_bits_byte >> 3) & 0x01
            original_bit = (other_bits_byte >> 2) & 0x01
            emphasis = other_bits_byte & 0x03

            # Print some info
            print("MP3 File Info:")
            print(f"  Version: {version}")
            print(f"  Layer: {layer}")
            print(f"  Protection Bit: {protection_bit}")
            print(f"  Bitrate Index: {bitrate_index}")
            print(f"  Sampling Rate Index: {sampling_rate_index}")
            print(f"  Padding Bit: {padding_bit}")
            print(f"  Private Bit: {private_bit}")
            print(f"  Channel Mode: {channel_mode}")
            print(f"  Mode Extension: {mode_extension}")
            print(f"  Copyright Bit: {copyright_bit}")
            print(f"  Original Bit: {original_bit}")
            print(f"  Emphasis: {emphasis}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    mp3_file = os.path.join(dir_path, "test.mp3")
    read_mp3_info(mp3_file)
