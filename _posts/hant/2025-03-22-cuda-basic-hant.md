---
audio: false
generated: true
lang: hant
layout: post
title: 基礎CUDA範例
translated: true
type: note
---

這是一個基礎的 CUDA 範例，展示使用 CUDA C 進行低階 GPU 程式設計。此範例使用最基本的 CUDA 結構在 GPU 上執行簡單的向量加法：

```c
#include <stdio.h>
#include <cuda.h>

// 用於向量加法的 CUDA 核心
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // 向量大小
    size_t size = n * sizeof(float);
    
    // 主機記憶體配置
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // 初始化主機陣列
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // 裝置記憶體指標
    float *d_a, *d_b, *d_c;
    
    // 配置裝置記憶體
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // 將資料從主機複製到裝置
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // 設定核心啟動參數
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // 啟動核心
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // 等待 GPU 完成
    cudaDeviceSynchronize();

    // 將結果複製回主機
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // 驗證結果
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // 釋放裝置記憶體
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // 釋放主機記憶體
    free(h_a);
    free(h_b);
    free(h_c);

    // 重設裝置
    cudaDeviceReset();

    return 0;
}
```

要編譯和執行此程式碼，您需要：
1. 支援 CUDA 的 NVIDIA GPU
2. 已安裝 CUDA Toolkit
3. 使用以下指令編譯：`nvcc vector_add.cu -o vector_add`

此範例展示了最基本的 CUDA 操作：
- `__global__` 核心定義
- 使用 `cudaMalloc` 手動配置記憶體
- 使用 `cudaMemcpy` 明確傳輸記憶體
- 使用 `<<<blocks, threads>>>` 設定核心啟動配置
- 裝置同步
- 記憶體清理

關鍵低階層面：
1. 直接記憶體管理，不使用 CUDA runtime helpers
2. 手動執行緒/區塊配置
3. 明確的裝置同步
4. 原始指標操作
5. 不使用高階抽象或函式庫

核心使用基本的 CUDA 執行緒層級結構：
- `blockIdx.x`：區塊索引
- `blockDim.x`：每個區塊的執行緒數量
- `threadIdx.x`：區塊內的執行緒索引

這會為每個元素計算唯一的執行緒 ID，並僅在範圍內執行加法。此範例保持簡單，但展示了 CUDA 程式設計在低階層面的核心概念。

輸出將顯示前 10 個結果，例如：
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```