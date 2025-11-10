---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 npm 權限不足錯誤
translated: true
type: note
---

您遇到的錯誤 `EACCES: permission denied` 表示您目前的使用者**沒有寫入權限**到 `/usr/local/lib/node_modules` 目錄。這是在 Linux 或 macOS 上安裝全域 npm 套件時常見的問題。

### **如何解決此問題**

#### **選項 1：使用 `sudo`（不建議常規使用）**
您可以使用 `sudo` 以 root 使用者身分執行指令，但**不建議**常規使用，因為這可能導致後續 npm 套件的權限問題。

```bash
sudo npm install -g @anthropic-ai/claude-code
```

#### **選項 2：變更 npm 的預設目錄（推薦）**
最佳做法是配置 npm 使用您擁有寫入權限的家目錄中的目錄。

1. **在家目錄中建立全域 npm 目錄：**
   ```bash
   mkdir ~/.npm-global
   ```
2. **配置 npm 使用此目錄：**
   ```bash
   npm config set prefix '~/.npm-global'
   ```
3. **將新目錄加入您的 `PATH`：**
   開啟您的 shell 配置檔案（例如 `~/.bashrc`、`~/.zshrc` 或 `~/.profile`）並加入這行：
   ```bash
   export PATH=~/.npm-global/bin:$PATH
   ```
   然後重新載入 shell：
   ```bash
   source ~/.bashrc  # 或 ~/.zshrc、~/.profile
   ```
4. **重新嘗試安裝：**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

#### **選項 3：修正 `/usr/local` 的權限（進階）**
如果您想繼續使用 `/usr/local`，可以將其擁有權變更為您的使用者：
```bash
sudo chown -R $(whoami) /usr/local/lib/node_modules
```
然後重新嘗試安裝。

---

**建議：** 使用**選項 2** 以避免未來的權限問題。