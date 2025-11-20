---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPU SM制限と最大自動チューニング
translated: true
type: note
---

警告「Not enough SMs to use max_autotune_gemm」は、PyTorchのTorchInductorバックエンド（`torch.compile`で`mode="max-autotune"`または同様の積極的オートチューニングモードを使用した際に利用）から発生します。これは、GPUのStreaming Multiprocessors（SM）の数が、最も網羅的なGEMM（行列乗算）オートチューニングオプションに必要な閾値よりも少ないことを示しています。このオプションは、最高のパフォーマンスを得るためにTriton/CUTLASSカーネル設定の広大な空間を探索します。

PyTorchは、GPUが十分な数のSM（通常は≥68〜80、正確な数はPyTorchのバージョンに依存。例: RTX 3080/3090は境界線上、A100/H100/RTX 4090は余裕をもって上回る）を持つ場合にのみ、そのGPUを「十分に大きい」と見なします。より小型のGPU（例: RTX 3060, 3070, 2080 Ti, T4など）では、過剰なコンパイル時間や最適でない選択を避けるために、完全な`max_autotune_gemm`パスを無効にします。

### 発生理由と影響
- オートチューニングはコンパイル時に多くのカーネルバリアントをベンチマークします。完全なGEMMオートチューニングは、最も積極的なテンプレートを価値あるものにするために十分な並列性（SM）を必要とします。
- この警告は**無害**です — コンパイルは成功し、良好な（ただし絶対的な最大ではない）パフォーマンスが得られます。他のオートチューニング（GEMM以外の部分、あまり積極的でないGEMM探索）は依然として実行されます。
- これは、ユーザーが推測するような、バッチサイズやモデルアーキテクチャに起因するパディング/非効率性を意味する**ものではありません**。この特定の警告は、入力/形状のパディングに関するものではなく、純粋にGPUのサイズに関するものです。

### 改善方法または回避策
1. **より多くのSMを持つGPUを使用する**（真の最大パフォーマンスに対する最善の解決策）:
   - 信頼性のある完全な`max_autotune_gemm`のための推奨最小値: RTX 4090 (128 SM), A100 (108 SM), H100 (132+ SM)、または新しいデータセンター向けカード。
   - 約80 SM未満のコンシューマー向けカード（例: RTX 3070 = 46 SM, RTX 3080 = 68 SM）では、この警告が発生します。

   | GPU 例           | SM数     | 完全な max_autotune_gemm? |
   |------------------|----------|---------------------------|
   | RTX 3060/3070    | 46–58   | いいえ                    |
   | RTX 3080/3090    | 68–82   | 境界線 (場合によりはい)    |
   | RTX 4090         | 128     | はい                      |
   | A100             | 108     | はい                      |
   | H100             | 132+    | はい                      |

2. **torch.compileモードを変更する**（ハードウェアの変更は不要）:
   - `mode="max-autotune-no-cudagraphs"`を使用する — オートチューニングの利点の大部分を維持しつつ、CUDAグラフとSMによって制限されるGEMMパスをスキップします。小型GPUでは、コンパイル時間を大幅に短縮しつつ、ほぼ同等の速度が出ることが多いです。
   - または `mode="reduce-overhead"` — 軽量で、低レイテンシのためにCUDAグラフを使用します。推論に適しています。
   - 例:
     ```python
     compiled_model = torch.compile(model, mode="max-autotune-no-cudagraphs", fullgraph=True)
     ```

3. **高精度な行列乗算を有効にする**（任意のモード/GPUで有効）:
   ```python
   torch.set_float32_matmul_precision("high")  # または "highest"
   ```
   これにより、TensorFloat-32 / より優れたcuBLASカーネルが使用可能になります。

4. **とにかくより積極的なチューニングを強制する**（ハック的、公式サポート外）:
   - PyTorchソースコード内のチェックをモンキーパッチする（`torch/_inductor/utils.py`を編集するか、実行時にパッチする）ことで、SMの閾値を下げます。リスクが高く、パフォーマンスを損なったり、コンパイル時間が爆発的に増加したりする可能性があります。

5. **配置/効率性を向上させるためのその他の一般的なヒント**（この正確な警告とは無関係ですが、パディングに関する懸念に対処します）:
   - 可能であれば、バッチ/シーケンスの次元を8/16/32の倍数にパディングします（Tensorコアで一般的）。
   - ワークロードが許せばバッチサイズを増やします — 大きなGEMMはGPUをより効率的に利用します。
   - 推論に重点を置くワークロードの場合、`torch.compile`の制限が続く場合は、vLLM、TensorRT-LLM、Hugging Face Optimumなどの代替手段を検討してください。

ほとんどの実際のケースでは、完全な`max_autotune_gemm`がなくてもパフォーマンスの差は小さく（数パーセント）、コンシューマー向けGPUでは`max-autotune-no-cudagraphs`で95%以上の性能を達成できます。

[PyTorch Inductor utils.py ソース](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/utils.py)  
[Torch.compile 警告に関する議論](https://discuss.torch.org/t/torch-compile-warning-not-enough-sms-to-use-max-autotune-gemm-mode/184405)  
[torch.compile の解剖](https://themlsurgeon.substack.com/p/dissecting-torchcompile-surgical)