---
audio: false
generated: true
lang: hant
layout: post
title: GitHub Pages 項目網站網址規則
translated: true
type: note
---

使用 GitHub Pages，除了您的用戶網站（`username.github.io`）外，您還可以在個人帳戶下建立**專案網站**。然而，專案網站的 URL 格式僅限於特定模式，並非所有子網域或子路徑配置都原生支援。讓我們來解答您關於能否使用 `username.github.io/project1` 或 `project1.username.github.io` 作為專案網站的問題。

### 關鍵要點
- **用戶網站**：名為 `username.github.io` 的單一儲存庫，其內容提供於 `https://username.github.io`。
- **專案網站**：您個人帳戶中的任何其他儲存庫都可以配置為專案網站，並提供於 `https://username.github.io/儲存庫名稱`（子路徑，而非子網域）。
- **子網域限制**：GitHub Pages 不原生支援像 `project1.username.github.io` 這樣的子網域於 `github.io` 網域下。`github.io` 網域由 GitHub 管理，只有 `username.github.io`（適用於用戶）或 `organization.github.io`（適用於組織）支援作為頂級子網域。像 `project1.username.github.io` 這樣的自訂子網域需要自訂網域和 DNS 配置。

### 您可以使用 `username.github.io/project1` 嗎？
**可以**，您可以將 `username.github.io/project1` 用於專案網站。這是 GitHub Pages 處理專案網站的標準方式：
- 在您的個人帳戶中建立一個儲存庫（例如 `username/project1`）。
- 為該儲存庫啟用 GitHub Pages：
  - 前往儲存庫的 **Settings** 標籤。
  - 滾動至 **Pages** 部分。
  - 在 **Source** 下，選擇要發布的分支（例如 `main` 或 `gh-pages`）並儲存。
- 配置完成後，網站將可於 `https://username.github.io/project1` 存取。
- 您可以透過在更多儲存庫（`username/project2`、`username/project3` 等）上啟用 GitHub Pages 來建立多個專案網站（例如 `username.github.io/project2`、`username.github.io/project3`）。
- **內容**：在每個儲存庫的發布分支中新增 `index.html` 或使用靜態網站生成器如 Jekyll。

### 您可以使用 `project1.username.github.io` 嗎？
**不行**，GitHub Pages 不原生支援像 `project1.username.github.io` 這樣的子網域於 `github.io` 網域下。`github.io` 網域僅允許：
- `username.github.io` 用於用戶網站。
- `organization.github.io` 用於組織網站。
- 像 `username.github.io/儲存庫名稱` 這樣的子路徑用於專案網站。

要實現像 `project1.username.github.io` 這樣的 URL，您需要：
1. **自訂網域**：從註冊商如 Namecheap 或 GoDaddy 購買一個網域（例如 `example.com`）。
2. **DNS 配置**：設定一個 CNAME 記錄，將子網域（例如 `project1.example.com`）指向您的 GitHub Pages 網站（例如 `username.github.io` 或 `username.github.io/project1`）。
3. **GitHub Pages 設定**：
   - 在儲存庫的 **Pages** 設定中，配置自訂網域（例如 `project1.example.com`）。
   - 可選擇啟用「Enforce HTTPS」以增強安全性。
4. **結果**：您可以將 `project1.example.com` 映射到 `project1` 儲存庫的內容，但無法映射到 `project1.username.github.io`，因為 GitHub 控制著 `github.io` 網域，且不允許在其下建立自訂子網域。

### `username.github.io/project1` 的設定範例
1. 在您的帳戶下建立一個名為 `project1` 的儲存庫（`username/project1`）。
2. 新增內容（例如 `index.html`）：
   ```bash
   git clone https://github.com/username/project1
   cd project1
   echo "Hello from Project 1" > index.html
   git add --all
   git commit -m "Initial commit"
   git push origin main
   ```
3. 啟用 GitHub Pages：
   - 前往 `username/project1` → **Settings** → **Pages**。
   - 將來源設定為 `main`（或其他分支）並儲存。
4. 前往 `https://username.github.io/project1` 查看即時網站（可能需要幾分鐘時間傳播）。

### 使用自訂網域設定自訂子網域的範例
如果您想要 `project1.example.com`：
1. 擁有一個網域（例如 `example.com`）。
2. 在您的 DNS 供應商設定中，新增一個 CNAME 記錄：
   - 名稱：`project1`
   - 值：`username.github.io`
3. 在 `project1` 儲存庫的 **Pages** 設定中，將自訂網域設定為 `project1.example.com`。
4. 將內容推送至 `project1` 儲存庫，它將提供於 `project1.example.com`。

### 限制
- **僅支援 `github.io` 的子路徑**：沒有自訂網域的情況下，專案網站始終以子路徑形式提供（`username.github.io/project1`），而非子網域（`project1.username.github.io`）。
- **一個用戶網站**：您的 `username.github.io` 儲存庫保留給用戶網站使用。專案網站使用其他儲存庫，並顯示為子路徑。
- **自訂子網域需要自訂網域**：要獲得 `project1.something`，您需要擁有 `something`（例如 `example.com`）並配置 DNS。
- **私人儲存庫**：私人儲存庫中的專案網站需要 GitHub Pro、Team 或 Enterprise。對於免費帳戶，儲存庫必須是公開的。

### 總結
- **使用 `username.github.io/project1`**：可以，這是原生支援的方式，透過建立儲存庫（`username/project1`）並啟用 GitHub Pages 來實現。您可以透過這種方式建立多個專案網站（例如 `username.github.io/project2` 等）。
- **使用 `project1.username.github.io`**：不行，這在 `github.io` 下不支援。您需要自訂網域（例如 `project1.example.com`）和 DNS 設定來達到類似效果。
- **多個子網域**：要獲得多個 `*.github.io` 子網域，請建立 GitHub 組織（如先前討論）以獲得 `org1.github.io`、`org2.github.io` 等，或使用自訂網域來獲得像 `project1.example.com` 這樣的子網域。

如果您需要協助設定特定專案網站、配置自訂網域或管理多個網站，請告訴我！