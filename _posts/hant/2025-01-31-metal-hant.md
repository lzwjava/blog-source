---
audio: false
generated: true
lang: hant
layout: post
title: 蘋果金屬性能
translated: true
---

以下是使用 PyTorch 測試 Metal（GPU）性能的腳本。

```python
import torch
import argparse
import time

parser = argparse.ArgumentParser(description="Test torch with MPS or CPU.")
parser.add_argument("--device", type=str, default="mps", choices=["mps", "cpu"], help="Device to use (mps or cpu)")
args = parser.parse_args()

if args.device == "mps":
    if torch.backends.mps.is_available():
        print("Metal is available")
        device = torch.device("mps")
    else:
        print("Metal is not available, using CPU instead")
        device = torch.device("cpu")
elif args.device == "cpu":
    device = torch.device("cpu")
    print("Using CPU")
else:
    print("Invalid device specified, using CPU instead")
    device = torch.device("cpu")

# Create a tensor and move it to the specified device
x = torch.randn(5000, 5000, device=device)
y = torch.randn(5000, 5000, device=device)

# Perform a more complex computation
start_time = time.time()
result = torch.matmul(x, y)
for _ in range(10):
    result = torch.matmul(result, y)
end_time = time.time()

# Print the result
print(result)
print(f"Time taken: {end_time - start_time:.4f} seconds")
```

結果顯示，MPS 比 CPU 快得多。在 MPS 上的執行時間僅為 CPU 時間的約 0.2%。

```bash
% python scripts/test_metal.py --device cpu
Time taken: 2.8784 seconds

% python scripts/test_metal.py --device mps
Time taken: 0.0061 seconds
```