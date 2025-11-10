---
audio: false
generated: true
lang: hant
layout: post
title: 修復 TeX Live tlmgr 使用者模式
translated: true
type: note
---

錯誤訊息顯示您的 Debian/Ubuntu 系統尚未初始化 `tlmgr` 使用者模式。這是從 Ubuntu 儲存庫安裝 TeX Live 時常見的問題。以下提供解決方法：

## 解決方案 1：初始化 tlmgr 使用者模式

首先初始化使用者模式：

```bash
tlmgr init-usertree
```

如果無效，請嘗試：

```bash
tlmgr --usermode init-usertree
```

## 解決方案 2：改用 apt（Ubuntu 推薦方案）

由於您使用的是 Ubuntu/Debian，通常使用系統套件管理器會更簡單：

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

這將安裝 FontAwesome5 及其他字型套件。

## 解決方案 3：檢查 FontAwesome5 是否已安裝

您可能已經安裝了該套件。請建立一個簡單的 LaTeX 檔案進行測試：

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome
\end{document}
```

使用以下指令編譯：
```bash
pdflatex test.tex
```

## 解決方案 4：如需最新版本

若您特別需要最新版的 FontAwesome5，可以：

1. 從 CTAN 手動下載套件
2. 安裝到本機 texmf 目錄：

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
# 將下載的套件解壓縮至此目錄
texhash ~/texmf
```

## 快速檢查

若要查看目前已安裝的 TeX 套件：

```bash
dpkg -l | grep texlive
```

對大多數使用者而言，`sudo apt install texlive-fonts-extra` 是最簡單的解決方案，能完全避開 tlmgr 使用者模式的問題。