---
audio: false
generated: true
lang: ja
layout: post
title: 基本的なCUDAの例
translated: true
type: note
---

以下は、CUDA Cを使用した低レベルGPUプログラミングを示す基本的なCUDAの例です。この例は、最も基本的なCUDA構成要素を使用してGPU上で単純なベクトル加算を実行します：

```c
#include <stdio.h>
#include <cuda.h>

// ベクトル加算用のCUDAカーネル
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // ベクトルサイズ
    size_t size = n * sizeof(float);
    
    // ホストメモリの割り当て
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // ホスト配列の初期化
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // デバイスメモリポインタ
    float *d_a, *d_b, *d_c;
    
    // デバイスメモリの割り当て
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // ホストからデバイスへデータをコピー
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // カーネル起動パラメータの設定
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // カーネルの起動
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // GPUの完了を待機
    cudaDeviceSynchronize();

    // 結果をホストにコピー
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // 結果の検証
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // デバイスメモリの解放
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // ホストメモリの解放
    free(h_a);
    free(h_b);
    free(h_c);

    // デバイスのリセット
    cudaDeviceReset();

    return 0;
}
```

このコードをコンパイルして実行するには、以下が必要です：
1. CUDAをサポートするNVIDIA GPU
2. インストールされたCUDA Toolkit
3. コンパイルコマンド：`nvcc vector_add.cu -o vector_add`

この例は、最も基本的なCUDA操作を示しています：
- `__global__`カーネル定義
- `cudaMalloc`による手動メモリ割り当て
- `cudaMemcpy`による明示的なメモリ転送
- `<<<blocks, threads>>>`によるカーネル起動設定
- デバイスの同期
- メモリのクリーンアップ

主な低レベル側面：
1. CUDAランタイムヘルパーを使用しない直接メモリ管理
2. 手動のスレッド/ブロック設定
3. 明示的なデバイス同期
4. 生ポインタ操作
5. 高レベル抽象化やライブラリの不使用

カーネルは基本的なCUDAスレッド階層を使用します：
- `blockIdx.x`：ブロックインデックス
- `blockDim.x`：ブロックあたりのスレッド数
- `threadIdx.x`：ブロック内のスレッドインデックス

これは各要素に対して一意のスレッドIDを計算し、境界内にある場合のみ加算を実行します。この例はシンプルに保っていますが、低レベルでのCUDAプログラミングの核心概念を示しています。

出力は最初の10件の結果を表示します：
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```