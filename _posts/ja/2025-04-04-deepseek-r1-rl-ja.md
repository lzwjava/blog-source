---
audio: false
generated: true
lang: ja
layout: post
title: ディープシーク R1
translated: true
type: note
---

DeepSeek R1は、大規模言語モデル(LLM)における**推論能力**を大幅に重視した新しい強化学習(RL)アプローチを採用しています。彼らの技術は、従来の人間フィードバックによる強化学習(RLHF)とはいくつかの重要な点で異なります。

以下に、DeepSeekがR1の強化学習で使用した技術の詳細を示します：

**1. 初期推論のための純粋強化学習(DeepSeek-R1-Zero):**

* **命令に対する初期教師ありファインチューニングなし:** 人間が書いた命令に対して最初に教師ありファインチューニング(SFT)を行う多くのLLMとは異なり、DeepSeek-R1-Zeroはベースモデル(DeepSeek-V3-Base)に対して**純粋なRL**で直接トレーニングされました。
* **Group Relative Policy Optimization (GRPO):** 彼らはコアRLアルゴリズムとしてGRPOを利用しました。GRPOは、別個の批評家ネットワークを必要としないことで、Proximal Policy Optimization (PPO)よりも効率的になるように設計されています。これは、生成された出力のグループを比較し、その品質に基づいて相対スコアを割り当てることでベースラインレワードを推定します。これにより、モデルは自身の以前の試みと比較してより良い応答を生成するよう促されます。
* **ルールベースの報酬システム:** 初期RLフェーズで人間の選好のみに依存する代わりに、DeepSeek-R1-Zeroは**ルールベースの報酬システム**を使用しました。このシステムは主に以下に焦点を当てました：
    * **正確性報酬:** 特に数学の問題（最終的な答えが正しいかどうかを確認）のように検証可能な解決策を持つタスクで、モデルが正しい答えを提供した場合に報酬を与えます。
    * **フォーマット報酬:** モデルが特定の出力フォーマット、特に``タグを使用して推論プロセスを囲むことに従った場合に報酬を与えます。これにより、連鎖思考推論の出現が促進されました。
* **創発的な推論行動:** この純粋RLアプローチにより、DeepSeek-R1-Zeroは、これらの行動に対する明示的な人間のデモンストレーションなしに、自己検証、反省、長い連鎖思考説明の生成を含む印象的な推論スキルを自然に発展させることができました。

**2. 読みやすさと一般能力の向上のための多段階トレーニング(DeepSeek-R1):**

DeepSeek-R1-Zeroの制限（読みやすさの悪さや言語の混合など）に対処するために、DeepSeek-R1はより包括的な多段階トレーニングパイプラインを採用しました：

* **コールドスタートデータファインチューニング:** 主要なRLフェーズの前に、ベースモデルは高品質な人間が書いた（または生成され改良された）長い連鎖思考推論例の小さなデータセットでファインチューニングされました。この「コールドスタート」データは、モデルがより読みやすく一貫した推論ステップを生成する方向に導くのに役立ちました。
* **推論指向強化学習（第2RLステージ）:** モデルはその後、大規模なRLの第2段階（DeepSeek-R1-Zeroと同様）を受けましたが、追加の**言語一貫性報酬**が含まれていました。この報酬は、モデルが推論プロセス内で言語を混合した場合にペナルティを与えます。
* **教師ありファインチューニング(SFT):** 推論指向RLの後、モデルは推論データ（RLモデルからの棄却サンプリングを使用して合成され、DeepSeek-V3によって判断された）と一般的な非推論データ（連鎖思考で拡張された）の両方を含む多様なデータセットでさらにファインチューニングされました。このSFT段階は、モデルの有益性と無害性を改善しながら、その強力な推論能力を保持することを目的としていました。
* **全シナリオに対するRL（第3RLステージ）:** 最終的なRLフェーズは、モデルの全体的な能力と望ましい行動との整合性をさらに洗練するために、より広範なシナリオからのプロンプトを使用して実施されました。

**従来のRLHFとの主な違い:**

* **大規模な人間の選好データへの依存軽減:** 合成データの品質判断にある程度の人間の評価が関与していた可能性がありますが、DeepSeek-R1のコアRLトレーニングは、特に初期段階で、ルールベースの報酬を重点的に活用しました。これにより、直接的な人間の選好比較の大量収集のコストと複雑さが軽減されます。
* **創発的推論への重点:** 純粋RLアプローチは、人間が提供した推論の例からだけ学ぶのではなく、モデルが効果的な推論戦略を自分で*発見*するよう動機付けることを目的としています。
* **多段階アプローチ:** DeepSeekのパイプラインは、強力な推論と言語能力の両方を達成するために、事前トレーニング、対象を絞ったファインチューニング、異なる報酬信号を持つ複数のRL段階を慎重に調整したシーケンスを含みます。

**強化学習を示すコード（概念的および簡略化）:**

DeepSeekのRLトレーニングプロセスを完全に複製する直接的な実行可能なコード例を提供することは、その複雑さと規模のために困難です。しかし、以下の概念的なPyTorch風のスニペットは、GRPOとルールベース報酬の核心的な考え方を示しています：

```python
import torch
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# 事前トレーニング済み言語モデルとトークナイザーがあると仮定
model_name = "gpt2"  # より適切なベースモデルに置き換え
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

def generate_responses(prompt, num_responses=4, max_length=128):
    input_tokens = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = policy_model.generate(
        input_tokens.input_ids,
        max_length=max_length,
        num_return_sequences=num_responses,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return responses

def calculate_accuracy_reward(response):
    # 数学の問題に対する簡略化された例: "What is 2 + 2?"
    if "2 + 2" in response and "4" in response:
        return 1.0
    else:
        return 0.0

def calculate_format_reward(response):
    if "" in response:
        return 0.5
    else:
        return 0.0

def calculate_combined_reward(response):
    accuracy_reward = calculate_accuracy_reward(response)
    format_reward = calculate_format_reward(response)
    return accuracy_reward + format_reward

def train_step(prompt, num_samples=4):
    optimizer.zero_grad()
    responses = generate_responses(prompt, num_samples=num_samples)
    rewards = torch.tensor([calculate_combined_reward(resp) for resp in responses]).float().to(device)

    # 簡略化されたGRPO風の更新: より高い報酬の応答を促進
    best_reward_index = torch.argmax(rewards)
    best_response = responses[best_reward_index]
    inputs = tokenizer(prompt + best_response, return_tensors="pt").to(device)
    outputs = policy_model(**inputs, labels=inputs.input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item(), best_response, rewards.tolist()

# トレーニングループ（非常に簡略化）
num_episodes = 10
training_prompts = ["Solve: 2 + 2 = ?", "Explain the concept of gravity