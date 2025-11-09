---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: SuperCLUE：中国語大規模言語モデルベンチマーク
translated: true
type: note
---

SuperCLUEは、中国語大規模言語モデル（LLM）を評価するために設計された包括的なベンチマークスイートです。これは、元のCLUE（Chinese Language Understanding Evaluation）ベンチマークを基盤として、より小型のモデルだけでなくLLMの高度な能力を評価するために拡張したものです。清華大学などの研究機関や中国AIエコシステム内の企業の研究者らによる共同プロジェクトであるCLUEbenchmarkチームによって開発され、SuperCLUEは2023年に初めて導入され、中国語LLMを国際基準に対して評価する際のギャップに対処することを目的としています。

### 主な特徴
- **重点分野**: 以下の4つの主要分野にわたってモデルを評価します：
  - 言語理解と生成（例：読解、要約）
  - 専門的スキルと知識（例：数学的推論、コーディング）
  - エージェント知能（例：ツールの使用、計画立案）
  - 安全性（例：バイアス検出、倫理的調整）
- **構造**: 12の核心タスクに分割され、SuperCLUE-Math6のようなデータセットは多段階の数学問題に使用されます。
- **目的**: 中国AIの進歩を追跡し、GPTシリーズのようなグローバルモデルと比較した強み（例：文化的ニュアンスの扱い）とギャップを明らかにするのに役立ちます。
- **更新**: 2025年半現在、定期的なチェックインに使用され、QwenやGLMのような中国モデルが国際モデルとの差を縮めていることを示すリーダーボードが公開されています。

このベンチマークはオープンソースで積極的にメンテナンスされており、評価結果はarXivの論文やGitHubを通じて共有されることが多いです。

[SuperCLUE: A Comprehensive Chinese Large Language Model Benchmark](https://arxiv.org/abs/2307.15020)  
[SuperCLUE GitHub Repository](https://github.com/CLUEbenchmark/SuperCLUE)  
[ChinAI: SuperCLUE Benchmarks —2025 Midyear Check-in](https://chinai.substack.com/p/chinai-324-superclue-large-model)