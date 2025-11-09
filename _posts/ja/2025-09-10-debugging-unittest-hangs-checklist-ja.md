---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: ユニットテストのデバッグハングチェックリスト
translated: true
type: note
---

`unittest` でのハングは通常、デッドロック（スレッド/非同期）、I/O の停止、サブプロセス/マルチプロセッシングの問題、またはネットワーク呼び出しを待機しているテストが原因です。以下は、*ハングが発生している場所を特定*し、*それを解決する*ための厳選されたチェックリストです。Python 3.9～3.11 で動作します。

### 1) unittest を詳細モードで（かつ正しく）実行する

```bash
# xx.py が unittest.main() を呼び出す場合
python xx.py -v

# または discovery を使用する（推奨）
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> 注: `python -v` は **インタープリターのインポート詳細モード**であり、テストの詳細モードではありません。テスト名と進捗を表示するには `-m unittest -v` を使用してください。

### 2) faulthandler と dev モードを有効化する（ハング時にスタックダンプ、警告を厳格化）

```bash
# 1回限りの実行
python -X faulthandler -X dev -u -m unittest -v
# または環境変数経由
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` は、致命的なシグナルやタイムアウト発生時に Python がスレッドのスタックトレースを出力できるようにします。
* `-X dev` は警告やエラーをより目立たせます。
* `-u` は標準出力/標準エラー出力のバッファリングを解除し、*リアルタイムで*出力を確認できるようにします。

### 3) ハングしていると思われる場合に強制的にトレースバックを取得する

オプション A — 別のターミナルから (Linux/macOS):

```bash
kill -SIGUSR1 <pid>  # faulthandler が有効な場合、全スレッドのスタックをダンプ
```

オプション B — テストのブートストラップコードに追加 (`xx.py` の先頭):

```python
import faulthandler, signal, sys
faulthandler.enable()
# SIGUSR1 でスタックをダンプ:
faulthandler.register(signal.SIGUSR1, all_threads=True)
# また、120秒以上ハングした場合も自動ダンプ:
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) 実行をステップバイステップでトレースする（重いが決定的）

```bash
python -m trace --trace xx.py
# または
python -m trace --trace -m unittest discover -v
```

実行されるすべての行が表示されます。出力が「フリーズ」した時点で停止します—それがハングの発生場所です。

### 5) すぐにデバッガを使用する

```bash
python -m pdb xx.py         # xx.py が unittest.main() を呼び出す場合
# 疑わしい行でブレーク:
# (Pdb) b mymodule.py:123
# (Pdb) c
```

discovery 実行の場合は、疑わしい箇所に `import pdb; pdb.set_trace()` を追加します。

### 6) 一般的な原因とクイックフィックス

* **macOS/Windows でのマルチプロセッシング**: 常にテストエントリをガードする。

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  macOS でテスト内でプロセスを生成する場合:

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # デフォルトの "spawn" よりハングを回避できることがある
  ```

  (コードが fork-safe であることが分かっている場合のみこれを行ってください。)

* **スレッドのデッドロック**: タイムアウトなしの `join()`、解放されていないロック、またはメインスレッドを待機しているバックグラウンドスレッドを確認する。以下を置き換える:

  ```python
  t.join()
  ```

  以下で置き換える:

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **非同期テスト**: `IsolatedAsyncioTestCase` (3.8+) または `asyncio.run()` を使用していることを確認する。二重のイベントループや忘れられた `await` がハングの原因になることが多い。

* **ネットワーク呼び出し**: すべての場所に**短いタイムアウト**を追加する:

  ```python
  requests.get(url, timeout=5)
  ```

* **stdin の待機**: `input()` を削除するか、テスト内でガードする。CI/標準入力が永久にブロックする可能性がある。

* **誤ったモッキング**: `Future`/プロミスを解決しないモックメソッド、または起動されていないスタブサーバー。

### 7) 追加の可視性

* リークやスピンが疑われる場合にアロケーションを確認する:

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* インポートのノイズを表示する（ハングではほとんど必要ない）:

  ```bash
  python -v -m unittest -v
  ```

### 8) 特定の Python バージョンでのみハングする場合

* 両方を試す:

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  違いは通常、`multiprocessing`、`asyncio`、または C 拡張の動作に関連して表面化します。

---

`faulthandler` からのトレースバック（または `trace --trace` からの最終行）を貼り付けて頂ければ、正確な原因を指摘し、対象を絞った修正を提案します。