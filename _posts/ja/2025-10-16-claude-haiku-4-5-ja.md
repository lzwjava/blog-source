---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: クロード俳句4.5 高速効率的AI
translated: true
type: note
---

Claude Haiku 4.5は、Anthropicが2025年10月16日にリリースした最新の小型AIモデルです。スピードと効率性を重視して設計されており、チャットボット、カスタマーサービスエージェント、コーディングアシスタントなどのリアルタイムアプリケーションに最適です。このモデルは、コーディング、コンピューター使用、エージェントワークフローなどのタスクにおいて、Claude Sonnet 4のような旧モデルを匹敵または凌駕する先進的な性能を発揮しつつ、大幅に高速（2倍以上の速度）かつ低コスト（約3分の1のコスト）を実現しています。

### 主な特徴と機能
- **高速性と低遅延**: ペアプログラミングやマルチエージェントシステムなどの対話型シナリオでの素早い応答に最適化
- **コーディングとツール使用の強さ**: SWE-bench（73.3%スコア）やTerminal-Bench（約41%）などのベンチマークで優れた成績を収め、ファイル編集やターミナルコマンドなどの複雑なタスクを処理可能
- **マルチモデルワークフロー**: Claude Sonnet 4.5のような大規模モデルと連携し、大規模モデルがタスクを計画、Haiku 4.5がサブタスクを並列実行する構成に適す
- **安全性への注力**: Anthropicのモデルの中で最も安全で、有害な出力の発生率が低く、AI安全レベル2（先進モデルのレベル3より制限が緩和）に分類。Sonnet 4.5よりも整合性のない動作が少ない

前身のClaude 3.5 Haikuと比較して、より整合性が高く能力も向上しており、直接的な置き換えとして使用可能。Anthropicの最新の先進モデル（2週間前にリリースされたClaude Sonnet 4.5）ではありませんが、Haiku 4.5は同社の最新の小型モデルであり、日常使用におけるコスト効率の高いアップグレードとなっています。

### 価格と利用可能性
- **価格**: 入力トークン100万あたり1ドル、出力トークン100万あたり5ドル
- **アクセス**: Claude API（`claude-haiku-4-5`として）、Anthropicアプリ、Amazon Bedrock、Google Vertex AI、GitHub Copilot連携など、すべてのユーザーが即時利用可能

[Claude Haiku 4.5の紹介](https://www.anthropic.com/news/claude-haiku-4-5)  
[Anthropic、Claude Haiku 4.5をローンチ](https://www.cnbc.com/2025/10/15/anthropic-claude-haiku-4-5-ai.html)  
[AWSでのClaude Haiku 4.5](https://aws.amazon.com/about-aws/whats-new/2025/10/claude-4-5-haiku-anthropic-amazon-bedrock)