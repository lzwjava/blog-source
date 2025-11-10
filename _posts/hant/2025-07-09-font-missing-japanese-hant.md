---
audio: false
generated: true
lang: hant
layout: post
title: 修復日文字體缺字問題
translated: true
type: note
---

您遇到的錯誤表明，LaTeX 文件中使用的 `FandolSong` 字型（包含常規與粗體變體）缺乏特定日文字元的必要字形，例如 `ー` (U+30FC，片假名-平假名長音符號)、`専` (U+5C02)、`証` (U+8A3C) 和 `発` (U+767A)。這導致 XeLaTeX 在編譯您的文件（很可能是 `resume-ja.tex` 或 `latex/ja/resume-ja/` 目錄中的相關文件）時回報「字元缺失」錯誤。

`FandolSong` 字型主要為中文文本設計，不完整支援日文字元，這解釋了字形缺失的原因。為解決此問題，您需要切換至支援日文字元的字型，例如先前建議的 `Noto Sans CJK JP` 或 `IPAGothic`。以下我將指導您透過更新字型配置並確保與您的日文翻譯履歷相容來修復此問題。

### 問題成因
- **字型限制**：`FandolSong` 是 TeX Live 中包含的用於 CJK 排版的中文字型，但並未包含所有日文字元，特別是片假名（`ー`）和日文常用的漢字。
- **XeLaTeX 與 xeCJK**：您的文件很可能使用了 `xeCJK` 套件，該套件依賴指定的 CJK 字型（此處為 `FandolSong`）來處理日文文本。當字形缺失時，XeLaTeX 會記錄錯誤並可能在輸出 PDF 中省略這些字元。
- **翻譯段落**：由於您正在將如 `blogposts.tex` 等段落翻譯為日文，翻譯後的文本包含了 `FandolSong` 無法渲染的日文字元。

### 解決方案：變更 CJK 字型
您需要更新 LaTeX 文件的字型配置，以使用相容日文的字型。根據您之前的訊息，我假設您使用的是帶有字型選擇條件結構的 XeLaTeX 與 `xeCJK`。

#### 步驟 1：安裝相容日文的字型
請確保您的 Linux 系統已安裝支援日文的字型。推薦使用 `Noto Sans CJK JP`，該字型廣泛可用並支援所有必要的日文字形。

在 Ubuntu/Debian 上安裝 `Noto Sans CJK JP`：
```bash
sudo apt-get install fonts-noto-cjk
```
在 Fedora 上：
```bash
sudo dnf install google-noto-cjk-fonts
```
在 Arch Linux 上：
```bash
sudo pacman -S noto-fonts-cjk
```

或者，您可以使用 `IPAGothic` 或 `IPAexGothic`：
```bash
sudo apt-get install fonts-ipaexfont
```

驗證字型是否已安裝：
```bash
fc-list :lang=ja | grep Noto
```
您應該能看到類似 `Noto Sans CJK JP` 或 `Noto Serif CJK JP` 的條目。如果使用 IPA 字型：
```bash
fc-list :lang=ja | grep IPA
```

#### 步驟 2：更新 LaTeX 字型配置
修改您的 LaTeX 文件（很可能是 `resume-ja.tex` 或共享的前言檔案）中的字型配置，以使用相容日文的字型。根據您之前的字型設定，以下是更新配置的方法：

```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    % Linux 字型
    \setCJKmainfont{Noto Sans CJK JP} % 日文主字型
    \setCJKsansfont{Noto Sans CJK JP} % 日文無襯線字型
    \setCJKmonofont{Noto Sans Mono CJK JP} % 日文等寬字型
    \setmainfont{Liberation Serif} % 英文字型
}
```

如果 `Noto Sans Mono CJK JP` 不可用，您可以使用 `Source Code Pro` 或 `DejaVu Sans Mono` 處理非 CJK 等寬文本，但請確保日文程式碼區塊使用 CJK 字型：
```latex
\setCJKmonofont{Noto Sans CJK JP}
```

如果您偏好 `IPAGothic`：
```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{IPAexGothic}
    \setCJKsansfont{IPAexGothic}
    \setCJKmonofont{IPAexMincho} % 或者使用 Noto Sans CJK JP 作為等寬字型
    \setmainfont{Liberation Serif}
}
```

#### 步驟 3：驗證 xeCJK 使用情況
確保您的 LaTeX 文件正確使用 `xeCJK` 套件並套用字型設定。`resume-ja.tex` 的最小範例可能如下所示：

```latex
\documentclass[a4paper]{article}
\usepackage{xeCJK}
\usepackage{ifthenelse}

% 字型系統檢測
\newcommand{\fontsystem}{linux}

\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}

\begin{document}

% 來自 blogposts.tex 的日文文本
\section{ブログ投稿}
こんにちは、私の名前は李智维です。最新の技術に関する記事を書いています。

% 英文文本
\section{Introduction}
Hello, my name is Zhiwei Li.

\end{document}
```

如果您的履歷使用像 `awesome-cv` 這樣的模板，請確保前言包含了 `xeCJK` 和上述字型設定。例如，在 `awesome-cv.cls` 或 `resume-ja.tex` 中加入：

```latex
\RequirePackage{xeCJK}
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}
```

#### 步驟 4：重新編譯文件
導航至日文履歷目錄並重新編譯：
```bash
cd latex/ja/resume-ja
xelatex resume-ja.tex
```

檢查日誌檔案（`resume-ja.log`）中的「字元缺失」錯誤。如果字型設定正確，這些錯誤應該會消失，且 PDF 應正確顯示 `ー`、`専`、`証` 和 `発` 等日文字元。

#### 步驟 5：若錯誤持續存在，進行除錯
如果您仍然看到「字元缺失」錯誤：
1. **確認字型名稱**：確保字型名稱與 `fc-list` 中列出的完全一致。例如，某些系統列出的是 `Noto Sans CJK JP Regular` 而非 `Noto Sans CJK JP`。調整 LaTeX 配置：
   ```latex
   \setCJKmainfont{Noto Sans CJK JP Regular}
   ```
2. **檢查 xeCJK 配置**：確保 `xeCJK` 在字型設定之前載入，且沒有其他套件覆寫 CJK 字型設定。例如，避免載入帶有衝突設定的 `fontspec`。
3. **測試最小範例文件**：建立一個包含日文文本的最小 LaTeX 文件以隔離問題：
   ```latex
   \documentclass{article}
   \usepackage{xeCJK}
   \setCJKmainfont{Noto Sans CJK JP}
   \begin{document}
   こんにちは、専ー証発
   \end{document}
   ```
   使用 `xelatex` 編譯並檢查錯誤。
4. **後備字型**：如果 `Noto Sans CJK JP` 無效，請嘗試 `Source Han Sans JP` 或 `IPAexGothic`。使用 `fc-list :lang=ja` 列出可用字型並相應地更新配置。

#### 步驟 6：更新翻譯段落
由於您使用 Python 腳本翻譯如 `blogposts.tex` 等段落，請確保翻譯後的文件（`latex/ja/resume-ja/blogposts.tex`）透過 `\input{blogposts}` 包含在 `resume-ja.tex` 中。您提供的腳本已正確替換文件，因此無需在此處進行變更。只需在必要時重新執行翻譯：
```bash
python translate_section.py --section blogposts.tex --lang ja --kind resume
```

然後重新編譯 `resume-ja.tex` 以合併更新後的段落。

### 補充說明
- **字型粗細**：`Noto Sans CJK JP` 支援多種粗細（常規、粗體等），因此 `\textbf{}` 應適用於日文文本。如果使用 `IPAexGothic`，請確保粗體變體（`IPAexGothic Bold`）可用或調整配置。
- **模板相容性**：如果您使用像 `awesome-cv` 這樣的模板，請檢查其是否在 `.cls` 檔案中覆寫了字型設定。您可能需要在主文件（`resume-ja.tex`）中套用 `xeCJK` 設定。
- **PDF 輸出**：檢查生成的 PDF 以確保日文字元正確渲染。如果字元顯示為方框，則表示字型仍然不正確或未正確嵌入。
- **系統字型快取**：安裝新字型後，請更新字型快取：
  ```bash
  fc-cache -fv
  ```

### 範例輸出
套用修復後，您在 `latex/ja/resume-ja/` 中的 `blogposts.tex` 可能包含如下日文文本：
```latex
\section{ブログ投稿}
\item 技術ブログ: 最新のAI技術について書いています。専門的な内容をわかりやすく説明します。
```
當使用 `Noto Sans CJK JP` 編譯時，像 `ー`、`専`、`証` 和 `発` 這樣的字元應在 PDF 中正確渲染。

如果您遇到更多錯誤或需要針對履歷模板的特定部分尋求協助，請分享相關的 LaTeX 程式碼（例如 `resume-ja.tex` 的前言或模板的字型設定），我可以提供更具針對性的修復方案！