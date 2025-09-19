import time
import numpy as np


def test_memory_speed(size_mb):
    # Convert size from MB to bytes
    size_bytes = size_mb * 1024 * 1024

    # Create a large array to test memory speed
    data = np.random.bytes(size_bytes)

    # Measure write speed
    start_time = time.time()
    memory_view = memoryview(data)
    write_time = time.time() - start_time

    # Measure read speed
    start_time = time.time()
    _ = memory_view.tobytes()
    read_time = time.time() - start_time

    return read_time, write_time


# Test with 100 MB of data
read_time, write_time = test_memory_speed(2000)
print(f"Read time: {read_time:.6f} seconds")
print(f"Write time: {write_time:.6f} seconds")
