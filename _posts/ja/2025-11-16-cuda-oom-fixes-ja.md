---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: CUDAメモリ不足エラーの修正方法
translated: true
type: note
---

### 問題分析
nanoGPTのトレーニングスクリプトが、モデルの初期化とコンパイル直後の順伝播における初期損失推定（`estimate_loss()`）中にCUDAメモリ不足（OOM）エラーで失敗しています。主な問題は、モデルの出力ロジット用に大きなバッファを割り当てる際のメモリ枯渇です：

- **バッファ詳細**: 形状`(65536, 50304)`、`bfloat16`（要素あたり2バイト）のテンソルで、約6.14GiB。これは以下に対応：
  - バッチサイズ：64
  - シーケンス長（block_size）：1024
  - 総トークン数：64 × 1024 = 65,536
  - 語彙サイズ：50,304（GPT-2デフォルト）
- **GPUステータス**: 使用GPU（おそらくRTX 3060など12GB VRAM搭載）の総容量は11.69GiBですが、割り当て時点で空きは2.68GiBのみ。プロセスは既に約7.04GiB（PyTorchが6.78GiB）を使用しており、モデル（約1.24億パラメータ × bfloat16で2バイト ≈ 248MB）、オプティマイザ状態（AdamWで約1-2GB）、コンパイルキャッシュ、活性化、オーバーヘッドを考慮すると残りメモリが不足。

これは、大規模なバッチサイズやシーケンス長を使用する場合、特にtorch.compileが有効な場合（グラフキャプチャと最適化中にメモリ使用量が一時的に増加する）、コンシューマー向けGPUでのGPT-2サイズモデル（1.24億パラメータ）では一般的です。

### 根本原因
1. **高いバッチサイズ（64）**: block_size=1024と組み合わさり、大規模な中間テンソル（ロジット、アテンション出力など）を生成。反復あたりの実効トークン数（65,536）がVRAM限界を押し上げ。
2. **モデルコンパイル**: デフォルトで有効な`torch.compile`はTorch Inductorを使用し、一時的なCUDAカーネルとバッファを生成。警告`[0/0] Not enough SMs to use max_autotune_gemm mode`は、ストリーミングマルチプロセッサ（SM）が制限されており、積極的な自動チューニングに使用できないことを示唆（断片化の可能性増加）。
3. **データ型と精度**: `bfloat16`（`torch.cuda.amp`経由）を使用しているが、非推奨の`GradScaler`警告は非効率性を示唆。他のプロセスや以前の実行によるVRAM断片化の可能性。
4. **評価オーバーヘッド**: `estimate_loss()`は評価データで順伝播を実行（eval_iters=200、ただしバッチ処理）、トレーニング開始前の問題を悪化。
5. **既存のメモリ使用**: 約7GBが既に割り当て済み（モデル、オプティマイザ、データセットローダーが初期消費）。非PyTorchメモリ（プロセスによる224.90MiB）はCUDAコンテキストやライブラリを含む可能性。

### 推奨修正
`config/train_openwebtext.py`（またはコマンドラインで上書き）で最も単純な変更から開始。各調整後に再実行し、有効な変更を特定。目標：トレーニング品質を維持しながらピークVRAMを約8-9GBに削減。

#### 1. **バッチサイズ削減（主要修正）**
   - `batch_size = 4`（または初期は1-2）を設定し、ロジットバッファを約0.38GiB（バッチ=4の場合）に削減。
   - `gradient_accumulation_steps = 16`で補償（実効バッチ=64、ピークメモリは低減）。
   - **理由**: バッチサイズはほとんどのテンソルでメモリ使用量と線形関係。OOM対策でトレーニング速度をあまり低下させずに最も効果的。
   - 更新設定例：
     ```
     batch_size = 4
     gradient_accumulation_steps = 16  # 元の実効バッチに合わせ調整
     ```
   - 期待VRAM：合計約4-6GB。

#### 2. **コンパイル無効化または最適化**
   - `compile = False`を追加しtorch.compileをスキップ、Inductorオーバーヘッド（一時的な約1-2GBの急増）を回避。
   - コンパイル維持の場合、`mode='reduce-overhead'`を追加（高速化されるが最適化は低下）。
   - 更新設定：
     ```
     compile = False
     ```
   - **代替案**: スクリプトで`torch._dynamo.config.suppress_errors = True`を実行してデバッグ可能だが、まずOOMを修正。

#### 3. **シーケンス長削減**
   - `block_size = 512`（コンテキスト半減）を設定し、反復あたりトークン数を約32,768に削減、ロジットメモリを半減（約3.07GiB）。
   - トレードオフ：短いコンテキストはモデル品質をわずかに損なう可能性があるが、より多くのトレーニングで回復可能。
   - 設定：
     ```
     block_size = 512
     ```

#### 4. **メモリ管理調整**
   - **断片化用環境変数**: エラーで示唆された通り、実行前に`export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`を設定。PyTorchがCUDA 12+で拡張可能メモリセグメントを使用可能（予約済み未使用ブロックからの浪費削減）。
   - **手動キャッシュクリア**: `train.py`（約100行目）のモデル初期化後に`torch.cuda.empty_cache()`を追加、ただし一時的対策。
   - **CPUオフローディング使用**: 評価のみ、`estimate_loss()`を変更し小バッチまたは非重要部分でCPU使用、ただし速度低下。
   - **VRAM監視**: 別端末で`nvidia-smi -l 1`を実行し使用量をリアルタイム監視。

#### 5. **その他設定調整**
   - `eval_interval = 1000`を増加、`eval_iters = 50`を削減し評価負荷軽減（初期メモリ変動低減）。
   - マルチGPU設定の場合、DDPを有効化、ただしシングルGPUと思われる。
   - bfloat16問題：GPUが対応確認（Ampere+ like RTX 30-series）。未対応の場合、スクリプトで`dtype = 'float16'`を強制。
   - 非推奨警告修正：`train.py`196行目を`scaler = torch.amp.GradScaler('cuda', enabled=(dtype == 'float16'))`に変更。

#### 6. **ハードウェア/セットアップ確認**
   - **VRAM解放**: 他のGPUプロセスを終了（`nvidia-smi`でPID一覧、`kill -9 <PID>`）。ターミナル/セッション再起動。
   - **データセット**: `openwebtext_local`が効率的にロードされているか確認。大規模データセットはDataLoader経由でRAM/VRAMにプリロードされる可能性。
   - **PyTorch/CUDAバージョン**: 互換性確認（例：PyTorch 2.4+とCUDA 12）。必要に応じて再インストール：`pip install torch --index-url https://download.pytorch.org/whl/cu121`。
   - **CPUフォールバック**: テスト用に`device = 'cpu'`と`compile = False`を追加、ただしトレーニングは非常に低速（GPUでは秒単位、CPUでは反復あたり時間単位）。

### 期待される結果
`batch_size=4`、`gradient_accumulation_steps=16`、`compile=False`でOOMを解消しトレーニング開始可能。max_iters=20,000の総実行時間は累積により長くなるが、`log_interval=100`で損失を監視。まだ失敗する場合、バッチサイズをさらに削減し後でスケールアップ。

これらで解決しない場合、GPUモデル（`nvidia-smi`）、PyTorchバージョン（`torch.__version__`）、更新された設定/ログを共有し、より具体的なアドバイスを提供可能。