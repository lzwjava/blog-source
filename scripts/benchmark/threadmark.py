# filepath: /home/lzw/projects/lzwjava.github.io/scripts/benchmark/threadmark.py
import threading
import random
import time
import os
import matplotlib.pyplot as plt


def sort_chunk(arr, start, end, result, idx):
    chunk = arr[start:end]
    chunk.sort()
    result[idx] = chunk


def merge(left, right):
    result = []
    i = j = 0
    left_len, right_len = len(left), len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def parallel_sort(arr, thread_count):
    n = len(arr)
    chunk_size = (n + thread_count - 1) // thread_count
    threads = []
    results = [None] * thread_count

    # Sort each chunk in a separate thread
    for i in range(thread_count):
        start = i * chunk_size
        end = min(start + chunk_size, n)
        t = threading.Thread(target=sort_chunk, args=(arr, start, end, results, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    sorted_chunks = results

    # Merge sorted chunks
    while len(sorted_chunks) > 1:
        merged_chunks = []
        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged = merge(sorted_chunks[i], sorted_chunks[i + 1])
                merged_chunks.append(merged)
            else:
                merged_chunks.append(sorted_chunks[i])
        sorted_chunks = merged_chunks

    return sorted_chunks[0] if sorted_chunks else []


def benchmark(thread_count=1, list_size=1000000):
    arr = [random.randint(0, 1000000) for _ in range(list_size)]
    start = time.time()
    parallel_sort(arr, thread_count)
    end = time.time()
    return end - start


if __name__ == "__main__":
    print(f"CPU cores: {os.cpu_count()}")
    thread_counts = [1, 2, 4, 8, 16, 32, 64]
    times = []
    list_size = 10_000_000  # Adjust for reasonable runtime

    for n in thread_counts:
        t = benchmark(thread_count=n, list_size=list_size)
        print(f"Threads: {n}, Time taken: {t:.4f} seconds")
        times.append(t)

    # Print results as CSV for external plotting
    print("\nThreadCount,TimeTakenSeconds")
    for i in range(len(thread_counts)):
        print(f"{thread_counts[i]},{times[i]:.6f}")

    plt.figure()
    plt.plot(thread_counts, times, marker="o")
    plt.xlabel("Number of Threads")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Thread Count vs Time Taken")
    plt.grid(True)
    plt.savefig("test/thread.png")
