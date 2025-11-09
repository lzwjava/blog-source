---
audio: false
date: 2025-09-06
generated: true
image: false
lang: hant
layout: post
title: 模型形狀修復與改進
translated: true
type: note
---

以下是你的腳本逐段解析，以及幾個你可能需要進行的重要修正。

# 模型架構說明

* 你定義了一個微型的**字符/詞級下一詞元預測器**：

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` 處理一個 one-hot 向量序列（大小 = `vocab_size`），並在每個時間步產生大小為 50 的隱藏狀態。
  * `nn.Linear(50, vocab_size, bias=False)` 將每個時間步的隱藏狀態映射到**詞彙表上的邏輯輯值**。

# 預期的張量形狀（關鍵）

由於你未設定 `batch_first=True`，PyTorch LSTM 的預設輸入形狀是 **(seq_len, batch_size, input_size)**。

* 對於批次大小為 1 的單一序列：

  * 輸入 LSTM 的張量應為 `(seq_len, 1, vocab_size)`。
  * LSTM 輸出的 `x` 形狀為 `(seq_len, 1, hidden_size)`。
  * 接著你使用 `view(-1, hidden_size)` → `(seq_len, hidden_size)`，使線性層產生 `(seq_len, vocab_size)`。
  * `CrossEntropyLoss` 預期：

    * `outputs`: `(N, C)` = `(seq_len, vocab_size)`
    * `targets`: `(N,)` = `(seq_len,)` 詞元索引

# 你的程式碼可能出錯的地方（形狀問題）

你執行了：

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

如果 `one_hot_encode_sequence` 返回 `(batch, seq_len, vocab)`，正確的置換方式應為 **`permute(1, 0, 2)`**（以得到 `(seq_len, batch, vocab)`）。你目前的 `permute(0,2,1)` 會產生 `(batch, vocab, seq_len)`，這將導致形狀不匹配，如果早期形狀與假設不同，可能會出錯或無聲地學習無意義的內容。

兩個簡潔的選項（擇一使用）：

**A) 保持預設 LSTM（批次第二）：**

```python
# 需要 (seq_len, batch, input_size)
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**B) 改為批次優先（通常更簡單）：**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# 需要 (batch, seq_len, input_size)
# 然後無需置換；保持為 (1, seq_len, vocab_size)
```

# 訓練循環邏輯

* 每個訓練週期你維護兩個運行總和：`epoch_training_loss` 和 `epoch_validation_loss`。
* **驗證階段**（`net.eval()` + 無梯度更新）：

  * 對於 `validation_set` 中的每個 (inputs, targets)：

    * 對輸入進行 one-hot 編碼，將目標轉換為索引
    * 前向傳播 → 邏輯輯值 `(seq_len, vocab_size)`（假設形狀已修正）
    * 針對形狀為 `(seq_len,)` 的目標索引計算 CE 損失
    * 累積損失
* **訓練階段**（`net.train()`）：

  * 相同的預處理
  * 前向傳播 → 損失 → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`
* 你記錄平均損失並每 5 個訓練週期輸出一次。

# 推理與輸出

* 你從 `test_set` 中選取樣本，運行模型，獲取每個時間步的邏輯輯值，對每個時間步取 `argmax` → 預測的詞元。
* 你輸出輸入詞、目標詞和預測詞。
* 你繪製訓練與驗證損失隨訓練週期的變化圖。

# 小而高效的改進

1. **修正輸入形狀**（最重要）。使用上述 A 或 B 選項之一。如果選擇批次優先，將前向傳播改為：

   ```python
   x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
   x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
   ```
2. **在評估/推理時使用 `with torch.no_grad()`** 以避免追蹤梯度，提升速度與記憶體效率：

   ```python
   net.eval()
   with torch.no_grad():
       outputs = net(inputs_one_hot)
       loss = criterion(outputs, targets_idx)
   ```

   以及轉換為 numpy 時：

   ```python
   outputs = net(inputs_one_hot).detach().numpy()
   ```
3. **也為 PyTorch 設定隨機種子**以確保可重現性：

   ```python
   torch.manual_seed(42)
   ```
4. **設備處理**（如果使用 GPU）：

   ```python
   device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
   net.to(device)
   inputs_one_hot = inputs_one_hot.to(device)
   targets_idx = targets_idx.to(device)
   ```
5. **目標對齊**：確保 `targets` 是與每個輸入時間步**對齊的下一個詞元**。如果你的資料集以這種方式配對 `(inputs, targets)`，那就沒問題。否則，請建立 `targets = inputs[1:]` 並丟棄最後一個輸入或類似處理。
6. **除非有特定原因，否則移除 `.bias=False`**；輸出層的偏置通常無害甚至有益。
7. **填充/可變長度**（可選）：如果序列長度不同，考慮使用 `pack_padded_sequence` 以避免在填充詞元上訓練。
8. **監控**：除了損失之外，計算驗證集上**下一詞元預測的準確率**（`% correct argmax`）可能更易於理解。

# 最小修正程式碼片段（批次優先版本）

```python
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1, batch_first=True)
        self.l_out = nn.Linear(50, vocab_size)

    def forward(self, x):
        # x: (batch, seq, vocab_size)
        x, _ = self.lstm(x)                    # (batch, seq, hidden)
        x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
        x = self.l_out(x)                      # (batch*seq, vocab)
        return x

# ... 在你的循環中，移除 permute；確保 inputs_one_hot 是 (batch, seq, vocab)
# 驗證/推理時使用 `with torch.no_grad()` 和 `.detach()`
```

如果你分享 `one_hot_encode_sequence` 返回的確切形狀（例如 `(seq, vocab)` 或 `(1, seq, vocab)`），我可以為你的情況精確調整置換/重塑的程式碼行。