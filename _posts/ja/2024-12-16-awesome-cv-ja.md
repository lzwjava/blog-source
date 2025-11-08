---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Awesome-CVを使用してプロフェッショナルな履歴書を作成する
translated: true
type: post
---

### はじめに

[ZhiyeApp](https://www.zhiyeapp.com)を使う前、私は強力でカスタマイズ可能な[Awesome-CV](https://github.com/posquit0/Awesome-CV)に切り替えました。このLaTeXベースのテンプレートは、プロフェッショナルな履歴書を作成することを容易にし、高度にカスタマイズ可能です。

---

### Awesome-CVを選ぶ理由  
- カスタマイズ可能: セクション、色、フォーマットを自由にカスタマイズできます。  
- プロフェッショナルな外観: 求職応募に最適なクリーンなデザインです。  
- 使いやすい: 最低限のLaTeX知識で使用可能です。

---

### 私の履歴書の例

以下は私が使用している`resume.tex`ファイルの簡略化バージョンです：

```latex
%-------------------------------------------------------------------------------
% 設定
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{awesome-cv}
```

% ページの余白とセクションのハイライト
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}
\colorlet{awesome}{awesome-red}
\setbool{acvSectionColorHighlight}{true}

%-------------------------------------------------------------------------------
% 個人情報
%-------------------------------------------------------------------------------
\name{李}{志偉}
\position{フルスタックエンジニア{\enskip\cdotp\enskip}バックエンドエンジニア}
\address{中国、広州}
\mobile{(+86) 132-6163-0925}
\email{lzwjava@gmail.com}
\homepage{https://lzwjava.github.io}
\github{lzwjava}
\linkedin{lzwjava}
\quote{``自由と真実"}

```plaintext
%-------------------------------------------------------------------------------
\begin{document}
```

上記のコードは、LaTeX文書の開始を示す部分です。具体的には、`\begin{document}`コマンドが文書の本文の開始を宣言しています。この部分は翻訳の対象外であり、そのまま保持されます。

% ヘッダーとフッター
\makecvheader[C]
\makecvfooter{\today}{Zhiwei Li~~~·~~~履歴書}{\thepage}

% コンテンツセクション
\input{resume/summary.tex} % 概要
\input{resume/experience.tex} % 経験
\input{resume/education.tex} % 学歴
\input{resume/corporateprojects.tex} % 企業プロジェクト
\input{resume/personalprojects.tex} % 個人プロジェクト
\input{resume/blogposts.tex} % ブログ記事
\input{resume/papers.tex} % 論文
\input{resume/books.tex} % 書籍
\input{resume/skills.tex} % スキル
\input{resume/tools.tex} % ツール
\input{resume/knowledge.tex} % 知識
\input{resume/certificates.tex} % 証明書

```latex
\end{document}
```

自動化のためのMakefile

PDF生成プロセスを自動化するために、以下のMakefileを使用しています：

```Makefile
.PHONY: awesome-cv
```

この行は、`awesome-cv`というターゲットがファイル名ではなく、常に実行されるべき「偽のターゲット」であることを示しています。`.PHONY`を使用することで、同じ名前のファイルが存在しても、Makeがそのターゲットを常に実行するようになります。

```makefile
CC = xelatex
EXAMPLES_DIR = awesome-cv
RESUME_DIR = awesome-cv/resume
RESUME_ZH_DIR = awesome-cv/resume-zh
RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')
RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')
```

このMakefileの設定は、以下のように翻訳できます：

- `CC = xelatex`：コンパイラとしてXeLaTeXを使用します。
- `EXAMPLES_DIR = awesome-cv`：例のディレクトリは`awesome-cv`です。
- `RESUME_DIR = awesome-cv/resume`：レジュメのディレクトリは`awesome-cv/resume`です。
- `RESUME_ZH_DIR = awesome-cv/resume-zh`：中国語のレジュメのディレクトリは`awesome-cv/resume-zh`です。
- `RESUME_SRCS = $(shell find $(RESUME_DIR) -name '*.tex')`：`RESUME_DIR`内のすべての`.tex`ファイルを検索し、ソースファイルとして指定します。
- `RESUME_ZH_SRCS = $(shell find $(RESUME_ZH_DIR) -name '*.tex')`：`RESUME_ZH_DIR`内のすべての`.tex`ファイルを検索し、中国語のレジュメのソースファイルとして指定します。

awesome-cv: $(foreach x, coverletter resume-zh resume, $x.pdf)

```makefile
resume.pdf: $(EXAMPLES_DIR)/resume.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<
```

このMakefileのルールは、`resume.pdf`というファイルを生成するためのものです。具体的には、`$(EXAMPLES_DIR)/resume.tex`と`$(RESUME_SRCS)`に依存しており、これらのファイルが変更されると、`resume.pdf`が再生成されます。

- `$(CC)`は、LaTeXコンパイラ（例えば`pdflatex`）を指します。
- `-output-directory=$(EXAMPLES_DIR)`オプションは、生成されたPDFファイルを`$(EXAMPLES_DIR)`ディレクトリに出力することを指定します。
- `$<`は、最初の依存ファイル（この場合は`$(EXAMPLES_DIR)/resume.tex`）を指します。

このルールを実行すると、`resume.tex`がコンパイルされ、`resume.pdf`が生成されます。

resume-zh.pdf: $(EXAMPLES_DIR)/resume-zh.tex $(RESUME_ZH_SRCS)
	$(CC) -output-directory=$(EXAMPLES_DIR) $<

```makefile
coverletter.pdf: $(EXAMPLES_DIR)/coverletter.tex
	$(CC) -output-directory=$(EXAMPLES_DIR) $<
```

このMakefileのルールは、`coverletter.pdf` というファイルを生成するためのものです。具体的には、`$(EXAMPLES_DIR)/coverletter.tex` というLaTeXファイルをコンパイルしてPDFを生成します。`$(CC)` はLaTeXコンパイラ（例えば `pdflatex`）を指し、`-output-directory=$(EXAMPLES_DIR)` オプションで出力ディレクトリを指定しています。`$<` は依存ファイル（この場合は `coverletter.tex`）を指します。

clean:
	rm -rf $(EXAMPLES_DIR)/*.pdf
```

### 仕組み

1. PDFの生成:
   - `make awesome-cv`を実行して、以下のPDFファイルを生成します:
     - `resume.pdf`: 英語の履歴書
     - `resume-zh.pdf`: 中国語の履歴書
     - `coverletter.pdf`: カバーレター
     
2. クリーンアップ:
   - `make clean`を実行して、生成されたすべてのPDFファイルを削除します。

### 結論

Awesome-CVとこのMakefileの設定を活用することで、プロフェッショナルな履歴書の作成と維持が簡単になります。技術職に応募する場合でも、自分の成果を共有する場合でも、Awesome-CVはあなたの仕事を美しく効率的に表現する手助けをします。

詳細については、Awesome-CVリポジトリをチェックしてください: [Awesome-CV on GitHub](https://github.com/posquit0/Awesome-CV)。