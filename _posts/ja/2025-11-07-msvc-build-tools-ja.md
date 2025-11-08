---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-4.5-sonnet
title: MSVC ビルドツールの用途と代替手段
translated: true
type: note
---

MSVC Build Toolsは確かに巨大です！以下が実際の使用用途です：

## 主な用途

**Rust固有の場合：**
- **C/C++依存関係**を持つRustクレートのビルド（非常に一般的）
- ネイティブWindowsシステムAPIのコンパイル
- Windowsライブラリへのリンク
- `cc`クレートやbindgenを使用するプロジェクトのビルド

**一般的な目的：**
- WindowsでのC/C++コードのコンパイル
- ネイティブ拡張を持つPythonパッケージのビルド（numpy、pandasなど）
- Node.jsネイティブアドオンのコンパイル
- WindowsでC/C++コンパイラを必要とするソフトウェアのビルド

## なぜこんなに大きいのか？

肥大化の原因：
- Windows SDK（すべてのWindowsバージョン用のヘッダー、ライブラリ）
- 複数のコンパイラツールチェーン（x86、x64、ARM、ARM64）
- ATL/MFCライブラリ
- デバッグツールとシンボル
- ビルドシステムコンポーネント（MSBuild）

## より軽量な代替案

Rustのみが必要な場合：
1. **GNUツールチェーンの使用** - `rustup`を`x86_64-pc-windows-gnu`ターゲットでインストール（MinGWが必要、約2-3GB）
2. **WSL2** - Linuxツールチェーンを完全に使用
3. **最小限のMSVCインストール** - インストール中に不要なオプションコンポーネントを選択解除

C/C++依存関係のない純粋なRustコードの場合、MSVCはまったく必要ありません。しかし現実的には、多くの人気クレート（`openssl-sys`、`ring`、ウィンドウライブラリなど）がCコンパイラを必要とするため、ほとんどのWindows Rust開発者は結局インストールすることになります。

これは煩わしいですが、Microsoftのツールチェーンは常に重いものでした。GNUの代替案は動作しますが、一部のクレートで互換性の問題が発生することがあります。