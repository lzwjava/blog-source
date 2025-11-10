---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Git 行尾控制指南
translated: true
type: note
---

`git config core.autocrlf` 控制 Git 在從存儲庫檢出文件及提交文件時如何處理行尾符號。這項設定很重要，因為 Windows 使用 **CRLF** (`\r\n`) 作為行尾符號，而 Linux 和 macOS 使用 **LF** (`\n`)。若未妥善處理，文件格式可能會因編輯者不同而變動，導致出現「不潔」的差異比對和不必要的更改。

---

### 運作原理

* **當檢出（讀取）** 文件時，Git 可能會轉換行尾符號以符合您作業系統的慣例（使它們在編輯器中顯示正常）。
* **當提交（寫入）** 文件時，Git 可能會將行尾符號轉換回 LF（存儲庫中的跨平台標準）。

---

### 設定選項

您可透過以下指令設定：

```bash
git config --global core.autocrlf <value>
```

常用數值：

* `true`
  在檢出時將 **LF → CRLF**，在提交時將 **CRLF → LF**。
  最適合使用 Windows 編輯器編寫程式碼的 **Windows 開發者**。

* `input`
  在檢出時**不**修改文件，但在提交時將 **CRLF → LF**。
  最適合 **Linux/macOS 開發者**，可確保存儲庫僅使用 LF。

* `false`
  完全不進行轉換。Git 會按原樣儲存和檢出文件。
  最適合團隊/編輯器能一致處理行尾符號的情況。

---

### 典型建議

* **Windows**：

  ```bash
  git config --global core.autocrlf true
  ```
* **Linux/macOS**：

  ```bash
  git config --global core.autocrlf input
  ```

對於混合團隊，建議在存儲庫中添加 `.gitattributes` 文件來強制統一行尾符號，例如：

```
* text=auto
```

---

您是否想了解推薦的 **`.gitattributes` 設定**，以便在跨平台團隊中使用（這樣就不僅依賴 `core.autocrlf`）？