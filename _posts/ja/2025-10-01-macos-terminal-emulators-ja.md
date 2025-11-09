---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: macOS用ターミナルエミュレーターの代替トップ
translated: true
type: note
---

iTerm2とGhostty以外のmacOS向け人気ターミナルエミュレーターには、パフォーマンス、機能、カスタマイズ性など様々なニーズに応えるオープンソースおよびプロプライエタリな選択肢がいくつかあります。これらは最近の推奨情報とランキングに基づき、macOS互換アプリケーションに焦点を当てています。

### 人気の代替案
- **Alacritty**: 高速なGPUアクセラレーション対応ターミナルで、カスタマイズ可能なテーマとVimライクな編集機能を備えています。軽量でコーディングに高いパフォーマンスを発揮しますが、余計な機能はありません。[1] [1][2]
- **Kitty**: GPUアクセラレーションと、タブ、分割、デスクトップ通知などのモダンな機能で知られています。拡張機能をサポートし、大規模ワークフローでの効率性を求めるパワーユーザーに最適です。[1] [2][3][4]
- **WezTerm**: シリアルマルチプレクシング、グラフィカルな選択、Luaによるスクリプトなどの高度な機能を備えたクロスプラットフォームのターミナルです。詳細な設定と効率的なマルチタスキングに理想的です。[1][5]
- **Warp**: AI連携機能（セッション共有の「Warptime」など）や組み込みの補完機能を備えたモダンなターミナルです。チームでの使用に便利ですが、独特なUIにより学習曲線があります。[1] [3][4][5]
- **Hyper**: Webテクノロジー上に構築され、プラグインとテーマによる拡張性を提供します。CSSとJavaScriptによるカスタマイズを求める開発者向けですが、リソースを多く消費する可能性があります。[4][5]
- **Tabby**: SSH/Telnetサポート、多言語テーマ、分割ビューを備えた多機能ターミナルです。リモート作業や基本的な日常使用に適しており、暗号化された資格情報のオプションがあります。[6] (Redditの議論では、潜在的なバグはあるものの、代替案としてTabbyが挙げられています。)
- **CoreShell**: SSHとSFTPに特化し、スマート認証やセッション管理などの機能を備えています。ローカルターミナル作業ではなく、安全なリモート接続に最適です。[3] [4]
- **Commander One**: 統合ターミナルを備えたファイルマネージャーで、デュアルペインブラウジングとクイックコマンドに便利です。ターミナル使用と併せてファイル操作を行うGUI指向です。[5]

これらの選択肢は無料または無料版があり、コミュニティサポートの程度は様々です。ネイティブのmacOS Terminalアプリは常にベースラインとして利用可能ですが、上級ユーザーにとっては、比較対象としてGhosttyとiTerm2が依然としてトップの選択肢です。AI連携やGPU速度などの特定の機能をお探しの場合は、WarpやAlacrittyが最適かもしれません。カスタマイズについては、各プロジェクトのGitHubでmacOS互換性を確認してください。[3] (2025年ガイド更新)

これらのほとんどをインストールするには、Homebrew (例: `brew install --cask kitty`) を使用するか、公式サイトからダウンロードします。ワークフローのアーキタイプに合ったものを一つ選んで始めてください。ターミナルの切り替えには設定の再構成が伴うためです。最新バージョンについては、機能が急速に進化するため、各アプリのリリースノートを参照してください。

Citations:
[1] https://www.youtube.com/watch?v=WxzYtdIcHnQ
[2] https://erlangforums.com/t/which-terminal-emulator-do-you-use-poll/4368
[3] https://setapp.com/how-to/terminal-alternatives-for-mac?srsltid=AfmBOorowizKiascb9JBZSccPQ7V_EMpI2oWZYKGgoMihcje_nKWgc-q
[4] https://www.zdnet.com/article/6-macos-terminal-apps-that-are-much-better-than-apples-default-and-theyre-free/
[5] https://thenewstack.io/the-best-macos-terminal-emulation-programs-for-developers/
[6] https://www.reddit.com/r/MacOS/comments/1hvujf0/best_terminal_for_macos/