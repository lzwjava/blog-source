---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: PyTorch 可學習權重參數
translated: true
type: note
---

`torch.nn.Parameter` 是 PyTorch 中 `torch.Tensor` 的一個子類，專門用於表示神經網絡模組中的可學習參數。其主要用途是當張量被賦值為 `torch.nn.Module` 的屬性時，能自動將其註冊為模組參數，使其可透過 `module.parameters()` 或 `module.named_parameters()` 等方法存取。這有助於區分可訓練權重（例如用於層的權重）與常規張量，避免臨時計算（如 RNN 中的緩存狀態）被錯誤當作參數處理。

### 主要特性
- **自動註冊**：當你將 `Parameter` 賦值給模組時（例如在自定義模組的 `__init__` 中寫入 `self.weight = nn.Parameter(torch.randn(3, 3))`），它會自動加入模組的參數列表，無需額外代碼。
- **梯度追蹤**：預設情況下 `requires_grad=True`，因此會參與反向傳播。即使在 `torch.no_grad()` 上下文內也是如此——若需更精細控制，請使用 autograd 的局部禁用功能。
- **屬性**：它繼承所有 `Tensor` 屬性，除特殊模組行為外不新增任何屬性。

### 基本用法
以下是一個自定義模組的簡單範例：

```python
import torch
import torch.nn as nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()
        # 這會自動註冊為參數
        self.weight = nn.Parameter(torch.randn(2, 3))
        # 普通張量不會被註冊
        self.bias = torch.zeros(3)

    def forward(self, x):
        return x @ self.weight + self.bias

model = MyModule()
print(list(model.parameters()))  # 輸出：[Parameter containing: tensor(...)]
```

更多詳細資訊請查閱官方文檔：[Parameter — PyTorch 2.9 documentation](https://pytorch.org/docs/stable/generated/torch.nn.parameter.Parameter.html)