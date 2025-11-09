---
audio: false
date: 2025-09-06
generated: true
image: false
lang: hant
layout: post
title: 長短期記憶實現錯誤與修正
translated: true
type: note
---

明白了——這是一個清晰、從頭到尾的逐步解說，說明這個從零開始的 LSTM 腳本在做什麼，以及那些會破壞訓練的細微錯誤和修復方法。我會保持線性結構，方便快速瀏覽（不使用寬表格）。

# 程式碼試圖實現的功能

你正在用 NumPy 實現一個最小化的字符/詞級 LSTM 語言模型：

1. **設定與尺寸**

* `hidden_size`、`vocab_size`、資料集（`training_set`、`validation_set`、`test_set`）、標記↔索引映射，以及像 `sigmoid`、`tanh`、`softmax`、`one_hot_encode_sequence` 這樣的函數，預期來自 `data.py` / `utils.py`。
* 每個時間步的輸入是一個 one-hot 向量 `x ∈ R^{vocab_size×1}`。
* 你將先前的隱藏狀態和當前輸入連接起來：
  `z = [h_{t-1}; x_t] ∈ R^{(hidden_size+vocab_size)×1}`。
  這就是為什麼 `W_f, W_i, W_g, W_o ∈ R^{hidden_size×(hidden_size+vocab_size)}`。

2. **參數初始化**

* `init_lstm(...)` 為四個門（遺忘門 f、輸入門 i、候選門 g、輸出門 o）分配權重，外加輸出投影 `W_v` 到詞彙表。
* `init_orthogonal` 使每個權重矩陣正交歸一（通過 QR 分解）。對於 RNN/LSTM 來說，這是一個不錯的選擇。

3. **前向傳播（每個序列）**
   對於每個時間步：

* 構建 `z = [h_prev; x]`。
* 計算門：

  * `f_t = σ(W_f z + b_f)`
  * `i_t = σ(W_i z + b_i)`
  * `g_t = tanh(W_g z + b_g)`
  * `C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t`
  * `o_t = σ(W_o z + b_o)`
  * `h_t = o_t ⊙ tanh(C_t)`
* 投影到詞彙表並進行 softmax：

  * `v_t = W_v h_t + b_v`
  * `ŷ_t = softmax(v_t)`
* 程式碼儲存了大量的中間結果（`z_s, f_s, i_s, g_s, C_s, o_s, h_s, v_s, output_s`）以供反向傳播使用。

4. **損失函數**

* 每個時間步與 one-hot 目標的交叉熵：
  `L_t = − log ŷ_t[target]`
  （程式碼使用逐元素的 `-mean(log(ŷ)*one_hot)`，這在常數縮放下等同於 `-log(ŷ[target])`。）

5. **反向傳播（通過 LSTM 的 BPTT）**

* 經典的 LSTM 梯度，從 `t = T−1 → 0` 累積。
* 裁剪全局梯度範數，然後進行 SGD 更新。

6. **訓練循環**

* 對於每個 epoch：在驗證集上評估（僅計算損失），然後在訓練集上訓練（損失 + 梯度 + 更新）。最後，繪製訓練/驗證損失。

---

# 關鍵問題（這些問題會無聲地破壞學習）

## 1) 反向傳播中 `h` 和 `C` 的索引偏移錯誤

在 `forward` 中，你首先推入*初始*狀態：

* `h_s[0] = h_init`，然後在步驟 0 之後附加 `h_0` → 所以 `h_s` 的長度是 `T+1`，且 `h_s[t+1] = h_t`。
* `C_s` 也一樣：`C_s[0] = C_init`，然後 `C_s[t+1] = C_t`。

但在 `backward(...)` 中，你使用 `h[t]` 和 `C[t]`，好像它們是 `h_t` 和 `C_t`。但它們不是；它們偏移了一位。

**修復（簡單的經驗法則）：**

* 在需要 `h_t` 的地方使用 `h[t+1]`。
* 在需要 `C_t` 的地方使用 `C[t+1]`。
* 對於「上一個細胞狀態」，你需要 `C_prev = C[t]`（而不是 `C[t-1]`）。

所以在 `for t in reversed(range(T)):` 循環內部：

* 當前狀態：`h_t = h[t+1]`，`C_t = C[t+1]`
* 上一個狀態：`C_{t-1} = C[t]`

你當前的代碼行：

```python
C_prev = C[t - 1]
```

對於 `t==0` 是錯誤的（會繞到最後一個元素），並且通常偏移一位。必須是：

```python
C_prev = C[t]       # 上一個細胞狀態
# 並使用 C_t = C[t+1] 作為「當前」
```

並且，任何你使用 `h[t]` 意圖表示當前隱藏狀態的地方，都改為 `h[t+1]`。

## 2) 幾個門的導數錯誤

你有時會再次應用非線性函數而不是其導數，或者忘記了導數標誌。

* **細胞狀態路徑：**
  正確：
  `dC_t += dh_t ⊙ o_t ⊙ (1 - tanh(C_t)^2)`
  你的代碼：

  ```python
  dC += dh * o[t] * tanh(tanh(C[t]), derivative=True)
  ```

  那是應用了兩次 `tanh`。替換為：

  ```python
  dC += dh * o_t * (1 - np.tanh(C_t)**2)
  ```

* **遺忘門：**
  正確：`df = dC_t ⊙ C_{t-1} ⊙ f_t ⊙ (1 - f_t)`
  你的代碼：

  ```python
  df = dC * C_prev
  df = sigmoid(f[t]) * df
  ```

  缺少導數項。應該是：

  ```python
  df = dC * C_prev
  df *= f[t] * (1 - f[t])      # 如果 f[t] 儲存的是 σ 激活前的輸出
  ```

* **輸入門：**
  你做了：

  ```python
  di = dC * g[t]
  di = sigmoid(i[t], True) * di
  ```

  如果 `sigmoid(x, True)` 返回 σ’(x) *而不是* σ(x)，這樣做是可以的。更穩健的方式（與你儲存 `i[t]` 作為門輸出相匹配）是：

  ```python
  di = dC * g[t]
  di *= i[t] * (1 - i[t])
  ```

* **候選門：**
  你做了：

  ```python
  dg = dC * i[t]
  dg = tanh(g[t], derivative=True) * dg
  ```

  如果 `g[t]` 儲存的是 `tanh(preact)`，那麼 `tanh’(preact) = 1 - g[t]^2`。所以：

  ```python
  dg = dC * i[t]
  dg *= (1 - g[t]**2)
  ```

* **輸出門：**
  你做了：

  ```python
  do = dh * tanh(C[t])
  do = sigmoid(o[t], derivative=True) * do
  ```

  配合索引修復（`C_t = C[t+1]`，`o_t = o[t]`）和上述的導數：

  ```python
  do = dh * np.tanh(C_t)
  do *= o[t] * (1 - o[t])
  ```

* **下一個細胞梯度：**
  正確：

  ```python
  dC_next = dC * f[t]
  ```

## 3) 使用 `h[0]` / `C[0]` 來確定 `dh_next` 和 `dC_next` 的尺寸

你需要的是*當前* h/C（序列結束時）的形狀，而不是初始的零。使用：

```python
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])
```

## 4) 交叉熵的數值穩定性

如果 `softmax` 內部有鉗位/epsilon 處理，那麼 `loss += -np.mean(np.log(outputs[t]) * targets[t])` 是沒問題的。如果沒有，添加一個小的 epsilon：

```python
eps = 1e-12
loss += -np.sum(targets[t] * np.log(outputs[t] + eps))
```

## 5) 訓練穩定性調整

* **遺忘門偏置：** 將 `b_f` 初始化為一個正值（例如 `1.0`），以便在訓練早期 LSTM 傾向於保留記憶：

  ```python
  b_f = np.ones((hidden_size, 1)) * 1.0
  ```
* **學習率：** 使用原始 SGD 時 `lr=1e-1` 過於激進。從 `1e-2` 開始或使用 Adam。
* **梯度裁剪：** 很好。如果需要，考慮使用每矩陣範數。

---

# 修正後的反向傳播循環核心代碼

這個草圖顯示了索引和導數的修正。它假設 `f[t], i[t], g[t], o[t]` 是它們非線性函數的*輸出*（如你的前向傳播中）：

```python
T = len(outputs)
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])

for t in reversed(range(T)):
    # 使用正確索引的簡稱
    y_hat = outputs[t]                 # softmax 輸出
    y_true = targets[t]
    h_t   = h[t+1]
    C_t   = C[t+1]
    C_tm1 = C[t]

    # 輸出層
    dv = y_hat.copy()
    dv[np.argmax(y_true)] -= 1
    W_v_d += dv @ h_t.T
    b_v_d += dv

    # 反向傳播到 h
    dh = W_v.T @ dv
    dh += dh_next

    # 輸出門
    do = dh * np.tanh(C_t)
    do *= o[t] * (1 - o[t])
    W_o_d += do @ z[t].T
    b_o_d += do

    # 細胞狀態
    dC = dC_next + dh * o[t] * (1 - np.tanh(C_t)**2)

    # 候選門 (g), 輸入門 (i), 遺忘門 (f)
    dg = dC * i[t]
    dg *= (1 - g[t]**2)               # 因為 g[t] = tanh(preact)

    di = dC * g[t]
    di *= i[t] * (1 - i[t])

    df = dC * C_tm1
    df *= f[t] * (1 - f[t])

    # 累積門權重/偏置梯度
    W_g_d += dg @ z[t].T;  b_g_d += dg
    W_i_d += di @ z[t].T;  b_i_d += di
    W_f_d += df @ z[t].T;  b_f_d += df

    # 傳播到 z 並拆分到 h_{t-1} 部分
    dz = (W_f.T @ df) + (W_i.T @ di) + (W_g.T @ dg) + (W_o.T @ do)
    dh_next = dz[:hidden_size, :]
    dC_next = dC * f[t]
```

---

# 較小但重要的細節與建議

* **正交初始化：** 對循環權重很好。對於輸入部分，你也可以按 `1/√fan_in` 縮放。這裡不關鍵。
* **批處理：** 代碼一次訓練 1 個序列（無批處理）。對於清晰度來說很好，但速度慢/噪聲大。小批量處理需要仔細的形狀更改。
* **教師強制：** 你使用真實的下一個標記作為目標；都很好。如果你以後進行自由運行生成，請從 `softmax` 輸出中採樣並反饋給模型。
* **損失報告：** 你對序列的每個時間步損失求和，然後按資料集長度平均；如果序列長度不同，這會混合尺度。考慮按總標記數歸一化。
* **繪圖：** 在本地工作。在無頭環境中，記得切換後端或使用 savefig。

---

# 你應該立即進行的修復總結

1. **索引**：在反向傳播中，將每個 `h[t]` 替換為 `h[t+1]`，每個 `C[t]` 替換為 `C[t+1]`，並設定 `C_prev = C[t]`。
2. **導數**：

   * 對細胞狀態路徑使用 `(1 - tanh(C_t)**2)`。
   * 對 σ 門使用 `gate * (1 - gate)`，因為你儲存的是門輸出。
   * 對候選門使用 `(1 - g[t]**2)`，因為 `g[t]=tanh(preact)`。
3. **初始化**：將 `b_f` 設為約 `1.0`。
4. **學習率**：降至 `1e-2`（或切換到 Adam）。
5. **穩定性**：在 `log` 中添加 `eps`。

進行這些更改後，你的損失應該會開始以更合理的方式下降。如果你需要，可以貼上你更新後的 `backward(...)`，我會幫你檢查一下。