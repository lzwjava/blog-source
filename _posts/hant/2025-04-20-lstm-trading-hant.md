---
audio: false
generated: true
lang: hant
layout: post
title: 結合歷史數據與長短期記憶網絡
translated: true
type: note
---

結合TigerOpen API的歷史股票數據與LSTM模型進行分析是可行的，也是金融時間序列預測中常見的方法。第二個腳本獲取的歷史股票數據（例如OHLCV柱狀圖）可用於構建訓練LSTM模型的數據集，類似於第一個腳本中的做法。以下我將說明如何整合這兩者，應對潛在挑戰，並提供使用LSTM分析股票數據的高層次方法。

### 整合兩者的高層次方法

1. **獲取歷史數據**：
   - 使用第二個腳本中的`get_history_data`函數獲取歷史股票數據（例如代號'00700'或其他）。
   - 數據包含開盤價、最高價、最低價、收盤價、交易量和時間戳，這些可作為LSTM的特徵。

2. **為LSTM預處理數據**：
   - 將歷史數據轉換為適合LSTM模型的格式。這包括：
     - 標準化數據（例如將價格和交易量縮放到[0, 1]範圍）。
     - 創建歷史數據序列（例如使用過去60天的數據預測下一日的收盤價）。
     - 將特徵（例如收盤價、交易量）編碼為與LSTM輸入兼容的張量格式。

3. **調整LSTM模型**：
   - 修改第一個腳本中的`Net`類別，使其處理金融時間序列數據而非文本序列。
   - 調整輸入大小以匹配特徵數量（例如收盤價、交易量等），而非`vocab_size`。
   - 更新輸出層以預測連續值（例如下一日收盤價）或進行分類（例如價格上漲/下跌）。

4. **訓練模型**：
   - 將歷史數據拆分為訓練集、驗證集和測試集。
   - 使用預處理後的數據訓練LSTM，類似於第一個腳本中的訓練循環。
   - 對於回歸任務使用均方誤差（MSE）損失函數，對於分類任務使用交叉熵損失。

5. **分析與預測**：
   - 使用訓練好的LSTM基於近期歷史數據預測未來股價或趨勢。
   - 使用`matplotlib`將預測結果與實際數據並列可視化。

6. **與交易整合**：
   - 使用預測結果為`place_order`函數中的交易決策提供依據。
   - 例如，若LSTM預測價格上漲超過某個閾值，則下達買入訂單。

### 代碼示例：整合歷史數據與LSTM

以下是整合兩個腳本的示例代碼片段，重點在於預處理歷史數據並調整LSTM用於股價預測。

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

# --- TigerOpen API 設置 ---
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

# --- LSTM 模型 ---
class StockLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=50, num_layers=1):
        super(StockLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, bidirectional=False)
        self.l_out = nn.Linear(in_features=hidden_size, out_features=1)  # 預測下一收盤價

    def forward(self, x):
        x, (h, c) = self.lstm(x)
        x = x[:, -1, :]  # 取最後時間步
        x = self.l_out(x)
        return x

# --- 數據預處理 ---
def prepare_data(df, sequence_length=60, target_col='close'):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[target_col]].values)
    
    X, y = [], []
    for i in range(len(scaled_data) - sequence_length):
        X.append(scaled_data[i:i + sequence_length])
        y.append(scaled_data[i + sequence_length])
    
    X = np.array(X)
    y = np.array(y)
    
    # 拆分為訓練集和測試集
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]
    
    return torch.Tensor(X_train), torch.Tensor(y_train), torch.Tensor(X_test), torch.Tensor(y_test), scaler

# --- 訓練循環 ---
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

# --- 主執行程序 ---
if __name__ == '__main__':
    # 獲取歷史數據
    df = get_history_data(symbol='00700', limit=1000)
    
    # 準備數據
    sequence_length = 60
    X_train, y_train, X_test, y_test, scaler = prepare_data(df, sequence_length=sequence_length, target_col='close')
    
    # 初始化並訓練 LSTM
    model = StockLSTM(input_size=1, hidden_size=50, num_layers=1)
    training_loss, validation_loss = train_model(model, X_train, y_train, X_test, y_test, num_epochs=50)
    
    # 繪製訓練和驗證損失
    plt.figure()
    plt.plot(training_loss, 'r', label='Training Loss')
    plt.plot(validation_loss, 'b', label='Validation Loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('MSE Loss')
    plt.show()
    
    # 進行預測
    model.eval()
    with torch.no_grad():
        predicted = model(X_test).numpy()
    
    # 反轉預測值的標準化
    predicted = scaler.inverse_transform(predicted)
    y_test_actual = scaler.inverse_transform(y_test.numpy())
    
    # 繪製預測與實際值對比
    plt.figure()
    plt.plot(y_test_actual, 'b', label='Actual Close Price')
    plt.plot(predicted, 'r', label='Predicted Close Price')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    plt.show()
```

### 主要修改與注意事項

1. **數據獲取**：
   - 使用`get_history_data`函數獲取指定代號（例如騰訊的'00700'）的歷史股票數據。
   - 數據轉換為pandas DataFrame以便於操作。

2. **預處理**：
   - 使用`MinMaxScaler`將收盤價標準化至[0, 1]範圍。
   - 創建`sequence_length`（例如60天）的序列以預測下一日的收盤價。
   - 數據按80%訓練集和20%測試集的比例拆分。

3. **LSTM模型**：
   - `StockLSTM`類別調整為處理單一特徵（收盤價）或多特徵（例如收盤價、交易量），通過調整`input_size`實現。
   - 輸出層使用線性層預測單一值（下一日收盤價）。

4. **訓練**：
   - 訓練循環使用MSE損失進行回歸，適用於預測連續值如股價。
   - 在測試集上評估模型以追踪驗證損失。

5. **可視化**：
   - 繪製訓練和驗證損失以評估模型收斂情況。
   - 繪製預測與實際收盤價對比圖以評估模型性能。

### 潛在挑戰與考量

1. **數據質量與數量**：
   - 歷史數據量（例如`limit=1000`根柱狀圖）可能不足以進行穩健的LSTM訓練。考慮獲取更多數據或使用較小的`sequence_length`。
   - 股票數據可能存在噪音，LSTM模型可能難以處理長期依賴關係或市場突變。

2. **特徵工程**：
   - 示例僅使用收盤價。加入額外特徵（例如交易量、移動平均線、技術指標如RSI）可提升模型表現。
   - 特徵選擇和預處理（例如處理缺失值、異常值）至關重要。

3. **模型複雜度**：
   - LSTM架構較為簡單（1層，50個隱藏單元）。對於複雜的金融數據，可考慮更深層的模型、使用dropout進行正則化，或其他架構如GRU或Transformer。

4. **過度擬合**：
   - 監控訓練與驗證損失以檢測過度擬合。必要時添加dropout或權重衰減。

5. **實時整合**：
   - 若將模型用於實時交易，需獲取近期數據，預處理後輸入訓練好的LSTM生成預測。
   - 將預測與交易策略結合（例如若預測價格高於當前價格X%則買入）。

6. **API限制**：
   - 確保TigerOpen API憑證正確設置於環境變量中（`TIGER_PEM`、`TIGER_TIGER_ID`、`TIGER_ACCOUNT`）。
   - 注意特定代號或時間段的API速率限制和數據可用性。

### 示例輸出
假設代碼成功運行，您可能看到：
- 控制台輸出顯示每個epoch的訓練和驗證損失（例如`Epoch 0, Training Loss: 0.1234, Validation Loss: 0.1345`）。
- 訓練和驗證損失隨epoch變化的圖表，顯示收斂情況。
- 測試集上預測與實際收盤價的對比圖，展示LSTM捕捉趨勢的能力。

### 後續步驟
- **增強特徵**：納入技術指標（例如MACD、布林帶）或來自X帖文的情緒數據（若可通過搜索獲取）。
- **回測**：在模擬交易環境中使用歷史數據測試LSTM預測，評估盈利能力。
- **交易整合**：使用`place_order`函數基於LSTM預測執行交易，並實施適當的風險管理。
- **超參數調優**：嘗試不同的`sequence_length`、`hidden_size`、`num_layers`和學習率以優化性能。

### 是否可行？
是的，結合歷史股票數據與LSTM進行分析是一種可行的方法，在算法交易中廣泛應用。然而，成功與否取決於：
- 充足且潔淨的數據。
- 適當的預處理和特徵工程。
- 調校良好的LSTM模型。
- 基於預測的穩健交易策略。

金融市場本質上充滿噪音且受外部因素影響（例如新聞、宏觀經濟事件），因此應謹慎使用LSTM預測，最好作為帶有風險控制的更廣泛策略的一部分。

如果您想深入了解任何部分（例如添加特徵、回測或實時交易），請告知！