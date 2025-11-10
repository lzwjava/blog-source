---
audio: false
generated: true
image: false
lang: ja
layout: post
title: CUDAライブラリとパッケージ
translated: true
type: note
---

以下に、インストールする各パッケージの概要を説明します：

* **nvidia-cusparselt-cu12**
  NVIDIAのcuSPARSELtライブラリ。CUDA 12上で超効率的な低精度スパース行列演算を提供します。

* **nvidia-cusparse-cu12**
  cuSPARSEライブラリ。CUDA 12上で一般的なスパース線形代数ルーチン（スパースソルバーなど）を提供します。

* **nvidia-cudnn-cu12**
  cuDNNライブラリ。深層ニューラルネットワーク向けに高度に最適化された基本演算（畳み込み、プーリング、活性化関数など）をCUDA 12上で提供します。

* **nvidia-cublas-cu12**
  cuBLASライブラリ。高性能な密行列線形代数（BLAS）ルーチンをCUDA 12上で実装します。

* **nvidia-cufft-cu12**
  cuFFTライブラリ。CUDA 12デバイス上で高速フーリエ変換を計算します。

* **nvidia-cusolver-cu12**
  cuSOLVERライブラリ。CUDA 12上で、密行列およびスパース行列の直接ソルバー、固有値問題などのルーチンを提供します。

* **nvidia-curand-cu12**
  cuRANDライブラリ。CUDA 12上で高品質な乱数生成を提供します。

* **nvidia-cufile-cu12**
  cuFileライブラリ。CUDA 12上で直接的な非同期GPUアクセラレーテッドファイルI/Oを可能にします。

* **nvidia-nvtx-cu12**
  NVTX（NVIDIA Tools Extension）。CUDA 12上でコード範囲の注釈付けとプロファイリングを行います。

* **nvidia-nvjitlink-cu12**
  NVJITLinkライブラリ。CUDA 12上でランタイム時にCUDAカーネルをJITリンクします。

* **nvidia-cuda-nvrtc-cu12**
  NVRTCランタイムコンパイラ。CUDA 12環境下でCUDA Cカーネルをオンザフライでコンパイルします。

* **nvidia-cuda-cupti-cu12**
  CUPTI（CUDA Profiling Tools Interface）。CUDA 12上で詳細なプロファイリングおよびトレーシングデータを収集します。

* **nvidia-cuda-runtime-cu12**
  コアCUDAランタイムライブラリ。CUDA 12上でのカーネル管理と起動を担当します。

* **nvidia-nccl-cu12**
  NCCLライブラリ。CUDA 12上で効率的なマルチGPUおよびマルチノードの集団通信プリミティブを提供します。

* **torch**
  メインのPyTorchライブラリ。テンソル演算、自動微分、深層学習モデルの構築を提供します。

* **networkx**
  複雑なネットワークとグラフ構造の作成、操作、解析のためのPythonパッケージです。

* **mpmath**
  任意精度の実数および複素数演算のための純粋なPythonライブラリです。

* **sympy**
  記号数学（代数、微積分、方程式求解など）のためのPythonライブラリです。

* **triton**
  生のCUDAよりも簡単にカスタムの高性能GPUカーネルを記述できる言語およびコンパイラです。