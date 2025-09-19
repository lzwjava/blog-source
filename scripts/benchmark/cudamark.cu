#include <cuda_runtime.h>
#include <stdio.h>
#include <stdlib.h>
#include <thrust/device_vector.h>
#include <thrust/sort.h>
#include <time.h>

void checkCudaError(cudaError_t err, const char *msg) {
    if (err != cudaSuccess) {
        fprintf(stderr, "CUDA Error: %s: %s\n", msg, cudaGetErrorString(err));
        exit(EXIT_FAILURE);
    }
}

void parallel_sort_gpu(int *arr, int n) {
    cudaError_t err;
    thrust::device_vector<int> d_vec(arr, arr + n);
    err = cudaGetLastError();
    checkCudaError(err, "After device_vector allocation");
    
    thrust::sort(d_vec.begin(), d_vec.end());
    err = cudaGetLastError();
    checkCudaError(err, "After thrust::sort");
    
    thrust::copy(d_vec.begin(), d_vec.end(), arr);
    err = cudaGetLastError();
    checkCudaError(err, "After thrust::copy");
}

double benchmark(int list_size) {
    int *arr = (int*)malloc(list_size * sizeof(int));
    if (!arr) {
        fprintf(stderr, "Host memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < list_size; ++i) {
        arr[i] = rand() % 1000001;
    }

    clock_t start = clock();
    parallel_sort_gpu(arr, list_size);
    clock_t end = clock();

    free(arr);
    return (double)(end - start) / CLOCKS_PER_SEC;
}

int main() {
    int list_size = 10000000; // Reduced for testing
    int num_runs = 8;

    printf("Run,TimeTakenSeconds\n");
    for (int i = 0; i < num_runs; ++i) {
        double t = benchmark(list_size);
        printf("%d,%.6f\n", i + 1, t);
    }
    return 0;
}