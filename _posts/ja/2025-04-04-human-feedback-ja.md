---
audio: false
generated: true
lang: ja
layout: post
title: 人間フィードバック強化学習（RLHF）の解説
translated: true
type: note
---

**人間のフィードバックによる強化学習 (RLHF)** は、AIモデル、特に大規模言語モデル(LLM)を、人間の好みや指示により適応させるために微調整する機械学習技術です。事前に定義された報酬関数のみに依存する代わりに、RLHFは学習プロセスを導くために人間からの直接的なフィードバックを取り入れます。

**RLHFが重要な理由**

*   **主観的なタスク:** RLHFは、望ましい結果を明示的なルールや数値的な報酬で定義することが難しいタスク、例えば創造的な文章の生成、自然な会話、役立ち有害でないコンテンツの生成などにおいて優れています。
*   **ニュアンスと整合性:** AIモデルが微妙な人間の好み、倫理的配慮、望ましい対話スタイルを理解し従うことを助けます。
*   **パフォーマンスの向上:** RLHFで訓練されたモデルは、従来の強化学習や教師あり学習のみで訓練されたモデルと比較して、多くの場合、大幅に改善されたパフォーマンスとユーザー満足度を示します。

**RLHFの仕組み (通常3段階で行われます):**

1.  **事前学習と教師ありファインチューニング (SFT):**
    *   ベースの言語モデルは、まず大規模なテキストとコードのデータセットで事前学習され、一般的な言語理解と生成を学びます。
    *   この事前学習済みモデルは、多くの場合、望ましい動作の高品質なデモンストレーション（例：プロンプトに対する理想的な応答を人間が書く）を含む小さなデータセットを用いた教師あり学習で微調整されます。このステップは、モデルが期待される出力の形式とスタイルを理解するのに役立ちます。

2.  **報酬モデルの訓練:**
    *   これはRLHFにおける重要なステップです。人間の好みを予測するために、別個の**報酬モデル**が訓練されます。
    *   人間の注釈者は、同じ入力プロンプトに対してSFTモデル（または後のバージョン）からの異なる出力を提示され、様々な基準（例：有益さ、一貫性、安全性）に基づいてこれらの出力をランク付けまたは評価します。
    *   この選好データ（例：「出力Aは出力Bより優れている」）は、報酬モデルの訓練に使用されます。報酬モデルは、任意のモデル出力に対して、人間がそれをどれだけ好むかを反映するスカラー報酬スコアを割り当てることを学びます。

3.  **強化学習によるファインチューニング:**
    *   元の言語モデル（SFTモデルから初期化されたもの）は、強化学習を用いてさらに微調整されます。
    *   前のステップで訓練された報酬モデルが、環境の報酬関数として機能します。
    *   RLエージェント（言語モデル）はプロンプトに対する応答を生成し、報酬モデルがこれらの応答にスコアを付けます。
    *   RLアルゴリズム（多くの場合 Proximal Policy Optimization - PPO）は、報酬モデルによって予測された報酬を最大化するように、言語モデルのポリシー（テキスト生成方法）を更新します。これにより、言語モデルは人間の好みに合致した出力を生成するよう促されます。
    *   RLファインチューニングがSFTモデルの動作から大きく逸脱する（望ましくない結果を招く可能性がある）ことを防ぐために、RLの目的関数には正則化項（例：KLダイバージェンスペナルティ）がしばしば含まれます。

**RLHFの実施方法 (簡略化されたステップ):**

1.  **人間の選好データの収集:**
    *   目的のAI動作に関連するプロンプトやタスクを設計します。
    *   現在のモデルを使用して、これらのプロンプトに対する複数の応答を生成します。
    *   人間の注釈者を募り、これらの応答を比較して選好を示してもらいます（例：ランク付け、最良の選択、評価）。
    *   このデータを（プロンプト、好ましい応答、好ましくない応答）のペアまたは類似の形式で保存します。

2.  **報酬モデルの訓練:**
    *   報酬モデルに適したモデルアーキテクチャ（多くの場合、言語モデルと同様のTransformerベースのモデル）を選択します。
    *   収集した人間の選好データを用いて報酬モデルを訓練します。目標は、報酬モデルが人間が好んだ応答に高いスコアを割り当てるようにすることです。一般的に使用される損失関数は、好ましい応答と好ましくない応答のスコア間のマージンを最大化するものです。

3.  **強化学習による言語モデルの微調整:**
    *   言語モデルをSFTステップ（実行した場合）からの重みで初期化します。
    *   PPOのような強化学習アルゴリズムを使用します。
    *   各訓練ステップで：
        *   プロンプトをサンプリングします。
        *   言語モデルに応答を生成させます。
        *   訓練された報酬モデルを使用して、生成された応答に対する報酬スコアを取得します。
        *   より高い報酬につながる行動（トークン生成）を促進するために、報酬信号に基づいて言語モデルのパラメータを更新します。
        *   更新されたポリシーをSFTポリシーに近づけるために、正則化項（例：KLダイバージェンス）を含めます。

**コード例 (概念的で簡略化されたPyTorchを使用した例):**

これは核心的な概念を説明するための非常に簡略化された概念的な例です。完全なRLHFの実装は、Hugging Face Transformers、Accelerate、RLライブラリなどを含む、はるかに複雑です。

```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# 人間の選好データを収集したと仮定:
# タプルのリスト: (プロンプト, 好ましい応答, 好ましくない応答)
preference_data = [
    ("猫について短い物語を書いてください。", "ウィスカーズという猫は居心地の良いコテージに住んでいました...", "猫の物語。終わり。"),
    ("この記事を要約してください:", "この記事は...について論じています。", "記事の要約。"),
    # ... さらにデータ
]

# 1. 事前学習済み言語モデルとトークナイザーの読み込み
model_name = "gpt2"  # または他の適切な事前学習済みモデル
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# 2. シンプルな報酬モデルの定義
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer  # Transformerレイヤーを使用
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])  # 最後のトークンから報酬を取得
        return reward

reward_model = RewardModel(policy_model)
reward_model.to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0) # 好ましい方の報酬を高くする

# 報酬モデルの訓練
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens)
        less_preferred_reward = reward_model(**less_preferred_tokens)

        labels = torch.ones(preferred_reward.size(0)).to(device) # preferred > less_preferred にしたい
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"報酬モデル エポック {epoch+1}, 損失: {loss.item()}")

# 3. 強化学習ファインチューニング (概念的 - PPOは複雑)
policy_optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)

num_rl_episodes = 5
for episode in range(num_rl_episodes):
    for prompt in [data[0] for data in preference_data]: # プロンプトをサンプリング
        input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
        output_sequences = policy_model.generate(
            input_tokens.input_ids,
            max_length=60,
            num_return_sequences=1,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        generated_response = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

        response_tokens = tokenizer(prompt + generated_response, return_tensors="pt", truncation=True, max_length=128).to(device)
        reward = reward_model(**response_tokens)

        # (簡略化) ポリシー更新 - 現実ではPPOはより洗練された方法を使用
        loss = -reward.mean() # 報酬を最大化しようとする
        policy_optimizer.zero_grad()
        loss.backward()
        policy_optimizer.step()

    print(f"RL エピソード {episode+1}, 報酬: {reward.item()}, 応答: {generated_response}")

print("RLHF訓練完了!")
```

**RLHFの主な課題:**

*   **データ収集:** 高品質で多様な人間の選好データを取得することは、費用と時間がかかる可能性があります。
*   **主観性とバイアス:** 人間の選好は主観的であり、報酬モデルによって学習される可能性のあるバイアスを含むことがあります。
*   **報酬ハッキング:** RLエージェントが、真の人間の選好に沿わない方法で報酬モデルを悪用する方法を見つける可能性があります。
*   **スケーラビリティ:** 非常に大規模なモデルとデータセットへのRLHFのスケーリングには、多大な計算資源と注意深いエンジニアリングが必要です。
*   **不安定性:** RLHFモデルの訓練は不安定になる可能性があり、注意深いハイパーパラメータの調整が必要です。

これらの課題にもかかわらず、RLHFはAIモデルを人間の価値観に合わせるための強力な技術であることが証明されており、ChatGPTや他の最先端の言語モデルの開発における重要な構成要素となっています。