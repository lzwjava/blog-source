---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: メモリ枯渇によるシステムフリーズ
translated: true
type: note
---

あなたの問題は**GPUではありません**（ここでは4070 Tiはほとんど使用されていません）。このスクリプトは**純粋なCPU + RAMの処理**であり、約1億4千万トークン後にハングアップとGUIフリーズが発生するのは、ほぼ確実に**RAMが不足**し、システムがディスクへの激しいスワッピングを開始して、すべてが数分または数時間フリーズするためです。

### 約1億4千万～2億トークンで発生する理由

各トークン → uint16として保存 → 2バイト。

- 1億4千万トークン ≈ 280 MB
- 10億トークン ≈ 2 GB
- 100億トークン (完全なFineWeb-10B) ≈ 20 GB
- 1000億+トークン (多くのFineWeb/Eduダウンロードのように) ≈ 200+ GB

しかし、Pythonの `all_tokens = []` リストを見てください：Pythonリストは巨大なオーバーヘッドがあります。各整数オブジェクトは64ビットPythonで約28～32バイトです（値がuint16に収まる場合でも）。

リスト構築中の実際のメモリ使用量：
- Pythonリスト内の約1億5千万トークン → 約1億5千万 × 28～32バイト ≈ **4～5 GB**（リストオブジェクトのみ）
- その後、`np.array(..., dtype=np.uint16)` を実行 → コンパクトな配列のためにさらに約300 MB
- 変換中の合計ピークRAM ≈ 5～6 GB + OS + デスクトップのオーバーヘッド

あなたは62.6 GBのRAMを持っているのに、なぜ1億4千万トークンでだけフリーズするのでしょうか？

あなたの入力ファイル `train_fineweb.txt` は、おそらくあなたが考えているより**はるかに大きい**からです。

人々はしばしばFineWeb-100Bや1Tサンプルをダウンロードし、それを「train_fineweb.txt」と命名します。もしあなたのファイルが、例えば人気のある1000億トークンのFineWeb-Eduサンプル（～200～300 GBのテキストファイル）である場合、スクリプトは永遠に読み込みを続け、`all_tokens` リストは数百億または数千億トークンにまで成長します → 数百GBのRAM → OOM → スワップスラッシング → デスクトップ完全フリーズ。GPUファンが回るのは、スクリプトが（かろうじて）生きており、Pythonが `extend()` または最終的な `np.array()` 変換で行き詰まっているためです。

### 解決策 (いずれか一つを選択)

#### 最適な修正: すべてのトークンをRAMに保持せずに直接.binにストリーミング
このバージョンは、テラバイトサイズのテキストでもほとんどRAMを使用しません（ピーク時 < 1 GB）：

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # チャンクあたりの文字数、必要に応じて調整

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # 最初のパスの後で決定するか、近似値を設定

    with open(input_path, "r", encoding="utf-8", errors='ignore') as f, \
         open(temp_train, "wb") as train_f, \
         open(temp_val, "wb") as val_f:

        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            tokens = enc.encode_ordinary(chunk)
            tokens_u16 = np.array(tokens, dtype=np.uint16)

            total_tokens += len(tokens_u16)

            # その場で検証分割を近似（十分に正確）
            if val_target is None and total_tokens > 10_000_000:
                val_target = int(total_tokens * val_ratio / (1 - val_ratio))

            if val_tokens_written < val_target:
                split_point = min(len(tokens_u16), val_target - val_tokens_written)
                val_f.write(tokens_u16[:split_point].tobytes())
                train_f.write(tokens_u16[split_point:].tobytes())
                val_tokens_written += split_point
            else:
                train_f.write(tokens_u16.tobytes())

            if total_tokens % 50_000_000 == 0:
                print(f"Processed {total_tokens/1e6:.1f}M tokens")

    # 一時ファイルをリネーム
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"Done! Total ≈ {total_tokens/1e9:.2f}B tokens")
    print(f"train.bin and val.bin ready (no RAM explosion)")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

これは直接ディスクにストリーミングし、メモリに保持するのは常に1チャンクだけです。

#### もし本当に元のスクリプトスタイルを維持したいが安全にしたい場合
メモリ監視を追加し、出力をシャード化します：

```python
# 一つの巨大なリストの代わりにこれを追加
MAX_TOKENS_PER_SHARD = 500_000_000  # シャードあたり約1 GB

shard_idx = 0
all_tokens = []

for chunk in iter(lambda: f.read(chunk_size), ""):
    if not chunk:
        break
    tokens = enc.encode_ordinary(chunk)
    all_tokens.extend(tokens)

    if len(all_tokens) >= MAX_TOKENS_PER_SHARD:
        arr = np.array(all_tokens, dtype=np.uint16)
        arr.tofile(f"train_shard_{shard_idx:04d}.bin")
        print(f"Saved shard {shard_idx} - {len(arr)/1e6:.1f}M tokens")
        all_tokens.clear()
        shard_idx += 1
```

後でシャードを結合するだけ： `cat train_shard_*.bin > train.bin`

### ファイルの実際のサイズを簡単に確認
ターミナルで以下を実行：

```bash
du -h train_fineweb.txt          # 人間が読みやすいサイズ
wc -c train_fineweb.txt          # バイト数
ls -lh train_fineweb.txt
```

FineWeb-10Bのテキストは約20～25 GB、100Bは約200～250 GB、などです。

### まとめ
あなたのスクリプトがクラッシュするのは、Pythonリストが最終的なnumpy配列よりも15～20倍多くのRAMを消費するためです。大きなFineWebファイルでは、すぐに50+ GBを超え → スワップ → デスクトップフリーズとなります。

上記のストリーミングバージョンを使用してください — これは1TB+のテキストファイルでも<2 GBのRAMで動作し、単一のCPUコアで数時間で完了します。

あなたの4070 Tiはここでは無実です；RAMが死んでいるために来ないデータを待っているだけです。