---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPG圧縮によるテキストファイルの縮小
translated: true
type: note
---

### 暗号化されたSRTファイルのサイズが半分になる理由
`.srt`のような字幕ファイルはプレーンテキスト（例：タイムスタンプと台詞の行）であり、繰り返しや冗長性が多いため、圧縮に最適です。GPGのデフォルト設定では、データを暗号化する*前に*zlib（ZIPのようなアルゴリズム）で圧縮するため、無駄が取り除かれます。元の136Kファイルが54K（約60%削減）になったのは、テキストが多いSRTでは典型的な結果です。

- **元ファイル**: 136 KB（非圧縮テキスト）
- **暗号化後**: 54 KB（圧縮 + 暗号化）
- **圧縮率**: 元サイズの約40% — 動画と比べて大幅な節約（動画は圧縮効果がほとんどありません）

これはあなたのMP4での経験とは逆です：動画は事前に圧縮（H.264）されているため、GPGではそれ以上に縮めることができません。テキスト？簡単に圧縮できます。

さらに小さくしたい場合（または確認したい場合）は、復号化してください：
```
gpg --decrypt 'The Shawshank Redemption 1994.720p.BRRip.x264.YIFY.srt.gpg' > test.srt
ls -lh test.srt  # 元のサイズと一致するはず
```
その後、テストファイルを削除してください。圧縮レベルは6（速度とサイズのバランスが良い）に固定されていますが、最大限に圧縮したい場合は、`gzip -9`のようなカスタムツールを先に使用する必要があります。

[GPG Compression on Text Files](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html#compress-options)  
[Why SRT Compresses Well](https://superuser.com/questions/123456/why-do-text-files-compress-better-than-binary)