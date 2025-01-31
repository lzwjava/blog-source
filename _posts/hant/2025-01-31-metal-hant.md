---
audio: false
lang: hant
layout: post
title: 金屬
translated: true
---

以下是一個使用 PyTorch 测試 Metal（GPU）性能的腳本。

```python
import torch
import argparse
import time

parser = argparse.ArgumentParser(description="使用 MPS 或 CPU 测试 torch。")
parser.add_argument("--device", type=str, default="mps", choices=["mps", "cpu"], help="使用的设备 (mps 或 cpu)")
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
    print("指定的设备无效，改用 CPU")
    device = torch.device("cpu")

# 创建一个张量并将其移动到指定的设备
x = torch.randn(5000, 5000, device=device)
y = torch.randn(5000, 5000, device=device)

# 执行更复杂的计算
start_time = time.time()
result = torch.matmul(x, y)
for _ in range(10):
    result = torch.matmul(result, y)
end_time = time.time()

# 打印结果
print(result)
print(f"所用时间: {end_time - start_time:.4f} 秒")
```

结果表明 MPS 显著快于 CPU。在 MPS 上的执行时间仅为 CPU 时间的约 0.2%。

```bash
% python scripts/test_metal.py --device cpu
所用时间: 2.8784 秒

% python scripts/test_metal.py --device mps
所用时间: 0.0061 秒
```