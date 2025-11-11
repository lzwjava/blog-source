---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: TinyGrad軽量機械学習ライブラリ
translated: true
type: note
---

### TinyGradの紹介
TinyGradは、教育とシンプルさを目的としたPythonの軽量でミニマルな機械学習および深層学習ライブラリです。PyTorchのように自動微分（autograd）を実装していますが、はるかに小さく約1,000行のコードです。大規模なライブラリのオーバーヘッドなしでMLの概念を学んだり、小さなモデルを構築したりするのに最適です。テンソル、ニューラルネットワーク、基本的な演算をサポートし、PyTorchやMetalを介したGPUアクセラレーションもサポートしています。

公式リポジトリはこちらです: [tinygrad GitHub](https://github.com/geohot/tinygrad)。注意: これは実験的であり、本番環境での使用においてPyTorchやTensorFlowほど堅牢ではありません。

### インストール
pip経由でTinyGradをインストールします:

```bash
pip install tinygrad
```

最小限の依存関係ですが、一部のバックエンドでオプションとしてPyTorchを使用します。GPUサポートのためには、PyTorchがインストールされていることを確認してください。

### 基本的な使用方法
インポートとコンテキストの設定から始めます（TinyGradでは、勾配が異なる方法で計算されるため、トレーニング中か推論中かを指定する必要があります）。

#### インポートとコンテキスト
```python
from tinygrad import Tensor
from tinygrad.nn import Linear, BatchNorm2d  # ニューラルネット用

# コンテキストの設定: トレーニング（勾配用）または推論
Tensor.training = True  # 勾配追跡を有効化
```

#### テンソルの作成と操作
テンソルは、NumPy配列やPyTorchテンソルに似たコアデータ構造です。

```python
# リスト、NumPy配列、または形状からテンソルを作成
a = Tensor([1, 2, 3])          # リストから
b = Tensor.zeros(3)            # 形状(3,)のゼロテンソル
c = Tensor.rand(2, 3)          # 形状(2, 3)のランダムテンソル

# 基本的な演算
d = a + b                      # 要素ごとの加算
e = d * 2                      # スカラー乗算
f = a @ Tensor([[1], [2], [3]])  # 行列乗算 (aは1D、暗黙的に転置)

print(e.numpy())               # 印刷またはさらに使用するためにNumPyに変換
```

#### 自動微分（バックプロパゲーション）
TinyGradは連鎖律を使用して自動的に勾配を計算します。

```python
# 勾配追跡を有効化
Tensor.training = True

x = Tensor([1.0, 2.0, 3.0])
y = (x * 2).sum()             # 何らかの演算; yはスカラー

y.backward()                  # 勾配を計算
print(x.grad.numpy())         # xに関する勾配: [2, 2, 2]になるはず
```

NumPyへのエクスポートには、`.numpy()`を使用します。リセットされない限り、勾配は蓄積されます。

#### ニューラルネットワークとトレーニング
TinyGradには基本的なレイヤーとオプティマイザーが含まれています。以下は単純なMLPの例です:

```python
from tinygrad.nn import Linear, optim

# 単純なモデルを定義（例: 線形層）
model = Linear(3, 1)          # 入力3、出力1

# ダミーデータ
x = Tensor.rand(4, 3)         # 4サンプルのバッチ、3特徴量
y_true = Tensor.rand(4, 1)    # ターゲット

# 順伝播
pred = model(x).sigmoid()      # 二値分類を仮定

# 損失（例: 平均二乗誤差）
loss = ((pred - y_true) ** 2).mean()

# バックプロパゲーションと最適化
loss.backward()
optim.Adam([model], lr=0.01).step()
```

畳み込みネットワークには、`tinygrad.nn`の`Conv2d`を使用します。

### 高度な機能
- **損失関数と活性化関数**: `tinygrad.nn`で利用可能（例: `sigmoid`, `relu`, `cross_entropy`）。
- **オプティマイザー**: `tinygrad.nn.optim`の`SGD`, `Adam`。
- **レイヤー**: `Linear`, `Conv2d`, `BatchNorm`など。
- **保存/読み込み**: モデルは状態辞書として保存可能（PyTorchと同様）。
- **GPU/アクセラレーション**: TinyGradはPyTorchバックエンドを介してGPUで実行可能: `TESOR_SET_DEVICE='cuda:0'`。macOSではMetalもサポート。
- **ビジョン/ノイズ除去の例**: リポジトリにはMNISTでのResNetのトレーニングなどの例があります。

完全な例については、GitHubリポジトリの`examples/`フォルダ（画像分類や強化学習など）を確認してください。

### 例: ニューラルネットワークのトレーニング
XORでネットワークをトレーニングするための完全で単純なスクリプトです:

```python
from tinygrad import Tensor
from tinygrad.nn import Linear, optim

# データ
X = Tensor([[0,0], [0,1], [1,0], [1,1]])
Y = Tensor([[0], [1], [1], [0]])

# モデル
model = Linear(2, 1)
opt = optim.Adam([model], lr=0.1)

Tensor.training = True

for epoch in range(1000):
    pred = model(X).sigmoid()
    loss = ((pred - Y) ** 2).mean()
    loss.backward()
    opt.step()
    opt.zero_grad()

# テスト
print(model(Tensor([[0,0]])))  # ~0になるはず
```

### ヒントと注意点
- **モード切り替え**: トレーニング時は常に`Tensor.training = True`を設定し、推論時は勾配計算を避けるために`False`に切り替えてください。
- **形状の取り扱い**: テンソルはNumPyのようなブロードキャストに従いますが、小さなモデルでのオーバーフローに注意してください。
- **デバッグ**: 値の検査に`.numpy()`を使用します。何かが失敗した場合は、形状の不一致を確認してください。
- **パフォーマンス**: 大規模なモデルでは遅いです。本番環境ではPyTorchを使用してください。
- **アップデート**: TinyGradは急速に進化します。最新バージョンについてはリポジトリを確認してください。

詳細については、[docs/README.md](https://github.com/geohot/tinygrad/blob/master/README.md)を訪問するか、ローカルで例を実行してください。特定のユースケースがある場合は、詳細を提供していただければ、より適切なアドバイスができます！