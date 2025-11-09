---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: LoRAコードの詳細解説
translated: true
type: note
---

LoRAデモコードを主要な部分に分解し、各部分を詳細に説明します。これにより、LoRAの仕組みを段階的に明確に理解できるようになります。このコードは前回の例に基づいており、PyTorchを使用してシンプルな線形層に対するLoRAを実装しています。

### コード部分 1: LoRA層の定義
```python
import torch
import torch.nn as nn

class LoRALayer(nn.Module):
    def __init__(self, in_features, out_features, rank=4):
        super(LoRALayer, self).__init__()
        # 元の凍結された重み
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # 元の重みを凍結
        # LoRAパラメータ: 低ランク行列AとB
        self.lora_A = nn.Parameter(torch.randn(in_features, rank))
        self.lora_B = nn.Parameter(torch.randn(rank, out_features))
        self.scaling = 1.0  # LoRA更新のスケーリング係数
```

#### 説明
この部分では、LoRA技術を実装する`LoRALayer`クラスを定義しています。以下で行われていることを説明します：

- **インポートとクラス設定**: PyTorch（`torch`）とそのニューラルネットワークモジュール（`nn`）をインポートします。`LoRALayer`クラスは`nn.Module`を継承しており、より大きなモデルに統築可能なPyTorchモジュールとなります。
- **元の線形層**: `self.linear = nn.Linear(in_features, out_features)`は、`in_features`個の入力と`out_features`個の出力を持つ標準的な線形層（ニューラルネットワークにおける全結合層のようなもの）を作成します。これは、適応させたい事前学習済みの重みを表します。
- **重みの凍結**: `self.linear.weight.requires_grad = False`は、線形層の元の重みを凍結し、学習中に更新されないようにします。これは、大規模な事前学習モデルを変更することを避けるというLoRAの効率性の鍵となります。
- **LoRAパラメータ**: `self.lora_A`と`self.lora_B`は低ランク行列です。`lora_A`の形状は`(in_features, rank)`、`lora_B`の形状は`(rank, out_features)`です。`rank`パラメータ（デフォルト=4）はこれらの行列のサイズを制御し、元の重み行列（形状`in_features x out_features`）よりもはるかに小さく保ちます。これらの行列は学習可能（`nn.Parameter`）で、乱数値（`torch.randn`）で初期化されます。
- **スケーリング係数**: `self.scaling = 1.0`は、適応の強さを微調整できるハイパーパラメータです。

この設定により、学習中は小さな`lora_A`行列と`lora_B`行列のみが更新され、学習可能なパラメータ数を劇的に削減します。

---

### コード部分 2: LoRAの順伝播
```python
    def forward(self, x):
        # 元の線形変換 + LoRA調整
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment
```

#### 説明
この部分では、`LoRALayer`の順伝播を定義しており、層の出力を計算します：

- **入力**: 入力`x`は形状`(batch_size, in_features)`のテンソルで、バッチの入力データを表します。
- **元の出力**: `original = self.linear(x)`は、凍結された線形層の出力を計算し、事前学習済みの重みを入力に適用します。
- **LoRA調整項**: `torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)`という項が低ランク適応を計算します。まず、`x`に`lora_A`（形状`in_features x rank`）を乗算して、形状`(batch_size, rank)`のテンソルを生成します。次に、これに`lora_B`（形状`rank x out_features`）を乗算して、形状`(batch_size, out_features)`のテンソル（元の出力と同じ形状）を生成します。この調整項がタスク固有の更新を表します。
- **スケーリングと結合**: 調整項は`self.scaling`でスケーリングされ、元の出力に加算されて最終的な出力を生成します。これにより、モデルは事前学習された知識を保持しつつ、タスク固有の適応を取り込むことができます。

低ランク構造（`rank`は小さい、例えば4）により、調整項はフルの重み行列を更新する場合と比較して、計算コストが低く、パラメータ効率が良くなります。

---

### コード部分 3: トイデータセットと学習
```python
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # ランダムな入力特徴量
    y = torch.randn(n_samples, 10)  # ランダムな目標出力
    return X, y

def train_model(model, X, y, epochs=10, lr=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.Adam([param for param in model.parameters() if param.requires_grad], lr=lr)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
```

#### 説明
この部分は、トイデータセットを作成し、LoRA適応されたモデルを学習します：

- **トイデータセット**: `create_toy_dataset`関数は、デモ用の合成データを生成します。`X`は形状`(1000, 64)`のテンソル（1000サンプル、64特徴量）、`y`は形状`(1000, 10)`のテンソル（1000サンプル、10出力次元）です。これらは入出力ペアをシミュレートするためのランダムなテンソルです。
- **学習関数**: `train_model`関数はシンプルな学習ループを設定します：
  - **損失関数**: `nn.MSELoss()`は平均二乗誤差を損失として定義し、この回帰のようなタスクに適しています。
  - **オプティマイザ**: `optim.Adam`は学習可能なパラメータ（`param.requires_grad`が`True`のもの）、すなわち`lora_A`と`lora_B`のみを最適化します。凍結された`linear.weight`は除外され、効率性が確保されます。
  - **学習ループ**: 各エポックで、モデルは出力を計算し、損失を算出し、誤差逆伝播（`loss.backward()`）を実行し、LoRAパラメータを更新（`optimizer.step()`）します。損失は学習の進捗を監視するために表示されます。

この設定は、LoRAが低ランク行列のみをファインチューニングし、プロセスを軽量に保つ方法を示しています。

---

### コード部分 4: メイン実行とパラメータ数
```python
def main():
    # 再現性のために乱数シードを設定
    torch.manual_seed(42)
    
    # トイデータセットを作成
    X, y = create_toy_dataset()
    
    # LoRAでモデルを初期化
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # 学習可能なパラメータを数える
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # モデルを学習
    train_model(model, X, y)

if __name__ == "__main__":
    main()
```

#### 説明
この部分はすべてをまとめ、LoRAの効率性を強調します：

- **乱数シード**: `torch.manual_seed(42)`は、乱数初期化の再現性を確保します。
- **データセットとモデル**: トイデータセットが作成され、`in_features=64`、`out_features=10`、`rank=4`で`LoRALayer`が初期化されます。
- **パラメータ数**: コードは以下を計算します：
  - **学習可能なパラメータ**: `lora_A`（64 × 4 = 256）と`lora_B`（4 × 10 = 40）のみで、合計296パラメータ。
  - **総パラメータ数**: 凍結された`linear.weight`（64 × 10 = 640）と`linear.bias`（10）、およびLoRAパラメータを含み、合計946パラメータ。
  - これはLoRAの効率性を示しています：フルのファインチューニングでは100%が学習可能ですが、ここでは約31%（296/946）のみが学習可能です。
- **学習**: `train_model`関数が呼び出され、トイデータセットでLoRAパラメータがファインチューニングされます。

これを実行すると、学習可能なパラメータ数が総数よりもはるかに少なく、低ランク更新によりモデルが迅速に学習することがわかります。

---

### コードの実行方法
実行にはPyTorchのインストール（`pip install torch`）が必要です。完全なコードを`.py`ファイルとして保存し、実行してください。出力にはパラメータ数と10エポックにわたる学習損失が表示され、ファインチューニングにおけるLoRAの効率性が実証されます。

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

どの部分についてより深く掘り下げたい場合や、例を変更したい場合はお知らせください！