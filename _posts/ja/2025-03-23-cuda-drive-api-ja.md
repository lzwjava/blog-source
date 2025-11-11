---
audio: false
generated: true
lang: ja
layout: post
title: CUDAドライバAPI
translated: true
type: note
---

`<cuda.h>`ヘッダーは、**CUDA Driver API**の一部であり、高レベルなCUDA Runtime API（例: `cudaMalloc`, `cudaMemcpy`）と比較して低レベルなAPIです。Driver APIは、GPUリソース（コンテキスト、モジュール、ストリームなど）をより細かく制御でき、マルチGPUプログラミング、動的カーネル読み込み、低レベル最適化などの高度なシナリオでよく使用されます。

### 主なCUDA Driver API関数
以下に、主要な関数とその目的を示します:

| 関数                                | 説明                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------|
| **`cuInit(unsigned int flags)`** | CUDAドライバを初期化します。他のDriver API関数を呼び出す前に必ず呼び出す必要があります。 |
| **`cuDeviceGet(CUdevice *dev, int ordinal)`** | 指定されたオーディナル（例: 最初のGPUの場合は`0`）のGPUデバイスへのハンドルを取得します。 |
| **`cuCtxCreate(CUcontext *ctx, unsigned int flags, CUdevice dev)`** | 指定されたデバイス上にCUDAコンテキストを作成します。 |
| **`cuModuleLoad(CUmodule *mod, const char *fname)`** | PTXまたはcubinファイルを現在のコンテキストにモジュールとして読み込みます。 |
| **`cuModuleGetFunction(CUfunction *func, CUmodule mod, const char *name)`** | 読み込まれたモジュールからカーネル関数を取得します。 |
| **`cuMemAlloc(CUdeviceptr *dptr, size_t bytesize)`** | GPU上にメモリを割り当てます。 |
| **`cuMemcpyHtoD(CUdeviceptr dst, const void *src, size_t bytes)`** | ホスト（CPU）からデバイス（GPU）へデータをコピーします。 |
| **`cuMemcpyDtoH(void *dst, CUdeviceptr src, size_t bytes)`** | デバイス（GPU）からホスト（CPU）へデータをコピーします。 |
| **`cuLaunchKernel(CUfunction f, ...)`** | 指定されたグリッド/ブロック次元とパラメータでカーネル関数を起動します。 |

---

### ワークフローの例
以下は、CUDA Driver APIを使用して以下の操作を行う簡略化された例です:
1. ドライバの初期化
2. GPUメモリの割り当て
3. GPUとの間でのデータコピー
4. PTXファイルからカーネルを読み込んで実行

```cpp
#include <cuda.h>
#include <stdio.h>

int main() {
    CUdevice dev;
    CUcontext ctx;
    CUmodule mod;
    CUfunction kernel;
    CUresult err;

    // 1. CUDAドライバの初期化
    cuInit(0);

    // 2. デバイス0（最初のGPU）へのハンドルを取得
    cuDeviceGet(&dev, 0);

    // 3. デバイス上にコンテキストを作成
    cuCtxCreate(&ctx, 0, dev);

    // 4. PTXモジュールの読み込み（例: .cuファイルから生成）
    cuModuleLoad(&mod, "my_kernel.ptx");

    // 5. モジュールからカーネル関数を取得
    cuModuleGetFunction(&kernel, mod, "my_kernel");

    // 6. GPUメモリの割り当て
    size_t N = 1024;
    CUdeviceptr d_data;
    cuMemAlloc(&d_data, N * sizeof(float));

    // 7. ホストからデバイスへデータをコピー
    float h_data[N] = {1.0f};
    cuMemcpyHtoD(d_data, h_data, N * sizeof(float));

    // 8. カーネルパラメータの設定
    void *args[] = { &d_data, &N };
    int blockSize = 256;
    int gridSize = (N + blockSize - 1) / blockSize;

    // 9. カーネルの起動
    cuLaunchKernel(
        kernel,
        gridSize, 1, 1,    // グリッド次元
        blockSize, 1, 1,   // ブロック次元
        0, NULL,           // 共有メモリとストリーム
        args, NULL         // カーネル引数
    );

    // 10. 結果をホストにコピー back
    cuMemcpyDtoH(h_data, d_data, N * sizeof(float));

    // 11. クリーンアップ
    cuMemFree(d_data);
    cuModuleUnload(mod);
    cuCtxDestroy(ctx);

    return 0;
}
```

---

### 主な注意点
1. **エラーハンドリング**: 戻り値（例: `CUresult err = cuSomeFunction(...);`）を常にチェックしてください。エラーのデコードには`cuGetErrorString(err)`を使用します。
2. **カーネルパラメータ**: `cuLaunchKernel`の場合、パラメータは引数へのポインタの配列として渡されます。順序がカーネルが期待するパラメータと一致していることを確認してください。
3. **PTXファイル**: カーネルはPTXにコンパイルする必要があります（例: `nvcc --ptx my_kernel.cu -o my_kernel.ptx`）。
4. **コンテキスト管理**: コンテキストはCPUプロセスに類似しており、GPUのリソースを管理します。マルチスレッドコードでは`cuCtxPushCurrent`/`cuCtxPopCurrent`を使用します。

---

### Driver APIを使用する場合
- **動的カーネル読み込み**: 実行時にPTXを読み込む場合
- **マルチGPU制御**: 複数のGPUを明示的に管理する場合
- **低レベル最適化**: コンテキスト、ストリーム、メモリをきめ細かく制御する必要がある場合

ほとんどのアプリケーションでは、高レベルな**Runtime API**（例: `cudaMalloc`, `cudaMemcpy`）で十分であり、より簡単です。高度な機能が必要な場合にDriver APIを使用してください。