---
audio: false
generated: true
lang: hant
layout: post
title: 解決 curl 下載問題
translated: true
---

當你嘗試從 eclipse.org 使用 `curl -O` 下載 Eclipse ZIP 文件時，可能會遇到下載 HTML 文件而不是所需 ZIP 文件的問題，並伴隨著「301 Moved Permanently」錯誤。這是因為你使用的 URL 正在重定向到另一個位置，而 `curl` 沒有自動跟隨該重定向到實際文件。以下是如何解決這個問題的方法：

### 了解問題

- **301 Moved Permanently**：這個 HTTP 狀態碼表示資源（ZIP 文件）已永久移動到新的 URL。伺服器通常使用重定向來指向鏡像站點或更新的位置。
- **`curl -O` 行為**：`-O` 選項告訴 `curl` 將下載的內容保存到以遠程文件命名的文件中。然而，如果不顯式處理重定向，`curl` 可能會保存中間重定向響應的內容（通常是 HTML 頁面），而不是跟隨它到 ZIP 文件。

### 解決方案

要確保 `curl` 跟隨重定向並下載 Eclipse ZIP 文件，請使用 `-L` 選項與 `-O` 一起使用。`-L` 旗標指示 `curl` 跟隨任何重定向，直到達到最終目的地。

#### 命令

```bash
curl -L -O <URL>
```

- **`-L`**：跟隨重定向，例如 301 重定向，到新位置。
- **`-O`**：使用最終 URL 的原始名稱保存文件。
- **`<URL>`**：將其替換為具體的 Eclipse 下載 URL，例如 `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`。

### 逐步指示

1. **找到正確的 URL**：
   - 訪問 Eclipse 網站（例如 `https://www.eclipse.org/downloads/`）。
   - 選擇所需的套件（例如 Eclipse IDE for Java Developers）。
   - 右鍵點擊下載鏈接或按鈕並複製 URL。或者，使用瀏覽器的開發者工具（F12，網絡標籤）在點擊下載時捕獲確切的 URL。

2. **運行命令**：
   - 打開你的終端。
   - 使用你複製的 URL 執行 `curl` 命令，帶有 `-L` 和 `-O` 選項：
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - 這應該會將 ZIP 文件（例如 `eclipse-java-2023-03-R-win32-x86_64.zip`）下載到你的當前目錄。

### 疑難排解

如果你仍然遇到問題，請嘗試這些額外步驟：

- **使用詳細輸出檢查重定向**：
  - 使用 `-v` 選項查看有關請求和重定向的詳細信息：
    ```bash
    curl -v -L -O <URL>
    ```
  - 查看 301 响應中的 `Location` 標頭，以查看它重定向的位置。如果它指向 HTML 頁面而不是 ZIP 文件，URL 可能不是直接下載鏈接。

- **驗證 URL**：
  - Eclipse 通常使用 `download.php` 腳本，這可能會重定向到鏡像。確保你的 URL 要麼是直接鏈接到 ZIP 文件，要麼是重定向鏈接，解析為文件。例如，直接鏡像鏈接可能看起來像：
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **設置 User-Agent 標頭**：
  - 有些伺服器根據客戶端的不同行為。如果伺服器返回 HTML 因為它檢測到 `curl`，模仿瀏覽器通過添加 User-Agent：
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### 為什麼這樣有效

Eclipse 網站可能會將下載請求重定向到鏡像或更新的 URL。如果沒有 `-L`，`curl -O` 會保存重定向響應（HTML 頁面），而不是跟隨它。添加 `-L` 確保 `curl` 跟蹤 301 重定向到實際的 ZIP 文件，解決問題。

按照這些步驟，你應該能夠成功從 eclipse.org 使用 `curl` 下載 Eclipse ZIP 文件。