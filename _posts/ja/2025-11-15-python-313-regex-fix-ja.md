---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Python 3.13 正規表現エラーの修正
translated: true
type: note
---

表示されているエラーは、**Python 3.13** が正規表現の構文に関して以前のバージョンよりも厳格になったことが原因です。

具体的には、`wikiextractor/extract.py` (およそ378行目) のこの行が、Python 3.13 では無効になりました:

```python
ExtLinkBracketedRegex = re.compile(
    '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
    re.S | re.U)
```

問題は、文字列連結の後にパターン内に配置されたインラインの `(?i)` フラグです。Python 3.12/3.13 から、**インラインフラグ `(?i)` などは、正規表現パターンの先頭以外では許可されなくなりました**。

### クイックフィックス (Python 3.13 で動作)

ファイルを編集します:

```bash
~/.local/lib/python3.13/site-packages/wikiextractor/extract.py
```

およそ378行目に移動し、壊れたブロックを以下の修正版に置き換えてください:

```python
# 古い壊れた方法 (Python 3.13 で失敗)
# ExtLinkBracketedRegex = re.compile(
#     '\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',
#     re.S | re.U)

# 修正版 – 大文字小文字を区別しないフラグを re.compile のフラグに移動
protocol_pattern = '|'.join(wgUrlProtocols)
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + protocol_pattern + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.IGNORECASE | re.DOTALL | re.UNICODE
)
```

または、さらに洗練された方法 (推奨):

```python
ExtLinkBracketedRegex = re.compile(
    r'\\['
    r'(((' + '|'.join(wgUrlProtocols) + r')' + EXT_LINK_URL_CLASS + r'+)'
    r'\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\])',
    re.I | re.S | re.U
)
```

`re.I` は `re.IGNORECASE` と同じであり、フラグとして渡すことでパターン内に `(?i)` を埋め込む必要がなくなります。

### 代替ソリューション

1.  Python 3.11 または 3.12 を使用する (パッチを適用したくない場合に最も簡単)
    ```bash
    python3.11 -m pip install wikiextractor
    # その後、python3.11 wikiextractor ... で実行
    ```

2.  Python 3.13 互換性を既に修正しているメンテナンスされているフォークを使用する:
    ```bash
    pip uninstall wikiextractor
    pip install git+https://github.com/attardi/wikiextractor.git
    ```

    Giuseppe Attardi のフォークは Python 3.12+ 用に更新されており、3.13 で完全に動作します。

3.  非常に高速な現代的で代替手段を使用する (大規模なダンプには強く推奨):
    ```bash
    pip install wikiextractor-ng   # または "wiki-dump-tools", "wikitextprocessor" など
    ```

パッチを適用するか、修正されたフォークに切り替えた後、あなたのコマンドは再び動作します:

```bash
wikiextractor *.bz2
```

ワンライナーパッチや、自動的に修正する正確な `sed` コマンドが必要な場合はお知らせください。