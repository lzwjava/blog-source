---
audio: false
generated: true
lang: hant
layout: post
title: 修復 typing-extensions 套件問題
translated: true
type: note
---

### 如何修復「Cannot uninstall typing-extensions None」錯誤

當您在使用 pip 安裝套件時遇到此錯誤，是由於解除安裝 `typing-extensions` 套件時出現問題。錯誤訊息顯示：

```
error: uninstall-no-record-file
× Cannot uninstall typing-extensions None
╰─> The package's contents are unknown: no RECORD file was found for typing-extensions.
```

此錯誤發生是因為 pip 試圖解除安裝現有的 `typing-extensions` 安裝（可能是為了替換成您要安裝的套件所需的版本），但由於 RECORD 檔案遺失而無法繼續。RECORD 檔案是 pip 用來追蹤套件安裝檔案的元數據檔案，沒有它，pip 就不知道如何正確解除安裝 `typing-extensions`。安裝日誌還提供了一個有用的提示：

```
hint: You might be able to recover from this via: pip install --force-reinstall --no-deps typing-extensions==4.14.0
```

以下是逐步解決此問題並成功完成套件安裝的方法。

---

### 步驟 1：了解問題
日誌顯示 pip 正在安裝以下套件：
- `pyperclip`
- `typing-extensions`
- `packaging`
- `jmespath`

在此過程中，pip 嘗試解除安裝現有的 `typing-extensions`，因為您正在安裝的某個套件（或現有依賴項）可能需要特定版本的 `typing-extensions`。然而，解除安裝失敗是因為當前 `typing-extensions` 安裝的 RECORD 檔案遺失或損毀。這可能是由於套件安裝不當、RECORD 檔案被刪除，或過往安裝過程中斷所致。

錯誤訊息中的「typing-extensions None」表明 pip 無法確定現有安裝的版本，這進一步顯示其元數據存在問題。

---

### 步驟 2：修復 `typing-extensions` 安裝
要解決此問題，您需要修復損壞的 `typing-extensions` 安裝。提示中的建議命令是最佳方法：

```bash
pip install --force-reinstall --no-deps typing-extensions==4.14.0
```

#### 此命令的作用：
- **`pip install`**：安裝指定套件。
- **`--force-reinstall`**：強制 pip 重新安裝 `typing-extensions`，即使已存在，並覆蓋現有安裝。
- **`--no-deps`**：防止 pip 安裝 `typing-extensions` 的任何依賴項。由於 `typing-extensions` 是一個獨立的純 Python 套件，沒有依賴項，此標誌可確保在不影響其他套件的情況下進行乾淨的重新安裝。
- **`typing-extensions==4.14.0`**：指定版本 4.14.0，這很可能是 pip 在發生錯誤時嘗試安裝的版本。

執行此命令將：
- 重新安裝 `typing-extensions` 版本 4.14.0。
- 在套件目錄（通常在 `site-packages` 中）創建正確的 RECORD 檔案。
- 修復損毀或不完整的安裝。

#### 執行命令：
開啟終端機並執行：

```bash
pip install --force-reinstall --no-deps typing-extensions==4.14.0
```

此命令成功完成後，`typing-extensions` 套件應正確安裝並包含所有必要的元數據。

---

### 步驟 3：重試原始安裝
一旦 `typing-extensions` 修復完成，您就可以繼續安裝原本打算安裝的套件。根據日誌，您可能執行了類似以下的命令：

```bash
pip install pyperclip
```

此命令可能觸發了 `pyperclip`、`typing-extensions`、`packaging` 和 `jmespath` 的安裝，因為 `pyperclip` 或其他套件對它們有依賴關係。現在 `typing-extensions` 已正確安裝，解除安裝問題應不再出現。

#### 執行原始命令：
重試安裝命令：

```bash
pip install pyperclip
```

現在這應該會無錯誤完成，並成功安裝所有收集的套件。

---

### 為何此方法有效
- 遺失的 RECORD 檔案阻止 pip 解除安裝舊的 `typing-extensions` 安裝，導致過程失敗。
- 強制重新安裝指定版本的 `typing-extensions` 確保 pip 能夠正確管理該套件。
- `--no-deps` 標誌將修復隔離在 `typing-extensions` 上，避免對其他套件進行不必要的更改。

---

### 補充說明
- **安全性**：由於 `typing-extensions` 是一個純 Python 套件，而非系統級依賴項，強制重新安裝是安全的，不會破壞您的 Python 環境。
- **版本確認**：提示指定了版本 4.14.0，這很可能是您安裝的某個套件所需的版本。如果您需要其他版本，可以檢查 `pyperclip`、`packaging` 或 `jmespath` 的要求（例如，透過它們的文件或安裝後使用 `pip show <package>`）。
- **手動清理（不推薦）**：您可以手動從 `site-packages` 刪除 `typing-extensions` 資料夾，但這樣做風險較高且不必要，因為 `pip --force-reinstall` 會乾淨地處理它。

---

### 最終步驟
1. 修復 `typing-extensions`：
   ```bash
   pip install --force-reinstall --no-deps typing-extensions==4.14.0
   ```
2. 安裝您的套件：
   ```bash
   pip install pyperclip
   ```

完成這些步驟後，錯誤應已解決，您的套件安裝將成功完成。如果您遇到任何其他問題，請隨時分享更新後的日誌以獲得進一步協助！