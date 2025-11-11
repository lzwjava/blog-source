---
audio: false
generated: true
lang: hant
layout: post
title: 疑難排解 curl 下載問題
translated: true
type: note
---

當你嘗試使用 `curl -O` 從 eclipse.org 下載 Eclipse ZIP 檔案時，可能會遇到下載到 HTML 檔案而非所需 ZIP 檔案的狀況，並伴隨「301 Moved Permanently」錯誤。這是因為你使用的 URL 會重新導向至其他位置，而 `curl` 並未自動跟隨該重新導向至實際檔案。以下是如何解決此問題：

### 問題解析

- **301 Moved Permanently**：此 HTTP 狀態碼表示資源（ZIP 檔案）已永久移至新 URL。伺服器通常會對下載連結使用重新導向，指向鏡像網站或更新後的位置。
- **`curl -O` 行為**：`-O` 選項會指示 `curl` 將下載內容儲存為遠端檔案名稱。然而，若未明確處理重新導向，`curl` 可能會儲存中間重新導向回應的內容（通常是 HTML 頁面），而非跟隨它至 ZIP 檔案。

### 解決方案

為確保 `curl` 跟隨重新導向並下載 Eclipse ZIP 檔案，請同時使用 `-L` 與 `-O` 選項。`-L` 標記會指示 `curl` 跟隨所有重新導向，直至抵達最終目的地。

#### 指令

```bash
curl -L -O <URL>
```

- **`-L`**：跟隨重新導向（例如 301 重新導向）至新位置。
- **`-O`**：以最終 URL 的原始名稱儲存檔案。
- **`<URL>`**：請替換為特定的 Eclipse 下載 URL，例如 `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`。

### 逐步操作說明

1. **尋找正確 URL**：
   - 造訪 Eclipse 網站（例如 `https://www.eclipse.org/downloads/`）。
   - 選擇所需套件（例如 Eclipse IDE for Java Developers）。
   - 在下載連結或按鈕上點擊右鍵並複製 URL。或者，使用瀏覽器的開發者工具（F12，Network 分頁）在點擊下載時擷取確切 URL。

2. **執行指令**：
   - 開啟終端機。
   - 使用你複製的 URL 執行帶有 `-L` 與 `-O` 選項的 `curl` 指令：
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - 這應會將 ZIP 檔案（例如 `eclipse-java-2023-03-R-win32-x86_64.zip`）下載至你的目前目錄。

### 疑難排解

若仍遇到問題，請嘗試以下額外步驟：

- **使用詳細輸出檢查重新導向**：
  - 使用 `-v` 選項查看請求與重新導向的詳細資訊：
    ```bash
    curl -v -L -O <URL>
    ```
  - 查看 301 回應中的 `Location` 標頭以了解其重新導向位置。若它指向 HTML 頁面而非 ZIP 檔案，則該 URL 可能不是直接下載連結。

- **驗證 URL**：
  - Eclipse 通常使用 `download.php` 腳本，可能會重新導向至鏡像網站。請確保你的 URL 是 ZIP 檔案的直接連結，或是能解析至該檔案的重新導向連結。例如，直接