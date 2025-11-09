---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: MinGW-w64 同梱実行ファイル
translated: true
type: note
---

### MinGW-w64に含まれる実行ファイル

MinGW-w64は主に、GCCおよび関連ツールを使用したネイティブWindowsアプリケーションのクロスコンパイル用の最小限のツールチェーンです。完全なUnixライクなコマンド一式（例えば、デフォルトでは`gpg`やGnuPGは含まれ**ません**。これらはMSYS2などの環境では別パッケージとして利用可能です）ではなく、開発ユーティリティに焦点を当てています。コアインストールの`bin`ディレクトリには通常、以下の実行ファイルが含まれています（公式SourceForgeリリースなどの標準的なスタンドアロン版ダウンロードに基づく）。このリストはバージョンやビルドによって若干異なる場合がありますが、一般的なものは以下の通りです：

| 実行ファイル | 説明 |
|------------|-------------|
| `gcc.exe` | GNU Cコンパイラ |
| `g++.exe` | GNU C++コンパイラ |
| `cpp.exe` | Cプリプロセッサ |
| `gfortran.exe` | GNU Fortranコンパイラ（ビルドに含まれる場合） |
| `ld.exe` | GNUリンカ |
| `as.exe` | GNUアセンブラ |
| `ar.exe` | ライブラリ作成用アーカイバ |
| `ranlib.exe` | アーカイブラブラリのインデックス生成 |
| `nm.exe` | オブジェクトファイルからのシンボル一覧表示 |
| `objdump.exe` | オブジェクトファイルの情報表示 |
| `objcopy.exe` | オブジェクトファイルのコピーと変換 |
| `strip.exe` | 実行ファイルからのシンボル削除 |
| `size.exe` | オブジェクトファイルのセクションサイズ一覧表示 |
| `strings.exe` | ファイル内の印刷可能文字列の表示 |
| `readelf.exe` | ELFファイル情報の表示（クロスツール用） |
| `dlltool.exe` | DLLインポート/エクスポートファイルの作成 |
| `windres.exe` | Windowsリソースファイルのコンパイル |
| `gendef.exe` | DLLからの.defファイル生成 |
| `genidl.exe` | DLLからの.idlファイル生成 |
| `widl.exe` | Wine/Winelib用IDLファイルコンパイル |
| `gcc-ar.exe` | ar用GCCラッパー |
| `gcc-nm.exe` | nm用GCCラッパー |
| `gcc-ranlib.exe` | ranlib用GCCラッパー |

これらは主にGCCとBinutilsからのコンパイラ、リンカ、およびバイナリ操作ツールです。`gpg`、`make`、`bash`などのより完全なUnixライクな環境については、MSYS2（MinGW-w64をコンポーネントとして含む）をインストールし、`pacman`経由でパッケージを追加することを検討してください。

[MinGW-w64公式サイト](https://www.mingw-w64.org/)  
[MSYS2パッケージ（GnuPGなどの拡張用）](https://packages.msys2.org/package/mingw-w64-x86_64-gnupg)  
[SourceForge MinGW-w64ダウンロード](https://sourceforge.net/projects/mingw-w64/files/)