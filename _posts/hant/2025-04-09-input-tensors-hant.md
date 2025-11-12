---
audio: false
generated: true
lang: hant
layout: post
title: 張量維度不匹配
translated: true
type: note
---

看來你在使用 PyTorch 和 Transformers 庫進行人類反饋強化學習（RLHF）設置時，訓練獎勵模型遇到了錯誤。錯誤訊息顯示 `MarginRankingLoss` 函數中存在維度不匹配問題，該函數要求所有輸入張量（`input1`、`input2` 和 `target`）具有相同尺寸。讓我們來分析並解決這個問題。

### 錯誤分析
追蹤資訊顯示：
```
RuntimeError: margin_ranking_loss : All input tensors should have same dimension but got sizes: input1: torch.Size([1, 1]), input2: torch.Size([1, 1]), target: torch.Size([1])
```
- `preferred_reward` (input1) 和 `less_preferred_reward` (input2) 的尺寸為 `[1, 1]`
- `labels` (target) 的尺寸為 `[1]`

`MarginRankingLoss` 要求輸入和目標具有相容的維度。這裡 `preferred_reward` 和 `less_preferred_reward` 的額外維度（即 `[1, 1]` 對比 `[1]`）導致了不匹配。這很可能是因為獎勵模型從線性層（`self.v_head`）輸出了一個帶有額外維度的張量。

### 問題根源
在你的 `RewardModel` 中：
```python
reward = self.v_head(last_hidden_states[:, -1])  # 形狀: [batch_size, 1]
```
`v_head` 層輸出的獎勵分數形狀為 `[batch_size, 1]`（例如批次大小為 1 時是 `[1, 1]`）。同時，`labels` 的創建方式為：
```python
labels = torch.ones(preferred_reward.size(0)).to(device)  # 形狀: [batch_size]
```
這使得 `labels` 的形狀為 `[1]`，與獎勵的 `[1, 1]` 形狀不匹配。

### 解決方案
為了解決這個問題，你需要確保獎勵張量和目標張量具有相容的形狀。由於 `MarginRankingLoss` 期望一維張量（或至少匹配的形狀），你可以從獎勵輸出中擠壓掉多餘的維度。以下是修改訓練循環的方法：

#### 更新後的程式碼片段
```python
# Train the Reward Model
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens).squeeze()  # 移除額外維度
        less_preferred_reward = reward_model(**less_preferred_tokens).squeeze()  # 移除額外維度

        labels = torch.ones(preferred_reward.size(0)).to(device)  # 形狀: [batch_size]，例如 [1]
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")
```

#### 關鍵修改
- 在 `preferred_reward` 和 `less_preferred_reward` 後添加 `.squeeze()`，將它們的形狀從 `[1, 1]` 減少為 `[1]`，與 `labels` 張量匹配。

### 補充說明
1. **批次大小考量**：
   - 如果你後續增加批次大小（例如一次處理多個樣本），請確保 `preferred_tokens` 和 `less_preferred_tokens` 正確批次化，擠壓後形狀仍能對齊。

2. **獎勵模型輸出**：
   - 目前的獎勵模型採用最後一個隱藏狀態（`last_hidden_states[:, -1]`）並通過線性層。對於簡單的獎勵模型這沒問題，但你可以嘗試聚合隱藏狀態（例如平均池化）以獲得更細緻的評分。

3. **RL 循環**：
   - 你的 RL 微調循環使用了簡化的損失函數（`-reward.mean()`）。實際上，RLHF 通常採用像 PPO（近端策略優化）這樣的演算法，需要更複雜的設置（例如價值函數、剪裁目標）。目前你的方法作為概念驗證是可行的。

4. **分詞器填充**：
   - 你可能需要在分詞器調用中添加 `padding=True` 以確保輸入長度一致，不過帶有 `max_length` 的 `truncation=True` 應該能處理大多數情況。

### 完整可運作範例（簡化版）
以下是修正後的獎勵訓練循環最小版本：
```python
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoModelForCausalLM, AutoTokenizer

# 樣本數據
preference_data = [
    ("Write a story about a cat.", "Whiskers the cat lived in a cozy cottage...", "A cat story. The end."),
]

# 載入模型和分詞器
model_name = "gpt2"
policy_model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
policy_model.to(device)

# 獎勵模型
class RewardModel(nn.Module):
    def __init__(self, base_model):
        super().__init__()
        self.base_model = base_model.transformer
        self.v_head = nn.Linear(base_model.config.n_embd, 1)

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        last_hidden_states = outputs.last_hidden_state
        reward = self.v_head(last_hidden_states[:, -1])
        return reward

reward_model = RewardModel(policy_model).to(device)
reward_optimizer = optim.AdamW(reward_model.parameters(), lr=1e-5)
reward_criterion = nn.MarginRankingLoss(margin=1.0)

# 訓練獎勵模型
for epoch in range(3):
    for prompt, preferred, less_preferred in preference_data:
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        preferred_reward = reward_model(**preferred_tokens).squeeze()
        less_preferred_reward = reward_model(**less_preferred_tokens).squeeze()

        labels = torch.ones(preferred_reward.size(0)).to(device)
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")
```

這應該能解決維度不匹配問題，讓你的獎勵模型成功訓練。如果你需要進一步澄清或幫助處理 RL 部分，請告訴我！

---

### 理解和修復 PyTorch 腳本中的 IndexError

你在 Python 腳本中遇到的錯誤訊息是：

```
IndexError: Dimension specified as 0 but tensor has no dimensions
```

這發生在你腳本 `rl.py` 的第 44 行，具體是以下這行程式碼：

```python
labels = torch.ones(preferred_reward.size(0)).to(device)
```

該錯誤表明 `preferred_reward` 是一個標量張量（即它沒有維度，形狀為 `[]`），而嘗試使用 `.size(0)` 訪問其第一個維度是無效的，因為標量沒有可索引的維度。

讓我們逐步分析並提供解決方案。

---

### 錯誤原因

在你的腳本中，你很可能正在使用像 `MarginRankingLoss` 這樣的損失函數來訓練獎勵模型，該函數期望其輸入（`preferred_reward`、`less_preferred_reward` 和 `labels`）是形狀相容的張量——通常是每個元素對應批次中一個樣本的一維張量。以下是具體情況：

1. **`preferred_reward` 的來源**：
   - `preferred_reward` 是 `reward_model` 前向傳播的輸出，例如 `reward_model(**preferred_tokens)`
   - 假設你的獎勵模型每個樣本輸出單個值，對於批次大小為 1 的情況，輸出形狀為 `[1, 1]`（批次大小 × 輸出維度）

2. **張量擠壓**：
   - 在你的原始程式碼中，你對 `preferred_reward` 應用了 `.squeeze()`：
     ```python
     preferred_reward = reward_model(**preferred_tokens).squeeze()
     ```
   - `.squeeze()` 方法會移除所有大小為 1 的維度。對於形狀為 `[1, 1]` 的張量，這會將其減少為 `[]`——一個沒有維度的標量張量

3. **訪問尺寸**：
   - 之後，你嘗試創建一個與 `preferred_reward` 相同批次大小的 `labels` 張量：
     ```python
     labels = torch.ones(preferred_reward.size(0)).to(device)
     ```
   - 對於標量張量（`[]`），`preferred_reward.size()` 返回 `torch.Size([])`，一個空的尺寸元組。嘗試使用 `.size(0)` 訪問第一個維度會引發 `IndexError`，因為沒有可訪問的維度

4. **預期行為**：
   - `MarginRankingLoss` 函數要求其輸入（`preferred_reward`、`less_preferred_reward` 和 `labels`）具有相同的形狀，通常是一維張量如 `[batch_size]`。對於批次大小為 1，這應該是 `[1]`，而不是標量 `[]`

根本原因是 `.squeeze()` 過於激進——它移除了所有單例維度，當批次大小為 1 時將 `[1, 1]` 變成了標量 `[]`，這破壞了後續的 `.size(0)` 調用。

---

### 解決方案

為了解決這個問題，你需要確保 `preferred_reward` 和 `less_preferred_reward` 保持為形狀 `[batch_size]` 的一維張量，即使在 `batch_size=1` 時也是如此。不要使用會移除所有大小為 1 維度的 `.squeeze()`，而是使用 `.squeeze(-1)` 僅移除最後一個維度。這會將 `[1, 1]` 轉換為 `[1]`，保留批次維度。

以下是修正後的獎勵模型訓練循環程式碼片段：

```python
# Train the Reward Model
num_reward_epochs = 3
for epoch in range(num_reward_epochs):
    for prompt, preferred, less_preferred in preference_data:
        # Tokenize inputs
        preferred_tokens = tokenizer(prompt + preferred, return_tensors="pt", truncation=True, max_length=128).to(device)
        less_preferred_tokens = tokenizer(prompt + less_preferred, return_tensors="pt", truncation=True, max_length=128).to(device)

        # Compute rewards, squeezing only the last dimension
        preferred_reward = reward_model(**preferred_tokens).squeeze(-1)  # Shape: [1]
        less_preferred_reward = reward_model(**less_preferred_tokens).squeeze(-1)  # Shape: [1]

        # Create labels tensor based on batch size
        labels = torch.ones(preferred_reward.size(0)).to(device)  # Shape: [1]
        
        # Compute loss
        loss = reward_criterion(preferred_reward, less_preferred_reward, labels)

        # Backpropagation
        reward_optimizer.zero_grad()
        loss.backward()
        reward_optimizer.step()
    
    print(f"Reward Epoch {epoch+1}, Loss: {loss.item()}")
```

#### 運作原理

- **在 `.squeeze(-1)` 之後**：
  - 來自 `reward_model` 的原始形狀：`[1, 1]`（batch_size=1, output_dim=1）
  - 在 `.squeeze(-1)` 之後：`[1]`（僅移除最後一個維度）
  - `preferred_reward.size(0)` 返回 `1`，即批次大小
  - `labels` 成為形狀為 `[1]` 的一維張量，與 `preferred_reward` 和 `less_preferred_reward` 的形狀匹配

- **與 `MarginRankingLoss` 的相容性**：
  - `MarginRankingLoss` 期望 `input1`（`preferred_reward`）、`input2`（`less_preferred_reward`）和 `target`（`labels`）具有相同的形狀。當三者都是 `[1]` 時，損失計算會順利進行而不會出錯

- **可擴展性**：
  - 如果你後續使用更大的批次大小（例如 2），獎勵模型輸出 `[2, 1]`，`.squeeze(-1)` 產生 `[2]`，而 `labels` 變成 `[2]`，保持一致性

---

### 替代方法

雖然 `.squeeze(-1)` 是一個乾淨且精確的修復方法，但以下兩種方法也同樣有效：

1. **使用索引**：
   ```python
   preferred_reward = reward_model(**preferred_tokens)[:, 0]  # Shape: [1]
   less_preferred_reward = reward_model(**less_preferred_tokens)[:, 0]  # Shape: [1]
   ```
   - 這會選擇最後一個維度的第一個（也是唯一一個）元素，將 `[1, 1]` 轉換為 `[1]`

2. **使用 `.view(-1)`**：
   ```python
   preferred_reward = reward_model(**preferred_tokens).view(-1)  # Shape: [1]
   less_preferred_reward = reward_model(**less_preferred_tokens).view(-1)  # Shape: [1]
   ```
   - 這會將張量展平為一維張量。對於 `[1, 1]`，由於只有一個元素，它會變成 `[1]`

這兩種替代方法在這種情境下都能達到與 `.squeeze(-1)` 相同的結果，但 `.squeeze(-1)` 是首選，因為它明確針對最後一個維度，與獎勵模型的輸出結構（`[batch_size, 1]`）對齊。

---

### 補充說明

- **輸出中的警告**：
  - 關於 `torch.utils._pytree._register_pytree_node` 和 `resume_download` 的 `FutureWarning` 訊息與 `IndexError` 無關。它們來自 `transformers` 庫，指示已棄用的函數或將在未來版本中改變的行為。目前，它們不影響你的腳本功能，可以忽略，除非你想為將來的相容性更新程式碼

- **獎勵模型輸出**：
  - 該修復假設你的 `reward_model` 輸出形狀為 `[batch_size, 1]` 的張量。如果其架構不同（例如直接輸出標量或不同形狀），你需要相應調整。基於典型的獎勵模型設計，`[batch_size, 1]` 在線性頭之後是標準的

- **批次處理**：
  - 你目前的循環一次處理一個偏好對（隱含批次大小為 1）。如果你計劃擴展規模，考慮使用 DataLoader 批次處理多個對以提高效率，但 `.squeeze(-1)` 修復仍然適用

---

### 驗證

對於批次大小為 1：
- `reward_model(**preferred_tokens)`：`[1, 1]`
- 在 `.squeeze(-1)` 之後：`[1]`
- `preferred_reward.size(0)`：`1`
- `labels`：`[1]`
- 損失輸入：全部為 `[1]`——完美運作

`IndexError` 被消除，你的獎勵模型訓練現在應該能順利運行。

---

### 最終答案

要修復 `rl.py` 第 44 行的 `IndexError: Dimension specified as 0 but tensor has no dimensions`，在計算 `preferred_reward` 和 `less_preferred_reward` 時將 `.squeeze()` 替換為 `.squeeze(-1)`。這確保它們保持形狀為 `[1]`（或對於更大的批次為 `[batch_size]`）的一維張量，允許 `preferred_reward.size(0)` 正確檢索批次大小以創建 `labels` 張量。

按照上面所示在你的獎勵模型訓練循環中應用此更改，錯誤將得到解決。