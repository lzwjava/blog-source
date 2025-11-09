---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ja
layout: post
title: コストとパフォーマンスのための最適モデル選択
translated: true
type: note
---

あなたのClaude Code設定を見ると、コストとパフォーマンスの両方を最適化したいと考えているようです。以下に、ルーター設定で「安くて高性能」なモデルを選ぶための推奨事項をご紹介します：

## あなたのリストから選ぶコストパフォーマンスの高いモデル：

**ほとんどのタスク（デフォルト）向け：**
- `deepseek/deepseek-chat-v3.1` - 非常に低コストで優れたパフォーマンス
- `deepseek/deepseek-r1` - 優れた推論能力、依然としてコスト効率が良い

**バックグラウンドタスク向け：**
- `deepseek/deepseek-chat-v3.1` - すでに良い選択肢
- `google/gemini-2.5-flash` - 高速で低コスト

**思考・推論向け：**
- `deepseek/deepseek-r1` - 推論タスク向けに特別に設計
- `z-ai/glm-4.5` - 現在の選択肢も悪くない

**更新されたルーターの提案：**
```json
"Router": {
  "default": "openrouter,deepseek/deepseek-chat-v3.1",
  "background": "openrouter,google/gemini-2.5-flash", 
  "think": "openrouter,deepseek/deepseek-r1",
  "longContext": "openrouter,moonshotai/kimi-k2",
  "webSearch": "openrouter,google/gemini-2.5-flash"
}
```

## 主な考慮事項：
- **DeepSeekモデル**は現在、最高の価格対性能比を提供
- **Gemini 2.5 Flash**はよりシンプルなタスクに対して非常に高速で安価
- **Kimi**は長いコンテキスト処理のために保持（200k+トークンを良好に処理）
- Flash以上の能力が必要な場合は**Gemini 2.5 Pro**

正確なコスト比較のためにOpenRouterのウェブサイトで現在の価格を確認できますが、DeepSeekモデルは通常、GPT-4レベルのモデルよりも10〜20倍安く、競争力のあるパフォーマンスを提供します。