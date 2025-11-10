---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ブラック：Pythonコードフォーマッターガイド
translated: true
type: note
---

Blackは、Python Software Foundation (PSF)によって開発された、意見を持つ妥協のないPythonコードフォーマッタです。主にPEP 8の厳格なサブセットに基づき、Pythonコードを一貫したスタイルに自動的に再フォーマットし、可読性、一貫性、バージョン管理での差分最小化を重視します。Blackを使用することで、開発者は細かいフォーマット詳細の制御を放棄する代わりに、コードレビュー時のスタイル議論の削減、速度、決定性を得られます。Blackはフォーマット済み（"blackened"）コードがプロジェクト間で統一されて見えることを保証し、開発のより重要な側面に時間と精神的エネルギーを節約します。Python 3.8以降をサポートし、最新の安定版リリースはバージョン25.1.0（2025年1月29日リリース）で、正規化されたUnicodeエスケープのケーシングや末尾カンマの改善処理などを持つ2025安定スタイルを導入しています。

Blackの哲学は以下を優先します：
- **一貫性**: 類似の構文は同一にフォーマット
- **一般性**: 特別なケースなしに広く適用されるルール
- **可読性**: 読みやすいコードに焦点
- **差分最小化**: Git差分での変更を減らしレビューを高速化

信頼性と統合機能の高さから、オープンソースおよび専門プロジェクトで広く使用されています。

## インストール

BlackはPyPIで利用可能で、pipを使用してインストールできます。プロジェクトの分離のために仮想環境内でのインストールが推奨されます。

- 基本インストール:
  ```
  pip install black
  ```

- Jupyter Notebookサポートやカラー化差分などの追加機能の場合:
  ```
  pip install 'black[jupyter,colorama]'
  ```
  （`d`エクストラは、エディタ統合用デーモンblackd用です）

Arch Linuxでは、パッケージマネージャ経由でインストール可能: `pacman -S python-black`

Blackはcondaや他のパッケージマネージャ経由でもインストールできます。インストール後、`black --version`で確認してください。

開発やテストのためには、GitHubリポジトリをクローンして編集可能モードでインストール:
```
git clone https://github.com/psf/black.git
cd black
pip install -e .
```

## 使用方法

Blackは主にコマンドラインツールです。基本コマンドはファイルやディレクトリをその場でフォーマットします:

```
black {source_file_or_directory}
```

スクリプトとしての実行が機能しない場合（環境問題など）、以下を使用:
```
python -m black {source_file_or_directory}
```

### 主要コマンドラインオプション

Blackはカスタマイズと制御のための様々なフラグを提供します。主なオプションの概要:

- `-h, --help`: ヘルプを表示して終了
- `-c, --code <code>`: コード文字列をフォーマット（例: `black --code "print ( 'hello, world' )"`）
- `-l, --line-length <int>`: 行の長さを設定（デフォルト: 88）
- `-t, --target-version <version>`: 互換性のためのPythonバージョンを指定（例: `py38`、複数指定可能: `-t py311 -t py312`）
- `--pyi`: ファイルを型スタブ（`.pyi`スタイル）として扱う
- `--ipynb`: ファイルをJupyter Notebookとして扱う
- `--python-cell-magics <magic>`: カスタムJupyterマジックを認識
- `-x, --skip-source-first-line`: 最初の行のフォーマットをスキップ（shebang用）
- `-S, --skip-string-normalization`: 文字列をダブルクォートやプレフィックスに正規化しない
- `-C, --skip-magic-trailing-comma`: 行分割のための末尾カンマを無視
- `--preview`: 次期リリースの実験的スタイル変更を有効化
- `--unstable`: すべてのプレビュー変更と不安定機能を有効化（`--preview`が必要）
- `--enable-unstable-feature <feature>`: 特定の不安定機能を有効化
- `--check`: ファイルを変更せずに再フォーマットが必要かチェック（変更が必要な場合終了コード1）
- `--diff`: ファイルを書き込まずに変更の差分を表示
- `--color / --no-color`: 差分出力をカラー化
- `--line-ranges <ranges>`: 特定の行範囲をフォーマット（例: `--line-ranges=1-10`）
- `--fast / --safe`: AST安全チェックをスキップ（`--fast`）または強制（`--safe`）（デフォルト: safe）
- `--required-version <version>`: 特定のBlackバージョンを要求
- `--exclude <regex>`: 正規表現でファイル/ディレクトリを除外
- `--extend-exclude <regex>`: デフォルト除外に追加
- `--force-exclude <regex>`: 明示的に渡されても除外
- `--include <regex>`: 正規表現でファイル/ディレクトリを含める
- `-W, --workers <int>`: 並列ワーカー数を設定（デフォルト: CPU数）
- `-q, --quiet`: エラー以外のメッセージを抑制
- `-v, --verbose`: 詳細な出力を表示
- `--version`: Blackバージョンを表示
- `--config <file>`: ファイルから設定を読み込み

### 例

- 単一ファイルをフォーマット: `black example.py`
- フォーマットせずにチェック: `black --check .`
- 差分を表示: `black --diff example.py`
- 標準入力をフォーマット: `echo "print('hello')" | black -`
- カスタム行長でフォーマット: `black -l 79 example.py`
- Jupyter Notebookをフォーマット: `black notebook.ipynb`

### ヒントと注意点

- Blackはファイル全体をフォーマット；ブロックをスキップするには`# fmt: off` / `# fmt: on`を、行をスキップするには`# fmt: skip`を使用
- 標準入力の場合、除外を尊重するには`--stdin-filename`を使用
- Blackは決定的：同じ入力は常に同じ出力を生成
- 今後のスタイルをテストするには`--preview`を使用（変更される可能性あり）

## 設定

Blackはコマンドラインフラグまたは`pyproject.toml`ファイル（プロジェクトでの推奨）で設定可能。`pyproject.toml`での設定は`[tool.black]`セクションに記述。

### pyproject.tomlの使用

例:
```
[tool.black]
line-length = 79
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
skip-string-normalization = true
```

サポートされるオプションはCLIフラグと対応（例: `line-length`, `skip-string-normalization`）。`target-version`のような複数値オプションは配列を使用。

### 優先順位

- コマンドラインフラグは設定ファイルの設定を上書き
- `pyproject.toml`が見つからない場合、Blackはデフォルトを使用し親ディレクトリを検索
- カスタム設定ファイルを指定するには`--config`を使用

### ファイル発見と無視

Blackはディレクトリ内のPythonファイルを自動的に発見し、デフォルトで`.gitignore`を尊重。カスタマイズには`--include`/`--exclude`を使用。上書きされない限り、`.git`、`.venv`などの共通ディレクトリを無視。

バージョン管理では、pre-commitのようなツールと統合してフォーマットを強制。

## Blackコードスタイル

Blackは限定的な設定可能性で特定のスタイルを強制します。主要ルール:

### 行の長さ
- デフォルト: 88文字。分割不能な場合（長い文字列など）は超過可能。

### 文字列
- 二重引用符を優先；プレフィックスを小文字に正規化（例: `r`が`f`の前）
- エスケープシーケンスを小文字化（`\N`名を除く）
- ドキュメント文字列を処理：インデント修正、余分な空白/改行を削除、テキスト内タブを保持

### 数値リテラル
- 構文部分を小文字化（例: `0xAB`）、数字を大文字化

### 改行と演算子
- 二項演算子の前で改行
- ほとんどの演算子の周りに単一スペース；単項/べき乗演算子と単純な被演算子ではスペースなし

### 末尾カンマ
- 複数行のコレクション/関数引数に追加（Python 3.6+の場合）
- 「マジック」末尾カンマは存在する場合リストを展開

### コメント
- インラインコメントの前に2スペース；テキストの前に1スペース
- shebang、ドキュメントコメントなどの特別な間隔を保持

### インデント
- 4スペース；括弧をデデントされたクローザーと一致

### 空行
- 最小限の空白：関数内で単一、モジュールレベルで二重
- ドキュメント文字列、クラス、関数の特定ルール

### インポート
- 長いインポートを分割；isortの`black`プロファイルと互換

### その他のルール
- バックスラッシュより括弧を優先
- ファイルに基づいて改行を正規化
- `.pyi`ファイルの簡潔スタイル（例: メソッド間の余分な行なし）
- プレビューモードでインポート後の空行を折りたたみ

Blackは差分削減と可読性向上を目指し、変更は主にバグ修正や新構文サポートのため。

## 統合

Blackはエディタやバージョン管理とシームレスに統合し、自動フォーマットを実現。

### エディタ

- **VS Code**: Python拡張機能でBlackをフォーマッタとして使用。settings.jsonで`"python.formatting.provider": "black"`を設定。LSPの場合、python-lsp-serverとpython-lsp-blackをインストール。
- **PyCharm/IntelliJ**:
  - 組み込み（2023.2+）: 設定 > ツール > Black、パスを設定
  - 外部ツール: 設定 > ツール > 外部ツール、`$FilePath$`引数でBlackを追加
  - ファイルウォッチャー: 保存時自動フォーマット用
  - デーモンベースフォーマット用BlackConnectプラグイン
- **Vim**: 公式プラグインを使用（vim-plug経由: `Plug 'psf/black', { 'branch': 'stable' }`）。コマンド: `:Black`でフォーマット。自動保存: vimrcにautocmdを追加。`g:black_linelength`などの設定変数。
- **Emacs**: reformatter.elまたはpython-blackパッケージを使用して保存時フォーマット
- **その他**: Sublime Text、JupyterLab、Spyderなどをプラグインや拡張機能でサポート

### バージョン管理

- **Pre-commitフック**: `.pre-commit-config.yaml`に追加:
  ```
  repos:
    - repo: https://github.com/psf/black-pre-commit-mirror
      rev: 25.1.0
      hooks:
        - id: black
          language_version: python3.11
  ```
  Jupyter用: `id: black-jupyter`を使用
- **GitHub Actions**: CIチェック用にワークフローで`psf/black-action`のようなアクションを使用
- **Git**: 事前コミットスクリプトやhuskyでBlackを実行して強制

## 高度なトピック

- **プレビューと不安定スタイル**: 将来の変更（例: 括弧の改善）に`--preview`を使用。実験的機能に`--unstable`。
- **Blackd**: 統合用HTTPサーバー（`blackd --bind-host 127.0.0.1 --bind-port 45484`）
- **Jupyterサポート**: マジックを保持しながらノートブックをフォーマット
- **型スタブ**: `.pyi`ファイル用の特別な簡潔フォーマット
- **互換性**: Python 3.8+をターゲット；古いコードには`--target-version`を使用
- **代替手段**: autopep8（より柔軟だが意見が少ない）やRuff（高速、リンティングを含む）との比較

トラブルシューティングは、公式ドキュメントのFAQやGitHubイシューを確認。

## 参考文献

- [Black 25.1.0 ドキュメント](https://black.readthedocs.io/en/stable/)
- [psf/black GitHubリポジトリ](https://github.com/psf/black)
- [The Black Code Style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [Usage and Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
- [Editor Integrations](https://black.readthedocs.io/en/stable/integrations/editors.html)
- [Version Control Integration](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
- [Python Code Formatting Using Black - GeeksforGeeks](https://www.geeksforgeeks.org/python/python-code-formatting-using-black/)
- [How to Auto-Format Your Python Code with Black - freeCodeCamp](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- [Black - PyPI](https://pypi.org/project/black/)
- [Introduction to Python Black Module - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-to-python-black-module/)
- [Python Auto Formatter: Autopep8 vs. Black - Built In](https://builtin.com/data-science/autopep8-vs-black)