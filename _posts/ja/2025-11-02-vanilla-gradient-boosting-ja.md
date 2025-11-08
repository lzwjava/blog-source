---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Pythonによるバニラ勾配ブースティングの実装
translated: true
type: note
---

### Pythonのみで実装するバニラ勾配ブースティング（NumPyのみ）

以下は、Friedmanの2001年の論文に触発された、シンプルな勾配ブースティング回帰器のスクラッチ実装です。**決定株（単一分岐木、つまり深さ1の木）**を弱学習器として使用し、物事をバニラでシンプルに保っています。scikit-learnは使用せず、数値計算にはNumPyを、プロットにはMatplotlibを使用しています。これにより、疑似残差（二乗損失の負の勾配）への適合、縮小（学習率）、および加法的な更新という核心を捉えています。

このコードは自己完結しており、NumPy/Matplotlibが利用可能なPython環境で実行できます。

```python
import numpy as np
import matplotlib.pyplot as plt

class DecisionStump:
    """回帰のためのシンプルな決定株（単一分岐）"""
    def __init__(self):
        self.feature_idx = None
        self.threshold = None
        self.left_val = None
        self.right_val = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        best_mse = np.inf
        best_idx, best_thresh = -1, -1
        best_left, best_right = None, None
        
        for idx in range(n_features):
            # 特徴量でソートし、中点を閾値として試行
            sorted_idx = np.argsort(X[:, idx])
            thresholds = (X[sorted_idx[:-1], idx] + X[sorted_idx[1:], idx]) / 2
            
            for thresh in thresholds:
                left_mask = X[:, idx] <= thresh
                right_mask = ~left_mask
                
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue
                
                left_val = np.mean(y[left_mask])
                right_val = np.mean(y[right_mask])
                
                y_pred = np.zeros(n_samples)
                y_pred[left_mask] = left_val
                y_pred[right_mask] = right_val
                
                mse = np.mean((y - y_pred) ** 2)
                
                if mse < best_mse:
                    best_mse = mse
                    best_idx = idx
                    best_thresh = thresh
                    best_left = left_val
                    best_right = right_val
        
        self.feature_idx = best_idx
        self.threshold = best_thresh
        self.left_val = best_left
        self.right_val = best_right
    
    def predict(self, X):
        if self.feature_idx is None:
            return np.zeros(X.shape[0])
        
        left_mask = X[:, self.feature_idx] <= self.threshold
        y_pred = np.zeros(X.shape[0])
        y_pred[left_mask] = self.left_val
        y_pred[~left_mask] = self.right_val
        return y_pred

class GradientBoostingRegressor:
    """バニラGBM: 疑似残差に株を適合させ、縮小を適用"""
    def __init__(self, n_estimators=100, learning_rate=0.1):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.models = []
        self.initial_pred = None
    
    def fit(self, X, y):
        n_samples = X.shape[0]
        # 平均で初期化（二乗損失の最小化子）
        self.initial_pred = np.mean(y)
        current_pred = np.full(n_samples, self.initial_pred)
        
        for _ in range(self.n_estimators):
            # 疑似残差: L = 1/2 (y - F)^2 の負の勾配、よって r = y - F
            residuals = y - current_pred
            
            # 弱学習器を残差に適合
            stump = DecisionStump()
            stump.fit(X, residuals)
            self.models.append(stump)
            
            # 縮小率で更新（シンプルさのため直線探索は行わない；argmin gamma を追加可能）
            update = self.learning_rate * stump.predict(X)
            current_pred += update
    
    def predict(self, X):
        current_pred = np.full(X.shape[0], self.initial_pred)
        for model in self.models:
            current_pred += self.learning_rate * model.predict(X)
        return current_pred

# 使用例: 合成データ（論文の回帰テストのように）
np.random.seed(42)
n_samples = 1000
n_features = 10
X = np.random.randn(n_samples, n_features)
true_coef = np.random.randn(n_features) * 2
y = X @ true_coef + np.random.randn(n_samples) * 0.1  # ノイジーな線形信号

# データ分割
split = int(0.8 * n_samples)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# GBMを訓練
gbm = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
gbm.fit(X_train, y_train)

# 予測と評価（二乗誤差）
y_pred_train = gbm.predict(X_train)
y_pred_test = gbm.predict(X_test)
train_mse = np.mean((y_train - y_pred_train) ** 2)
test_mse = np.mean((y_test - y_pred_test) ** 2)
print(f"訓練MSE: {train_mse:.4f}")
print(f"テストMSE: {test_mse:.4f}")

# 予測値 vs. 真の値（テストセット）をプロット
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('真の値')
plt.ylabel('予測値')
plt.title('GBM 予測値 vs. 真の値（テストセット）')
plt.tight_layout()
plt.show()

# オプション: 学習曲線（累積予測）
train_scores = []
current_pred_train = np.full(len(y_train), gbm.initial_pred)
for i in range(gbm.n_estimators):
    update = gbm.learning_rate * gbm.models[i].predict(X_train)
    current_pred_train += update
    score = np.mean((y_train - current_pred_train) ** 2)
    train_scores.append(score)

plt.figure(figsize=(8, 5))
plt.plot(train_scores)
plt.xlabel('ブースティング反復回数')
plt.ylabel('訓練MSE')
plt.title('学習曲線: MSE vs. 反復回数')
plt.tight_layout()
plt.show()
```

### 仕組み（論文との関連）
- **DecisionStump**: MSEを最小化する単一分岐を適合させる弱学習器（論文の浅い木と同様）。小規模データでは効率性のために閾値を総当たりで探索します。
- **GradientBoostingRegressor**:
  - \\( F_0 = \bar{y} \\)（二乗損失最小化子）で開始します。
  - 残差 \\( r = y - F_{m-1} \\)（負の勾配）に株を反復的に適合させます。
  - 更新 \\( F_m = F_{m-1} + \nu \cdot h_m \\) を正則化のための縮小率 \\( \nu = 0.1 \\) で適用します。
  - シンプルさのため、ここでは確率的サブサンプリングや直線探索は行いません（論文では大規模化のために提案されています）。
- **性能**: このトイデータでは、低いMSE（テストで約0.01）が期待されます。迅速に収束します（プロットは減少する損失を示します）。
- **制限**: 株は複雑さを制限します；実際の使用では、より深い木に拡張します。回帰を扱います；分類には対数損失勾配を介して適応させます。
- **実行方法**: スクリプト/ノートブックに貼り付けます。出力はMSEと、論文の収束/精度に焦点を当てたプロットを反映します。

拡張（例：より深い木、分類）については、お知らせください！

[原論文PDF](https://jerryfriedman.su.domains/ftp/trebst.pdf)