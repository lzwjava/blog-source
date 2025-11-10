---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Pythonカバレッジガイドの基礎
translated: true
type: note
---

以下は、**coverage**（coverage.py）パッケージの実践的で開発者向けの紹介です。このパッケージが測定する内容、効果的な使用方法、そして実際に気にするべき設定について説明します。

# coverage.py とは

* テストや任意の実行中に**コードのどの行とブランチが実行されたかを測定する** Python ツールです。
* **テキスト、HTML、XML、JSON** レポートを出力するため、テストカバレッジのギャップを確認したり、CI の品質ゲートに組み込んだりできます。
* unittest、pytest、nose、またはプレーンなスクリプトで動作します。

# 核心的な概念 (平易な言葉で)

*   **行カバレッジ**: その行が少なくとも1回は実行されましたか？
*   **ブランチカバレッジ**: 条件分岐（if/else、ブーリアン短絡評価、例外、内包表記など）の各可能な経路が実行されましたか？
*   **ソース選択**: venv や site-packages からのノイズを避けるため、自身のコードのみを測定対象とします。
*   **データ保存**: 実行により `.coverage` (SQLite) データファイルが作成され、複数の実行結果をマージできます。
*   **コンテキスト**: 実行にラベル（例: テストごと）を付与し、テスト名やコマンドなどでレポートを分割して確認できます。

# クイックスタート

```bash
# 1) インストール
pip install coverage

# 2) カバレッジ計測下でテストを実行 (pytestは一例)
coverage run -m pytest

# 3) ターミナルレポートを表示 (未実行行の行番号付き)
coverage report -m

# 4) HTMLを生成 (ブラウザで htmlcov/index.html を開く)
coverage html

# オプション: 機械可読なレポート
coverage xml        # Sonar, Jenkins, Azure DevOps などのCIツール向け
coverage json       # スクリプトによる分析向け
```

# 推奨される .coveragerc

リポジトリのルートに設定ファイルを作成し、ローカル環境とCIで一貫した結果を得られるようにします。

```ini
[run]
# ノイズを抑えるため、自身のパッケージのみを測定
source = src, your_package
branch = True
parallel = True                 # 複数プロセス/実行が各自のデータを書き込めるようにする
relative_files = True           # レポート内のパスをクリーンに (CIフレンドリー)
concurrency = thread, multiprocessing

# ファイルやパターンを完全に除外することも可能
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # より短いレポートが必要な場合は True に設定
fail_under = 90                 # カバレッジが90%未満の場合にCIを失敗させる
exclude_lines =
    pragma: no cover            # 行を無視する標準プラグマ
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# 異なるマシン/コンテナからのデータを結合する際に有用
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# サブプロセスと並列実行の計測

コードがサブプロセス（マルチプロセシング、CLIツール）を生成する場合、**サブプロセスカバレッジ**を設定します：

1.  `[run]` セクションで `parallel = True` を維持します。
2.  サブプロセスが同じ設定で自動的にカバレッジ計測を開始するよう、環境変数をエクスポートします：

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3.  プログラム/テストを通常通り（または `coverage run -m ...` 経由で）実行します。
4.  全ての実行が終了した後、データをマージしてレポートを生成します：

```bash
coverage combine
coverage report -m
```

> ヒント: `concurrency = multiprocessing, thread, gevent, eventlet, greenlet` とすると、カバレッジが様々な非同期モデルにフックします。

# ブランチカバレッジとプラグマ

*   `[run]` セクションで `branch = True` を有効にします。これにより、見落とされがちな `else` 節、短絡評価、例外経路などが検出されます。
*   テスト不可能な行は末尾コメントで無視できます：
    *   `# pragma: no cover` — その行をカバレッジから除外します。
    *   複雑なブランチの場合、プラグマを過度に使用するよりもリファクタリングを検討してください。

# コンテキスト (テストやタスクごとにカバレッジを分割)

コンテキストは実行された行にラベルを付与し、「どのテストがこのコードをカバーしているか？」という問いに答えられるようにします。

*   pytest を使用する場合が最も簡単です：
    *   `.coveragerc` に `dynamic_context = test_function` を追加します。
    *   その後、`coverage html --show-contexts` を実行するか、コンテキストごとのデータを検査して、どのテストが行を実行したかを確認します。
*   `dynamic_context = test` (テスト nodeid) を設定したり、カスタムランナーで環境変数経由で `dynacontext` を設定することもできます。

# Pytest 連携

主に2つのパターンがあります：

**A. ネイティブな coverage CLI (シンプルで高速)**

```bash
coverage run -m pytest -q
coverage report -m
```

**B. pytest-cov プラグイン (CLIでの利便性を追加)**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

どちらも内部では coverage.py を使用しています。チームの慣習に合う方を選択してください。

# 典型的なCI連携 (GitHub Actions の概略)

```yaml
- name: Install
  run: pip install -U pip coverage pytest

- name: Test with coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Enforce threshold
  run: coverage report --fail-under=90
- name: Upload HTML
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# よくある落とし穴と解決策

*   **レポートが巨大/遅い**: `source=` を制限し、`omit=` を使用して venv、テスト、生成コードをスキップします。
*   **CIとローカルでパスが異なる**: `[paths]` セクションを追加し、`coverage combine` がデータセットをマージできるようにします。
*   **サブプロセスが計測されない**: `COVERAGE_PROCESS_START` を設定し、`parallel = True` を維持した上で、`coverage combine` を実行します。
*   **非同期フレームワーク**: `concurrency = ...` に関連するエントリを追加します。
*   **C拡張**: coverage.py は Python コードを測定し、ネイティブコードは測定しません。Pythonの境界を囲むハーネステストを書いてください。
*   **到達不能コードでの誤検知**: `# pragma: no cover` でマークしますが、テスト可能な動作にするためのリファクタリングを検討してください。

# 実際に使える便利なコマンド

```bash
coverage erase                       # 以前のデータをクリーンアップ
coverage run -m pytest               # 収集
coverage report -m                   # 未実行行の行番号付きテキストサマリー
coverage html                        # htmlcov/index.html を開く
coverage xml                         # CIパーサー向け
coverage json                        # スクリプト/自動化向け
coverage combine                     # 並列/サブプロセスのデータをマージ
coverage annotate                    # 行ごとの .py ファイルを生成し、どの行が実行されたかを表示
```

# チューニングをやめるタイミング

**意味のある閾値**（例: 80–95%）を目標とし、`fail_under` でそれを強制し、コードレビューでは **差分カバレッジ**（新規/変更された行がテストされているか？）に焦点を当てます。（フィーチャーフラグ、防御的ガードなどの）テストが困難なコードで100%を追い求めることは避け、控えめにプラグマを使用し、よりシンプルでテスト可能な設計を優先してください。

必要であれば、すぐにプロジェクトに組み込める、最小限のサンプルリポジトリレイアウト（実行準備の整った `.coveragerc`、pytest 設定、失敗する閾値ゲートを含む）を生成できます。