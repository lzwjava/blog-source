---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPG ASCIIアーマーの解説
translated: true
type: note
---

GPG（GNU Privacy Guard）において、「armor」はASCII armorを指し、バイナリ形式のOpenPGPデータ（暗号化ファイル、署名、鍵など）を人間が読み取り可能なテキストベースの表現にエンコードする形式です。これは、uuencodeやbase64と同様に、メールなどのテキスト専用チャネルでデータを壊れることなく送信する際に有用ですが、さらにヘッダー（例: "-----BEGIN PGP MESSAGE-----"）と整合性チェックのためのチェックサムが追加されています。

暗号化（`gpg -a -e file.txt`）や鍵のエクスポート（`gpg --armor --export keyid`）などのコマンド実行時に `--armor`（または `-a`）オプションを指定することで有効にでき、結果が生のバイナリではなく、このarmoredテキスト形式で出力されます。

## 参考文献
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)