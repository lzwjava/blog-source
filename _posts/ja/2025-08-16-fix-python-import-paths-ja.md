---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Pythonモジュールのインポートパス修正
translated: true
type: note
---

短い答え: `from scripts.create.delete import delete_md` を実行する前にPythonのモジュール検索パス (`sys.path`) を変更する必要があるため、ここでは `sys` が必要です。

---

### `sys` が必要な理由

* Pythonはインポートするモジュール/パッケージを `sys.path` に格納されたディレクトリリストから検索します。
* デフォルトでは以下が含まれます:

  * 現在のスクリプトのディレクトリ
  * 標準ライブラリのディレクトリ
  * インストールされた site-packages
* あなたの `scripts/create/delete.py` ファイルがこれらのデフォルトの場所にない場合、インポートは `ModuleNotFoundError` で失敗します。

したがって、コードでは以下を実行します:

```python
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
```

これは以下を意味します:

* 現在のファイルの絶対パス (`__file__`) を取得
* 3つ上のディレクトリに移動
* そのディレクトリを `sys.path` に追加

これにより、Pythonは `scripts.create.delete` をプロジェクトルートにあるか、インストールされたもののように解決できるようになります。

---

### `sys` なしの場合

プロジェクトが以下のような構造の場合:

```
project/
├── scripts/
│   └── create/
│       └── delete.py
└── tools/
    └── myscript.py   <-- 実行しているスクリプト
```

`myscript.py` を直接実行すると、Pythonは `project/` がルートであることを自動的に認識しません。以下のいずれかを行わない限り、インポートは失敗します:

* `PYTHONPATH=...` を設定して実行（例: `PYTHONPATH=.. python myscript.py`）、または
* プロジェクトをパッケージ化してインストール（`pip install -e .`）、または
* コード内で `sys.path.append(...)` を使って動的にパスを追加（ここで行われている方法）

---

👉 つまり、`sys` は純粋に**実行時にインポートパスを操作する**ために必要であり、プロジェクトルートを基準にモジュールをインポートできるようにします。

`sys.path` を手動で操作することを避けるための**よりクリーンな代替方法**もお見せしましょうか？