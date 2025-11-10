---
audio: false
generated: true
lang: ja
layout: post
title: 日本語フォントの欠落グリフ修正
translated: true
type: note
---

発生しているエラーは、LaTeX文書で使用されている `FandolSong` フォント（Regular と Bold の両バリアント）が、特定の日本語文字（例: `ー` (U+30FC, 音引き記号)、`専` (U+5C02)、`証` (U+8A3C)、`発` (U+767A)）に必要なグリフを含んでいないことを示しています。これが原因で、XeLaTeX が文書（おそらく `resume-ja.tex` または `latex/ja/resume-ja/` 内の関連ファイル）をコンパイルする際に「Missing character」エラーを報告しています。

`FandolSong` フォントは主に中国語テキスト用に設計されており、日本語文字の完全なサポートを備えていないため、グリフが欠落しています。この問題を解決するには、以前に推奨したように、`Noto Sans CJK JP` や `IPAGothic` など、日本語文字をサポートするフォントに切り替える必要があります。以下では、フォント設定を更新し、日本語に翻訳された履歴書との互換性を確保するための修正手順を説明します。

### 問題の原因
- **フォントの制限**: `FandolSong` は TeX Live に含まれる中国語フォントであり、日本語のカタカナ（`ー`）や一般的な漢字など、すべての日本語文字を含んでいません。
- **XeLaTeX と xeCJK**: お使いの文書はおそらく `xeCJK` パッケージを使用しており、日本語テキストに対して指定された CJK フォント（この場合は `FandolSong`）に依存しています。グリフが欠落している場合、XeLaTeX はエラーを記録し、出力 PDF から文字を省略する可能性があります。
- **翻訳されたセクション**: `blogposts.tex` などのセクションを日本語に翻訳しているため、翻訳されたテキストには `FandolSong` がレンダリングできない日本語文字が含まれています。

### 解決策: CJK フォントの変更
LaTeX 文書のフォント設定を、日本語に対応したフォントを使用するように更新する必要があります。以前のメッセージで Linux システムとフォント設定ブロックを使用していることが示されていたため、XeLaTeX と `xeCJK`、およびフォント選択のための `ifthenelse` 構造を使用していると仮定します。

#### ステップ 1: 日本語対応フォントのインストール
Linux システムに日本語サポートを備えたフォントがインストールされていることを確認してください。推奨フォントは `Noto Sans CJK JP` です。これは広く利用可能で、必要なすべての日本語グリフをサポートしています。

Ubuntu/Debian に `Noto Sans CJK JP` をインストールするには:
```bash
sudo apt-get install fonts-noto-cjk
```
Fedora の場合:
```bash
sudo dnf install google-noto-cjk-fonts
```
Arch Linux の場合:
```bash
sudo pacman -S noto-fonts-cjk
```

または、`IPAGothic` または `IPAexGothic` を使用することもできます:
```bash
sudo apt-get install fonts-ipaexfont
```

フォントがインストールされていることを確認します:
```bash
fc-list :lang=ja | grep Noto
```
`Noto Sans CJK JP` や `Noto Serif CJK JP` などのエントリが表示されるはずです。IPA フォントを使用する場合:
```bash
fc-list :lang=ja | grep IPA
```

#### ステップ 2: LaTeX フォント設定の更新
LaTeX 文書（おそらく `resume-ja.tex` または共有プリアンブルファイル）のフォント設定を変更し、日本語対応フォントを使用するようにします。以前のフォント設定に基づいて、設定を更新する方法は以下のとおりです:

```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    % Linux フォント
    \setCJKmainfont{Noto Sans CJK JP} % 日本語用メインフォント
    \setCJKsansfont{Noto Sans CJK JP} % 日本語用サンセリフフォント
    \setCJKmonofont{Noto Sans Mono CJK JP} % 日本語用等幅フォント
    \setmainfont{Liberation Serif} % 英語フォント
}
```

`Noto Sans Mono CJK JP` が利用できない場合は、非 CJK 等幅テキストに `Source Code Pro` や `DejaVu Sans Mono` を使用できますが、日本語のコードブロックが CJK フォントを使用するようにしてください:
```latex
\setCJKmonofont{Noto Sans CJK JP}
```

`IPAGothic` を希望する場合:
```latex
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{IPAexGothic}
    \setCJKsansfont{IPAexGothic}
    \setCJKmonofont{IPAexMincho} % または等幅に Noto Sans CJK JP を使用
    \setmainfont{Liberation Serif}
}
```

#### ステップ 3: xeCJK の使用を確認
LaTeX 文書が `xeCJK` パッケージを使用し、フォント設定が正しく適用されていることを確認してください。`resume-ja.tex` の最小限の例は以下のようになります:

```latex
\documentclass[a4paper]{article}
\usepackage{xeCJK}
\usepackage{ifthenelse}

% フォントシステム検出
\newcommand{\fontsystem}{linux}

\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}

\begin{document}

% blogposts.tex からの日本語テキスト
\section{ブログ投稿}
こんにちは、私の名前は李智维です。最新の技術に関する記事を書いています。

% 英語テキスト
\section{Introduction}
Hello, my name is Zhiwei Li.

\end{document}
```

履歴書が `awesome-cv` のようなテンプレートを使用している場合は、プリアンブルに `xeCJK` と上記のフォント設定が含まれていることを確認してください。例えば、`awesome-cv.cls` または `resume-ja.tex` に以下を追加します:

```latex
\RequirePackage{xeCJK}
\ifthenelse{\equal{\fontsystem}{linux}}{
    \setCJKmainfont{Noto Sans CJK JP}
    \setCJKsansfont{Noto Sans CJK JP}
    \setCJKmonofont{Noto Sans Mono CJK JP}
    \setmainfont{Liberation Serif}
}
```

#### ステップ 4: 文書の再コンパイル
日本語履歴書のディレクトリに移動して再コンパイルします:
```bash
cd latex/ja/resume-ja
xelatex resume-ja.tex
```

ログファイル (`resume-ja.log`) で「Missing character」エラーを確認してください。フォントが正しく設定されていれば、これらのエラーは消え、PDF で `ー`、`専`、`証`、`発` などの日本語文字が正しく表示されるはずです。

#### ステップ 5: エラーが続く場合のデバッグ
「Missing character」エラーがまだ表示される場合:
1. **フォント名の確認**: フォント名が `fc-list` にリストされているものと正確に一致することを確認してください。例えば、一部のシステムでは `Noto Sans CJK JP` の代わりに `Noto Sans CJK JP Regular` とリストされます。LaTeX 設定を調整します:
   ```latex
   \setCJKmainfont{Noto Sans CJK JP Regular}
   ```
2. **xeCJK 設定の確認**: `xeCJK` がフォント設定の前にロードされ、他のパッケージが CJK フォントを上書きしていないことを確認してください。例えば、競合する設定で `fontspec` をロードしないでください。
3. **最小限の文書でのテスト**: 日本語テキストを含む最小限の LaTeX ファイルを作成して問題を切り分けます:
   ```latex
   \documentclass{article}
   \usepackage{xeCJK}
   \setCJKmainfont{Noto Sans CJK JP}
   \begin{document}
   こんにちは、専ー証発
   \end{document}
   ```
   `xelatex` でコンパイルし、エラーを確認します。
4. **フォールバックフォント**: `Noto Sans CJK JP` が機能しない場合は、`Source Han Sans JP` や `IPAexGothic` を試してください。利用可能なフォントを `fc-list :lang=ja` でリストし、設定を適宜更新します。

#### ステップ 6: 翻訳セクションの更新
`blogposts.tex` などのセクションを翻訳するために Python スクリプトを使用しているのであれば、翻訳されたファイル (`latex/ja/resume-ja/blogposts.tex`) が `resume-ja.tex` で `\input{blogposts}` を介してインクルードされていることを確認してください。提供されたスクリプトは既にファイルを正しく置き換えているため、変更は必要ありません。必要に応じて翻訳を再実行してください:
```bash
python translate_section.py --section blogposts.tex --lang ja --kind resume
```

その後、`resume-ja.tex` を再コンパイルして更新されたセクションを組み込みます。

### 追加の注意点
- **フォントの太さ**: `Noto Sans CJK JP` は複数の太さ（Regular、Bold など）をサポートしているため、日本語テキストで `\textbf{}` が機能するはずです。`IPAexGothic` を使用する場合は、太字バリアント (`IPAexGothic Bold`) が利用可能であることを確認するか、設定を調整してください。
- **テンプレートの互換性**: `awesome-cv` のようなテンプレートを使用している場合、`.cls` ファイルでフォント設定が上書きされていないか確認してください。メイン文書 (`resume-ja.tex`) で `xeCJK` 設定を適用する必要があるかもしれません。
- **PDF 出力**: 生成された PDF を確認し、日本語文字が正しくレンダリングされていることを確認してください。文字がボックスとして表示される場合は、フォントがまだ正しくないか、適切に埋め込まれていません。
- **システムフォントキャッシュ**: 新しいフォントをインストールした後、フォントキャッシュを更新します:
  ```bash
  fc-cache -fv
  ```

### 出力例
修正を適用した後、`latex/ja/resume-ja/` 内の `blogposts.tex` には以下のような日本語テキストが含まれる可能性があります:
```latex
\section{ブログ投稿}
\item 技術ブログ: 最新のAI技術について書いています。専門的な内容をわかりやすく説明します。
```
`Noto Sans CJK JP` でコンパイルすると、`ー`、`専`、`証`、`発` などの文字が PDF で正しくレンダリングされるはずです。

さらなるエラーが発生した場合、または履歴書テンプレートの特定の部分についてヘルプが必要な場合は、関連する LaTeX コード（例: `resume-ja.tex` のプリアンブルやテンプレートのフォント設定）を共有していただければ、より具体的な修正を提供できます！