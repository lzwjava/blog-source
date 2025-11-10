---
audio: false
generated: true
lang: hant
layout: post
title: 安裝 XeLaTeX
translated: true
type: note
---

在 Ubuntu 24.04 或 22.04 上安裝 XeLaTeX，請按照以下步驟操作：

1. **更新套件清單**：
   ```bash
   sudo apt update
   ```

2. **安裝 TeX Live（包含 XeLaTeX）**：
   - 完整安裝（推薦大多數使用者使用，包含 XeLaTeX 及眾多套件）：
     ```bash
     sudo apt install texlive-xetex
     ```
   - 若需要最小化安裝，可改為安裝 `texlive`，但建議使用 `texlive-xetex` 以獲得完整的 XeLaTeX 支援。

3. **驗證安裝**：
   執行以下指令檢查 XeLaTeX 是否成功安裝：
   ```bash
   xelatex --version
   ```
   您應該會看到類似 `XeTeX 3.14159265-2.6-0.999991` 的輸出（版本號碼可能有所不同）。

4. **可選：安裝額外字型**（若需為 XeLaTeX 使用特定字型）：
   ```bash
   sudo apt install texlive-fonts-extra
   ```

5. **測試 XeLaTeX**：
   建立簡單的 `.tex` 檔案，例如 `test.tex`：
   ```latex
   \documentclass{article}
   \usepackage{fontspec}
   \setmainfont{Liberation Serif}
   \begin{document}
   Hello, XeLaTeX!
   \end{document}
   ```
   使用以下指令編譯：
   ```bash
   xelatex test.tex
   ```
   此操作將生成 `test.pdf` 檔案。

**注意事項**：
- `texlive-xetex` 套件可在 Ubuntu 22.04 及 24.04 的套件庫中取得。
- 若需最新版 TeX Live，可從 TeX Live 官網手動安裝，但通常 Ubuntu 套件版本已足夠使用。
- 請確保磁碟空間充足（`texlive-xetex` 約需 1-2 GB，`texlive-full` 需要更多空間）。
- 若遇到問題，可透過 `sudo apt install -f` 檢查並安裝缺失的相依套件。

如需進一步協助，請隨時告知！