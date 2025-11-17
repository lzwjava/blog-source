---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 優化Hugging Face下載速度
translated: true
type: note
---

您目前的下載正連接到 Hugging Face 的主要端點 (`huggingface.co`)，該端點主要託管在歐洲/美國的數據中心。從廣州經由台灣代理伺服器路由會增加與之前類似的延遲問題：約 200–300 毫秒的往返時間，加上大型檔案可能遇到的節流（每個 Parquet 分片約 500MB–1GB）。您看到的 302 重定向很可能是指向 CloudFront CDN 邊緣節點，但可能不是針對亞洲優化的節點，從而導致速度下降（例如 1–5 MB/s）。

要達到與 Wikimedia 下載相同的 20–60 MB/s 速度，請使用以下調整——優先選擇對亞洲友好的選項。所有方法均保留您的 Clash/台灣代理設定。

### 1. **切換至 HF Mirror（對中國/台灣最快——推薦）**
   HF Mirror (`hf-mirror.com`) 是一個為東亞優化的社區運營 CDN（透過國內清華等網絡代理）。它完全鏡像所有 HF 數據集，包括 FineWeb Parquet 檔案。從台灣代理預期速度可達 30–80 MB/s。

   更新您的腳本：
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (已更新以提升速度)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "透過 HF Mirror 下載 FineWeb 分片（對亞洲更快）..."
   
   # 將 huggingface.co 替換為 hf-mirror.com
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"
   
   echo "完成！分片大小：約 500MB–1GB"
   echo "如需更多分片，可循環處理例如 000_00001.parquet 等"
   echo "在 Python 中載入：from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   執行：`./scripts/train/wget_fineweb_1.sh`  
   - 如果鏡像延遲（罕見），可回退至官方網址：`https://huggingface.co/datasets/...`（但請加入第 2 點的速度提示）。

### 2. **使用 hf_transfer 加速（適用於任何 HF 下載——可續傳下載速度提升 100 倍）**
   Hugging Face 官方的 Rust 工具，用於並行/多線程下載。它會自動重試、使用更多連接，並在良好鏈接下達到 >500 MB/s。可間接與 `wget` 配合使用，或直接透過 Python（如果您的腳本使用 `huggingface_hub`）使用。

   安裝（一次性，透過 pip——您的環境已具備）：
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   然後重新執行您的原始腳本。它會加速底層對 HF URL 的 `wget` 呼叫。  
   - 專業提示：如需完整數據集串流（無需完整下載），請在您的流程中使用 Python：
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # 在導入前啟用
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # 即時串流/處理
         print(example)
     ```
     如果您設定了 `HF_ENDPOINT=https://hf-mirror.com`，這將透過鏡像懶加載分片。

### 3. **Clash 規則調整（如果允許——超快國內速度）**
   如果您的代理設定允許對 HF 繞行（或路由至香港/新加坡節點），請為 `huggingface.co` / `hf-mirror.com` 添加規則以直連/走國內線路。在 `clash.yaml` 中：
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # 或您的國內鏡像節點
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   重啟 Clash，然後下載。與第 1 點搭配使用，可透過清華鏡像達到 50–100+ MB/s。

### 為何能匹配 Wikimedia 速度
- Wikimedia：重定向器自動選擇亞洲（日本/韓國/新加坡）節點 → 低延遲。
- HF：預設為歐洲/美國節點 → 高延遲；鏡像 + 傳輸工具將其切換為針對亞洲優化的節點。

請先測試一個分片——如果仍然緩慢，請檢查 `curl -I https://hf-mirror.com/...` 的回應標頭（應顯示亞洲 CDN）。對於完整的 15T FineWeb 數據集，請透過 `datasets` 庫進行串流處理，以避免下載數百 GB 的數據。如果速度沒有提升，請隨時聯繫我！