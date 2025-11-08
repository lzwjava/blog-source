---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Pythonでの基本的な勾配ブースティングの例
translated: true
type: note
---

### Pythonでの単純な勾配ブースティングの例

以下は、scikit-learnの`GradientBoostingRegressor`を使用して、トイ回帰データセットにFriedmanの勾配ブースティングマシンを実装する基本的な例です。これは2001年の論文の核心的なアイデア（疑似残差へのツリーの逐次適合、正則化のための縮小）を反映しています。

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# ステップ1: 合成データの生成（論文の回帰例と同様）
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ステップ2: GBMの初期化と学習
# 論文に基づく主要パラメータ: n_estimators=1000（多数の反復）、learning_rate=0.1（縮小）、
# max_depth=3（弱学習器としての浅いツリー）、subsample=0.5（確率的バリアント）
gbm = GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.5,
    random_state=42
)
gbm.fit(X_train, y_train)

# ステップ3: 予測と評価
y_pred = gbm.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"テストMSE: {mse:.4f}")

# ステップ4: 特徴量重要度のプロット（論文の解釈可能性セクションから）
importances = gbm.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8, 5))
plt.title("特徴量重要度")
plt.bar(range(X.shape[1]), importances[indices])
plt.xticks(range(X.shape[1]), [f'特徴量 {i}' for i in indices], rotation=45)
plt.tight_layout()
plt.show()

# オプション: 学習曲線のプロット（損失 vs 反復回数）
test_score = np.zeros((gbm.n_estimators,), dtype=np.float64)
for i, y_pred in enumerate(gbm.staged_predict(X_test)):
    test_score[i] = gbm.loss_(y_test, y_pred)
plt.figure(figsize=(8, 5))
plt.title("逸脱度（損失） vs ブースティング反復回数")
plt.plot(test_score, label="テスト逸脱度")
plt.xlabel("反復回数")
plt.ylabel("逸脱度")
plt.legend()
plt.show()
```

### 動作の仕組み（論文との関連）
- **データ**: ノイズを含む合成回帰データ。論文の実証テストと同様。
- **モデル**: デフォルトで最小二乗損失を使用し、負の勾配（残差）にツリーを適合。
- **学習**: 過学習を防ぐための縮小（`learning_rate=0.1`）を適用しながらツリーを逐次追加。論文で推奨された方法。
- **評価**: 論文の二乗誤差に焦点を合わせたMSE。プロットは収束と重要度（不純度減少の総和）を示す。
- **実行方法**: Jupyter notebookやPythonスクリプトにコピー＆ペースト。`scikit-learn`と`matplotlib`が必要。

これは実用的な出発点です。scikit-learnの実装はFriedmanのアルゴリズムに密接に従っています。スクラッチからの実装バージョンが必要な場合は、お知らせください！

[scikit-learn Gradient Boosting Docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)