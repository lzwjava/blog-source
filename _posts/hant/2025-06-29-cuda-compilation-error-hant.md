---
audio: false
generated: true
lang: hant
layout: post
title: 修正使用 nvcc 時的 CUDA 編譯錯誤
translated: true
type: note
---

錯誤訊息顯示 CUDA 工具包未安裝或配置不正確，因為編譯器無法找到 `cuda.h`。此外，您的程式碼是 CUDA 原始檔（`.cu`），但您嘗試使用 `gcc` 編譯，這並不適用於 CUDA 程式碼。您需要使用 NVIDIA CUDA 編譯器 `nvcc`。以下是解決方法：

### 解決步驟

1. **安裝 CUDA 工具包**：
   - 確保系統已安裝 NVIDIA CUDA 工具包。您可從 [NVIDIA CUDA 工具包網站](https://developer.nvidia.com/cuda-downloads)下載。
   - 根據您的作業系統（根據提示應為 Linux）遵循安裝說明。
   - 安裝後，執行以下指令驗證：
     ```bash
     nvcc --version
     ```
     若安裝正確，將顯示 CUDA 版本。

2. **使用 `nvcc` 編譯**：
   - 由於您的檔案是 CUDA 原始檔（`.cu`），請改用 `nvcc` 編譯。將：
     ```bash
     gcc scripts/benchmark/cudamark.c
     ```
     改為：
     ```bash
     nvcc scripts/benchmark/cudamark.cu
     ```
   - 注意：請確保副檔名與實際檔案相符（您程式碼中是 `.cu` 而非錯誤訊息中的 `.c`）。

3. **設定 CUDA 環境**：
   - 確保環境變數包含 CUDA 工具包路徑。將以下內容加入 `~/.bashrc` 或對應的 shell 設定檔：
     ```bash
     export PATH=/usr/local/cuda/bin:$PATH
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     接著重新載入設定檔：
     ```bash
     source ~/.bashrc
     ```

4. **連結 Thrust 函式庫**：
   - 您的程式碼使用 CUDA 工具包內建的 Thrust，因此無需明確連結額外函式庫。但請確保 CUDA 版本相容（CUDA 7.0 及以上版本包含 Thrust）。

5. **修正程式碼問題**：
   - 程式碼引用 `thread_counts` 但未在 `benchmark` 函式中使用。`parallel_sort_gpu` 函式使用 Thrust，其內部管理並行處理，因此 `main` 中的 `thread_counts` 迴圈易造成誤解。若需對不同執行緒配置進行基準測試，請注意 Thrust 的排序功能不允許直接控制執行緒數量。建議釐清此邏輯或移除未使用的 `thread_counts`。
   - 為求清晰，可修改程式碼以多次對相同列表大小進行基準測試，計算平均時間：

     ```cuda
     #include <stdio.h>
     #include <stdlib.h>
     #include <cuda.h>
     #include <thrust/device_vector.h>
     #include <thrust/sort.h>
     #include <time.h>

     void parallel_sort_gpu(int *arr, int n) {
         thrust::device_vector<int> d_vec(arr, arr + n);
         thrust::sort(d_vec.begin(), d_vec.end());
         thrust::copy(d_vec.begin(), d_vec.end(), arr);
     }

     double benchmark(int list_size) {
         int *arr = (int*)malloc(list_size * sizeof(int));
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
         int list_size = 50000000;
         int num_runs = 8; // 用於計算平均值的執行次數

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```

6. **編譯更新後的程式碼**：
   - 將程式碼儲存為 `cudamark.cu` 並編譯：
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ```
   - 若遇到連結錯誤，請確保 CUDA 函式庫可正常存取（參見步驟 3）。

7. **執行程式**：
   - 執行編譯後的二進位檔：
     ```bash
     ./cudamark
     ```

8. **補充說明**：
   - **副檔名**：請確保檔案使用 `.cu` 副檔名，CUDA 檔案需透過此副檔名才能由 `nvcc` 正確處理。
   - **GPU 可用性**：請確保擁有支援 CUDA 的 GPU 並安裝正確驅動程式。可透過以下指令檢查：
     ```bash
     nvidia-smi
     ```
   - **Thrust 與 CUDA 版本**：請確認 CUDA 版本支援 Thrust。建議使用 CUDA 11.x 或更新版本以獲得現代 Thrust 功能。
   - **計時精確度**：`clock()` 函式測量的是 CPU 時間，而非 GPU 執行時間。若需更精確的 GPU 計時，建議使用 CUDA 事件：
     ```cuda
     cudaEvent_t start, stop;
     cudaEventCreate(&start);
     cudaEventCreate(&stop);
     cudaEventRecord(start);
     parallel_sort_gpu(arr, list_size);
     cudaEventRecord(stop);
     cudaEventSynchronize(stop);
     float milliseconds = 0;
     cudaEventElapsedTime(&milliseconds, start, stop);
     return milliseconds / 1000.0; // 轉換為秒
     ```

9. **若錯誤持續出現**：
   - 若仍找不到 `cuda.h`，請驗證 CUDA 工具包安裝路徑（例如 `/usr/local/cuda/include`）。可能需要明確指定包含路徑：
     ```bash
     nvcc -I/usr/local/cuda/include -o cudamark scripts/benchmark/cudamark.cu
     ```
   - 請確認檔案路徑 `scripts/benchmark/cudamark.cu` 相對於當前目錄是否正確。

### 更新後的編譯指令
```bash
nvcc -o cudamark scripts/benchmark/cudamark.cu
```

### 預期輸出
問題修正後，執行 `./cudamark` 應產生類似以下輸出：
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

若需要進一步協助或遇到特定錯誤，請隨時分享！