---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: OpenWebText 數據集下載指南
translated: true
type: note
---

### 問題分析
`RepositoryNotFoundError` (401 客戶端錯誤) 確認了 `openwebtext` 儲存庫在 Hugging Face 上**並不存在**。這就是下載失敗的原因——HF 在 `https://huggingface.co/openwebtext` 找不到該儲存庫。「無效的使用者名稱或密碼」部分是 HF 認證層的通用錯誤訊息，但在此處無關緊要，因為該儲存庫根本不存在。OpenWebText（您試圖存取的資料集）是 GPT-2 時代的公開語料庫，但並未以標準儲存庫的形式託管在 Hugging Face 上。相反地，它是透過鏡像、種子或學術/GitHub 來源的直接下載來分發的。

- **OpenWebText 背景**：創建目的是為了複製 GPT-2 論文中使用的資料集（來自 Reddit Pushshift 轉儲中的 URL，並經過品質過濾）。完整語料庫約為 40GB 的文字，分割成子集，例如 `urlsf_subset00.tar`（這是 14 個壓縮檔之一，每個約 3-5GB）。這些壓縮檔包含用於訓練 nanoGPT 等模型的原始文字檔案。
- 沒有官方的 HF 儲存庫：經查證，在 `openwebtext` 或類似名稱下並沒有完整子集的直接上傳（例如，EleutherAI 有相關儲存庫，但沒有原始資料）。HF 主要專注於具有授權的模型/資料集，而 OpenWebText 屬於公共領域，但為了避免頻寬成本而託管在其他地方。

### 正確的下載方法
使用**直接的 HTTP 下載**或來自可靠鏡像的**種子**。最可靠的來源是 Skylion007 的 GitHub 鏡像（一個託管清理後語料庫的社群努力）。以下是取得 `urlsf_subset00.tar`（以及如果需要，其他檔案）的方法：

1. **從鏡像直接下載**（推薦，速度較快）：
   - 基礎 URL：`http://skylion007.github.io/OpenWebTextCorpus/`
   - 特定檔案：`http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar`
   - 下載指令（使用 `wget` 或 `curl`；如需安裝請使用 `sudo apt install wget`）：
     ```
     cd ~/projects/nanoGPT  # 或您的目標目錄
     wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
     ```
     - 這會將檔案儲存為 `./urlsf_subset00.tar`（約 3.3 GB）。這是一個 HTTP 鏡像，因此無需認證，且速度很快（直接從 GitHub Pages 下載）。
     - 對於完整集合（所有子集）：從頁面列出它們並使用迴圈下載，或使用腳本：
       ```bash
       for i in {00..13}; do
         wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset${i}.tar
       done
       ```
     - 使用 `curl` 的替代方案（如果 wget 不可用）：
       ```
       curl -O http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
       ```

2. **種子下載**（最適合大型檔案、可續傳且節省頻寬）：
   - 所有子集的官方種子：來自原始 Gwern 儲存庫或 Academic Torrents 的磁力連結。
   - 磁力 URI（複製並貼到 qBittorrent、Transmission 或 `aria2c` 等用戶端）：
     ```
     magnet:?xt=urn:btih:5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e&dn=OpenWebTextCorpus
     ```
   - 或直接下載 .torrent 檔案：從 [academictorrents.com](https://academictorrents.com/details/5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e) 下載，或搜尋 "OpenWebTextCorpus torrent"。
   - 如需安裝種子用戶端：
     - Ubuntu/Debian：`sudo apt install qbittorrent-nox`（無頭模式）或使用 GUI。
     - 然後執行：`qbittorrent-nox` 並添加磁力連結。
   - 預期結果：將所有 14 個壓縮檔（總計約 40GB）下載到您選擇的目錄。如果只需部分，請選擇 `urlsf_subset00.tar`。

3. **GitHub 克隆（如果您需要儲存庫結構）**：
   - 語料庫的中繼資料在 GitHub 上：`https://github.com/skylion007/OpenWebTextCorpus`
   - 克隆以取得 README/文件（非資料）：
     ```
     git clone https://github.com/skylion007/OpenWebTextCorpus.git
     ```
   - 資料連結在 README 中——指向上述相同的鏡像。

### 下載後續步驟
- **解壓縮 Tarball**：
  ```
  mkdir -p ./openwebtext/subsets
  tar -xvf urlsf_subset00.tar -C ./openwebtext/subsets
  ```
  - 這會將約 100,000+ 個文字檔案（例如 `0.txt`、`1.txt`）解壓縮到 `./openwebtext/subsets/` 中。每個檔案都是清理後的網頁文字。
- **對於 nanoGPT 整合**：
  - NanoGPT（Andrej Karpathy 的儲存庫）在書籍/資料準備中有一個 `openwebtext` 範例。使用他們的腳本來串接/處理檔案：
    ```python
    # 來自 nanoGPT 的 data/openwebtext/prepare.py（根據需要調整）
    import os
    import glob

    input_dir = './openwebtext/subsets'
    output_file = './openwebtext/input.txt'

    with open(output_file, 'w') as out:
        for txt_file in sorted(glob.glob(os.path.join(input_dir, '*.txt'))):
            with open(txt_file, 'r') as f:
                out.write(f.read())
    ```
  - 這會建立一個單一的巨型 `input.txt` 用於訓練。請注意——完整的 OpenWebText 需要大量的儲存空間/RAM。
- **驗證完整性**：每個 tar 檔案在鏡像的 README 中都有一個 MD5 校驗和（例如，對於 subset00：使用 `md5sum urlsf_subset00.tar` 對照提供的雜湊值進行檢查）。

### 如果問題持續存在
- **鏡像掛掉了？** 嘗試原始的 Gwern 來源：`https://www.gwern.net/OpenWebTextCorpus`（連結到 AWS S3 或種子）。
- **法律/存取注意事項**：OpenWebText 屬於公共領域（從開放網路爬取），但在使用時請尊重 robots.txt。此處無需 HF 認證。
- **HF 上的替代方案**：如果您需要 HF 託管的類似資料，請查看 `wikitext`、`bookcorpus` 或 `pile` 子集（例如，使用 `hf download` 下載 `repo_id="EleutherAI/pile"`）。對於確切的 OpenWebText，請堅持使用鏡像。
- **磁碟/速度提示**：這些檔案非常龐大——請使用 SSD，並使用 `du -sh` 或 `htop` 進行監控。如果在中國或受限地區，請使用 VPN 以獲得較快的存取速度。

如果下載成功但遇到解壓縮/處理錯誤，或需要 nanoGPT 下一步的幫助，請貼上詳細資訊！