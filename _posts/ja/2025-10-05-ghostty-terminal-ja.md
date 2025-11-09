---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ghostty クロスプラットフォーム ターミナルエミュレータ
translated: true
type: note
---

はい、Ghosttyはクロスプラットフォームのターミナルエミュレータとして設計されており、これが実際に主要なセールスポイントの一つです。GPUアクセラレーションとネイティブUI統合により、高いパフォーマンスを発揮しながら複数のオペレーティングシステムで一貫して動作するように構築されています。ただし、2025年10月現在、完全なサポートは現在macOSとLinuxに限定されており、Windows版は計画段階ですがまだリリースされていません。

体験について：Ghosttyは各プラットフォームで慣用的で統合された感じ（macOSではCocoa、LinuxではGTKなど、ネイティブUIコンポーネントを使用）を得るために、まるで専用に構築されたアプリのように、汎用ポートではなく設計されているため、プラットフォーム間で*完全に*同一というわけではありません。とはいえ、コア機能、機能（タブ、分割、検索、高度なターミナルプロトコルなど）、およびパフォーマンスは、サポートされているすべての場所で非常に類似し信頼性が高く、洗練されていないエミュレータで見られるようなプラットフォーム固有の癖を最小限に抑えることを意図しています。

もしWindows版が近いうちに登場すれば（GitHubでの継続的な議論に基づく）、同様にネイティブなアプローチに従い、シームレスな感触を提供するはずです。

[Ghostty 公式機能](https://ghostty.org/docs/features)  
[Ghostty GitHub リポジトリ](https://github.com/ghostty-org/ghostty)  
[Ghostty リリースノート](https://ghostty.org/docs/install/release-notes)