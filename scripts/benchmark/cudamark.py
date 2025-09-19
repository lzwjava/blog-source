import cupy as cp
import numpy as np
import time
import os


def parallel_sort_gpu(arr):
    # Transfer to GPU, sort, and transfer back
    gpu_arr = cp.array(arr)
    gpu_arr = cp.sort(gpu_arr)
    return cp.asnumpy(gpu_arr)


def benchmark(list_size):
    arr = np.random.randint(0, 1_000_001, size=list_size, dtype=np.int32)
    start = time.time()
    sorted_arr = parallel_sort_gpu(arr)
    end = time.time()
    return sorted_arr, end - start


def main():
    cpu_cores = os.cpu_count()
    print(f"CPU cores: {cpu_cores}")
    thread_counts = [1, 2, 4, 8, 16, 32, 64, 128]
    times = []
    list_size = 50_000_000

    for n in thread_counts:
        sorted_arr, t = benchmark(list_size)
        print(f"Threads: {n}, Time taken: {t:.4f} seconds")
        times.append(t)
    print("\nThreadCount,TimeTakenSeconds")
    for n, t in zip(thread_counts, times):
        print(f"{n},{t:.6f}")


if __name__ == "__main__":
    main()
