---
audio: false
generated: true
lang: hant
layout: post
title: 使用組織託管多個 GitHub Pages
translated: true
type: note
---

是的，建立 GitHub 組織確實是託管額外 GitHub Pages 網站並使用獨特 `*.github.io` 子網域的有效方法，因為每個組織都可以擁有自己的 `organization.github.io` 網站，與你個人的 `username.github.io` 網站分開。以下是具體操作方法及注意事項：

### 關鍵要點
- **個人帳戶限制**：每個 GitHub 用戶帳戶只能擁有一個用戶網站，託管在 `username.github.io`，並與名為 `username.github.io` 的儲存庫綁定。如果你已為個人帳戶使用了此功能，則無法在同一帳戶下建立另一個 `*.github.io` 子網域。
- **組織網站**：每個 GitHub 組織也可以擁有自己的組織網站，託管在 `organization.github.io`，方法是建立一個名為 `organization.github.io` 的儲存庫。這讓你可以透過建立多個組織來建立額外的 `*.github.io` 子網域。
- **專案網站**：用戶和組織帳戶都可以從其他儲存庫託管多個專案網站（例如 `username.github.io/project` 或 `organization.github.io/project`），但這些是子路徑，而非子網域。如果你特別想要獨立的子網域（例如 `sub.example.github.io`），在沒有自訂網域的情況下，無法直接透過 GitHub Pages 實現，因為 GitHub 不支援在 `github.io` 網域下使用自訂子網域，如 `sub.example.github.io`。

### 建立 GitHub 組織以獲取額外 `*.github.io` 子網域的步驟
1. **建立 GitHub 組織**：
   - 登入 GitHub 帳戶。
   - 點擊右上角的「+」圖示，選擇 **New organization**。
   - 按照提示設定組織，選擇一個獨特的名稱（例如 `myorg`）。此名稱將決定子網域（例如 `myorg.github.io`）。
   - 注意：可以免費建立組織，但某些功能（如私人儲存庫）可能需要付費方案，視你的需求而定。公開儲存庫的 GitHub Pages 在 GitHub Free 方案中可用。

2. **建立組織的 GitHub Pages 儲存庫**：
   - 在新的組織中，建立一個名為 `myorg.github.io` 的儲存庫（將 `myorg` 替換為你的組織名稱）。
   - 此儲存庫將託管組織網站，可透過 `https://myorg.github.io` 存取。

3. **設定 GitHub Pages**：
   - 前往 `myorg.github.io` 儲存庫的 **Settings** 分頁。
   - 滾動至 **Pages** 部分。
   - 在 **Source** 下，選擇要發布的分支（例如 `main` 或 `gh-pages`）並儲存。
   - 設定完成後，網站將在幾分鐘後在 `https://myorg.github.io` 上線。

4. **新增內容**：
   - 在儲存庫的發布分支中新增 `index.html` 檔案或使用靜態網站生成器如 Jekyll。
   - 提交並推送變更。例如：
     ```bash
     git clone https://github.com/myorg/myorg.github.io
     cd myorg.github.io
     echo "Hello World" > index.html
     git add --all
     git commit -m "Initial commit"
     git push origin main
     ```
   - 訪問 `https://myorg.github.io` 以確認網站已上線。

5. **重複操作以獲取更多子網域**：
   - 建立額外的組織（例如 `myorg2`、`myorg3`）並重複上述過程，以獲得 `myorg2.github.io`、`myorg3.github.io` 等。
   - 每個組織可以擁有一個 `*.github.io` 子網域，讓你可以根據組織數量建立任意多個子網域。

### 限制與注意事項
- **`github.io` 上的自訂子網域**：你無法直接使用 GitHub Pages 建立像 `sub.myorg.github.io` 這樣的子網域。`github.io` 網域由 GitHub 管理，僅支援 `username.github.io` 或 `organization.github.io`。要使用自訂子網域（例如 `blog.example.com`），你必須擁有一個自訂網域並設定 DNS（CNAME 記錄）指向 `myorg.github.io`。
- **每個子網域對應單一儲存庫**：每個 `*.github.io` 子網域都與單一儲存庫（`username.github.io` 或 `organization.github.io`）綁定。在沒有自訂網域和額外託管或代理服務的情況下，你無法從單一儲存庫提供多個子網域。
- **管理開銷**：每個組織都需要獨立管理（例如成員、權限、帳單）。請確保你願意管理多個組織。
- **DNS 與自訂網域**：如果你想使用自訂網域（例如 `example.com` 或 `sub.example.com`）而非 `*.github.io`，可以在儲存庫的 **Pages** 設定中進行配置，並在 DNS 供應商處新增 CNAME 記錄。例如，將 `sub.example.com` 指向 `myorg.github.io`。請務必驗證網域以防止接管風險。
- **私人儲存庫**：私人儲存庫的 GitHub Pages 需要 GitHub Pro、Team 或 Enterprise 方案。如果你使用免費方案，請確保你的 `myorg.github.io` 儲存庫是公開的。

### 多子網域的替代方案
如果你的目標是在單一自訂網域下擁有多個子網域（例如 `blog.example.com`、`shop.example.com`），你可以：
1. 從註冊商（如 Namecheap 或 GoDaddy）購買自訂網域（例如 `example.com`）。
2. 在你的組織中建立多個儲存庫（例如 `myorg/blog`、`myorg/shop`）。
3. 為每個儲存庫啟用 GitHub Pages，在各自的 **Pages** 設定中設定自訂網域，如 `blog.example.com` 和 `shop.example.com`。
4. 在 DNS 供應商處配置 CNAME 記錄，將 `blog.example.com` 指向 `myorg.github.io`，將 `shop.example.com` 指向 `myorg.github.io`。請注意，所有沒有自訂網域的儲存庫將以子路徑形式出現在組織的自訂網域下（例如 `example.com/blog`）。
5. 請注意，GitHub Pages 不原生支援從單一儲存庫提供多個子網域，可能需要使用外部服務，如 CDN 或反向代理。

### 範例情境
- 你已將 `username.github.io` 用於個人網站。
- 建立一個名為 `myorg` 的組織和一個 `myorg.github.io` 儲存庫，以獲得 `myorg.github.io`。
- 建立另一個名為 `myorg2` 的組織和一個 `myorg2.github.io` 儲存庫，以獲得 `myorg2.github.io`。
- 對於自訂子網域，擁有 `example.com`，並透過 CNAME 記錄設定 `blog.example.com`（指向 `myorg.github.io`）和 `shop.example.com`（指向 `myorg2.github.io`）。

### 最後注意事項
- 建立多個組織是在不需要自訂網域的情況下，獲取額外 `*.github.io` 子網域的簡單方法。
- 如果你想要真正的子網域（例如 `sub.myorg.github.io`），則需要自訂網域和 DNS 配置，因為 GitHub 的 `github.io` 不原生支援此功能。
- 請務必驗證自訂網域以避免網域接管等安全風險。
- DNS 變更可能需要最多 24 小時才能傳播。

如果你有進一步的問題或需要特定設定的協助，請告訴我！