---
lang: hant
layout: post
title: 使用Awesome-CV生成专业简历
---

### 引言

在使用[知页简历](https://www.zhiyeapp.com)之前，我转向了功能强大且可高度定制的[Awesome-CV](https://github.com/posquit0/Awesome-CV)。这款基于LaTeX的模板让制作专业简历变得既简单又极具个性化。

---

### 为何选择Awesome-CV？
- **高度可定制**：您可以自由调整章节、颜色及格式。
- **专业外观**：简洁设计，非常适合求职申请。
- **易于使用**：只需基础的LaTeX知识即可上手。

---

### 我的简历示例

以下是我使用的简化版 `resume.tex` 文件：

```latex
%-------------------------------------------------------------------------------
% 配置
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% 页面边距和章节高亮设置
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% 个人信息
%-------------------------------------------------------------------------------
\name{李}{志伟}
\position{全栈工程师{\enskip\cdotp\enskip}后端工程师}
\address{中国，广州}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``自由与真理"}

%-------------------------------------------------------------------------------
\begin{document}

% 页眉与页脚
\makecvheader[C]
\makecvfooter{\today}{李志伟~~~·~~~简历}{\thepage}

% 内容章节
\input{resume/summary.tex} % 个人简介
\input{resume/experience.tex} % 工作经验
\input{resume/education.tex} % 教育背景
\input{resume/corporateprojects.tex} % 公司项目
\input{resume/personalprojects.tex} % 个人项目
\input{resume/blogposts.tex} % 博客文章
\input{resume/papers.tex} % 论文发表
\input{resume/books.tex} % 书籍著作
\input{resume/skills.tex} % 技能专长
\input{resume/tools.tex} % 工具使用
\input{resume/knowledge.tex} % 知识领域
\input{resume/certificates.tex} % 证书资质

\end{document}

自动化构建的Makefile

为了自动化PDF生成过程，我使用了以下的Makefile：

```Makefile
.PHONY: awesome-cv
```

CC = xelatex
范例目录 = awesome-cv
简历目录 = awesome-cv/resume
中文简历目录 = awesome-cv/resume-zh
简历源文件 = $(shell find $(简历目录) -name '*.tex')
中文简历源文件 = $(shell find $(中文简历目录) -name '*.tex')

awesome-cv: $(foreach x, 求职信 简历-中文 简历, $x.pdf)

resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

這段程式碼是一個 Makefile 中的 `clean` 目標，用於刪除指定目錄下的所有 PDF 文件。具體來說：

- `clean:` 是目標名稱，通常用於清理生成的文件。
- `rm -rf $(EXAMPLES_DIR)/*.pdf` 是執行的命令，其中：
  - `rm` 是刪除文件的命令。
  - `-rf` 是選項，`-r` 表示遞歸刪除目錄及其內容，`-f` 表示強制刪除，不提示確認。
  - `$(EXAMPLES_DIR)` 是一個變量，通常指向存放範例文件的目錄。
  - `*.pdf` 表示刪除該目錄下所有以 `.pdf` 結尾的文件。

這段程式碼的作用是清理指定目錄下的所有 PDF 文件。

### 运作原理

1. 生成PDF文件：
   - 运行`make awesome-cv`命令，生成以下PDF文件：
     - `resume.pdf`：英文简历
     - `resume-zh.pdf`：中文简历
     - `coverletter.pdf`：求职信
     
2. 清理：
   - 运行`make clean`命令，删除所有生成的PDF文件。

### 结论

通过利用Awesome-CV和此Makefile设置，生成和维护专业简历变得轻而易举。无论您是申请技术职位还是分享您的成就，Awesome-CV都能帮助您美观高效地展示您的工作。

查看 Awesome-CV 仓库以获取更多详情：Awesome-CV on GitHub。