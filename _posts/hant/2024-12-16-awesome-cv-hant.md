---
audio: false
generated: false
lang: hant
layout: post
title: 使用Awesome-CV生成專業簡歷
translated: true
---

### 簡介  

在使用[ZhiyeApp](https://www.zhiyeapp.com)之前，我轉向了功能強大且可自定義的[Awesome-CV](https://github.com/posquit0/Awesome-CV)。這個基於LaTeX的模板使得創建專業的簡歷變得簡單且高度可定制。

---

### 為什麼選擇Awesome-CV？  
- 可定制性：您可以個性化各個部分、顏色和格式。  
- 專業外觀：乾淨的設計非常適合求職申請。  
- 易於使用：只需基本的LaTeX知識。  

---

### 我的簡歷示例  

以下是我使用的`resume.tex`文件的簡化版本：

```latex
%-------------------------------------------------------------------------------
% 配置
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}

% 頁面邊距和部分高亮
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% 個人信息
%-------------------------------------------------------------------------------
\name{Zhiwei}{Li}
\position{全棧工程師{\enskip\cdotp\enskip}後端工程師}
\address{中國廣州}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``自由真理"}

%-------------------------------------------------------------------------------
\begin{document}

% 頁眉和頁腳
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~簡歷}{\thepage}

% 內容部分
\input{resume/summary.tex}
\input{resume/experience.tex}
\input{resume/education.tex}
\input{resume/corporateprojects.tex}
\input{resume/personalprojects.tex}
\input{resume/blogposts.tex}
\input{resume/papers.tex}
\input{resume/books.tex}
\input{resume/skills.tex}
\input{resume/tools.tex}
\input{resume/knowledge.tex}
\input{resume/certificates.tex}

\end{document}
```

### 自動化的Makefile

為了自動化PDF生成過程，我使用了以下Makefile：

```Makefile
.PHONY: awesome-cv

CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')

awesome-cv: $(foreach x, coverletter resume-zh resume, $x.pdf)

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### 如何使用

1. 生成PDF：
   - 運行`make awesome-cv`以生成以下PDF文件：
     - `resume.pdf`：英文簡歷
     - `resume-zh.pdf`：中文簡歷
     - `coverletter.pdf`：求職信
     
2. 清理：
   - 運行`make clean`以刪除所有生成的PDF文件。

### 結論

通過利用Awesome-CV和這個Makefile設置，生成和維護專業簡歷變得輕而易舉。無論您是申請技術職位還是分享您的成就，Awesome-CV都能幫助您以美觀且高效的方式展示您的工作。

查看Awesome-CV存儲庫以獲取更多詳細信息：[GitHub上的Awesome-CV](https://github.com/posquit0/Awesome-CV)。