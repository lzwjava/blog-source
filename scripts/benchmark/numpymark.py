import numpy as np
import time
import os


def parallel_sort_cpu(arr):
    # Sort using numpy on CPU
    return np.sort(arr)


def benchmark(list_size):
    arr = np.random.randint(0, 1_000_001, size=list_size, dtype=np.int32)
    start = time.time()
    sorted_arr = parallel_sort_cpu(arr)
    end = time.time()
    return sorted_arr, end - start


def main():
    cpu_cores = os.cpu_count()
    print(f"CPU cores: {cpu_cores}")
    times = []
    list_size = 1_000_000_000

    # Run the benchmark once (thread_counts removed)
    sorted_arr, t = benchmark(list_size)
    print(f"Time taken: {t:.4f} seconds")
    times.append(t)
    print("\nTimeTakenSeconds")
    for t in times:
        print(f"{t:.6f}")


if __name__ == "__main__":
    main()
