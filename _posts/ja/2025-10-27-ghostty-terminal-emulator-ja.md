---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 'Ghostty: 高速クロスプラットフォームターミナルエミュレータ'
translated: true
type: note
---

Ghosttyは、macOSとLinux（Windowsサポートは開発中）向けに速度、機能、ネイティブ統合を目指して設計されたクロスプラットフォームのターミナルエミュレータです。主に**Zig**（安全性、パフォーマンス、シンプルさに焦点を当てた現代的なシステムプログラミング言語）で構築されており、あなたが尋ねたRustではありません。

### 主な実装詳細
- **コアアーキテクチャ**: 共有コア（ターミナルエミュレーション、レンダリング、および多くのロジックを処理）はZigで書かれています。これにより、低レベル制御と高いパフォーマンス（macOSではMetal、クロスプラットフォームではVulkan/OpenGLによるGPUアクセラレーションを含む）が実現されています。
- **プラットフォーム固有のレイヤー**: ネイティブな操作性を実現するため、GUIにはプラットフォームのツールキットを使用しています：
  - macOS: ウィンドウ管理とUIにSwift/AppKit。
  - Linux: ウィンドウ管理にGTK。
  - Zigで書かれた共有レンダリングパイプラインが全体を統合します。
- **設計上の注目すべき機能**:
  - 超高速な起動とレンダリング（例：大量の出力でもラグなしで処理）。
  - 合字、絵文字、高度なタイポグラフィのサポート。
  - 拡張性のためのLuaスクリプトによる設定可能。
  - 無駄がなくミニマリストですが、タブ、検索、OSC 52クリップボード統合などの基本機能を備えています。
- **開発哲学**: Mitchell Hashimoto（HashiCorpで有名）によって作成され、xtermのような古いターミナルで一般的な互換性ハックよりも正確性と効率性を重視しています。MITライセンスの下でオープンソースです。

ビルドやハッキングに興味がある場合は、Zigコードベースとビルド手順（Zig 0.13以上が必要）についてGitHubリポジトリを確認してください。

### 参考文献
- [Ghostty GitHubリポジトリ](https://github.com/ghostty-org/ghostty)
- [Ghosttyの紹介（Mitchell Hashimotoのブログ）](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Ghostty 1.0 リリースノート](https://dansasser.me/posts/ghostty-1-0-a-terminal-emulator-built-for-speed-features-and-native-integration/)