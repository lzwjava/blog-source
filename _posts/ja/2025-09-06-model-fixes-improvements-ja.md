---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ja
layout: post
title: モデル形状の修正と改善
translated: true
type: note
---

以下に、スクリプトが行っていることを部分ごとに説明し、加えておそらく必要となる重要な修正点をいくつか示します。

# モデルの概要

* あなたは小さな**文字/単語レベルの次トークン予測器**を定義しています：

  * `nn.LSTM(input_size=vocab_size, hidden_size=50, num_layers=1)` は、one-hotベクトル（サイズ = `vocab_size`）のシーケンスを処理し、各タイムステップでサイズ50の隠れ状態を生成します。
  * `nn.Linear(50, vocab_size, bias=False)` は、各タイムステップの隠れ状態を**語彙に対するロジット**にマッピングします。

# 期待されるテンソルの形状（重要）

PyTorch LSTMのデフォルトの入力形状は **(seq\_len, batch\_size, input\_size)** です。これは `batch_first=True` を設定していないためです。

* バッチサイズ1の単一シーケンスの場合：

  * LSTMへの入力は `(seq_len, 1, vocab_size)` であるべきです。
  * LSTMは形状 `(seq_len, 1, hidden_size)` の出力 `x` を生成します。
  * その後、`view(-1, hidden_size)` → `(seq_len, hidden_size)` とすることで、線形層が `(seq_len, vocab_size)` を生成します。
  * `CrossEntropyLoss` は以下を期待します：

    * `outputs`: `(N, C)` = `(seq_len, vocab_size)`
    * `targets`: `(N,)` = `(seq_len,)` トークンのインデックス

# コードが間違っている可能性が高い箇所（形状）

あなたのコード：

```python
inputs_one_hot = inputs_one_hot.permute(0, 2, 1)
```

もし `one_hot_encode_sequence` が `(batch, seq_len, vocab)` を返す場合、デフォルトのLSTMに対する正しいpermuteは **`permute(1, 0, 2)`** です（`(seq_len, batch, vocab)` を得るため）。あなたの現在の `permute(0,2,1)` は `(batch, vocab, seq_len)` を与え、これは不一致であり、以前の形状が想定と異なっていれば、エラーになるか、あるいは無意味なことを学習したまま処理が進む可能性があります。

クリーンな選択肢は二つです（一つを選んでください）：

**A) デフォルトのLSTM（batch\_second）を維持する：**

```python
# (seq_len, batch, input_size) が欲しい
inputs_one_hot = inputs_one_hot.permute(1, 0, 2)  # (seq_len, 1, vocab_size)
```

**B) バッチファーストにする（しばしばより簡単）：**

```python
self.lstm = nn.LSTM(input_size=vocab_size, hidden_size=50, batch_first=True)
# (batch, seq_len, input_size) が欲しい
# その後、permuteは行わず、(1, seq_len, vocab_size) のままにする
```

# トレーニングループのロジック

* 各エポックに対して、2つの実行中の合計 `epoch_training_loss` と `epoch_validation_loss` を保持します。
* **検証フェーズ** (`net.eval()` + 勾配ステップなし)：

  * `validation_set` 内の各 (inputs, targets) に対して：

    * 入力をone-hotエンコードし、ターゲットをインデックスに変換
    * フォワードパス → ロジット `(seq_len, vocab_size)`（形状が修正されていると仮定）
    * 形状 `(seq_len,)` のターゲットインデックスに対するCE損失
    * 損失を累積
* **トレーニングフェーズ** (`net.train()`)：

  * 同じ前処理
  * フォワード → 損失 → `optimizer.zero_grad()` → `loss.backward()` → `optimizer.step()`
* 平均損失を記録し、5エポックごとに表示します。

# 推論と出力

* `test_set` からサンプルを選び、モデルを実行し、各タイムステップのロジットを取得し、タイムステップごとに `argmax` を取る → 予測されたトークン。
* 入力単語、ターゲット単語、予測された単語を表示します。
* エポックにわたるトレーニング損失と検証損失をプロットします。

# 小さな、高インパクトな改善点

1.  **入力形状を修正する**（最も重要）。上記のAまたはBのいずれかを使用してください。バッチファーストを選択した場合、フォワードパスを次のように変更します：

    ```python
    x, (h, c) = self.lstm(x)         # x: (batch, seq, hidden)
    x = x.reshape(-1, self.lstm.hidden_size)  # (batch*seq, hidden)
    ```
2.  **評価/推論には `with torch.no_grad()` を使用する**：勾配の追跡を避け、速度とメモリのために：

    ```python
    net.eval()
    with torch.no_grad():
        outputs = net(inputs_one_hot)
        loss = criterion(outputs, targets_idx)
    ```

    そして、numpy変換には：

    ```python
    outputs = net(inputs_one_hot).detach().numpy()
    ```
3.  **再現性のためにPyTorchにもシードを設定する**：

    ```python
    torch.manual_seed(42)
    ```
4.  **デバイス処理**（GPUを使用する場合）：

    ```python
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net.to(device)
    inputs_one_hot = inputs_one_hot.to(device)
    targets_idx = targets_idx.to(device)
    ```
5.  **ターゲットのアラインメント**：`targets` が各入力タイムステップと整列された**次のトークン**であることを確認してください。あなたのデータセットがそのように `(inputs, targets)` をペアにしているなら問題ありません。そうでない場合は、`targets = inputs[1:]` を作成し、最後の入力をドロップするなどの対応をしてください。
6.  **理由がない限り `.bias=False` はドロップする**；出力層のバイアスは通常、無害か役に立ちます。
7.  **パディング/可変長**（オプション）：シーケンスの長さが異なる場合、パディングトークンでのトレーニングを避けるために `pack_padded_sequence` の使用を検討してください。
8.  **モニタリング**：損失だけよりも、次トークン予測の正解率を計算する方が解釈しやすい場合があります—検証データに対する `% correct argmax` を計算してください。

# 最小限の修正済みスニペット（バッチファースト版）

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

# ... ループ内では、permuteを削除し、inputs_one_hotが (batch, seq, vocab) であることを確認する
# 検証/推論では `with torch.no_grad()` と `.detach()` を使用する
```

もし `one_hot_encode_sequence` が返す正確な形状（例: `(seq, vocab)` 対 `(1, seq, vocab)`）を共有していただければ、あなたのケースに正確に合わせて permute/reshape の行を調整できます。