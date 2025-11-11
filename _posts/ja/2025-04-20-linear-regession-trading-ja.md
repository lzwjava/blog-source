---
audio: false
generated: true
lang: ja
layout: post
title: 線形回帰を用いた取引
translated: true
type: note
---

素晴らしい質問です！ここでは2つのタスクを組み合わせていますね：

1. **TigerOpen APIを使用した過去の株価データ（例：Tencent）の取得**
2. **取得したデータを既存のnumpyベースの線形回帰コードで使用する**

---

## そのまま動作しますか？

**いいえ、直接には動作しません。** 現在のMLコードは、特徴量とラベル（例：人口と利益）を表す数値のnumpy配列として `x_train` と `y_train` を期待しています。しかし、TigerOpen APIは**過去の株価バー**（OHLCVデータ）を返します。これは各タイムスタンプに複数のフィールドを持つ時系列データです。

以下の対応が必要です：

- 株価データを適切な `x_train` と `y_train` 配列に抽出・前処理する
- モデルとコードを株価データの文脈に適応させる（例：前日のデータから終値を予測）

---

## 線形回帰モデル用に株価データを適応させる方法は？

### ステップ1：Tencent（シンボル `'00700'`）の過去データを取得

```python
bars_dict = quote_client.get_bars(
    symbols=['00700'],
    period=BarPeriod.DAY,
    begin_time='2024-01-01',
    end_time=datetime.now().strftime('%Y-%m-%d'),
    limit=100,
    right=QuoteRight.BR
)

bars = bars_dict.get('00700', [])
```

### ステップ2：特徴量とラベルの抽出

シンプルなアプローチ：

- 日付インデックスを `x_train` として使用（例：0, 1, 2, ...）
- 終値を `y_train` として使用

```python
import numpy as np

x_train = np.array([i for i in range(len(bars))])
y_train = np.array([bar.close for bar in bars])
```

別の方法として、前日の終値を特徴量として翌日の終値を予測する、あるいはより高度な特徴量を使用することもできます。

### ステップ3：線形回帰コードを使用

これで `x_train` と `y_train` が数値のnumpy配列になったので、`compute_cost` と `compute_gradient` 関数（現在はゼロまたはゼロ勾配を返している）を修正すればコードは正常に動作するはずです。

---

## 例：compute_costとcompute_gradientの実装

```python
def compute_cost(x, y, w, b):
    m = x.shape[0]
    total_cost = 0.5 * np.sum((w * x + b - y) ** 2) / m
    return total_cost

def compute_gradient(x, y, w, b):
    m = x.shape[0]
    error = w * x + b - y
    dj_dw = np.sum(error * x) / m
    dj_db = np.sum(error) / m
    return dj_dw, dj_db
```

---

## まとめ

- TigerOpen APIで過去の株価データを取得
- 時系列データを数値配列（`x_train`, `y_train`）に変換
- コスト関数と勾配関数を実装または修正
- 勾配降下法とプロットコードが株価データに線形モデルを適合させるように動作

---

## ボーナス：株価のプロット

散布図は日数に対する終値を示し、回帰直線はトレンドに適合します。

---

必要であれば、TigerOpenデータ取得とnumpy線形回帰コードを統合した完全な例を作成するお手伝いをします！お気軽にお声がけください。