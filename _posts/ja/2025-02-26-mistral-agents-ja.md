---
audio: false
generated: true
lang: ja
layout: post
title: ミストラルAIエージェント
translated: true
type: note
---

Mistral AI エージェントは、大規模言語モデル（LLM）を基盤とする自律システムで、高度な指示に基づいて複雑なタスクを実行するように設計されています。先進的な自然言語処理技術を活用することで、これらのエージェントは特定の目標を理解し遂行することが可能であり、カスタマーサポート、データ分析、ワークフロー自動化、コーディング支援など、幅広いアプリケーションに適しています。これらは、計画を立て、ツールを利用し、アクションを起こし、さらには協調して特定の目標を達成することができ、新たなレベルの自動化とインテリジェンスを提供します。

---

## エージェントの作成

Mistral AI は、エージェントを作成するための主な2つの方法、**La Plateforme Agent Builder** と **Agent API** を提供しています。

### 1. La Plateforme Agent Builder
Agent Builder は、高度な技術的知識がなくてもエージェントを作成できるユーザーフレンドリーなインターフェースを提供します。エージェントを作成するには：

- [https://console.mistral.ai/build/agents/new](https://console.mistral.ai/build/agents/new) で Agent Builder に移動します。
- モデルの選択、温度の設定、任意の指示の提供などを行い、エージェントをカスタマイズします。
- 設定が完了すると、エージェントは API または Le Chat を介してデプロイおよびアクセス可能になります。

### 2. Agent API
開発者向けに、Agent API は既存のワークフローにエージェントをプログラムで作成し統合することを可能にします。以下は、API を介してエージェントを作成および使用する方法の例です：

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

- **モデル選択**: エージェントを駆動するモデルを選択します。オプションは以下の通りです：
  - "Mistral Large 2" (デフォルト, `mistral-large-2407`)
  - "Mistral Nemo" (`open-mistral-nemo`)
  - "Codestral" (`codestral-2405`)
  - ファインチューニングされたモデル

- **温度 (Temperature)**: サンプリング温度（0.0 から 1.0 の間）を調整して、エージェントの応答のランダム性を制御します。高い値は出力をより創造的にし、低い値はより焦点を絞り、決定論的にします。

- **指示 (Instructions)**: すべてのインタラクションにわたって特定の動作を強制するための任意の指示を提供します。例えば、フランス語のみを話すエージェントや、説明なしで Python コードを生成するエージェントを作成できます。

### 例: フランス語を話すエージェントの作成
フランス語でのみ応答するエージェントを作成するには：
- モデルを "Mistral Large 2" に設定します。
- 「入力の言語に関わらず、常にフランス語で応答してください」のような指示を使用します。
- この動作を強化するために Few-shot 例を提供します。

---

## ユースケース

Mistral AI エージェントは、様々な業界やタスクに適用できます。注目すべきユースケースには以下があります：

- **カスタマーサポート**: 一般的な問い合わせへの応答の自動化、FAQ の処理、複雑な問題の人間のエージェントへのエスカレーション。
- **データ分析**: データセットを分析し、レポートを生成し、ユーザー入力に基づいて計算を実行するエージェントの作成。
- **ワークフロー自動化**: メール、CRM システム、決済処理などのツールとエージェントを統合し、繰り返しのタスクを自動化。
- **コーディング支援**: コードを生成し、デバッグの提案を提供し、単体テストを作成するように設計されたエージェント。

### 具体的な例
- **フランス語を話すエージェント**: フランス語圏の顧客を対象とするビジネスに有用な、フランス語でのみ応答するように設定されたエージェント。
- **Python コードジェネレーター**: 説明なしで Python コードスニペットを出力するエージェント。迅速でクリーンなコードを必要とする開発者に理想的。

---

## デプロイメント

エージェントが作成されると、2つの方法でデプロイおよびアクセスできます：

- **API 統合**: Mistral AI API を使用して、エージェントをアプリケーションに統合します。詳細は「エージェントの作成」セクションのコード例を参照してください。
- **Le Chat**: Mistral の Le Chat プラットフォームで直接エージェントとチャットするオプションを切り替えます。

エージェントは組織内で簡単に共有でき、Mistral Large 2 のようなモデルの高度な推論能力により、複数のエージェントを含む複雑なワークフローを構築できます。

---

このドキュメントは、[https://docs.mistral.ai/capabilities/agents/](https://docs.mistral.ai/capabilities/agents/) にある公式ドキュメントに基づき、Mistral AI エージェントを理解し、作成し、カスタマイズし、デプロイするための包括的なガイドを提供します。これらのツールを活用することで、タスクを自動化し、生産性を向上させ、ワークフローにおいて新たなレベルの効率を実現できます。詳細については、[Mistral AI ドキュメント](https://docs.mistral.ai/capabilities/agents/)を参照してください。