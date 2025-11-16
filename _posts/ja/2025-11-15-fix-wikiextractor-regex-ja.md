---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Python 3.13 正規表現エラーを修正
translated: true
type: note
---

発生しているエラーは、`wikiextractor` パッケージと Python 3.13 の正規表現インラインフラグの厳格な扱いにおける互換性の問題によるものです。具体的には、正規表現パターン内の `(?i)` フラグがグローバルフラグとして解釈されていますが、このフラグが式の先頭に配置されていないため、`re.PatternError` が発生しています。

これを修正するには、ファイル `/home/lzw/.local/lib/python3.13/site-packages/wikiextractor/extract.py` を編集し、378行目付近（または近くの `ExtLinkBracketedRegex` 定義）を以下のように変更します。

- 変更前: `'\\[(((?i)' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`
- 変更後: `'\\[(((?i:' + '|'.join(wgUrlProtocols) + ')' + EXT_LINK_URL_CLASS + r'+)\s*([^\\]\x00-\x08\x0a-\x1F]*?)\\]',`

これにより、`(?i)` の後に `:` を追加して、プロトコルマッチンググループにのみ適用されるローカルインラインフラグ `(?i:...)` に変更され、パースエラーが解決されます。

さらに、`SyntaxWarning: invalid escape sequence '\\['` の警告は、Python 3.13 がより厳格に扱う（ただし主要な失敗の原因ではない）エスケープを含む非 raw 文字列から発生しています。今のところこれらは無視するか、気になる場合は同じファイル内でそれらの文字列を raw 文字列（例: `r'\\['`）に更新してください。

編集後、`wikiextractor *.bz2` を再実行してください。パッケージが古い場合は、`pip install --upgrade wikiextractor` でアップデートを確認するか、回避策としてより古い Python バージョン（例: 3.10）を使用する仮想環境の利用を検討してください。