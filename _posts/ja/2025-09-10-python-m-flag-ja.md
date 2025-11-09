---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Pythonの-mフラグによるモジュール実行
translated: true
type: note
---

はい、`-m` は **モジュールをスクリプトとして実行する** ことを意味します。例を使って詳しく説明しましょう：

### `python -m unittest`

これはPythonに以下のように指示しています：

* 標準ライブラリの一部である `unittest` モジュールを検索します。
* それをスクリプトであるかのように実行します（これが `-m` の役割です）。
* そのため、以下のようなコマンドが実行できます：

  ```bash
  python -m unittest test_example.py
  python -m unittest discover
  ```

  これは、プロジェクト内にスタンドアロンの `unittest` ファイルがなくても動作します — これは標準ライブラリのモジュールだからです。

### `python -m pip`

これは同じパターンです：

* Pythonと一緒にインストールされた `pip` モジュールを検索します。
* それを `pip` 実行ファイルであるかのように実行します。
* したがって、`python -m pip install requests` は pip を実行する「公式の」安全な方法です。なぜなら、使用している `python` と同じ Python インタープリタに対応する pip を使用することが保証されるからです。
  （システム上の `pip` が異なる Python インストールを指している場合があるため、`python -m pip` は混乱を避けることができます。）

### `python test_xx.py` との違い

以下のコマンドを実行する場合：

```bash
python test_xx.py
```

これは、特定のファイルを直接実行しており、`unittest` のテストディスカバリやランナーを使用していません。

* `test_xx.py` の最後に `unittest.main()` がある場合、それはテストを実行します。
* しかし、ディレクトリ配下のすべてのテストを Python に自動的に発見させたい場合は、通常 `python -m unittest discover` に頼ることになります。

---

✅ **まとめ**：

* `-m` = モジュールをスクリプトとして実行する。
* `python -m unittest` は標準ライブラリのテストランナーを実行する。
* `python -m pip` は pip が同じ Python インタープリタに対応することを保証する。
* `python test_xx.py` は単に1つのファイルを実行するだけで、一般的なテストランナーではない。

**pytest** がこれとどのように異なる扱いをするかも説明しましょうか？ `unittest` と `pytest` を比較されるかもしれませんので。