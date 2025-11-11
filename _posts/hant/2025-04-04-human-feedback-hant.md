---
audio: false
generated: true
lang: hant
layout: post
title: 人類反饋強化學習（RLHF）詳解
translated: true
type: note
---

**基於人類回饋的強化學習 (RLHF)** 是一種機器學習技術，用於微調 AI 模型，特別是大型語言模型 (LLM)，以使其更符合人類的偏好和指令。RLHF 並非僅依賴預先定義的獎勵函數，而是結合了來自人類的直接回饋來指導學習過程。

**為何 RLHF 如此重要？**

* **主觀性任務：** 對於那些難以用明確規則或數值獎勵來定義期望結果的任務，例如生成創意文本、進行自然對話，或產出有用且無害的內容，RLHF 表現卓越。
* **細微差異與對齊：** 它有助於 AI 模型理解並遵循細微的人類偏好、道德考量以及期望的互動風格。
* **提升效能：** 與僅使用傳統強化學習或監督式學習訓練的模型相比，採用 RLHF 訓練的模型通常展現出顯著提升的效能和使用者滿意度。

**RLHF 如何運作（通常分為三個階段）：**

1.  **預訓練與監督式微調 (SFT)：**
    * 首先，一個基礎語言模型會在大量的文本和程式碼資料集上進行預訓練，以學習通用的語言理解和生成能力。
    * 接著，這個預訓練模型通常會使用監督式學習，在一個較小的高品質示範資料集上進行微調，這些資料展示了期望的行為（例如，人類針對提示寫出理想回應）。此步驟有助於模型理解期望輸出的格式和風格。

2.  **獎勵模型訓練：**
    * 這是 RLHF 的關鍵步驟。一個獨立的**獎勵模型**會被訓練來預測人類的偏好。
    * 人類標註員會收到來自 SFT 模型（或後續版本）針對相同輸入提示所產生的不同輸出。他們根據各種標準（例如：幫助性、連貫性、安全性）對這些輸出進行排序或評分。
    * 這些偏好資料（例如：「輸出 A 優於輸出 B」）被用來訓練獎勵模型。獎勵模型學會為任何給定的模型輸出分配一個標量獎勵分數，以反映人類對該輸出的偏好程度。

3.  **強化學習微調：**
    * 原始的語言模型（從 SFT 模型初始化）會使用強化學習進行進一步的微調。
    * 上一步訓練好的獎勵模型充當環境的獎勵函數。
    * RL 代理（即語言模型）針對提示生成回應，而獎勵模型則為這些回應評分。
    * RL 演算法（通常是近端策略優化 - PPO）會更新語言模型的策略（其生成文本的方式），以最大化獎勵模型預測的獎勵。這鼓勵語言模型生成更符合人類偏好的輸出。
    * 為了防止 RL 微調過度偏離 SFT 模型的行為（這可能導致不良後果），RL 目標函數中通常會包含一個正則化項（例如：KL 散度懲罰項）。

**如何進行 RLHF（簡化步驟）：**

1.  **收集人類偏好資料：**
    * 設計與您期望的 AI 行為相關的提示或任務。
    * 使用您當前的模型為這些提示生成多個回應。
    * 招募人類標註員來比較這些回應並指出他們的偏好（例如：排序、選擇最佳或評分）。
    * 將這些資料儲存為（提示、偏好回應、次偏好回應）的配對或類似格式。

2.  **訓練獎勵模型：**
    * 為您的獎勵模型選擇合適的模型架構（通常是與語言模型相似的基於 Transformer 的模型）。
    * 使用收集到的人類偏好資料來訓練獎勵模型。目標是讓獎勵模型為人類偏好的回應分配更高的分數。常用的損失函數是基於最大化偏好回應與次偏好回應之間的分數差距。

3.  **使用強化學習微調語言模型：**
    * 使用 SFT 步驟的權重來初始化您的語言模型（如果您執行了該步驟）。
    * 使用強化學習演算法（如 PPO）。
    * 對於每個訓練步驟：
        * 取樣一個提示。
        * 讓語言模型生成一個回應。
        * 使用訓練好的獎勵模型來獲取生成回應的獎勵分數。
        * 根據獎勵信號更新語言模型的參數，以鼓勵能帶來更高獎勵的動作（詞元生成）。
        * 包含一個正則化項（例如：KL 散度），以使更新後的策略接近 SFT 策略。

**程式碼範例（概念性與簡化，使用 PyTorch）：**

這是一個高度簡化的概念性範例，用於說明核心概念。完整的 RLHF 實現要複雜得多，並且涉及像 Hugging Face Transformers、Accelerate 和 RL 函式庫。

```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# 假設您已收集人類偏好資料：
# 元組列表：(提示, 偏好回應, 次偏好回應)
preference_data = [
    ("Write a short story about a cat.", "Whiskers the cat lived in a cozy cottage...", "A cat story. The end."),
    ("Summarize this article:", "The article discusses...", "Article summary."),
    # ... 更多資料
]

# 1. 載入預訓練語言模型和分詞器
model_name = "gpt2"  # 或其他合適的預訓練模型
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# 2. 定義一個簡單的獎勵模型
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer  # 使用 Transformer 層
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])  # 從最後一個詞元獲取獎勵
        return reward

reward_model = RewardModel(policy_model)
reward_model.to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0) # 鼓勵偏好回應獲得更高獎勵

# 訓練獎勵模型
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens)
        less_preferred_reward = reward_model(**less_preferred_tokens)

        labels = torch.ones(preferred_reward.size(0)).to(device) # 我們希望 preferred > less_preferred
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")

# 3. 強化學習微調（概念性 - PPO 很複雜）
policy_optimizer = optim.AdamW(policy_model.parameters(), lr=5e-6)

num_rl_episodes = 5
for episode in range(num_rl_episodes):
    for prompt in [data[0] for data in preference_data]: # 取樣提示
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

        # （簡化）策略更新 - 實際上，PPO 使用更複雜的方法
        loss = -reward.mean() # 嘗試最大化獎勵
        policy_optimizer.zero_grad()
        loss.backward()
        policy_optimizer.step()

    print(f"RL Episode {episode+1}, Reward: {reward.item()}, Response: {generated_response}")

print("RLHF Training Done!")
```

**RLHF 的主要挑戰：**

* **資料收集：** 獲取高品質且多樣化的人類偏好資料可能成本高昂且耗時。
* **主觀性與偏見：** 人類偏好可能具有主觀性，並可能包含偏見，這些偏見可能被獎勵模型學習。
* **獎勵破解：** RL 代理可能會找到利用獎勵模型的方法，但這些方法並不符合真實的人類偏好。
* **可擴展性：** 將 RLHF 擴展到非常大的模型和資料集需要大量的計算資源和仔細的工程設計。
* **不穩定性：** 訓練 RLHF 模型可能不穩定，需要仔細調整超參數。

儘管存在這些挑戰，RLHF 已被證明是一種強大的技術，能有效將 AI 模型與人類價值觀對齊，並且是先進語言模型（如 ChatGPT 等）開發中的關鍵組件。