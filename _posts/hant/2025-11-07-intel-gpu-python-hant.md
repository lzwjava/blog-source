---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-4.5-sonnet
title: 英特爾 GPU 與 Python 計算
translated: true
type: note
---

以下是如何設定和使用 Intel oneAPI 搭配 Python 進行 GPU 運算：

## 安裝

```bash
# 安裝 Intel Extension for PyTorch（包含 oneAPI 運行環境）
pip install intel-extension-for-pytorch

# 或安裝完整的 oneAPI Base Toolkit（更全面）
# 下載網址：https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html
```

## Python 範例## 安裝指令

```bash
# 安裝 Intel Extension for PyTorch（推薦用於您的系統）
pip install torch torchvision torchaudio intel-extension-for-pytorch

# 安裝 dpctl 以進行底層控制
pip install dpctl dpnp

# 安裝 Intel 優化的 scikit-learn
pip install scikit-learn-intelex

# 驗證安裝
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available() if hasattr(torch, 'xpu') else False)"
```

## 重點說明：

1. **裝置命名**：Intel 在 PyTorch 中使用 `xpu` 而非 CUDA 的 `cuda`
2. **相容性**：您的 Intel UHD Graphics 應該可以運作，但效能會比獨立 GPU 有限
3. **安裝**：Intel Extension for PyTorch 是最容易開始使用的方式

## 快速測試：

儲存這個簡單測試：

```python
import torch
import intel_extension_for_pytorch as ipex

print(f"PyTorch version: {torch.__version__}")
print(f"IPEX version: {ipex.__version__}")

if hasattr(torch, 'xpu') and torch.xpu.is_available():
    print(f"✓ Intel GPU available: {torch.xpu.get_device_name(0)}")
    
    # 簡單計算
    x = torch.randn(100, 100, device='xpu')
    y = torch.randn(100, 100, device='xpu')
    z = x @ y
    print(f"✓ Successfully computed on GPU")
else:
    print("✗ Intel GPU not detected")
```

執行指令：`python test_intel_gpu.py`

注意：您的整合式 Intel UHD Graphics 運算能力有限，與獨立 GPU 相比效能較低，因此不要預期能達到 NVIDIA 等級的效能。它仍然適用於學習和輕量 GPU 運算任務。