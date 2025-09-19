import torch
import time
import os


def parallel_sort_gpu(arr):
    # Move data to GPU, sort, then move back to CPU
    arr_gpu = arr.to("cuda")
    sorted_arr_gpu = torch.sort(arr_gpu).values
    return sorted_arr_gpu.cpu()


def benchmark(list_size):
    arr = torch.randint(0, 1_000_001, (list_size,), dtype=torch.int32)
    start = time.time()
    sorted_arr = parallel_sort_gpu(arr)
    end = time.time()
    return sorted_arr, end - start


def main():
    if not torch.cuda.is_available():
        print("CUDA is not available. Exiting.")
        return

    cpu_cores = os.cpu_count()
    print(f"CPU cores: {cpu_cores}")
    print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    times = []
    list_size = 1_000_000_000

    # Run the benchmark once
    sorted_arr, t = benchmark(list_size)
    print(f"Time taken: {t:.4f} seconds")
    times.append(t)
    print("\nTimeTakenSeconds")
    for t in times:
        print(f"{t:.6f}")


if __name__ == "__main__":
    main()
