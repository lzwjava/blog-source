---
audio: false
generated: true
lang: hant
layout: post
title: DeepSeek R1
translated: true
type: note
---

DeepSeek R1 採用了一種新穎的強化學習方法，特別注重大型語言模型的**推理能力**。他們的技術在幾個關鍵方面與傳統的從人類反饋中進行強化學習有所不同。

以下是 DeepSeek 在 R1 強化學習中使用的技術細分：

**1. 純強化學習用於初始推理（DeepSeek-R1-Zero）：**

* **無需對指令進行初始監督微調：** 與許多先對人類編寫指令進行監督微調的大型語言模型不同，DeepSeek-R1-Zero 直接在基礎模型上使用**純強化學習**進行訓練。
* **群組相對策略優化：** 他們使用 GRPO 作為核心強化學習算法。GRPO 旨在通過消除對單獨評論者網絡的需求，比近端策略優化更有效率。它通過比較一組生成的輸出來估計基準獎勵，並根據其質量分配相對分數。這鼓勵模型生成比其先前嘗試更好的回應。
* **基於規則的獎勵系統：** DeepSeek-R1-Zero 在初始強化學習階段並非僅依賴人類偏好，而是使用了**基於規則的獎勵系統**。該系統主要專注於：
    * **準確性獎勵：** 獎勵模型提供正確答案，特別是在具有可驗證解決方案的任務中，如數學問題（檢查最終答案是否正確）。
    * **格式獎勵：** 獎勵模型遵循特定的輸出格式，特別是使用 `` 標籤來包圍其推理過程。這鼓勵了思維鏈推理的出現。
* **湧現的推理行為：** 這種純強化學習方法讓 DeepSeek-R1-Zero 能夠自然地發展出令人印象深刻的推理技能，包括自我驗證、反思和生成長思維鏈解釋，而無需對這些行為進行明確的人類示範。

**2. 用於增強可讀性和通用能力的多階段訓練（DeepSeek-R1）：**

為了解決 DeepSeek-R1-Zero 的局限性（如可讀性差和語言混合），DeepSeek-R1 採用了更全面的多階段訓練流程：

* **冷啟動數據微調：** 在主要強化學習階段之前，基礎模型在一個小型的高質量、人類編寫（或生成並精煉）的長思維鏈推理示例數據集上進行微調。這種「冷啟動」數據有助於引導模型產生更易讀和連貫的推理步驟。
* **面向推理的強化學習（第二強化學習階段）：** 模型隨後進行大規模強化學習的第二階段（類似於 DeepSeek-R1-Zero），但增加了**語言一致性獎勵**。該獎勵會懲罰在推理過程中混合使用語言的模型。
* **監督微調：** 在面向推理的強化學習之後，模型在一個多樣化的數據集上進一步微調，該數據集包括推理數據（使用從強化學習模型中通過拒絕抽樣合成的數據，並由 DeepSeek-V3 評判）和通用的非推理數據（通過思維鏈增強）。這個監督微調階段旨在提高模型的有用性和無害性，同時保留其強大的推理能力。
* **適用於所有場景的強化學習（第三強化學習階段）：** 最後一個強化學習階段使用來自更廣泛場景的提示進行，以進一步完善模型的整體能力和與期望行為的對齊。

**與傳統 RLHF 的主要區別：**

* **減少對大量人類偏好數據的依賴：** 雖然在評估合成數據質量時可能涉及一些人為評估，但 DeepSeek-R1 的核心強化學習訓練大量利用了基於規則的獎勵，特別是在初始階段。這降低了收集大量直接人類偏好比較的成本和複雜性。
* **強調湧現推理：** 純強化學習方法旨在激勵模型自行*發現*有效的推理策略，而不僅僅是從人類提供的推理示例中學習。
* **多階段方法：** DeepSeek 的流程涉及精心策劃的預訓練、針對性微調和具有不同獎勵信號的多個強化學習階段的序列，以實現強大的推理和通用語言能力。

**展示強化學習的程式碼（概念性與簡化）：**

由於其複雜性和規模，提供一個直接可運行的程式碼示例來完全複製 DeepSeek 的強化學習訓練過程具有挑戰性。然而，以下概念性的 PyTorch 風格程式碼片段說明了 GRPO 和基於規則獎勵的核心思想：

```python
import torch
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# 假設您有一個預訓練的語言模型和分詞器
model_name = "gpt2"  # 替換為更合適的基礎模型
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
    # 數學問題的簡化示例："What is 2 + 2?"
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

    # 簡化的類 GRPO 更新：鼓勵更高獎勵的回應
    best_reward_index = torch.argmax(rewards)
    best_response = responses[best_reward_index]
    inputs = tokenizer(prompt + best_response, return_tensors="pt").to(device)
    outputs = policy_model(**inputs, labels=inputs.input_ids)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    return loss.item(), best_response, rewards.tolist()

# 訓練循環（非常簡化）
num_episodes = 10
training_prompts = ["Solve: 2 + 2 = ?", "Explain the concept of gravity