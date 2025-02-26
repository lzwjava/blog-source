---
audio: false
lang: ja
layout: post
title: Mistral AI エージェント
translated: true
---

Mistral AI エージェントは、高度な自然言語処理を活用して、高レベルの指示に基づいて複雑なタスクを実行するために設計された、自律的なシステムです。これらのエージェントは、特定の目標を理解し実行することができ、カスタマーサポート、データ分析、ワークフローの自動化、コーディングのサポートなど、幅広い用途に適しています。計画を立て、ツールを利用し、行動を起こし、特定の目標を達成するために協力することができ、新しいレベルの自動化と知能を提供します。

---

## エージェントの作成

Mistral AI は、エージェントを作成するための2つの主要な方法を提供しています：**La Plateforme Agent Builder** と **Agent API**です。

### 1. La Plateforme Agent Builder
Agent Builder は、技術的な知識がなくてもエージェントを作成するための使いやすいインターフェースを提供します。エージェントを作成するには：

- [https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new) の Agent Builder にアクセスします。
- モデルを選択し、温度を設定し、オプションの指示を提供してエージェントをカスタマイズします。
- 設定が完了したら、エージェントは API または Le Chat を通じてデプロイおよびアクセスできます。

### 2. Agent API
開発者向けに、Agent API は、エージェントをプログラム的に作成し、既存のワークフローに統合することを可能にします。以下に、API を通じてエージェントを作成し使用する方法の例を示します。

#### Python の例
```python
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id="your-agent-id",
    messages=[{"role": "user", "content": "What is the best French cheese?"}],
)
print(chat_response.choices[0].message.content)
```

#### JavaScript の例
```javascript
import { Mistral } from '@mistralai/mistralai';

const apiKey = process.env.MISTRAL_API_KEY;
const client = new Mistral({ apiKey: apiKey });

const chatResponse = await client.agents.complete({
    agentId: "your-agent-id",
    messages: [{ role: 'user', content: 'What is the best French cheese?' }],
});
console.log('Chat:', chatResponse.choices[0].message.content);
```

---

## エージェントのカスタマイズ

Mistral AI エージェントは、いくつかのオプションを通じて特定のニーズに合わせてカスタマイズできます：

- **モデルの選択**：エージェントを駆動するモデルを選択します。オプションには以下が含まれます：
  - "Mistral Large 2"（デフォルト、`mistral-large-2407`）
  - "Mistral Nemo"（`open-mistral-nemo`）
  - "Codestral"（`codestral-2405`）
  - ファインチューニングされたモデル

- **温度**：サンプリング温度（0.0 から 1.0 まで）を調整して、エージェントの応答のランダム性を制御します。高い値は出力をより創造的にし、低い値はより集中して決定論的にします。

- **指示**：すべてのインタラクションで特定の行動を強制するためのオプションの指示を提供します。例えば、フランス語のみを話すエージェントや、説明なしで Python コードを生成するエージェントを作成できます。

### 例：フランス語を話すエージェントの作成
フランス語のみで応答するエージェントを作成するには：
- モデルを "Mistral Large 2" に設定します。
- 指示として「入力の言語に関係なく、常にフランス語で応答する」と指定します。
- 行動を強化するために、少数の例を提供します。

---

## 用途

Mistral AI エージェントは、さまざまな業界やタスクに適用できます。注目すべき用途には以下が含まれます：

- **カスタマーサポート**：一般的な問い合わせに対する応答を自動化し、FAQ を処理し、複雑な問題を人間のエージェントにエスカレートします。
- **データ分析**：ユーザーの入力に基づいてデータセットを分析し、レポートを生成したり、計算を実行したりするエージェントを作成します。
- **ワークフローの自動化**：メール、CRM システム、または支払い処理などのツールと統合して、繰り返しのタスクを自動化します。
- **コーディングのサポート**：コードを生成し、デバッグの提案を提供したり、ユニットテストを作成したりするエージェントを設計します。

### 特定の例
- **フランス語を話すエージェント**：フランス語を話す顧客を対象とするビジネスに適した、フランス語のみで応答するエージェント。
- **Python コード生成エージェント**：説明なしで Python コードのスニペットを出力するエージェントで、迅速でクリーンなコードが必要な開発者に最適です。

---

## デプロイ

エージェントが作成されると、2つの方法でデプロイおよびアクセスできます：

- **API 統合**：Mistral AI API を使用して、エージェントをアプリケーションに統合します。詳細については、「エージェントの作成」セクションのコード例を参照してください。
- **Le Chat**：Mistral の Le Chat プラットフォームでエージェントと直接チャットするオプションを切り替えます。

エージェントは組織内で簡単に共有でき、Mistral Large 2 のようなモデルの高度な推論能力を活用して、複数のエージェントを使用した複雑なワークフローを構築できます。

---

このドキュメントは、公式ドキュメント [https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/) に基づいて、Mistral AI エージェントの理解、作成、カスタマイズ、デプロイの包括的なガイドを提供します。これらのツールを活用することで、タスクを自動化し、生産性を向上させ、ワークフローの効率を新たなレベルに引き上げることができます。詳細については、[Mistral AI ドキュメント](https://docs.mistral.ai/capabilities/agents/)をご覧ください。