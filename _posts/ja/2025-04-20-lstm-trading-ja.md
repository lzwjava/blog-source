---
audio: false
generated: true
lang: ja
layout: post
title: 履歴データとLSTMの統合
translated: true
type: note
---

TigerOpen APIから取得した過去の株価データとLSTMモデルを組み合わせた分析は実現可能であり、金融時系列予測における一般的なアプローチです。2つ目のスクリプトは過去の株価データ（OHLCVバーなど）を取得するもので、最初のスクリプトと同様にLSTMモデルを訓練するためのデータセット構築に使用できます。以下では、これら2つを統合する方法、潜在的な課題への対応、LSTMを使用した株価データ分析の高レベルなアプローチについて説明します。

### 2つのスクリプトを統合する高レベルなアプローチ

1. **過去データの取得**:
   - 2つ目のスクリプトの`get_history_data`関数を使用して、過去の株価データ（例：シンボル '00700' など）を取得します。
   - データには始値、高値、安値、終値、出来高、タイムスタンプが含まれており、これらをLSTMの特徴量として使用できます。

2. **LSTM用のデータ前処理**:
   - 過去データをLSTMモデルに適した形式に変換します。これには以下が含まれます：
     - データの正規化（例：価格と出来高を[0, 1]範囲にスケーリング）
     - 過去データのシーケンス作成（例：過去60日間のデータを使用して翌日の終値を予測）
     - 特徴量（終値、出来高等）をLSTM入力と互換性のあるテンソル形式にエンコード

3. **LSTMモデルの適応**:
   - 最初のスクリプトの`Net`クラスを、テキストシーケンスではなく金融時系列データを処理できるように修正します。
   - 入力サイズを`vocab_size`ではなく特徴量の数（終値、出来高等）に合わせて調整します。
   - 出力層を連続値（翌日の終値）予測または分類（価格上昇/下降）用に更新します。

4. **モデルの訓練**:
   - 過去データを訓練用、検証用、テスト用に分割します。
   - 最初のスクリプトと同様に、前処理済みデータを使用してLSTMを訓練します。
   - 回帰タスクには平均二乗誤差（MSE）、分類タスクには交差エントロピー損失などの損失関数を使用します。

5. **分析と予測**:
   - 訓練済みLSTMを使用して、最近の過去データに基づいて将来の株価やトレンドを予測します。
   - `matplotlib`を使用して予測値を実際のデータと並べて可視化します。

6. **取引との統合**:
   - 予測値を`place_order`関数での取引判断に活用します。
   - 例：LSTMが価格上昇を一定閾値以上で予測した場合、買い注文を出します。

### コード例：過去データとLSTMの統合

以下は、2つのスクリプトを統合し、過去データの前処理と株価予測向けLSTMの適応に焦点を当てたサンプルコードスニペットです。

```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tigeropen.common.consts import Language, Market, BarPeriod, QuoteRight
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.util.signature_utils import read_private_key
import os
from datetime import datetime

# --- TigerOpen API セットアップ ---
def get_client_config(sandbox=False):
    client_config = TigerOpenClientConfig(sandbox_debug=sandbox)
    client_config.private_key = read_private_key(os.environ.get('TIGER_PEM'))
    client_config.tiger_id = os.environ.get('TIGER_TIGER_ID')
    client_config.account = os.environ.get('TIGER_ACCOUNT')
    client_config.language = Language.zh_CN
    return client_config

def get_history_data(symbol='00700', period=BarPeriod.DAY, begin_time='2024-01-01', end_time=None, limit=100):
    client_config = get_client_config()
    quote_client = QuoteClient(client_config)
    if not end_time:
        end_time = datetime.now().strftime('%Y-%m-%d')
    bars_dict = quote_client.get_bars(
        symbols=[symbol], period=period, begin_time=begin_time, end_time=end_time, limit=limit, right=QuoteRight.BR
    )
    bars = bars_dict.get(symbol, [])
    return pd.DataFrame([{
        'time': bar.time,
        'open': bar.open,
        'high': bar.high,
        'low': bar.low,
        'close': bar.close,
        'volume': bar.volume
    } for bar in bars])

# --- LSTMモデル ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # 翌日終値予測

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # 最終タイムステップを取得
        x = self.l_out(x)
        return x

# --- データ前処理 ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # 訓練用とテスト用に分割
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- 訓練ループ ---
def train_model(model, X_train, y_train, X_test, y_test, num_epochs=50, lr=3e-4):
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    training_loss, validation_loss = [], []
    
    for epoch in range(num_epochs):
        model.train()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        training_loss.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            val_outputs = model(X_test)
            val_loss = criterion(val_outputs, y_test)
            validation_loss.append(val_loss.item())
        
        if epoch % 5 == 0:
            print(f'Epoch {epoch}, Training Loss: {training_loss[-1]:.4f}, Validation Loss: {validation_loss[-1]:.4f}')
    
    return training_loss, validation_loss

# --- メイン実行 ---
if __name__ == '__main__':
    # 過去データ取得
    df = get_history_data(symbol='00700', limit=1000)
    
    # データ準備
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # LSTM初期化と訓練
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # 訓練損失と検証損失をプロット
    plt.figure()
    plt.plot(training_loss, 'r', label='Training Loss')
    plt.plot(validation_loss, 'b', label='Validation Loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.show()
    
    # 予測実行
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # 予測値を逆変換
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # 予測値と実際の値をプロット
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Actual Close Price')
    plt.plot(predicted, 'r', label='Predicted Close Price')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.show()
```

### 主な修正点と注意事項

1. **データ取得**:
   - `get_history_data`関数を使用して特定シンボル（例：Tencentの'00700'）の過去株価データを取得します。
   - データは操作しやすいpandas DataFrameに変換されます。

2. **前処理**:
   - 終値を[0, 1]範囲にスケーリングするため`MinMaxScaler`でデータを正規化します。
   - 翌日終値を予測するため`sequence_length`（例：60日）のシーケンスを作成します。
   - データを訓練用（80%）とテスト用（20%）に分割します。

3. **LSTMモデル**:
   - `StockLSTM`クラスは、`input_size`を調整することで単一特徴量（終値）または複数特徴量（終値、出来高等）を処理できるように適応されています。
   - 出力層は線形層を使用して単一値（翌日終値）を予測します。

4. **訓練**:
   - 訓練ループは株価のような連続値予測に適したMSE損失を使用します。
   - モデルは検証損失を追跡するためテストセットで評価されます。

5. **可視化**:
   - モデルの収束を評価するため、訓練損失と検証損失をプロットします。
   - モデルの性能を評価するため、予測値と実際の終値を比較してプロットします。

### 潜在的な課題と考慮事項

1. **データ品質と量**:
   - 過去データ量（例：`limit=1000`バー）は堅牢なLSTM訓練には不十分な場合があります。より多くのデータ取得またはより短い`sequence_length`の使用を検討してください。
   - 株価データはノイズが多く、LSTMモデルは長期的依存関係や急激な市場変動に苦戦する可能性があります。

2. **特徴量エンジニアリング**:
   - 例では終値のみを使用しています。出来高、移動平均、RSIなどのテクニカル指標といった追加特徴量を含めることでモデル性能を向上できます。
   - 特徴量選択と前処理（欠損値処理、外れ値処理など）が重要です。

3. **モデル複雑性**:
   - LSTMアーキテクチャはシンプル（1層、50隠れユニット）です。複雑な金融データには、より深いモデル、正則化のためのドロップアウト、GRUやTransformerなどの他のアーキテクチャを検討してください。

4. **過学習**:
   - 訓練損失と検証損失を監視し過学習を検出します。必要に応じてドロップアウトや重み減衰を追加してください。

5. **リアルタイム統合**:
   - モデルをリアルタイム取引に使用するには、最近のデータを取得し、前処理して訓練済みLSTMに入力し予測を生成します。
   - 予測を取引戦略（例：予測価格 > 現在価格 + X% の場合買い）と組み合わせます。

6. **API制限**:
   - TigerOpen API資格情報が環境変数（`TIGER_PEM`, `TIGER_TIGER_ID`, `TIGER_ACCOUNT`）に正しく設定されていることを確認してください。
   - 特定シンボルや期間におけるAPIレート制限とデータ可用性に注意してください。

### 出力例
コードが正常に実行されると、以下が表示される可能性があります：
- エポックごとの訓練損失と検証損失（例：`Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`）
- エポックごとの訓練損失と検証損失のプロット（収束状況を示す）
- テストセットにおける予測値と実際の終値の比較プロット（LSTMがトレンドをどの程度捉えているかを示す）

### 次のステップ
- **特徴量強化**: テクニカル指標（MACD、ボリンジャーバンド等）またはX投稿からの感情分析データ（検索経由で利用可能な場合）を組み込む
- **バックテスト**: 収益性を評価するため、過去データを使用してシミュレーション取引環境でLSTM予測をテストする
- **取引統合**: 適切なリスク管理のもと、LSTM予測に基づいて注文を実行するため`place_order`関数を使用する
- **ハイパーパラメータチューニング**: `sequence_length`, `hidden_size`, `num_layers`, 学習率を実験し性能を最適化する

### 実現可能性
はい、過去株価データとLSTMを組み合わせた分析は、アルゴリズム取引で広く使用されている実現可能なアプローチです。ただし、成功は以下に依存します：
- 十分かつクリーンなデータ
- 適切な前処理と特徴量エンジニアリング
- 適切に調整されたLSTMモデル
- 予測に基づいた行動する堅牢な取引戦略

金融市場は本質的にノイズが多く、外部要因（ニュース、マクロ経済イベント等）の影響を受けるため、LSTM予測は注意して使用すべきであり、理想的にはリスク管理を備えたより広範な戦略の一部として活用すべきです。

特定の部分（特徴量追加、バックテスト、リアルタイム取引など）についてさらに深く掘り下げたい場合は、お知らせください！