---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ja
layout: post
title: LSTM実装のバグと修正
translated: true
type: note
---

了解しました。以下に、LSTMスクラッチ実装の詳細な解説と修正点を日本語で記述します。

# コードの目的

NumPyでの最小限の文字/単語レベルLSTM言語モデルを実装しています：

1. **セットアップとサイズ**

* `hidden_size`、`vocab_size`、データセット（`training_set`、`validation_set`、`test_set`）、トークン↔インデックスマップ、および`sigmoid`、`tanh`、`softmax`、`one_hot_encode_sequence`などの関数は`data.py`/`utils.py`から提供されることを想定
* 各タイムステップの入力はone-hotベクトル`x ∈ R^{vocab_size×1}`
* 前の隠れ状態と現在の入力を連結：
  `z = [h_{t-1}; x_t] ∈ R^{(hidden_size+vocab_size)×1}`
  これが`W_f, W_i, W_g, W_o ∈ R^{hidden_size×(hidden_size+vocab_size)}`の理由

2. **パラメータ初期化**

* `init_lstm(...)`は4つのゲート（忘却f、入力i、候補g、出力o）の重みと、語彙への出力射影`W_v`を割り当て
* `init_orthogonal`は各重み行列を正規直交化（QR経由）。RNN/LSTMには適切な選択

3. **順伝播（シーケンスごと）**
   各タイムステップで：

* `z = [h_prev; x]`を構築
* ゲートを計算：

  * `f_t = σ(W_f z + b_f)`
  * `i_t = σ(W_i z + b_i)`
  * `g_t = tanh(W_g z + b_g)`
  * `C_t = f_t ⊙ C_{t-1} + i_t ⊙ g_t`
  * `o_t = σ(W_o z + b_o)`
  * `h_t = o_t ⊙ tanh(C_t)`
* 語彙への射影とsoftmax：

  * `v_t = W_v h_t + b_v`
  * `ŷ_t = softmax(v_t)`
* コードは逆伝播のために多くの中間値を保存（`z_s, f_s, i_s, g_s, C_s, o_s, h_s, v_s, output_s`）

4. **損失**

* one-hotターゲットを用いた各ステップの交差エントロピー：
  `L_t = − log ŷ_t[target]`
  （コードは要素ごとの`-mean(log(ŷ)*one_hot)`を使用。これは定数スケーリングを除き`-log(ŷ[target])`と等価）

5. **逆伝播（LSTMを通したBPTT）**

* 古典的なLSTM勾配、`t = T−1 → 0`から累積
* グローバル勾配ノルムをクリップ、その後SGD更新

6. **トレーニングループ**

* 各エポック：検証セットで評価（損失のみ）、その後トレーニングセットで学習（損失＋勾配＋更新）。最後にトレーニング/検証損失をプロット

---

# 重大な問題（これらは学習を静かに破壊します）

## 1) 逆伝播における`h`と`C`のオフバイワンインデックス

`forward`では、*初期*状態を最初にプッシュ：

* `h_s[0] = h_init`、その後ステップ0の後に`h_0`を追加 → したがって`h_s`は`T+1`の長さで`h_s[t+1] = h_t`
* `C_s`も同様：`C_s[0] = C_init`、その後`C_s[t+1] = C_t`

しかし`backward(...)`では、`h[t]`と`C[t]`を`h_t`と`C_t`であるかのように使用。そうではなく、1つシフトしている

**修正（簡単な経験則）：**

* `h_t`が必要な場所で`h[t+1]`を使用
* `C_t`が必要な場所で`C[t+1]`を使用
* 「前のセル状態」には`C_prev = C[t]`（`C[t-1]`ではない）を使用

したがって`for t in reversed(range(T)):`ループ内で：

* 現在の状態：`h_t = h[t+1]`、`C_t = C[t+1]`
* 前の状態：`C_{t-1} = C[t]`

現在の行：

```python
C_prev = C[t - 1]
```

は`t==0`で間違い（最後の要素にラップ）し、一般的にオフバイワン。以下でなければならない：

```python
C_prev = C[t]       # 前のセル状態
# そして「現在」としてC_t = C[t+1]を使用
```

そして現在の隠れ状態を意図して`h[t]`を使用する場所はすべて`h[t+1]`に変更

## 2) いくつかのゲートの誤った導関数

導関数の代わりに再度非線形関数を適用したり、導関数フラグを忘れたりしている

* **セル状態パス：**
  正しい：
  `dC_t += dh_t ⊙ o_t ⊙ (1 - tanh(C_t)^2)`
  あなたのコード：

  ```python
  dC += dh * o[t] * tanh(tanh(C[t]), derivative=True)
  ```

  これは`tanh`が2回適用されている。以下で置き換え：

  ```python
  dC += dh * o_t * (1 - np.tanh(C_t)**2)
  ```

* **忘却ゲート：**
  正しい：`df = dC_t ⊙ C_{t-1} ⊙ f_t ⊙ (1 - f_t)`
  あなたのコード：

  ```python
  df = dC * C_prev
  df = sigmoid(f[t]) * df
  ```

  導関数項が欠落。以下であるべき：

  ```python
  df = dC * C_prev
  df *= f[t] * (1 - f[t])      # f[t]がσ事前活性化出力を格納する場合
  ```

* **入力ゲート：**
  あなたのコード：

  ```python
  di = dC * g[t]
  di = sigmoid(i[t], True) * di
  ```

  これは、`sigmoid(x, True)`がσ(x)ではなくσ'(x)を返す場合に問題ない。`i[t]`をゲート出力として保存した方法に合わせるより堅牢な方法は：

  ```python
  di = dC * g[t]
  di *= i[t] * (1 - i[t])
  ```

* **候補ゲート：**
  あなたのコード：

  ```python
  dg = dC * i[t]
  dg = tanh(g[t], derivative=True) * dg
  ```

  `g[t]`が`tanh(preact)`を格納する場合、`tanh'(preact) = 1 - g[t]^2`。したがって：

  ```python
  dg = dC * i[t]
  dg *= (1 - g[t]**2)
  ```

* **出力ゲート：**
  あなたのコード：

  ```python
  do = dh * tanh(C[t])
  do = sigmoid(o[t], derivative=True) * do
  ```

  インデックス修正（`C_t = C[t+1]`、`o_t = o[t]`）と上記の導関数で：

  ```python
  do = dh * np.tanh(C_t)
  do *= o[t] * (1 - o[t])
  ```

* **次のセル勾配：**
  正しい：

  ```python
  dC_next = dC * f[t]
  ```

## 3) `dh_next`と`dC_next`のサイズ設定に`h[0]`/`C[0]`を使用

初期ゼロではなく、**現在**のh/C（シーケンス終了時）の形状が必要。以下を使用：

```python
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])
```

## 4) 交差エントロピーの数値的安定性

`loss += -np.mean(np.log(outputs[t]) * targets[t])`は、`softmax`が内部でクランプ/イプシロン処理する場合は問題ない。そうでない場合、小さなイプシロンを追加：

```python
eps = 1e-12
loss += -np.sum(targets[t] * np.log(outputs[t] + eps))
```

## 5) トレーニング安定性の調整

* **忘却ゲートバイアス：** `b_f`を正の値（例：`1.0`）で初期化し、トレーニング初期にLSTMがメモリを保持する傾向を持つように：

  ```python
  b_f = np.ones((hidden_size, 1)) * 1.0
  ```
* **学習率：** 生のSGDで`lr=1e-1`は攻撃的。`1e-2`から開始またはAdamを使用
* **勾配クリッピング：** 良い。必要に応じて行列ごとのノルムを検討

---

# 逆伝播ループの修正された核心

このスケッチは、インデックスと導関数の修正を示す。`f[t], i[t], g[t], o[t]`がそれらの非線形性の*出力*であると仮定（順伝播と同様）：

```python
T = len(outputs)
dh_next = np.zeros_like(h[-1])
dC_next = np.zeros_like(C[-1])

for t in reversed(range(T)):
    # 正しいインデックスでの短い名前
    y_hat = outputs[t]                 # softmax出力
    y_true = targets[t]
    h_t   = h[t+1]
    C_t   = C[t+1]
    C_tm1 = C[t]

    # 出力層
    dv = y_hat.copy()
    dv[np.argmax(y_true)] -= 1
    W_v_d += dv @ h_t.T
    b_v_d += dv

    # hへの逆伝播
    dh = W_v.T @ dv
    dh += dh_next

    # 出力ゲート
    do = dh * np.tanh(C_t)
    do *= o[t] * (1 - o[t])
    W_o_d += do @ z[t].T
    b_o_d += do

    # セル状態
    dC = dC_next + dh * o[t] * (1 - np.tanh(C_t)**2)

    # 候補（g）、入力（i）、忘却（f）
    dg = dC * i[t]
    dg *= (1 - g[t]**2)               # g[t] = tanh(preact)なので

    di = dC * g[t]
    di *= i[t] * (1 - i[t])

    df = dC * C_tm1
    df *= f[t] * (1 - f[t])

    # ゲート重み/バイアス勾配を累積
    W_g_d += dg @ z[t].T;  b_g_d += dg
    W_i_d += di @ z[t].T;  b_i_d += di
    W_f_d += df @ z[t].T;  b_f_d += df

    # zへ伝播し、h_{t-1}部分に分割
    dz = (W_f.T @ df) + (W_i.T @ di) + (W_g.T @ dg) + (W_o.T @ do)
    dh_next = dz[:hidden_size, :]
    dC_next = dC * f[t]
```

---

# 小さくても重要な詳細と推奨事項

* **直交初期化：** 再帰重みに良い。入力部分については、`1/√fan_in`でスケーリングも可能。ここでは重要ではない
* **バッチ処理：** コードは1シーケンスずつトレーニング（バッチ処理なし）。明確さには良いが、低速/ノイズ多い。ミニバッチ処理には注意深い形状変更が必要
* **Teacher forcing：** グラウンドトゥルースの次のトークンをターゲットとして使用。問題ない。フリーランニング生成を行う場合は、`softmax`出力からサンプリングし、モデルにフィードバック
* **損失報告：** シーケンス全体のステップごとの損失を合計し、データセットの長さで平均。シーケンス長が異なる場合、スケールが混在。総トークン数で正規化を検討
* **プロット：** ローカルで動作。ヘッドレス環境では、バックエンドの切り替えまたはsavefigを忘れずに

---

# 今すぐ行うべき修正の要約

1. **インデックス**: すべての`h[t]`を`h[t+1]`に、すべての`C[t]`を`C[t+1]`に置き換え、逆伝播で`C_prev = C[t]`を設定
2. **導関数**:

   * セル状態パスに`(1 - tanh(C_t)**2)`を使用
   * ゲート出力を保存したため、σゲートに`gate * (1 - gate)`を使用
   * `g[t]=tanh(preact)`のため、候補ゲートに`(1 - g[t]**2)`を使用
3. **初期化**: `b_f`を\~`1.0`に設定
4. **学習率**: `1e-2`に低下（またはAdamに切り替え）
5. **安定性**: `log`に`eps`を追加

これらの変更を行うと、損失がより合理的な方法で減少し始めるはず。必要であれば、更新した`backward(...)`を貼り付けてください。健全性チェックを行います。