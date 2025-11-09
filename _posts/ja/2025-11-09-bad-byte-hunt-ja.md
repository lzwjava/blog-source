---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 悪しきバイトを追って
translated: true
type: note
---

### 悪いバイトが見つからなかった理由
取得した`hexdump`の出力は、**ファイルオフセット** (`000008d0`) に一致しており、実際のコンテンツ内の`\x8D`バイトではありません。Grepは行全体をテキスト検索しており、「8d」は16進数のアドレス（例: `08d0`）に現れるため、無関係な行を引き出してしまいました。その場所のデータバイト（`6f 67 20 ...`）は、`"og = og_images[i"`という通常のASCII文字であり、問題はありません。

### `\x8D`を探すより良い方法
プロジェクトディレクトリ（`_layouts/default.html`の隣）で以下のコマンドを試してください。これらはファイルのバイトを直接スキャンします。

1. **改良されたHexdump（データ内のバイトをGrep）**:
   これは` 8d `（オフセットではなく16進バイトに一致するよう前後にスペース）をgrepします:
   ```
   hexdump -C _layouts/default.html | grep ' 8d '
   ```
   - 何か見つかった場合、オフセット（左列）と周囲のバイトが表示されます。オフセットをメモし、エディタ（例: VS Code: Ctrl+G > バイトオフセット / 16 でおおよその行）でその位置にジャンプします。
   - ヒット時の出力例: `00001234  ...  8d  20  61  62  ... |... ab...|`

2. **`xxd`を使用（Hexdumpより優れていることが多い）**:
   macOSには`xxd`が組み込まれています:
   ```
   xxd _layouts/default.html | grep 8d
   ```
   - 同様: 16進バイト内の「8d」に一致します。出力がなければ、そのバイトは存在しません（稀ですが、別のファイルにある場合は可能性あり）。

3. **バイナリGrep（直接バイト検索）**:
   ```
   grep -a -o -P '\x8d' _layouts/default.html | hexdump -C
   ```
   - これはバイトに完全一致するものを抽出し、16進数でダンプします。空であれば、`\x8D`はありません。

4. **Rubyワンライナー（正確な位置）**:
   前に提案した通り—これを実行してバイトインデックスを取得します:
   ```
   ruby -e "File.open('_layouts/default.html', 'rb') { |f| f.read.each_byte.with_index { |b, i| puts \"Found at byte #{i}: #{b.chr(Encoding::ASCII_8BIT).inspect}\" if b == 0x8D } }"
   ```
   - 出力例: `Found at byte 1234: "\x8D"`。その後、編集: ファイルを開き、文字のおよそ1234番目（または行 = 1234/80程度）に移動し、不可視文字を削除します（何もないように見えるかもしれません；周囲を選択/削除してください）。

### もし一致しなければ？
- `\x8D`は**別のファイル**（例: レイアウトの`{{ content }}`経由でレンダリングされる`_posts/`内の投稿）にある可能性があります。サイト全体をスキャンします:
  ```
  find . -name "*.md" -o -name "*.html" | xargs grep -l $'\x8D'
  ```
  （または疑わしいファイルそれぞれに対してRubyスクリプトを使用します。）
- または、ファイル先頭のBOM/不可視文字である可能性: エディタで開き、最初の行が空なら削除し、UTF-8で再保存します。

一度削除したら、`bundle exec jekyll serve --incremental`を再度実行してください。まだ問題が解決しない場合は、これらのコマンド（またはRubyのもの）のいずれかの出力を貼り付けてください。それで解決します。

[バイト狩りのためのHexdumpのヒント](https://unix.stackexchange.com/questions/38331/finding-bad-characters-in-hex-dump)