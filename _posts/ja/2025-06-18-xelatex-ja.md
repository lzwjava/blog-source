---
audio: false
generated: true
lang: ja
layout: post
title: XeLaTeXのインストール
translated: true
type: note
---

Ubuntu 24.04 または 22.04 に XeLaTeX をインストールするには、以下の手順に従ってください。

1. **パッケージリストの更新**:
   ```bash
   sudo apt update
   ```

2. **TeX Live のインストール (XeLaTeX を含みます)**:
   - 完全なインストールの場合 (ほとんどのユーザーに推奨、XeLaTeX と多数のパッケージを含む):
     ```bash
     sudo apt install texlive-xetex
     ```
   - 最小限のインストールを希望する場合は `texlive` をインストールすることもできますが、XeLaTeX サポートのためには `texlive-xetex` が推奨されます。

3. **インストールの確認**:
   XeLaTeX がインストールされているか確認するには、次のコマンドを実行します:
   ```bash
   xelatex --version
   ```
   `XeTeX 3.14159265-2.6-0.999991` のような出力が表示されるはずです (バージョン番号は異なる場合があります)。

4. **オプション: 追加フォントのインストール** (XeLaTeX で特定のフォントが必要な場合):
   ```bash
   sudo apt install texlive-fonts-extra
   ```

5. **XeLaTeX のテスト**:
   簡単な `.tex` ファイルを作成します (例: `test.tex`):
   ```latex
   \documentclass{article}
   \usepackage{fontspec}
   \setmainfont{Liberation Serif}
   \begin{document}
   Hello, XeLaTeX!
   \end{document}
   ```
   以下のコマンドでコンパイルします:
   ```bash
   xelatex test.tex
   ```
   `test.pdf` ファイルが生成されるはずです。

**注意点**:
- `texlive-xetex` パッケージは Ubuntu 22.04 および 24.04 のリポジトリで利用可能です。
- 最新版の TeX Live が必要な場合は、TeX Live のウェブサイトから手動でインストールできますが、通常は Ubuntu パッケージで十分です。
- 十分なディスク容量があることを確認してください (`texlive-xetex` で約 1-2 GB、`texlive-full` ではさらに多く必要です)。
- 問題が発生した場合は、`sudo apt install -f` で不足している依存関係を確認してください。

さらにサポートが必要な場合はお知らせください！