---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: PyTorchによるLoRA実装例
translated: true
type: note
---

以下は、シンプルなニューラルネットワークをファインチューニングするためにPyTorchを使用してLoRA（Low-Rank Adaptation）を実装する方法を示すPythonコード例です。この例は、事前学習済みの線形層をLoRAで適応させることに焦点を当て、元の重みを凍結したまま低ランクの更新行列を導入します。コードには、トイデータセットを使った基本的なセットアップと、概念を説明するための最小限のトレーニングループが含まれています。

<xaiArtifact artifact_id="1327e99b-24b5-4b0d-9ffd-5b4c2d1472af" artifact_version_id="4053525d-2225-4913-a3b9-b7d66b48daea" title="lora_demo.py" contentType="text/python">
import torch
import torch.nn as nn
import torch.optim as optim

# LoRA層を定義
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

    def forward(self, x):
        # 元の線形変換 + LoRA調整
        original = self.linear(x)
        lora_adjustment = self.scaling * torch.matmul(torch.matmul(x, self.lora_A), self.lora_B)
        return original + lora_adjustment

# デモンストレーション用のトイデータセット
def create_toy_dataset(n_samples=1000):
    X = torch.randn(n_samples, 64)  # ランダムな入力特徴量
    y = torch.randn(n_samples, 10)  # ランダムなターゲット出力
    return X, y

# トレーニング関数
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

# メイン実行
def main():
    # 再現性のためにランダムシードを設定
    torch.manual_seed(42)
    
    # トイデータセットを作成
    X, y = create_toy_dataset()
    
    # LoRAでモデルを初期化
    model = LoRALayer(in_features=64, out_features=10, rank=4)
    
    # 学習可能なパラメータをカウント
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params}")
    print(f"Total parameters: {total_params}")
    
    # モデルをトレーニング
    train_model(model, X, y)

if __name__ == "__main__":
    main()
</xaiArtifact>

このコードは、標準的な線形層を低ランク適応行列（`lora_A`と`lora_B`）でラップする`LoRALayer`を定義しています。元の重みは凍結され、トレーニング中はLoRAパラメータのみが更新されます。トイデータセットとトレーニングループは、LoRAが学習可能なパラメータ数を削減しつつ、ファインチューニングを可能にする方法を示しています。PyTorchがインストールされていれば、このコードを実行してトレーニングプロセスとパラメータ効率を確認できます。

[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)