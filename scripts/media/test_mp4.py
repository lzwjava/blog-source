import os
import struct


def read_chunk(f, size):
    """Reads a chunk of data from the file."""
    chunk = f.read(size)
    print(f"Read chunk of size: {size}, data: {chunk}")
    return chunk


def unpack_data(data, format_string):
    """Unpacks data according to the given format string."""
    unpacked_data = struct.unpack(format_string, data)[0]
    print(f"Unpacked data: {unpacked_data}, format: {format_string}, from data: {data}")
    return unpacked_data


def find_atom(f, file_size, name, parent_offset=0):
    """
    Finds an atom (box) within the MP4 file.

    Args:
        f (file): The file object.
        file_size (int): The size of the file.
        name (str): The name of the atom to find (e.g., 'moov', 'mvhd').
        parent_offset (int): The offset of the parent atom.

    Returns:
        tuple: A tuple containing the size and start position of the atom,
               or (None, None) if the atom is not found.
    """
    current_position = f.tell()
    print(
        f"Finding atom: {name}, current position: {current_position}, file size: {file_size}, parent_offset: {parent_offset}"
    )
    f.seek(parent_offset)  # Always seek to parent_offset initially
    end_offset = parent_offset + file_size
    while f.tell() < end_offset:
        try:
            size = unpack_data(read_chunk(f, 4), ">I")
            atom_type = read_chunk(f, 4).decode("utf-8")
            print(f"  Atom type: {atom_type}, size: {size}, position: {f.tell() - 4}")
            if atom_type == name:
                print(f"  Found atom: {name} at position: {f.tell() - 8}, size: {size}")
                return size, f.tell() - 8
            # Correctly handle atoms with size <= 8 (empty atoms or errors)
            if size <= 8:
                print(f"  Skipping atom with size {size} <= 8")
                continue

            f.seek(size - 8, 1)  # Seek relative to current position

        except struct.error:
            print(f"  Reached end of file prematurely while searching for {name}.")
            break
        except Exception as e:
            print(f"  An error occurred while searching for {name}: {e}")
            break
    f.seek(current_position)
    print(f"  Atom: {name} not found.")
    return None, None


def get_atom_data(f, parent_offset, atom_name):
    """
    Finds an atom and returns its size and offset.

    Args:
        f (file): The file object.
        parent_offset (int): The offset of the parent atom.
        atom_name (str): The name of the atom to find.

    Returns:
        tuple: A tuple containing the size and offset of the atom,
               or (None, None) if the atom is not found.
    """
    current_position = f.tell()
    print(
        f"Getting atom data: {atom_name}, parent offset: {parent_offset}, current position: {current_position}"
    )
    # Removed file_size calculation from here, it's calculated in find_atom
    size, offset = find_atom(
        f, 0, atom_name, parent_offset
    )  # Pass 0 for file_size, as it's not needed
    f.seek(current_position)
    print(f"  Atom {atom_name} data: size={size}, offset={offset}")
    return size, offset


def get_timescale_and_duration(f, mvhd_offset):
    """Reads timescale and duration from 'mvhd' atom."""
    print(f"Getting timescale and duration from mvhd_offset: {mvhd_offset}")
    f.seek(mvhd_offset + 12)  # Skip version, flags, creation_time, modification_time
    timescale = unpack_data(read_chunk(f, 4), ">I")
    duration = unpack_data(read_chunk(f, 4), ">I")
    print(f"  Timescale: {timescale}, duration: {duration}")
    return timescale, duration


def get_media_timescale(f, mdhd_offset):
    """Reads media timescale from 'mdhd' atom."""
    print(f"Getting media timescale from mdhd_offset: {mdhd_offset}")
    f.seek(mdhd_offset + 12)  # Skip version, flags
    media_timescale = unpack_data(read_chunk(f, 4), ">I")
    print(f"  Media timescale: {media_timescale}")
    return media_timescale


def get_codec_info(f, stsd_offset):
    """Gets codec information from 'stsd' atom."""
    print(f"Getting codec info from stsd_offset: {stsd_offset}")
    f.seek(stsd_offset + 16)
    codec_size = unpack_data(read_chunk(f, 4), ">I")
    codec_name = read_chunk(f, 4).decode("utf-8")
    print(f"  Codec size: {codec_size}, codec name: {codec_name}")
    return codec_name


def get_width_and_height(f, tkhd_offset):
    """Reads width and height from 'tkhd' atom."""
    print(f"Getting width and height from tkhd_offset: {tkhd_offset}")
    f.seek(tkhd_offset + 76)  # fixed the offset to account for the correct fields.
    width = (
        unpack_data(read_chunk(f, 4), ">I") / 65536
    )  # Width and height are fixed point 16.16 values
    height = unpack_data(read_chunk(f, 4), ">I") / 65536
    print(f"  Width: {width}, height: {height}")
    return width, height


def read_mp4_info(file_path):
    """
    Reads and extracts information from an MP4 file.

    Args:
        file_path (str): The path to the MP4 file.
    """
    print(f"Reading MP4 info from: {file_path}")
    try:
        with open(file_path, "rb") as f:
            file_size = os.path.getsize(file_path)
            print(f"File size: {file_size}")

            # Find 'moov' atom (Movie Header)
            moov_size, moov_offset = find_atom(f, file_size, "moov")
            if not moov_size:
                raise ValueError("'moov' atom not found.")
            print(f"moov_size: {moov_size}, moov_offset: {moov_offset}")

            # Find 'mvhd' atom inside 'moov'
            mvhd_size, mvhd_offset = get_atom_data(f, moov_offset, "mvhd")
            if not mvhd_size:
                raise ValueError("'mvhd' atom not found.")
            print(f"mvhd_size: {mvhd_size}, mvhd_offset: {mvhd_offset}")

            # Read timescale and duration from 'mvhd'
            timescale, duration = get_timescale_and_duration(f, mvhd_offset)

            # Find 'trak' atom inside 'moov'
            trak_size, trak_offset = find_atom(f, moov_size, "trak", moov_offset)
            if not trak_size:
                raise ValueError("'trak' atom not found.")
            print(f"trak_size: {trak_size}, trak_offset: {trak_offset}")

            # Find 'mdia' atom inside 'trak'
            mdia_size, mdia_offset = get_atom_data(f, trak_offset, "mdia")
            if not mdia_size:
                raise ValueError("'mdia' atom not found.")
            print(f"mdia_size: {mdia_size}, mdia_offset: {mdia_offset}")

            # Find 'mdhd' atom inside 'mdia'
            mdhd_size, mdhd_offset = get_atom_data(f, mdia_offset, "mdhd")
            if not mdhd_size:
                raise ValueError("'mdhd' atom not found.")
            print(f"mdhd_size: {mdhd_size}, mdhd_offset: {mdhd_offset}")

            # Read media timescale from 'mdhd'
            media_timescale = get_media_timescale(f, mdhd_offset)

            # Find 'hdlr' atom inside 'mdia'
            hdlr_size, hdlr_offset = get_atom_data(f, mdia_offset, "hdlr")
            if not hdlr_size:
                raise ValueError("'hdlr' atom not found.")
            print(f"hdlr_size: {hdlr_size}, hdlr_offset: {hdlr_offset}")

            # Find 'minf' atom inside 'mdia'
            minf_size, minf_offset = get_atom_data(f, mdia_offset, "minf")
            if not minf_size:
                raise ValueError("'minf' atom not found.")
            print(f"minf_size: {minf_size}, minf_offset: {minf_offset}")

            # Find 'stbl' atom inside 'minf'
            stbl_size, stbl_offset = get_atom_data(f, minf_offset, "stbl")
            if not stbl_size:
                raise ValueError("'stbl' atom not found.")
            print(f"stbl_size: {stbl_size}, stbl_offset: {stbl_offset}")

            # Find 'stsd' atom inside 'stbl'
            stsd_size, stsd_offset = get_atom_data(f, stbl_offset, "stsd")
            if not stsd_size:
                raise ValueError("'stsd' atom not found.")
            print(f"stsd_size: {stsd_size}, stsd_offset: {stsd_offset}")

            # Get codec information from 'stsd'
            codec_name = get_codec_info(f, stsd_offset)

            # Find 'tkhd' atom (Track Header) inside 'trak'
            tkhd_size, tkhd_offset = get_atom_data(f, trak_offset, "tkhd")
            if not tkhd_size:
                raise ValueError("'tkhd' atom not found.")
            print(f"tkhd_size: {tkhd_size}, tkhd_offset: {tkhd_offset}")

            # Read width and height from 'tkhd'
            width, height = get_width_and_height(f, tkhd_offset)

            # Calculate frame rate
            frame_rate = timescale / media_timescale

            # Print the extracted information
            print(f"File: {file_path}")
            print(f"Resolution: {width:.2f}x{height:.2f}")
            print(f"Frame rate: {frame_rate:.2f} FPS")
            print(f"Codec: {codec_name}")

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(
        dir_path, "test.mp4"
    )  # Replace with the actual path to your MP4 file
    read_mp4_info(file_path)
