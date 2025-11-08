---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: フラッシュアテンションがトランスフォーマーのメモリーボトルネックを解決
translated: true
type: note
---

### 背景：標準的なAttentionがTransformerにもたらす課題

GPTやBERTのようなモデルの基盤であるTransformerは、シーケンス処理において自己注意機構に大きく依存しています。自己注意では、入力シーケンスがクエリ行列 \\(Q\\)、キー行列 \\(K\\)、バリュー行列 \\(V\\)（それぞれ形状は \\(N \times d\\)。\\(N\\)はシーケンス長、\\(d\\)はヘッド次元数で通常64-128）として表現され、注意出力 \\(O\\) は以下のように計算されます：

\\[
S = QK^T \in \mathbb{R}^{N \times N}, \quad P = \softmax(S) \in \mathbb{R}^{N \times N}, \quad O = PV \in \mathbb{R}^{N \times d},
\\]

ここで、\\(\softmax\\) は行単位で適用され、\\(S\\) は安定性のために \\(\tau = 1 / \sqrt{d}\\) でスケーリングされることが多いです。因果マスキング（自己回帰モデル用）やドロップアウトなどの追加操作も一般的です。

この定式化は優雅ですが、計算コストが高くなります。中間行列 \\(S\\) と \\(P\\) は \\(N \times N\\) となり、シーケンス長 \\(N\\) に対して**二次の時間・メモリ計算量** \\(O(N^2)\\) をもたらします。長いコンテキスト（例えば、GPT-2では \\(N = 4096\\)、現代のLLMでは最大128k）では、これは深刻なボトルネックとなります：

- **メモリの大食い**: GPUでは、高帯域メモリ（HBM）が主記憶装置ですが、\\(S\\) と \\(P\\) を実体化すると、利用可能なHBM（例：A100/H100で40-80 GB）を超えることがあります。\\(N=4096\\), \\(d=64\\) では、中間結果だけで約1-2 GBを消費し、入力/出力/活性化を加えると、メモリ不足（OOM）エラーを頻発させます。
- **速度の制限**: Attentionは計算束縛ではなく、メモリ束縛です。現代のGPU（例：NVIDIA A100）は約1.5 TB/sのHBM帯域幅を持ちますが、計算性能は約19 TFLOPSです。しかし、softmaxのような操作は完全な \\(N^2\\) 行列を複数回（例：順伝播/逆伝播で要素ごとに4-6回のHBMアクセス）読み書きする必要があります。これにより、実測時間は二次関数的にスケールします：例：PyTorchでは、\\(N=4096\\) で順伝播 ~36 ms、逆伝播 ~88 ms。
- **学習/生成の障壁**: 学習中、勾配計算には逆伝播のために \\(P\\) を保存する必要があり、メモリ使用量が倍増します。推論では、長いコンテキスト（例：64k トークン）は、スパースAttentionや低ランク法（例：Reformer, Linformer）のような近似手法なしでは実現不可能です。これらの手法は正確さと効率性をトレードオフしますが、I/Oコストを無視するため、しばしば性能が劣ります。

FlashAttention（2022年にTri Daoらによって発表）は、近似を行わずに、GPUメモリ階層（高速なSRAM ~20 MB vs 低速なHBM）を活用する、**I/Oを考慮した** アルゴリズムを再考することでこれらの問題に対処します。

### 核心的なアイデア：タイリング、カーネルフュージョン、およびオンラインSoftmax

FlashAttentionは、以下の方法で**正確な**Attention（近似なし）を計算します：

1.  **タイリング**: 完全な \\(N \times N\\) 行列を実体化する代わりに、\\(Q, K, V\\) をSRAMに収まる小さなブロックに分割します。\\(Q\\) は \\(T_r = \lceil N / B_r \rceil\\) 個の行ブロック（サイズ \\(B_r \times d\\)、例：\\(B_r \approx 64-256\\)）に、\\(K, V\\) は \\(T_c = \lceil N / B_c \rceil\\) 個の列ブロック（サイズ \\(B_c \times d\\)、例：\\(B_c \approx 128-1024\\)）に分割されます。ブロックサイズはSRAM容量 \\(M\\)（例：\\(B_c \approx M / (4d)\\)）に基づいて動的に選択され、再利用を最大化します。

2.  **カーネルフュージョン**: すべての操作（\\(S\\) のための行列積、マスキング、softmax、ドロップアウト、\\(O\\) のための行列積）が単一のCUDAカーネルに融合されます。これにより、中間結果をHBMに書き込むことを回避し、I/Oを約50-70%削減します。このカーネルは、ブロックをHBMからSRAMにロードし、オンチップで計算し、部分和のみを書き戻します（例：要素ごとではなく、ブロックごとに1回のHBM読み書き）。

3.  **統計量を用いたオンラインSoftmax**: Softmaxは行全体なしでは部分的に計算できませんが、FlashAttentionは増分計算のために**結合的な分解**を使用します。ブロック \\(x = [x^{(1)}; x^{(2)}]\\) に分割された行に対して、実行中の統計量を追跡します：
    - 行最大値 \\(m_i = \max_j S_{ij}\\),
    - 指数和 \\(\ell_i = \sum_j \exp(S_{ij} - m_i)\\).

   ローカル統計量 \\(\tilde{m}_t, \tilde{\ell}_t\\) を持つ新しいブロック \\(x^{(t)}\\) に対して更新します：
   \\[
   m_i^{\new} = \max(m_i, \tilde{m}_t), \quad \ell_i^{\new} = e^{m_i - m_i^{\new}} \ell_i + e^{\tilde{m}_t - m_i^{\new}} \tilde{\ell}_t.
   \\]
   部分的なsoftmaxは \\(\tilde{P}_{ij} = \exp(S_{ij} - m_i^{\new})\\) となり、出力は \\(O_i \leftarrow \frac{\ell_i}{\ell_i^{\new}} e^{m_i - m_i^{\new}} O_i + \frac{\tilde{\ell}_t}{\ell_i^{\new}} e^{\tilde{m}_t - m_i^{\new}} \tilde{P}_{ij} V_j\\) として累積されます。

   これは数値的に安定しており（融合softmaxと一致）、帰納的に証明されるように正確です：すべてのブロックを処理後、\\(O = \softmax(S) V\\) となります。

これらのアイデアにより、**メモリ使用量は \\(O(N)\\)**（入力 + 出力 + \\(m, \ell\\) のような \\(O(N)\\) の統計量）に削減され、**HBMアクセス回数は \\(O(N^2 d / M)\\)** に削減されます。これは準二次的です。各 \\(K/V\\) 要素は1回読み込まれ、\\(Q/O\\) は \\(T_c \approx N d / M\\) 回読み込まれるためです。

### 順伝播：ブロック単位の計算

順伝播（論文のAlgorithm 2の擬似コード）は、\\(K, V\\) の列ブロックに対して反復処理します：

- HBM内で \\(O = 0^{N \times d}\\), \\(m = -\infty^N\\), \\(\ell = 0^N\\) を初期化。
- 各列ブロック \\(j = 1\\) から \\(T_c\\) まで：
  - \\(K_j, V_j\\) をSRAMにロード（行間で再利用）。
  - 各行ブロック \\(i = 1\\) から \\(T_r\\) まで：
    - \\(Q_i, O_i, m_i, \ell_i\\) をSRAMにロード。
    - ローカルな \\(S_{ij} = \tau Q_i K_j^T\\) (\\(B_r \times B_c\\)) を計算。
    - マスキング: \\(S_{ij}^{\masked} = \mask(S_{ij})\\)（例：因果的：下三角部分を \\(-\infty\\) に）。
    - ローカルsoftmax統計量: \\(\tilde{m}_{ij} = \rowmax(S_{ij}^{\masked})\\), \\(\tilde{P}_{ij} = \exp(S_{ij}^{\masked} - \tilde{m}_{ij})\\), \\(\tilde{\ell}_{ij} = \rowsum(\tilde{P}_{ij})\\).
    - 上記の式を使用してグローバルな統計量と出力を更新し、\\(\tilde{P}_{ij}\\) にドロップアウトを適用。
    - 更新された \\(O_i, m_i, \ell_i\\) をHBMに書き戻す。

これによりすべてが融合されます：総FLOP数は \\(O(N^2 d)\\) のままですが、I/Oは劇的に減少します（例：標準より9倍少ないアクセス）。因果的Attentionでは、マスキングは低コストです（ベクトル化）。ドロップアウトは、逆伝播用に保存された共有RNG状態 \\(R\\) を使用します。

### 逆伝播：再計算による勾配計算

逆伝播（Algorithm 4）はより複雑で、勾配は \\(P\\) に依存します：

\\[
dP = dO \cdot V^T, \quad dS = P \odot (dP - \rowsum(dO \odot O)), \quad dQ = dS \cdot K, \quad dK = Q^T \cdot dS, \quad dV = P^T \cdot dO.
\\]

\\(P\\) を保存すると \\(O(N^2)\\) となるため、FlashAttentionは**オンザフライでブロックを再計算**します（選択的再計算。チェックポイントと似ていますが、タイリングされています）：

- 同様に反復処理：各 \\(j\\) について、\\(K_j, V_j\\) をロード；ローカルな \\(dK_j, dV_j = 0\\) を初期化。
- 各 \\(i\\) について：保存された \\(m_i, \ell_i\\) を使用して \\(S_{ij}, P_{ij}\\) を再計算；\\(R\\) からドロップアウトマスクを再生成。
- ローカル勾配を計算：\\(dV_j += P_{ij}^{dropped^T} dO_i\\), \\(dP_{ij} = dO_i V_j^T \odot Z_{ij}\\)（ドロップアウトマスク）, \\(dS_{ij} = P_{ij} \odot (dP_{ij} - D_i)\\)、ここで \\(D_i = \rowsum(dO_i \odot O_i)\\)。
- \\(dQ_i += \tau dS_{ij} K_j\\), \\(dK_j += \tau Q_i^T dS_{ij}\\) を累積。

これはさらに \\(O(N^2 d)\\) のFLOP数を消費しますが、追加メモリは \\(O(N)\\) のみです（\\(P\\) の保存なし）。順伝播＋逆伝播の合計：標準の約2-3倍のFLOP数ですが、I/O削減により2-4倍高速化されます。

### I/O考慮とGPU最適化

GPUは階層構造を持っています：レジスタ/SRAM（高速、小容量）>> HBM（低速、大容量）。標準的なAttentionは、パスごとに \\(\Theta(N^2)\\) 回のアクセスでHBMを激しく使用します。FlashAttentionのタイリングにより以下が保証されます：
- \\(K, V\\) は1回ロード（\\(O(N d)\\)）。
- \\(Q, O\\) は \\(T_c \approx N / B_c \approx N d / M\\) 回ロード（\\(O(N^2 d / M)\\)）。
- 下限：中程度の \\(M\\) に対して、正確なアルゴリズムで \\(\Omega(N^2 d^2 / M)\\) を下回るものはありません。

実測値：A100では、HBMの待機時間が実行時間を支配します。FlashAttentionはこれを50-80%削減し、計算束縛の領域に到達させます。ブロックスパース性（ゼロマスクブロックをスキップ）もサポートし、密行列よりもさらに大きな向上（2-4倍）をもたらします。

### 利点：速度、メモリ、および下流への影響

- **メモリ**: 線形 \\(O(N d)\\)。単一GPUで64k+のシーケンスを可能にします（標準では2k-4k）。例：\\(N=65k\\) で13 GB vs 標準では200+ GB。
- **速度**: GPT/BERT学習においてエンドツーエンドで2-4倍高速化；生のAttentionでは最大7倍。例：順伝播＋逆伝播合計：\\(N=128\\) で0.43 msから \\(N=65k\\) で9s（PyTorchはOOM）。
- **品質**: 正確な計算のため、パープレキシティの低下なし。より長いコンテキストを可能にします：GPT-2で長さ4倍で0.7ポイントのパープレキシティ向上；長文ドキュメントタスク（例：64k seqsでPath-256の63%）でState-of-the-Artを達成。
- **拡張**: FlashAttention-2 (2023) はより優れた並列性を追加（最大2倍高速）；FlashAttention-3 (2024) はH100向けに非同期/低精度を使用（50%高速）。

### PyTorch統合：シームレスな使用

PyTorch 2.0+ は、`torch.nn.functional.scaled_dot_product_attention(q, k, v)` を介してFlashAttentionをネイティブに統合しており、条件が満たされれば（例：連続したテンソル、サポートされているデータ型）自動的に融合カーネルにディスパッチします。カスタムCUDAは不要です：

```python
import torch
from torch.nn.functional import scaled_dot_product_attention

q, k, v = torch.randn(1, 8, 1024, 64, device='cuda')  # バッチ, ヘッド数, シーケンス, 次元数
with torch.backends.cuda.sdp_kernel(enable_flash=True, enable_math=False):
    out = scaled_dot_product_attention(q, k, v, attn_mask=mask, dropout_p=0.1)
```

これはマスキング/ドロップアウトを処理します；サポートされていない場合はmathカーネルにフォールバックします。カスタムモデルでは、手動のAttentionループのドロップイン代替となり、すぐに2-3倍の高速化をもたらします。

FlashAttentionは長文コンテキスト学習に革命をもたらし、Llama-2 (4k→70B) のようなモデルを支えています。

[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)  
[PyTorch 2.2: FlashAttention-v2 Integration](https://pytorch.org/blog/pytorch2-2/)  
[GitHub: Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention)