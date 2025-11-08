---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PyTorchの学習可能重みパラメータ
translated: true
type: note
---

`torch.nn.Parameter`は、PyTorchにおける`torch.Tensor`のサブクラスであり、ニューラルネットワークモジュールの学習可能なパラメータを表現するために特別に設計されています。その主な目的は、テンソルが`torch.nn.Module`の属性として割り当てられたときに、それらを自動的にモジュールパラメータとして登録し、`module.parameters()`や`module.named_parameters()`などのメソッドでアクセス可能にすることです。これにより、トレーニング可能な重み（例：レイヤーの重み）と通常のテンソルを区別し、一時的な計算（RNNのキャッシュ状態など）が誤ってパラメータとして扱われるのを防ぎます。

### 主な特徴
- **自動登録**: カスタムモジュールの`__init__`内で`Parameter`をモジュールに割り当てると（例：`self.weight = nn.Parameter(torch.randn(3, 3))`）、追加のコードなしでモジュールのパラメータリストに追加されます。
- **勾配追跡**: デフォルトで`requires_grad=True`であるため、バックプロパゲーションに参加します。これは`torch.no_grad()`コンテキスト内でも維持されます。より細かい制御にはautogradのローカル無効化を使用してください。
- **属性**: すべての`Tensor`プロパティを継承しますが、特別なモジュール動作以外に新しい属性は追加しません。

### 基本的な使用方法
カスタムモジュールでの簡単な例を以下に示します：

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # これは自動的にパラメータとして登録されます
        self.weight = nn.Parameter(torch.randn(2, 3))
        # 通常のテンソルは登録されません
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # 出力: [Parameter containing: tensor(...)]
```

詳細については、公式ドキュメントを参照してください：[Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)