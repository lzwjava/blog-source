---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上安裝 FontAwesome5 於 LaTeX
translated: true
type: note
---

在 Ubuntu 上安裝 LaTeX 的 FontAwesome5，您有幾種選擇：

## 方法 1：使用 tlmgr（TeX Live 管理器）

如果您已安裝 TeX Live，可以使用套件管理器：

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5
```

## 方法 2：使用 apt 套件管理器

Ubuntu 透過其軟體庫提供 FontAwesome5：

```bash
sudo apt update
sudo apt install texlive-fonts-extra
```

這將安裝包含 FontAwesome5 的完整字型套裝。

## 方法 3：手動安裝

如果以上方法無效，您可以手動安裝：

1. 從 CTAN 下載 FontAwesome5 套件
2. 將其解壓縮到本機 texmf 目錄：

```bash
mkdir -p ~/texmf/tex/latex/fontawesome5
cd ~/texmf/tex/latex/fontawesome5
# 在此處解壓縮下載的套件
```

3. 更新 TeX 資料庫：
```bash
texhash ~/texmf
```

## 在 LaTeX 中使用 FontAwesome5

安裝完成後，您可以在 LaTeX 文件中使用：

```latex
\documentclass{article}
\usepackage{fontawesome5}

\begin{document}
\faHome \quad 主頁圖示
\faEnvelope \quad 電郵圖示
\faGithub \quad GitHub 圖示
\end{document}
```

## 疑難排解

若遇到問題：

1. 檢查 TeX Live 安裝是否為最新版本：
```bash
tlmgr --version
```

2. 驗證套件是否已安裝：
```bash
tlmgr info fontawesome5
```

3. 確保使用 XeLaTeX 或 LuaLaTeX 以獲得 FontAwesome5 的完整 Unicode 支援。

最簡便的方式通常是使用方法 2，使用 `apt install texlive-fonts-extra`，因為它會自動處理相依性問題。