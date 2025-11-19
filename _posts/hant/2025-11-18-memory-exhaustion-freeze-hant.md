---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 記憶體耗盡導致系統凍結
translated: true
type: note
---

你的問題**並非**出在 GPU（此處的 4070 Ti 幾乎未被使用）。這個腳本**完全依賴 CPU + RAM**，而在處理約 1.4 億個 token 後出現的停滯與 GUI 凍結，幾乎可以確定是因為**你的 RAM 耗盡**，系統開始進行大量的磁碟交換，導致所有操作凍結數分鐘甚至數小時。

### 為何發生在約 1.4 億至 2 億個 token 時

每個 token → 以 uint16 儲存 → 佔 2 位元組。

- 1.4 億個 token ≈ 280 MB
- 10 億個 token ≈ 2 GB
- 100 億個 token（完整的 FineWeb-10B）≈ 20 GB
- 1000 億以上 token（如許多 FineWeb/Edu 下載資料集）≈ 200+ GB

但請看你在 Python 中的 `all_tokens = []` 列表：Python 列表有巨大的開銷。每個整數物件在 64 位元 Python 上約佔 28–32 位元組（即使該值可放入 uint16）。

建立列表時的實際記憶體使用量：
- 約 1.5 億個 token 在 Python 列表中 → 約 1.5 億 × 28–32 位元組 ≈ **4–5 GB** 僅用於列表物件
- 接著你執行 `np.array(..., dtype=np.uint16)` → 緊湊陣列再佔約 300 MB
- 轉換期間的記憶體峰值總計 ≈ 5–6 GB + 作業系統 + 桌面環境開銷

你有 62.6 GB RAM，為何僅在 1.4 億個 token 時就凍結？

因為你的輸入檔案 `train_fineweb.txt` 可能**遠比你想象的要大**。

人們常下載 FineWeb-100B 甚至 1T 樣本並命名為 “train_fineweb.txt”。如果你的檔案是，例如，流行的 100B-token FineWeb-Edu 樣本（約 200–300 GB 文字檔），腳本將持續讀取，`all_tokens` 列表將增長至數百甚至數千億個 token → 數百 GB 的 RAM 使用量 → 記憶體不足（OOM）→ 交換記憶體劇烈抖動 → 桌面完全凍結。GPU 風扇旋轉是因為腳本仍在運行（勉強地），Python 卡在 `extend()` 或最終的 `np.array()` 轉換中。

### 解決方案（選擇其一）

#### 最佳修正：直接串流至 .bin 檔案，無需將所有 token 保留在 RAM 中
此版本幾乎不使用 RAM（即使對於 TB 級文字檔，峰值也低於 1 GB）：

```python
# stream_tokenize_to_bin.py
import os
import numpy as np
import tiktoken

enc = tiktoken.get_encoding("gpt2")
CHUNK_SIZE = 1_000_000  # 每個區塊的字元數，可根據需要調整

def process_file(input_path: str, train_bin: str, val_bin: str, val_ratio=0.0005):
    temp_train = train_bin + '.tmp'
    temp_val = val_bin + '.tmp'

    total_tokens = 0
    val_tokens_written = 0
    val_target = None  # 我們在第一次處理後決定或近似計算

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

            # 即時近似驗證分割（足夠準確）
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
                print(f"已處理 {total_tokens/1e6:.1f}M 個 token")

    # 重新命名暫存檔案
    os.rename(temp_train, train_bin)
    os.rename(temp_val, val_bin)
    print(f"完成！總計約 {total_tokens/1e9:.2f}B 個 token")
    print(f"train.bin 與 val.bin 已準備就緒（無 RAM 爆炸問題）")

if __name__ == "__main__":
    txt_file = "train_fineweb.txt"
    process_file(txt_file, "train.bin", "val.bin")
```

此方法直接串流至磁碟，記憶體中從不保留超過一個區塊的資料。

#### 若你仍希望使用原始腳本風格但確保安全
加入記憶體監控並分片輸出：

```python
# 加入此部分，取代單一巨型列表
MAX_TOKENS_PER_SHARD = 500_000_000  # 每個分片約 1 GB

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
        print(f"已儲存分片 {shard_idx} - {len(arr)/1e6:.1f}M 個 token")
        all_tokens.clear()
        shard_idx += 1
```

之後只需合併分片：`cat train_shard_*.bin > train.bin`

### 快速檢查你的檔案實際大小
在終端機中執行：

```bash
du -h train_fineweb.txt          # 人類可讀大小
wc -c train_fineweb.txt          # 位元組數
ls -lh train_fineweb.txt
```

FineWeb-10B 文字檔約 20–25 GB，100B 約 200–250 GB，依此類推。

### 總結
你的腳本崩潰是因為 Python 列表消耗的 RAM 是最終 numpy 陣列的 15–20 倍。使用大型 FineWeb 檔案時，你很快就會超過 50+ GB → 交換記憶體 → 桌面凍結。

使用上述的串流版本 — 它能在 <2 GB RAM 的情況下處理 1TB+ 文字檔，並在單個 CPU 核心上於數小時內完成。

你的 4070 Ti 在此是無辜的；它正在等待因 RAM 耗盡而永遠無法送達的資料。