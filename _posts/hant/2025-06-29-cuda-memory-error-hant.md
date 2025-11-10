---
audio: false
generated: true
lang: hant
layout: post
title: 解決Thrust CUDA記憶體分配錯誤
translated: true
type: note
---

錯誤 `thrust::system::detail::bad_alloc` 伴隨 `cudaErrorUnknown: unknown error` 以及後續的 `Aborted (core dumped)` 表明您的 CUDA 程式在執行時出現問題，很可能與使用 Thrust 進行排序時的記憶體分配或 GPU 相容性有關。此錯誤通常發生在 CUDA 執行時遇到問題時，例如 GPU 記憶體不足、GPU 不相容或 CUDA 環境配置錯誤。以下我將根據提供的程式碼和錯誤，列出診斷和修復問題的步驟。

### 修復步驟

1. **檢查 GPU 記憶體可用性**：
   - 您的程式使用 Thrust 的 `device_vector` 在 GPU 上分配了一個大型陣列（`list_size = 50,000,000` 個整數，約 200 MB）。如果您的 GPU 記憶體有限或其他進程正在使用它，可能會導致 `bad_alloc` 錯誤。
   - 執行 `nvidia-smi` 以檢查 GPU 記憶體使用情況：
     ```bash
     nvidia-smi
     ```
   - 確保 GPU 上有足夠的可用記憶體。如果其他進程佔用了記憶體，請終止它們或重新啟動以釋放資源。
   - **修復**：減少 `list_size` 以測試問題是否與記憶體相關。在 `main` 中嘗試設定 `list_size = 10,000,000`（40 MB）：
     ```cuda
     int list_size = 10000000;
     ```

2. **驗證 CUDA 安裝和 GPU 相容性**：
   - `cudaErrorUnknown` 表明可能存在 CUDA 驅動程式、執行時或 GPU 相容性問題。請驗證您的 CUDA 設定：
     ```bash
     nvcc --version
     nvidia-smi
     ```
   - 確保 CUDA 工具包版本與驅動程式版本匹配。例如，CUDA 11.x 需要相容的 NVIDIA 驅動程式（請查閱 [NVIDIA 相容性表](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)）。
   - **修復**：將您的 NVIDIA 驅動程式和 CUDA 工具包更新到最新版本。對於 Ubuntu，您可以使用以下指令更新驅動程式：
     ```bash
     sudo apt update
     sudo apt install nvidia-driver-<version> nvidia-cuda-toolkit
     ```
     將 `<version>` 替換為與您的 GPU 相容的最新驅動程式版本。

3. **檢查 CUDA 錯誤處理**：
   - 程式碼缺乏明確的 CUDA 錯誤檢查，這有助於準確定位問題。修改 `parallel_sort_gpu` 以包含 CUDA 操作的錯誤檢查：
     ```cuda
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
         if (!arr