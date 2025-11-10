---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Pythonバージョン不一致の修正
translated: true
type: note
---

**Pythonバージョンの不一致**の問題が発生しているようですね。

ログを確認すると:

* `python3` → **3.10.12**
* `python` → **3.13.7**

Claude Code（またはリサーチエージェントスクリプト）が `python3` を呼び出すと、3.10が使用されますが、この環境には `pyperclip` がインストールされていません。あなたは3.13の環境に `pyperclip` をインストールしたため、3.10からは見えません。

解決方法はいくつかあります:

---

### 1. 使用したいPythonでClaude Codeを実行する

Claude Codeに常にPython 3.13を使用させたい場合は、シェルで実行ファイルを明示的に設定します:

```bash
export PYTHON_EXECUTABLE=$(which python)
```

または `python3` を指定したい場合:

```bash
export PYTHON_EXECUTABLE=$(which python3)
```

その後、Claude Codeやエージェントを起動すると、この環境変数を読み取ります。

---

### 2. `python3` をPython 3.13にポイントする

Ubuntuでは `alternatives` システムを更新できます:

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 2
sudo update-alternatives --config python3
```

そしてPython 3.13を選択します。

---

### 3. Python 3.10に `pyperclip` をインストールする

`python3` で3.10を使用し続けたい場合は、そこにインストールします:

```bash
python3 -m pip install --user pyperclip
```

これで `python3` がインポートできるようになります。

---

### 4. 仮想環境を使用する

ベストプラクティス: 使用したいPythonでvenvを作成し、その中でClaude Codeを実行します:

```bash
python3.13 -m venv ~/.venvs/claude
source ~/.venvs/claude/bin/activate
pip install pyperclip
```

その後、このvenv内でエージェントを起動すると、常に3.13が使用されます。

---

👉 質問: Claude Codeを**常にPython 3.13で実行**したいですか？それとも、`python3` を3.10のままにして、不足しているモジュールだけを修正すれば十分ですか？