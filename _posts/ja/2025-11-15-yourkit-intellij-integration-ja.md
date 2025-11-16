---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: YourKitプロファイラーとIntelliJのシームレスな統合
translated: true
type: note
---

はい、YourKit Java ProfilerはIntelliJ IDEA（Community EditionとUltimate Editionの両方）と非常に良く統合されており、Java向けのプロファイラとIDEの連携において最もスムーズな体験の一つです。

以下に、ご質問いただいた主な統合機能をご紹介します：

- **IDEAからの直接起動**  
  YourKitプラグイン（JetBrains MarketplaceまたはYourKit自身のプラグインから入手可能）をインストールすると、通常のRun/Debugボタンの隣に「YourKit Snapshot」、「YourKit Profiling (CPU)」、「YourKit Profiling (Memory)」などの新しい実行構成が追加されます。

- **IDEツールバーからの直接的なプロファイリングの開始/停止**  
  ワンクリックでプロファイリングを開始でき、停止するとキャプチャされたスナップショットが自動的に開かれ、IDEAから離れることなく操作できます。

- **プロファイラUIでのクリック → IDEAのソースコードへの即時ジャンプ**  
  YourKitはIDEAが実行されていることを検出し、自動的に逆コンパイル/ソースナビゲーションを設定します。YourKitのUIでメソッド、スタックフレーム、アロケーションホットスポットなどをダブルクリックすると、IDEAエディタで正確な行が開きます（組み込みの逆コンパイラサポートにより、バイトコードのみの場合でも機能します）。

- **アプリケーション終了時の自動スナップショット取得**  
  アプリ終了時に自動的にスナップショットをキャプチャするようにYourKitを設定でき、IDEAが即座にそれを開きます。

**現在の状況（2025年後半時点での最新安定版であるYourKit 2024.9時点）：**
- IntelliJ IDEA 2023.3–2025.2+ を完全サポート
- Java 8–24（Java 21+ での仮想スレッドのプロファイリングを含む）で完全動作
- Kotlin、Scala、Groovyなどもサポートし、正しいソースにジャンプ

**インストール手順（簡易版）：**
1. IDEA → Settings → Plugins → Marketplace → 「YourKit」を検索
2. インストール/再起動
3. YourKitエージェントはプラグインに同梱されているため、基本的な使用には別途YourKitのインストールは不要（ただし、IDEA外でよりリッチなUIを使用したい場合は、完全なスタンドアロンのYourKitアプリをインストール可能）

YourKitを日常的に使用するJava開発者のほとんどは、このプラグインを設定すると、プロファイリングのためにIDEAを離れることはありません。

つまり、まさにあなたがおっしゃったワークフローがそのまま利用可能で、非常に洗練されています。