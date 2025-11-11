---
audio: false
generated: true
lang: hant
layout: post
title: 金屬向量加法示例
translated: true
type: note
---

若你正在使用 macOS，並希望透過 Metal（Apple 的低階圖形與計算 API）來對 GPU 進行編程，你可以實現與我之前提供的 CUDA 範例類似的功能。Metal 旨在讓你直接存取 Apple 裝置上的 GPU，包括 Mac，並支援圖形與計算操作。以下是一個基礎的 Metal 範例，使用 C++ 中的低階 Metal 結構來執行向量加法（類似於 CUDA 範例）。

### Metal 向量加法範例

此範例使用 Metal 在 GPU 上對兩個陣列進行加法運算。它避開高階抽象，堅持使用核心 Metal API 以實現低階方法。

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // 初始化 Metal 裝置
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Failed to create Metal device" << std::endl;
        return 1;
    }

    // 向量大小
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // 主機資料
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // 初始化主機陣列
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // 建立 Metal 緩衝區
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // 建立命令佇列
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // 載入 Metal 著色器原始碼（向量加法核心）
    const char* kernelSource = R"(
        #include <metal_stdlib>
        using namespace metal;

        kernel void vectorAdd(device const float* a,
                             device const float* b,
                             device float* c,
                             uint id [[thread_position_in_grid]]) {
            c[id] = a[id] + b[id];
        }
    )";

    // 建立 Metal 程式庫與函式
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "Failed to create library: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "Failed to create function" << std::endl;
        return 1;
    }

    // 建立計算管線狀態
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "Failed to create pipeline: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // 建立命令緩衝區與編碼器
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // 設定管線與緩衝區
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // 配置執行緒群組
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // 派發計算核心
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // 執行並等待
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // 取得結果
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // 清理
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### 必要條件
1. **macOS**：此程式碼需在 macOS 上執行，並配備相容的 GPU（任何現代 Mac 皆應適用）。
2. **Xcode**：安裝 Xcode 以取得 Metal 框架與命令列工具。
3. **編譯**：使用 `clang++` 並連結 Metal 框架：
   ```bash
   clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
   ```
   注意：請將檔案儲存為 `.mm` 副檔名，因為它使用了 Objective-C++（Metal 需要 Objective-C 執行環境）。

### 關鍵低階層面
1. **手動資源管理**：明確使用 `newBuffer` 建立緩衝區，並在無高階封裝的情況下管理記憶體。
2. **直接著色器定義**：Metal 著色語言（MSL）核心以字串形式內聯定義，並在執行時期編譯。
3. **執行緒配置**：手動計算網格與執行緒群組大小，類似於 CUDA 的區塊與執行緒概念。
4. **命令緩衝區控制**：明確建立並提交命令緩衝區以執行 GPU 運算。
5. **無抽象化**：避免使用 MetalKit 或其他高階框架，僅使用核心 Metal API。

### 輸出
執行此程式將產生類似以下的輸出：
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### 與 CUDA 的差異
- **API 風格**：Metal 使用基於 Objective-C++ 的 API 與 `NS::` 物件，不同於 CUDA 的 C 風格 API。
- **記憶體模型**：Metal 的共享儲存模式（`MTL::ResourceStorageModeShared`）允許 CPU/GPU 存取同一記憶體，相較於 CUDA 的明確 `cudaMemcpy` 更為簡化。
- **執行緒模型**：Metal 使用 `dispatchThreads` 與網格/執行緒群組大小，概念上類似 CUDA 的網格/區塊模型，但術語與配置方式不同。

### macOS 上使用 Metal 的提示
- **除錯**：使用 Xcode 的 Metal 除錯器來檢查 GPU 執行情況。
- **文件**：查閱 Apple 的 Metal 文件以獲取更深入的細節（可在 Xcode 或 developer.apple.com 線上取得）。
- **效能**：對於較大的資料集，根據 `maxTotalThreadsPerThreadgroup` 優化執行緒群組大小。

這是 macOS 上低階 Metal 編程的起點。你可以根據需要擴展它以處理更複雜的計算任務或圖形渲染！