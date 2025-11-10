---
audio: false
generated: true
lang: hant
layout: post
title: 使用 LaTeX 製作暗色履歷
translated: true
type: note
---

為了支援使用你的 `awesome-cv-dark.cls` 建置 `resume-en-dark.pdf`，你需要：

### ✅ 1. 為深色版本建立新的 LaTeX 原始檔

複製你現有的 `resume-en.tex` 到一個新檔案，該檔案使用深色主題類別：

#### `latex/en/resume-en-dark.tex`

```latex
%-------------------------------------------------------------------------------
% 設定
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{../awesome-cv-dark} % 在此使用深色版本

% 設定頁面邊界
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

% 高亮顏色
\colorlet{awesome}{awesome-red}

% 設定章節高亮
\setbool{acvSectionColorHighlight}{true}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{ifthen}

% 包含實際的履歷內容（與你的正常版本相同）
\input{resume-en-content.tex}
```

> ✅ 你可以重複使用現有的 `resume-en-content.tex` 以避免重複，或從 `resume-en.tex` 複製/貼上。

---

### ✅ 2. 更新 `Makefile`

在你的 `Makefile` 中為建置 `resume-en-dark.pdf` 新增一條規則。

找到 `Makefile` 中的這部分：

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)
```

修改它以包含深色履歷：

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume resume-en-dark, $x.pdf)
```

然後新增建置規則：

```make
resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<
```

> 🔁 如果你將所有資源保存在同一資料夾 (`latex/en/resume-en/`) 中，則無需更新 `RESUME_SRCS`。

---

### ✅ 3. 可選：新增到 `copy` 目標

如果你想將生成的檔案複製到 `assets/resume`，請更新 `copy`：

```make
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
```

---

### ✅ 4. 建置它

現在你只需執行：

```bash
make resume-en-dark.pdf
```

---

如果你希望內容在不同主題間共享，並想使用像 `resume-en-content.tex` 這樣的共享 `.tex` 檔案來建立更聰明的結構，請告訴我。