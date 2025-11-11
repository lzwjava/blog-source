---
audio: false
generated: true
lang: hant
layout: post
title: CUDA 驅動程式 API
translated: true
type: note
---

`<cuda.h>` 標頭檔案屬於 **CUDA Driver API**，這是比高階 CUDA Runtime API（例如 `cudaMalloc`、`cudaMemcpy`）更低階的應用程式介面。Driver API 提供對 GPU 資源（例如上下文、模組、流）更精細的控制，常用於進階場景，如多 GPU 程式設計、動態核心載入或低階優化。

### 常用 CUDA Driver API 函式
以下是一些關鍵函式及其用途：

| 函式                             | 描述                                                                                   |
|----------------------------------|-----------------------------------------------------------------------------------------------|
| **`cuInit(unsigned int flags)`** | 初始化 CUDA 驅動程式。必須在其他 Driver API 函式之前呼叫。              |
| **`cuDeviceGet(CUdevice *dev, int ordinal)`** | 取得指定序號（例如 `0` 代表第一個 GPU）的 GPU 裝置控制代碼。     |
| **`cuCtxCreate(CUcontext *ctx, unsigned int flags, CUdevice dev)`** | 在指定裝置上建立 CUDA 上下文。                                              |
| **`cuModuleLoad(CUmodule *mod, const char *fname)`** | 將 PTX 或 cubin 檔案載入當前上下文作為模組。                               |
| **`cuModuleGetFunction(CUfunction *func, CUmodule mod, const char *name)`** | 從已載入的模組中取得核心函式。                                             |
| **`cuMemAlloc(CUdeviceptr *dptr, size_t bytesize)`** | 在 GPU 上分配記憶體。                                                                  |
| **`cuMemcpyHtoD(CUdeviceptr dst, const void *src, size_t bytes)`** | 將資料從主機（CPU）複製到裝置（GPU）。                                                  |
| **`cuMemcpyDtoH(void *dst, CUdeviceptr src, size_t bytes)`** | 將資料從裝置（GPU）複製到主機（CPU）。                                                  |
| **`cuLaunchKernel(CUfunction f, ...)`** | 以指定的網格/區塊維度和參數啟動核心函式。               |

---

### 範例工作流程
以下是使用 CUDA Driver API 的簡化範例，用於：
1. 初始化驅動程式。
2. 分配 GPU 記憶體。
3. 與 GPU 之間複製資料。
4. 從 PTX 檔案載入核心並執行。

```cpp
#include <cuda.h>
#include <stdio.h>

int main() {
    CUdevice dev;
    CUcontext ctx;
    CUmodule mod;
    CUfunction kernel;
    CUresult err;

    // 1. 初始化 CUDA 驅動程式
    cuInit(0);

    // 2. 取得裝置 0（第一個 GPU）的控制代碼
    cuDeviceGet(&dev, 0);

    // 3. 在裝置上建立上下文
    cuCtxCreate(&ctx, 0, dev);

    // 4. 載入 PTX 模組（例如從 .cu 檔案生成）
    cuModuleLoad(&mod, "my_kernel.ptx");

    // 5. 從模組中取得核心函式
    cuModuleGetFunction(&kernel, mod, "my_kernel");

    // 6. 分配 GPU 記憶體
    size_t N = 1024;
    CUdeviceptr d_data;
    cuMemAlloc(&d_data, N * sizeof(float));

    // 7. 將資料從主機複製到裝置
    float h_data[N] = {1.0f};
    cuMemcpyHtoD(d_data, h_data, N * sizeof(float));

    // 8. 配置核心參數
    void *args[] = { &d_data, &N };
    int blockSize = 256;
    int gridSize = (N + blockSize - 1) / blockSize;

    // 9. 啟動核心
    cuLaunchKernel(
        kernel,
        gridSize, 1, 1,    // 網格維度
        blockSize, 1, 1,   // 區塊維度
        0, NULL,           // 共享記憶體和流
        args, NULL         // 核心參數
    );

    // 10. 將結果複製回主機
    cuMemcpyDtoH(h_data, d_data, N * sizeof(float));

    // 11. 清理資源
    cuMemFree(d_data);
    cuModuleUnload(mod);
    cuCtxDestroy(ctx);

    return 0;
}
```

---

### 關鍵注意事項
1. **錯誤處理**：始終檢查回傳值（例如 `CUresult err = cuSomeFunction(...);`）。使用 `cuGetErrorString(err)` 解碼錯誤。
2. **核心參數**：對於 `cuLaunchKernel`，參數以參數指標陣列形式傳遞。確保順序與核心預期參數匹配。
3. **PTX 檔案**：核心必須編譯為 PTX（例如 `nvcc --ptx my_kernel.cu -o my_kernel.ptx`）。
4. **上下文管理**：上下文類似於 CPU 進程——它們管理 GPU 的資源。在多執行緒程式碼中使用 `cuCtxPushCurrent`/`cuCtxPopCurrent`。

---

### 何時使用 Driver API？
- **動態核心載入**：在執行階段載入 PTX。
- **多 GPU 控制**：明確管理多個 GPU。
- **低階優化**：對上下文、流或記憶體進行細粒度控制。

對於大多數應用程式，高階的 **Runtime API**（例如 `cudaMalloc`、`cudaMemcpy`）已經足夠且更簡單。當您需要 Driver API 的進階功能時才使用它。