---
audio: false
generated: true
lang: hant
layout: post
title: Git 憑證管理員
translated: true
type: note
---

你正在 **macOS** 上使用 **Git Credential Manager (GCM) 版本 2.6.1**，並且遇到執行 `git config --global credential.helper manager-core` 時出現錯誤：

```
warning: credential.helper has multiple values
error: cannot overwrite multiple values with a single value
```

這是因為你的 Git 設定中已經設定了多個憑證協助程式。你需要在設定新的協助程式之前**清除現有的值**。

---

### **🛠 修復問題：重設憑證協助程式**
#### **步驟 1：檢查目前的憑證協助程式**
執行：
```sh
git config --global --get-all credential.helper
```
這將列出所有已設定的憑證協助程式。

#### **步驟 2：取消設定先前的憑證協助程式**
使用以下指令重設所有憑證協助程式：
```sh
git config --global --unset-all credential.helper
```

#### **步驟 3：將 GCM 設為唯一的憑證協助程式**
現在，再次將 **Git Credential Manager (GCM)** 設為協助程式：
```sh
git config --global credential.helper manager-core
```

#### **步驟 4：驗證變更**
檢查是否正確設定：
```sh
git config --global --get credential.helper
```
預期輸出：
```
manager-core
```

---

### **🛠 替代方案：使用 `--replace-all`**
如果你想直接覆蓋現有值，而不是先取消設定，請使用：
```sh
git config --global --replace-all credential.helper manager-core
```

---

### **🧩 額外除錯**
如果問題仍然存在，你可以檢查完整的 Git 全域設定：
```sh
git config --global --list
```
如果問題持續，請告訴我！ 🚀

---

Git Credential Manager (GCM) 是一個安全的 Git 憑證協助程式，用於儲存和管理 HTTPS Git 儲存庫的身份驗證憑證。它適用於 GitHub、GitLab、Bitbucket 和 Azure DevOps 等服務。

---

## **1. 安裝 Git Credential Manager**
GCM 隨附於 Git for Windows 以及 macOS 和 Linux 的官方 Git 發行版。如果未安裝，請從以下網址下載：

🔗 **[GitHub 上的 Git Credential Manager](https://github.com/GitCredentialManager/git-credential-manager)**

### **檢查 GCM 是否已安裝**
執行：
```sh
git credential-manager version
```
如果已安裝，你將看到版本號。如果未安裝，請手動安裝。

---

## **2. 設定 Git 使用 GCM**
執行以下指令：
```sh
git config --global credential.helper manager
```
對於 macOS/Linux，請使用：
```sh
git config --global credential.helper manager-core
```

檢查目前的憑證協助程式：
```sh
git config --global credential.helper
```

---

## **3. 向 Git 伺服器進行身份驗證**
設定完成後，當你第一次透過 HTTPS 與遠端儲存庫互動時（例如 `git clone`、`git pull`），GCM 將提示你輸入憑證。

- 如果使用 GitHub、GitLab 或 Bitbucket，GCM 將開啟瀏覽器進行 OAuth 身份驗證。
- 如果使用個人存取權杖 (PAT)，請輸入權杖而非密碼。

---

## **4. 儲存和管理憑證**
GCM 將憑證安全地儲存在作業系統的憑證儲存區中：
- **Windows**：Windows 憑證管理員
- **macOS**：macOS 鑰匙圈
- **Linux**：GPG 加密檔案 (`~/.git-credentials` 或 `~/.gitconfig`)

手動新增憑證：
```sh
git credential approve
```

移除儲存的憑證：
```sh
git credential reject https://github.com
```

清除所有憑證：
```sh
git credential reject
```

---

## **5. 將 Git Credential Manager 用於不同的 Git 供應商**
### **GitHub**
使用**個人存取權杖 (PAT)** 而非密碼：
```sh
git credential reject https://github.com
git pull
```
你將被提示登入並輸入權杖。

### **GitLab**
對於 GitLab，使用 OAuth 或 **PAT**：
```sh
git credential reject https://gitlab.com
git pull
```

### **Azure DevOps**
使用 **PAT** 或 Azure 身份驗證。

---

## **6. 除錯問題**
如果憑證未正確儲存或檢索：
1. 檢查憑證協助程式：
   ```sh
   git config --global credential.helper
   ```
2. 重設 Git Credential Manager：
   ```sh
   git credential reject https://your-git-service.com
   ```
3. 如有需要，請重新安裝 GCM。

需要針對特定服務進行設定協助嗎？ 🚀