---
audio: false
generated: true
lang: hant
layout: post
title: 忽略失敗的 Pip 安裝
translated: true
type: note
---

抱歉造成混淆；`--skip-existing` 並非 `pip` 的有效選項。若要在安裝需求檔案時忽略失敗的套件並繼續安裝其他套件，您可以使用 `--no-dependencies` 標記來避免依賴衝突，或手動處理錯誤。不過，最佳做法是透過 shell 腳本中的迴圈來實現。以下是一行指令，可逐個嘗試安裝 `requirements.top.txt` 中的套件並忽略失敗：

```bash
while read -r package; do pip install --ignore-installed "$package" || true; done < scripts/requirements/requirements.top.txt
```

### 說明：
- `while read -r package`：讀取需求檔案中的每一行（套件名稱）。
- `pip install --ignore-installed "$package"`：嘗試安裝每個套件，忽略已安裝的版本。
- `|| true`：確保即使套件安裝失敗（例如因版本不相容，如 `tensorflow` 與 Python 3.13），迴圈仍會繼續執行。
- `< scripts/requirements/requirements.top.txt`：指定需求檔案的路徑。

### 注意事項：
- **TensorFlow 問題**：您先前遇到的錯誤表示 `tensorflow` 與 Python 3.13 不相容。您可能需要使用 Python 3.12 或更早版本。請按以下步驟操作：
  1. 建立使用 Python 3.12 的虛擬環境：
     ```bash
     python3.12 -m venv venv
     source venv/bin/activate
     ```
  2. 在啟動的虛擬環境中執行上述指令。
- **依賴關係**：可在迴圈中的 `pip install` 指令加入 `--no-dependencies` 標記（`pip install --ignore-installed --no-dependencies "$package" || true`）以避免依賴衝突，但若套件依賴特定相依套件，可能會導致問題。
- **替代方案**：若想排除有問題的套件（如 `tensorflow`），請編輯 `requirements.top.txt` 移除這些套件，或指定相容版本（例如針對 Python 3.12 使用 `tensorflow==2.17.0`）。

若您遇到其他問題或需要協助修改需求檔案，請隨時告知！