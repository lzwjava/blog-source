---
audio: false
generated: true
lang: ja
layout: post
title: LaTeXで作るダークレジュメ
translated: true
type: note
---

`resume-en-dark.pdf`をあなたの`awesome-cv-dark.cls`を使用してビルドするには、以下の手順が必要です：

### ✅ 1. ダークバージョン用の新しいLaTeXソースファイルを作成

既存の`resume-en.tex`を複製し、ダークテーマクラスを使用する新しいファイルを作成します：

#### `latex/en/resume-en-dark.tex`

```latex
%-------------------------------------------------------------------------------
% CONFIGURATIONS
%-------------------------------------------------------------------------------
\documentclass[11pt, a4paper]{../awesome-cv-dark} % ここでダークバージョンを使用

% ページマージンを設定
\geometry{left=1.4cm, top=.8cm, right=1.4cm, bottom=1.8cm, footskip=.5cm}

% ハイライトの色
\colorlet{awesome}{awesome-red}

% セクションハイライトを設定
\setbool{acvSectionColorHighlight}{true}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{ifthen}

% 実際の履歴書コンテンツを含める（通常バージョンと同じ）
\input{resume-en-content.tex}
```

> ✅ 重複を避けるために既存の`resume-en-content.tex`を再利用するか、`resume-en.tex`からコピー＆ペーストできます。

---

### ✅ 2. `Makefile`を更新

`resume-en-dark.pdf`をビルドするための新しいルールを`Makefile`に追加します。

`Makefile`のこの部分を見つけて：

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume, $x.pdf)
```

ダーク版の履歴書を含むように修正：

```make
latex: $(foreach x, coverletter coverletter-zh resume-zh resume resume-en-dark, $x.pdf)
```

次にビルドルールを追加：

```make
resume-en-dark.pdf: $(RESUME_EN_DIR)/resume-en-dark.tex $(RESUME_SRCS)
	$(CC) -output-directory=$(RESUME_EN_DIR) $<
```

> 🔁 すべてのアセットを同じフォルダ（`latex/en/resume-en/`）に保持している場合、`RESUME_SRCS`を更新する必要はありません。

---

### ✅ 3. オプション：`copy`ターゲットに追加

生成されたファイルを`assets/resume`にコピーしたい場合は、`copy`を更新：

```make
	cp $(RESUME_EN_DIR)/resume-en-dark.pdf assets/resume/Zhiwei.Li.Resume.Dark.pdf
```

---

### ✅ 4. ビルド実行

以下のコマンドを実行できます：

```bash
make resume-en-dark.pdf
```

---

コンテンツがテーマ間で共有されており、`resume-en-content.tex`のような共有`.tex`ファイルを使用したよりスマートな構造にしたい場合はお知らせください。