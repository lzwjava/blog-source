---
audio: false
generated: true
lang: hant
layout: post
title: 構建 pycrypto 時出錯
translated: true
type: note
---

發生此錯誤是因為 `pycrypto` 套件需要 Python 標頭檔 `longintrepr.h`，該檔案屬於 Python 開發標頭檔的一部分。您的 Python 3.13 環境中缺少此檔案。解決方法如下：

### 解決方案：
1. **安裝 Python 開發標頭檔**  
   為您的作業系統安裝 Python 3.13 開發套件。在 Ubuntu/Debian 上執行：
   ```bash
   sudo apt-get install python3.13-dev
   ```

2. **重新安裝 `pycrypto`**  
   安裝標頭檔後，重新嘗試安裝：
   ```bash
   pip install pycrypto
   ```

---

### 替代建議：
**選項 1：將 `pycrypto` 替換為 `pycryptodome`（推薦）**  
`pycrypto` 已過時且無人維護。請改用維護中的分支 `pycryptodome`，它具備 API 相容性：
```bash
pip uninstall pycrypto
pip install pycryptodome
```

**選項 2：使用舊版 Python**  
如果相容性允許，請使用 Python ≤3.9（已知 `pycrypto` 可在該版本運作）：
```bash
# 使用 pyenv 的範例
pyenv install 3.9.18
pyenv local 3.9.18
pip install -r requirements.txt
```

---

### 問題原因：
- `longintrepr.h` 是 Python 內部標頭檔，用於整數表示。它包含在 Python 開發套件中，但標準安裝不包含。
- Python 3.13 可能進行了結構性變更，導致像 `pycrypto`（最後更新於 2014 年）這類舊版套件無法運作。
- 棄用警告表明 `pycrypto` 使用了新版 `pip` 不支援的過時建置方法。

### 預防措施：
1. **避免使用 `pycrypto`**：密碼學需求請改用 `pycryptodome`。
2. **固定 Python 版本**：對於舊版專案，請在 Docker/Venv 等環境中使用 Python ≤3.9。
3. **檢查相依性**：使用 `pip check` 識別不相容的套件。

---

您列出的所有套件（`aliyunsdkcore`、`aliyun-python-sdk-ecs`、`alibabacloud_vpc20160428` 等）均不直接依賴 **`pycrypto`**。

然而，如果您看到 `pycrypto` 被安裝，可能是某個套件的**間接相依性**。要檢查哪個套件需要 `pycrypto`，請執行：

```bash
pip show pycrypto
```  
或  
```bash
pipdeptree | grep -i pycrypto
```  

### 可能原因：
1. **過時或已棄用的安全相關套件**（儘管您列表中的套件均未明確要求 `pycrypto`）。
2. **來自套件（如 `paramiko` (SSH) 或 `google-auth`）的舊版相依性**，但這些套件通常已改用 `pycryptodome`。

### 建議操作：
1. **將 `pycrypto` 替換為 `pycryptodome`**（現代化、維護中的分支）：
   ```bash
   pip uninstall pycrypto
   pip install pycryptodome
   ```  
   部分套件可將 `pycryptodome` 作為直接替代品。

2. **強制重新安裝相依性**以確保沒有隱藏連結：
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```  

3. **如果 `pycrypto` 仍然存在**，請審核您的環境：
   ```bash
   pipdeptree --warn silence | grep -i crypto
   ```  

### 關鍵要點：
您列出的套件不直接依賴 `pycrypto`，但可能有其他隱藏相依性。使用 `pipdeptree` 進行隔離將有助於找出問題根源。如果沒有關鍵套件需要它，**請直接移除 `pycrypto`**——它已過時且可能存在安全風險。

---

根據您的日誌，您**明確列出的套件**均不直接依賴 `pycrypto`。然而，您的一個相依性存在**間接依賴**。以下是識別和解決方法：

### 1. 識別問題套件
執行以下命令找出哪個頂層套件需要 `pycrypto`：
```bash
pipdeptree --warn silence | grep -i pycrypto
```

### 2. 您套件堆疊中的常見嫌疑對象
根據您的套件列表，最可能的候選對象包括：
- **`paramiko`**（被 `hcloud`、`tigeropen` 或雲端 SDK 使用）
- **`google-auth`**（被 Google Cloud 套件使用）
- **`boto`**（舊版 AWS 函式庫）
- **`ansible`**（如果被間接使用）

### 3. 立即解決方案：替換 `pycrypto`
由於 `pycrypto` 已過時且在 Python 3.13 上無法運作，請改用維護中的分支：
```bash
pip uninstall pycrypto
pip install pycryptodome
```

### 4. 若相依性仍然存在
強制重新安裝所有套件並進行相依性檢查：
```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### 5. 驗證安裝
檢查 `pycryptodome` 是否滿足相依性：
```bash
python -c "from Crypto import Random; print('Success')"
```

### 發生原因
- `pycrypto` 是舊版套件常用的密碼學相依性（最後更新：2014 年）
- Python 3.13 移除了 `pycrypto` 所依賴的內部標頭檔（如 `longintrepr.h`）
- 現代替代方案（如您正在安裝的 `cryptography`）不使用 `pycrypto`

最快解決方案是**步驟 3**——將 `pycrypto` 替換為 API 相容的 `pycryptodome`。這可在保持相容性的同時解決編譯問題。