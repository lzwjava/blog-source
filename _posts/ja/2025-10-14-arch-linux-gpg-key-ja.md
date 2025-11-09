---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Arch Linux ISO 検証 GPG キー
translated: true
type: note
---

あなたの鍵束にはこのGPG鍵（Pierre Schmitzに属するフィンガープリント `3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` のもの）が含まれています。これはArch Linux開発者がISOイメージに暗号署名するために使用する公式署名鍵であるためです。これにより、ダウンロードが本物であり改ざんされていないことが保証されます。

macOSにArch Linuxをインストールするための起動可能USBドライブを準備していたとき（おそらく公式Arch wikiガイドに従って）、標準的な検証プロセスには以下の2つのステップが含まれます：
1. ISOとその `.sig` ファイルをダウンロードする
2. 関連する開発者のGPG鍵（今回の場合、最近のISOの主要署名者であるPierre Schmitzの鍵）をインポートし、`gpg --verify archlinux-YYYY.MM.DD-x86_64.iso.sig` のようなコマンドで署名を確認する

おそらく `gpg --keyserver hkps://keys.openpgp.org --recv-keys 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` のようなコマンドを実行して鍵を取得・インポートし、ローカルのGPG鍵束に永続的に追加したため、`gpg --list-keys` に表示されているのです。

これは無害です——GPG鍵は検証用の公開データに過ぎません——多くのArchユーザーはISOを検証した後、こうした鍵をいくつか持つことになります。もし不要であれば削除するには以下を実行してください：
```
gpg --delete-key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
```
（確認を求められますが、これは公開鍵のみを削除し、既に検証済みの署名には影響しません）

[Arch Linux ISO ダウンロードページ](https://archlinux.org/download/)  
[Arch Wiki: MacにArch Linuxをインストール](https://wiki.archlinux.org/title/Install_Arch_Linux_on_Mac)  
[Pierre SchmitzのGPG鍵](https://pierre-schmitz.com/gpg-keys/)