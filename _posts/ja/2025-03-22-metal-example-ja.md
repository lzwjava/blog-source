---
audio: false
generated: true
lang: ja
layout: post
title: メタルベクトル加算の例
translated: true
type: note
---

macOSでGPUをプログラミングする場合、Metal（Appleの低レベルグラフィックスおよびコンピュートAPI）を使用して、私が以前提供したCUDAの例と同様の機能を実現できます。Metalは、Macを含むAppleデバイス上のGPUへの直接アクセスを提供するように設計されており、グラフィックスとコンピュート操作の両方をサポートしています。以下は、C++での低レベルMetalコンストラクトを使用してベクトル加算（CUDAの例と同様）を実行する基本的なMetalの例です。

### Metal ベクトル加算の例

この例では、GPU上で2つの配列を加算するためにMetalを使用します。高レベルの抽象化を避け、低レベルアプローチのためにコアMetal APIに固執しています。

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // Metalデバイスの初期化
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Metalデバイスの作成に失敗しました" << std::endl;
        return 1;
    }

    // ベクトルサイズ
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // ホストデータ
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // ホスト配列の初期化
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // Metalバッファの作成
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // コマンドキューの作成
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // Metalシェーダーソースの読み込み（ベクトル加算カーネル）
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

    // Metalライブラリと関数の作成
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "ライブラリの作成に失敗しました: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "関数の作成に失敗しました" << std::endl;
        return 1;
    }

    // コンピュートパイプライン状態の作成
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "パイプラインの作成に失敗しました: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // コマンドバッファとエンコーダーの作成
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // パイプラインとバッファの設定
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // スレッドグループの設定
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // コンピュートカーネルのディスパッチ
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // 実行と待機
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // 結果の取得
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // クリーンアップ
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### 前提条件
1. **macOS**: このコードは互換性のあるGPUを搭載したmacOS上で動作します（最新のMacであれば動作するはずです）。
2. **Xcode**: Metalフレームワークとコマンドラインツールを入手するためにXcodeをインストールしてください。
3. **コンパイル**: Metalフレームワークを使用して`clang++`でコンパイルします：
   ```bash
   clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
   ```
   注意：Objective-C++を使用しているため（MetalはObjective-Cランタイムを必要とします）、ファイルは`.mm`拡張子で保存してください。

### 主な低レベル側面
1. **手動リソース管理**: `newBuffer`で明示的にバッファを作成し、高レベルラッパーなしでメモリを管理します。
2. **直接シェーダー定義**: Metal Shading Language（MSL）カーネルは文字列としてインラインで定義され、実行時にコンパイルされます。
3. **スレッド設定**: CUDAのブロックとスレッドに似た、グリッドとスレッドグループサイズを手動で計算します。
4. **コマンドバッファ制御**: GPU実行のために明示的にコマンドバッファを作成しコミットします。
5. **抽象化なし**: MetalKitや他の高レベルフレームワークを避け、コアMetal APIに固執します。

### 出力
これを実行すると、以下のような出力が得られます：
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### CUDAとの違い
- **APIスタイル**: Metalは`NS::`オブジェクトを使用したObjective-C++ベースのAPIを使用しますが、CUDAはCスタイルのAPIです。
- **メモリモデル**: Metalの共有ストレージモード（`MTL::ResourceStorageModeShared`）はCPU/GPUが同じメモリにアクセスすることを可能にし、CUDAの明示的な`cudaMemcpy`と比較して転送を簡素化します。
- **スレッドモデル**: Metalはグリッド/スレッドグループサイズで`dispatchThreads`を使用します。概念的にはCUDAのグリッド/ブロックモデルに似ていますが、用語と設定が異なります。

### macOSでのMetal使用に関するヒント
- **デバッグ**: GPU実行を検査するためにXcodeのMetalデバッガーを使用してください。
- **ドキュメント**: 詳細についてはAppleのMetalドキュメントを参照してください（Xcode内またはdeveloper.apple.comでオンラインで利用可能）。
- **パフォーマンス**: より大きなデータセットの場合、`maxTotalThreadsPerThreadgroup`に基づいてスレッドグループサイズを最適化してください。

これはmacOSでの低レベルMetalプログラミングの出発点です。必要に応じて、より複雑なコンピュートタスクやグラフィックスレンダリングに拡張できます！