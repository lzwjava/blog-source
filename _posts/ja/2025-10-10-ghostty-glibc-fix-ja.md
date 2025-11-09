---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ghostty GLIBCバージョン競合の解決
translated: true
type: note
---

あなたが遭遇している問題は、単にインストールの競合だけではありません。主な原因は、Snapとダウンロードした`.deb`の両方がGLIBC 2.38（Ubuntu 24.04のもの）に対してビルドされているのに対し、あなたのシステムはUbuntu 22.04（`libc-bin`パッケージのバージョンからGLIBC 2.35を使用）であることです。これが原因で、バイナリを実行しようとすると「version `GLIBC_2.38' not found」エラーが発生します。両方のインストールが有効な状態だと、パスの競合（例えば、どの`ghostty`バイナリが実行されるか）も引き起こす可能性があるため、まずはそれらを削除して環境を整理すべきです。

### ステップ 1: 既存のインストールを削除する
以下のコマンドを実行して両方をアンインストールします：
```
sudo snap remove ghostty
sudo apt remove ghostty
```
- これにより、Snapバージョンと`.deb`バージョンが削除され、システムには他の影響はありません。
- `which ghostty`（何も返さないはず）と`snap list | grep ghostty`（空のはず）で削除を確認してください。

### ステップ 2: 互換性のあるバージョンをインストールする
GhosttyにはUbuntu 22.04向けの公式`.deb`パッケージはまだありませんが、互換性のある`.deb`ファイルを（他のバージョン向けと同様に）ビルドする信頼できる非公式リポジトリがあります。これはGLIBCの互換性を自動的に処理します。

最も簡単な方法は、自動インストーラスクリプトを使用することです。これはあなたのUbuntuバージョンを検出し、適切なパッケージを取得します：
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/mkasberg/ghostty-ubuntu/HEAD/install.sh)"
```
- これにより、最新の互換性のある`.deb`（現在の最新リリースではv1.2.x前後）がダウンロードされインストールされます。
- 終了後、`ghostty`を実行してテストしてください。GLIBCエラーなしで起動するはずです。
- インストール中に依存関係に関するプロンプト（例: `libonig5`）が表示された場合は、`Y`で承認してください。

手動インストールを希望する場合：
1. [リリースページ](https://github.com/mkasberg/ghostty-ubuntu/releases)にアクセスします。
2. Ubuntu 22.04用と表示されている`.deb`ファイル（例: `ghostty_1.2.1-0.ppa1_amd64_22.04.deb`のような名前。正確な名前はリリースにより異なります）をダウンロードします。
3. `sudo dpkg -i ghostty_*.deb`を実行してインストールします（ダウンロードフォルダから実行してください）。
4. 依存関係の不足に関するエラーが表示された場合は、`sudo apt install -f`で修正してください。

### 追加の注意点
- **ソースからのビルドがここで必要ない理由**: 非公式リポジトリが面倒な作業を代行してくれます。ただし、Ghosttyを自分でビルドしたい場合（例えば、カスタムバージョンのため）は、[公式のソースビルドガイド](https://ghostty.org/docs/install/build)に従ってください。その場合はZig 0.13と`libgtk-4-dev`などの依存関係が必要になりますが、`.deb`を使用する方法の方が簡単です。
- **Ubuntuのアップグレード**: 可能であれば、24.04に移行すると、あなたが試した公式Snapや24.04用の`.deb`を問題なく使用できるようになります。
- インストール後、`~/.config/ghostty/config`でGhosttyを設定できます（オプションについては[ドキュメント](https://ghostty.org/docs/config)を参照してください）。

これらの手順中にエラーが発生した場合は、出力結果をここに貼り付けてさらにサポートを受けてください！