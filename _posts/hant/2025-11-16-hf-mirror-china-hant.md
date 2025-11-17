---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在中國使用hf-mirror.com
translated: true
type: note
---

### 了解 hf-mirror.com
hf-mirror.com 是官方 Hugging Face Hub（huggingface.co）的社群維護鏡像站，專門協助中國（包括廣州）用戶突破網路限制，更快下載 AI 模型與資料集。它完整複製了原始儲存庫結構，因此您無需直接存取速度緩慢或經常被封鎖的原始站點，即可使用 GPT-2 等模型或 WikiText 等資料集。由於您經常使用 Clash 代理，請注意 hf-mirror.com 託管在境內，通常無需代理即可存取——它專為在中國直接使用而優化。若您已透過 Clash 代理流量，可選擇將 hf-mirror.com 流量直連（避免不必要的跳轉），或根據偏好維持代理。

### 基礎設定：使用鏡像站
關鍵在於設定 `HF_ENDPOINT` 環境變數指向鏡像站。這對 Hugging Face 工具（如 `transformers` 函式庫、`huggingface-cli` 或 `hfd` 下載器）全域有效。請在導入函式庫或執行下載**前**完成設定。

#### 1. 設定環境變數
- **Linux/macOS（永久設定）**：新增至 `~/.bashrc` 或 `~/.zshrc`：
  ```
  echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.bashrc
  source ~/.bashrc
  ```
- **Windows（PowerShell，永久設定）**：執行一次：
  ```
  [System.Environment]::SetEnvironmentVariable('HF_ENDPOINT', 'https://hf-mirror.com', 'User')
  ```
  完成後重新啟動終端機。
- **臨時設定（任何作業系統）**：在指令前綴加入：
  ```
  HF_ENDPOINT=https://hf-mirror.com your_command_here
  ```

如此即可在不修改程式碼的情況下，將所有 Hugging Face 下載導向鏡像站。

#### 2. 安裝必要工具
- 安裝 Hugging Face Hub CLI（用於下載）：
  ```
  pip install -U huggingface_hub
  ```
- 若需更高速下載，可安裝 `hfd`（Hugging Face Downloader，使用 aria2 實現多線程加速）：
  ```
  wget https://hf-mirror.com/hfd/hfd.sh  # 或透過瀏覽器下載
  chmod +x hfd.sh
  ```

#### 3. 下載模型與資料集
- **使用 huggingface-cli**（支援中斷續傳）：
  ```
  # 下載模型（例如 GPT-2）
  huggingface-cli download gpt2 --resume-download --local-dir ./gpt2

  # 下載資料集（例如 WikiText）
  huggingface-cli download --repo-type dataset wikitext --resume-download --local-dir ./wikitext
  ```
- **使用 hfd**（速度更快，特別適合大檔案）：
  ```
  # 模型下載
  ./hfd.sh gpt2

  # 資料集下載
  ./hfd.sh wikitext --dataset
  ```
- **在 Python 程式碼中**（例如使用 transformers 函式庫）：
  ```python
  import os
  os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'  # 需在導入前設定

  from transformers import AutoModel, AutoTokenizer
  model = AutoModel.from_pretrained('gpt2')  # 將自動從鏡像站下載
  tokenizer = AutoTokenizer.from_pretrained('gpt2')
  ```
  執行時使用：`HF_ENDPOINT=https://hf-mirror.com python your_script.py`

#### 4. 處理需授權/登入的模型
部分模型（如 Llama-2）需要 Hugging Face 帳號與 token：
- 在 huggingface.co 登入（若網站被封鎖請使用 Clash 代理）。
- 於 https://huggingface.co/settings/tokens 生成 token。
- 使用以下指令下載：
  ```
  huggingface-cli download --token hf_YourTokenHere meta-llama/Llama-2-7b-hf --resume-download --local-dir ./Llama-2-7b-hf
  ```
  或使用 hfd：
  ```
  ./hfd.sh meta-llama/Llama-2-7b-hf --hf_username your_username --hf_token hf_YourTokenHere
  ```

### 與 Clash 代理整合
由於 hf-mirror.com 是中國鏡像站，理應無需 Clash 即可存取（直連速度更快）。但若您仍希望透過代理（例如為了統一設定或遇到連線問題），可配置 Clash 將 hf-mirror.com 流量導向您偏好的代理群組。Clash 無需特殊 "HF" 設定——其作用為全域代理。

#### Clash 快速設定要點
- 確保 Clash 正在運行並設為系統代理（在 Clash 中：前往 "General" > 啟用 "System Proxy"）。
- **將 hf-mirror.com 設為直連（推薦以提升速度）**：編輯 Clash 設定檔 YAML（通常位於 Clash 資料夾中的 `config.yaml`）。新增規則繞過代理：
  ```
  rules:
    # ... 您現有的規則 ...
    - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # 繞過代理，直連
    # ... 其餘規則 ...
  ```
  在 Clash 中重新載入設定（Profiles > Reload）。
- **如需代理**：若偏好透過 Clash 路由，無需新增特殊規則——將遵循預設規則（例如 `MATCH,Proxy`）。可透過開關 Clash 測試瀏覽器 ping hf-mirror.com 的結果。
- 下載時：在系統代理生效的終端機中執行指令（Clash 會自動處理）。若使用 Python，`requests` 等函式庫（被 transformers 使用）會遵循 Clash 設定的 `HTTP_PROXY`/`HTTPS_PROXY` 環境變數（例如 HTTP 端口為 `http://127.0.0.1:7890`）。
- 測試：嘗試下載小型模型如 `distilbert-base-uncased`。若速度緩慢，可嘗試關閉 hf-mirror.com 的 Clash 代理。

### 疑難排解
- **下載仍指向 huggingface.co？** 請確認在導入任何 HF 函式庫**前**已設定 `HF_ENDPOINT`（重新啟動您的 notebook/終端機）。
- **下載速度緩慢？** 使用支援多線程的 `hfd` 搭配 aria2。或檢查網路狀態——廣州用戶在 hf-mirror.com 通常可達 10-50MB/s。
- **資料集相關錯誤？** 部分資料集包含自訂腳本；需手動編輯將基礎 URL 改為 `https://hf-mirror.com`。
- **Windows 特定問題**：若使用 Anaconda，請在基礎環境中設定環境變數。
- 進階自建本地鏡像（若需完全控制），可參考 GitHub 上的開源工具如 Olah 或 hf-mirror-site，但建議先從公共鏡像站開始。

此設定應能確保穩定下載。若遇到特定錯誤，請提供輸出內容以獲取進一步協助！

### 參考資源
- [HF-Mirror 官方指南](https://hf-mirror.com/)
- [Hugging Face Hub 端點文件](https://huggingface.co/docs/huggingface_hub/en/package_reference/environment_variables#huggingface_hub_constants.HF_ENDPOINT)
- [hfd 下載器](https://hf-mirror.com/hfd/hfd.sh)
- [Clash 設定規則](https://github.com/Dreamacro/clash/wiki/Configuration#rules)
- [Stack Overflow：在中國下載相關討論](https://stackoverflow.com/questions/77388822/how-to-download-huggingface-bert-base-uncased-in-china)