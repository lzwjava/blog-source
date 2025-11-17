---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Hugging Face 下載速度解決方案
translated: true
type: note
---

你的問題在中國大陸（特別是像廣州這樣的華南地區）從 Hugging Face 下載大型檔案時非常典型。

### 為何不使用代理 → 極度緩慢（約 200–300 KB/s）
- 即使你使用 **hf-mirror.com**（由 HF 與 01.AI 營運的官方中國鏡像），FineWeb 的實際大型 parquet 檔案**並未在中國境內快取**。
- hf-mirror.com 僅將你重新導向至全球 CDN（現使用 AWS us-east-1 上的 xet-bridge）。
- 從廣州不使用代理 → 你的流量會經過國際閘道（中國電信/聯通/移動骨幹網 → 美國 AWS），且大型檔案下載會受到嚴重節流或 QoS 限制。2 GB 的檔案很容易降至 < 500 KB/s，有時甚至低至 100 KB/s。

### 為何使用 Clash 代理 → 突然變得非常快（通常 20–100 MB/s）
- 你的 Clash 幾乎肯定使用了香港、台灣、日本、新加坡或韓國節點（對廣州用戶非常常見）。
- 這些節點具有：
  - 與 AWS us-east-1（或 HF 也使用的 Cloudflare）的直接對等互連或極佳連線能力
  - 對外流量不受防火牆節流限制
  - 更高的頻寬
- 因此，即使你透過代理「繞道」，實際路徑仍比從中國大陸直接國際出口快得多。

### 簡而言之
從廣州直接連線（即使透過 hf-mirror.com）→ 緩慢，因為實際儲存位置仍在美國，且 2025 年中國 → 美國的大型檔案頻寬狀況依然糟糕。  
Clash 代理（香港/台灣/日本節點）→ 快速，因為這些節點與美國 AWS 的連線極佳。

### 推薦解決方案（從最快到最慢）

1. **繼續使用 Clash（或 v2rayN、Surge 等）搭配低延遲的香港/台灣/日本節點** — 這目前是在中國大陸下載 FineWeb、RedPajama、The Stack 等資料集最快的方式。

2. 使用 **HF 在中國的官方加速端點**（對許多 2024-2025 年的用戶無需任何代理即可運作）：
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```
   然後直接使用 huggingface-cli 或 datasets 庫（非 wget）。因 HF 在 2025 年已開始在阿里雲/騰訊雲快取更多分片，許多中國用戶回報以此方式可達 50–200 MB/s。

3. 使用 **FastGit + hugger** 或 **openi/pkulaw 鏡像**（部分分片在中國境內快取）：
   範例：
   ```bash
   pip install hugger
   hugger download HuggingFaceFW/fineweb --revision main --include "CC-MAIN-2013-20/*.parquet"
   ```

4. 保持使用 wget + hf-mirror.com，但強制其透過你的 Clash 代理（你已在執行的方式）。

### 從廣州快速下載任何 FineWeb 分片的一行指令
```bash
# 設定 Clash HTTP 代理（連接埠通常為 7890）
export https_proxy=http://127.0.0.1:7890

# 然後使用 aria2（比 wget 更快且支援續傳）
aria2c -x16 -s16 -k1M "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet"
```

根據你的代理節點，你將輕鬆獲得 30–100 MB/s 的速度。

總而言之：在 2025 年的中國大陸，對於 Hugging Face 上 >1 GB 的檔案，使用香港/台灣/日本代理幾乎總是比直接連線更快，即使使用 hf-mirror.com 也是如此。這只是當前中國國際頻寬的現實情況。