---
audio: false
generated: true
image: false
lang: ja
layout: post
title: MeCab設定ファイルパスの修正
translated: true
type: note
---

あなたのエラー

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

は、**MeCabが設定ファイル（`mecabrc`）を見つけられない**ことを意味します。
macOSで、最近Homebrew経由でMeCabをインストールした場合、`/usr/local/`の代わりに`/opt/homebrew/`以下にインストールされている可能性が高いですが、Pythonバインディングは依然として古い`/usr/local/etc/mecabrc`パスを探しています。

以下の方法で修正できます：

---

### 1. `mecabrc`の実際の場所を確認する

以下を実行します：

```bash
brew list mecab
```

または：

```bash
find /opt/homebrew -name mecabrc
```

おそらく以下のような結果が表示されます：

```
/opt/homebrew/etc/mecabrc
```

---

### 2. MeCabに正しいmecabrcを指定する

Pythonコード内でパスを指定できます：

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. 環境変数を設定する方法

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

その後、通常通りスクリプトを実行します：

```bash
python try_mecab.py
```

---

### 4. `/usr/local/etc/mecabrc`を有効にしたい場合

シンボリックリンクを作成することもできます：

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

ただし、環境変数を使用する方法の方がクリーンです。

---

必要であれば、**Homebrewの再インストール + ipadicセットアップ**コマンドもお伝えできます。これにより`-r`を毎回指定せずに動作し、`try_mecab.py`をクリーンな状態に保てます。