---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 開源工具：自動SS配置
translated: true
type: post
---

我很高興地宣布，我已經開源了一個名為 **Auto SS Config** 的工具。這個工具能夠自動從 Shadowsocks URL 生成並上傳 Shadowsocks 或 Clash 的訂閱 URL，讓管理和更新你的代理伺服器配置變得更加輕鬆。

這個工具對我來說是一個改變遊戲規則的存在，尤其是在我的 Shadowsocks 伺服器被封鎖時。我會使用 Outline Manager 創建一個新的伺服器，獲取一個新的地址，並通過 Mac 應用直接導入這個 URL 來繞過防火牆的限制。運行這個項目中的 `python upload_configs.py` 可以更新我的訂閱 URL，確保我所有的數位設備都能保持正常的網絡連接。

## 功能

- **將 Shadowsocks URL 轉換為 Clash 配置**：輕鬆切換不同的代理配置。
- **支持多個 Shadowsocks 伺服器**：輕鬆管理多個伺服器。
- **自動上傳配置到 Google Cloud Storage**：確保你的配置安全且可訪問。
- **使配置公開可訪問**：與他人分享你的配置。
- **使用緩存控制以實現即時更新**：確保你的配置始終是最新的。

## 文件

- `app_config_tmp.yaml`：應用程序配置（存儲桶名稱、SS URL）。
- `clash_config_tmp.yaml`：臨時的 Clash 配置文件。
- `upload_configs.py`：生成 Clash 配置並上傳配置到 Google Cloud Storage 的腳本。
- `requirements.txt`：Python 依賴項。

## 設置

1. **安裝依賴項**：
    ```bash
    pip install -r requirements.txt
    ```

2. **設置 Google Cloud 憑證**：
    - 安裝 Google Cloud SDK。
    - 運行 `gcloud auth application-default login`。
    - 或者設置 `GOOGLE_APPLICATION_CREDENTIALS` 環境變量。

3. **將 `app_config_tmp.yaml` 複製為 `app_config.yaml` 並進行配置**：
    ```yaml
    bucket_name: your-bucket-name
    ss_urls:
        - ss://method:password@server:port
    ```

## 使用

1. **將你的 Shadowsocks URL 添加到 `app_config.yaml` 中的 `ss_urls` 列表**：
    ```yaml
    ss_urls:
        - ss://method:password@server:port
    ```

2. **上傳配置**：
    ```bash
    python upload_configs.py
    ```

    腳本將輸出兩個配置的公開 URL。

## 開發

- **Python 3.6+**
- 使用 `ruamel.yaml` 處理 YAML。
- 使用 `google-cloud-storage` 進行 GCS 操作。

## 許可證

MIT

---

歡迎查看 [存儲庫](https://github.com/lzwjava/auto-ss-config) 獲取更多詳情並參與貢獻！