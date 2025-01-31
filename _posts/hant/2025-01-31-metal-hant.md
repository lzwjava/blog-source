---
audio: false
lang: hant
layout: post
title: 金屬
translated: true
---

以下是一個使用 PyTorch 測試 Metal (GPU) 性能的腳本。

```python
import torch
import argparse
import time

parser = argparse.ArgumentParser(description="使用 MPS 或 CPU 測試 torch。")
parser.add_argument("--device", type=str, default="mps", choices=["mps", "cpu"], help="使用的設備 (mps 或 cpu)")
args = parser.parse_args()

if args.device == "mps":
    if torch.backends.mps.is_available():
        print("Metal 可用")
        device = torch.device("mps")
    else:
        print("Metal 不可用，改用 CPU")
        device = torch.device("cpu")
elif args.device == "cpu":
    device = torch.device("cpu")
    print("使用 CPU")
else:
    print("指定的設備無效，改用 CPU")
    device = torch.device("cpu")

# 創建一個張量並將其移動到指定的設備
x = torch.randn(5000, 5000, device=device)
y = torch.randn(5000, 5000, device=device)

# 進行較複雜的計算
start_time = time.time()
result = torch.matmul(x, y)
for _ in range(10):
    result = torch.matmul(result, y)
end_time = time.time()

# 打印結果
print(result)
print(f"所需時間: {end_time - start_time:.4f} 秒")
```

結果顯示 MPS 比 CPU 快得多。在 MPS 上的執行時間僅為 CPU 時間的約 0.2%。

```bash
% python scripts/test_metal.py --device cpu
所需時間: 2.8784 秒

% python scripts/test_metal.py --device mps
所需時間: 0.0061 秒
```