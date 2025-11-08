---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Python 基本梯度提升範例
translated: true
type: note
---

### 簡單的 Python 梯度提升範例

以下是一個使用 scikit-learn 的 `GradientBoostingRegressor` 來實作 Friedman 梯度提升機器的基礎範例，應用於玩具迴歸資料集。這反映了 2001 年論文中的核心概念：對偽殘差進行樹的序列擬合，並通過縮減進行正則化。

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 步驟 1：生成合成資料（類似論文中的迴歸範例）
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 步驟 2：初始化並訓練 GBM
# 關鍵參數靈感來自論文：n_estimators=1000（多次迭代）、learning_rate=0.1（縮減）、
# max_depth=3（淺層樹作為弱學習器）、subsample=0.5（隨機變體）
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# 步驟 3：預測與評估
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"測試 MSE: {mse:.4f}")

# 步驟 4：繪製特徵重要性（來自論文的可解釋性部分）
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("特徵重要性")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'特徵 {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# 可選：繪製學習曲線（損失 vs. 迭代次數）
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("偏差（損失）vs. 提升迭代次數")
plt.plot(test_score, label="測試偏差")
plt.xlabel("迭代次數")
plt.ylabel("偏差")
plt.legend()
plt.show()
```

### 運作原理（與論文關聯）
- **資料**：帶有噪音的合成迴歸資料，類似論文中的實證測試。
- **模型**：預設使用最小平方損失，將樹擬合到負梯度（殘差）。
- **訓練**：依序添加樹並使用縮減（`learning_rate=0.1`）以防止過度擬合，如論文所建議。
- **評估**：MSE 符合論文對平方誤差的關注；圖表顯示收斂性和重要性（總雜質減少）。
- **執行**：複製貼上到 Jupyter notebook 或 Python 腳本中。需要 `scikit-learn` 和 `matplotlib`。

這是一個實用的起點——scikit-learn 的實作緊密遵循 Friedman 的演算法。如需從頭開始的版本，請告訴我！

[scikit-learn 梯度提升文檔](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)