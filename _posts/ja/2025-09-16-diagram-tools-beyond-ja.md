---
audio: false
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: GraphvizとNetworkXを超えるダイアグラムツール
translated: true
type: note
---

GraphvizとNetworkXを超える優れた選択肢を、作業スタイル別にグループ分けしました。

## テキスト/DSL「ダイアグラム・アズ・コード」
- **PlantUML**: 完全なUML（シーケンス、クラス、コンポーネント、配置）、C4モデル、アクティビティ図に対応。巨大なエコシステム。
- **Mermaid**: 軽量なMarkdown風シンタックス。フローチャート、シーケンス図、クラス図、ER図、状態遷移図に最適。GitHub/GitLabでネイティブレンダリング。
- **D2 (by Terrastruct)**: クリーンで汎用性の高い図用DSL。優れた自動レイアウト機能。レイヤーと大規模図表をサポート。
- **Structurizr (C4)**: モデルファースト（C4）アプローチのDSL。PlantUML/Mermaidへのエクスポート可能。アーキテクチャ文書に最適。
- **C4-PlantUML**: PlantUML上に構築されたC4モデルテンプレート。
- **nomnoml**: 最小限のシンタックス。素早いクラス/リレーションシップスケッチに。
- **Kroki**: 多数のDSL（PlantUML、Mermaid、Graphviz）をレンダリングするサーバー。ドキュメントパイプライン向け。

## コードファースト（コード/IaCから図を生成）
- **diagrams (mingrammer, Python)**: プログラムによるクラウドアーキテクチャ図（AWS/Azure/GCP/K8s）。
- **Terraformヘルパー**: Inframap（状態から描画）、Blast Radius（Terraformからのインタラクティブグラフ）。
- **AWS CDK**: CDKアプリからアーキテクチャ図を生成するcdk-dia。
- **Go/TSライブラリ**: コードベースの生成向けにGoDiagrams (Go)、ts-graphviz (TypeScript)。

## Web可視化ライブラリ（インタラクティブグラフ）
- **Cytoscape.js**: 大規模グラフ可視化、レイアウトアルゴリズム、優れたパフォーマンス。
- **D3.js**: 強力だが低レベル。カスタムグラフ/図ビジュアル向け。
- **vis-network (vis.js)**: 物理演算を備えた簡単なネットワークグラフ。
- **Sigma.js**: 大規模グラフの高速レンダリング。
- **ECharts**: グラフモジュールを備えた汎用チャート。素早い結果生成。
- **pyvis (Python)**: Vis.js経由のシンプルなインタラクティブネットワークグラフ。

## GUIダイアグラミングツール（ドラッグ＆ドロップ）
- **diagrams.net (draw.io)**: 無料、簡単、大規模ステンシル（UML、クラウドアイコン）。
- **yEd/yFiles**: 優れた自動レイアウト。yFilesは商用SDK、yEdは無料デスクトップ版。
- **Lucidchart/Miro**: コラボレーティブWebツール。チーム作業に最適。
- **OmniGraffle (macOS), Visual Paradigm, StarUML, Enterprise Architect**: UML/アーキテクチャツール群。

## アーキテクチャ特化およびドメイン別ツール
- **C4モデル**: Structurizr、C4-PlantUML、Mermaid C4拡張。
- **クラウドアーキテクチャSaaS**: Cloudcraft (AWS)、Hava、Lucidscale、CloudSkew。クラウド/IaCからのインポート対応。
- **BPMN/プロセス**: Camunda Modeler、bpmn.io。
- **シーケンス/タイミング**: WebSequenceDiagrams、WaveDrom（タイミング図）。
- **ER/DBダイアグラム**: dbdiagram.io、SchemaSpy。

## シナリオ別おすすめ選択肢
- Markdown/READMEでのドキュメント・アズ・コード: **Mermaid**
- テンプレートを使った完全なUML + C4: **PlantUML** または **Structurizr**
- コード/IaCからのクラウドアーキテクチャ: **diagrams (Python)**、**Inframap/Blast Radius (Terraform)**、**cdk-dia (AWS CDK)**
- インタラクティブWebアプリグラフ: **Cytoscape.js** または **vis-network**。カスタム可視化には **D3.js**
- 高速GUI描画: **diagrams.net (draw.io)**。自動レイアウトには **yEd**

ご自身の好み（テキスト vs GUI、静的画像 vs インタラクティブ、使用言語、シーケンス図/C4/クラウド/ER図などの図の種類）を共有していただければ、短いリストとスターターテンプレートをご提案できます。