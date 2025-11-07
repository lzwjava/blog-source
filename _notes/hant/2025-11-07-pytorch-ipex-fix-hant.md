---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-4.5-sonnet
title: 修復 PyTorch 與 IPEX 相容性問題
translated: true
---

你遇到兩個問題：

1. **版本不相容**：Intel Extension for PyTorch (IPEX) 需要 PyTorch 2.8.*，但你安裝的是 PyTorch 2.7.1+cu126（CUDA 版本）。

2. **IPEX 中的錯誤**：IPEX 庫本身存在一個錯誤 - 它試圖調用不存在的 `os.exit(127)`。正確的函數應該是 `sys.exit(127)`。

以下是解決方法：

## 解決方案 1：安裝相容的 PyTorch 版本

```bash
# 解除安裝目前的 PyTorch
pip uninstall torch torchvision torchaudio

# 安裝 PyTorch 2.8.*（CPU 版本，因為你使用 Intel GPU）
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# 重新安裝 IPEX
pip install intel-extension-for-pytorch
```

## 解決方案 2：升級至最新版本

```bash
# 將 PyTorch 和 IPEX 升級至最新的相容版本
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install --upgrade intel-extension-for-pytorch
```

## 解決方案 3：如果你需要 CUDA PyTorch

如果你確實需要 CUDA 支援（用於 NVIDIA GPU），那麼你根本不應該使用 Intel Extension for PyTorch - 它們服務於不同的硬體。Intel Extension 適用於 Intel GPU（Arc、Flex、Max）和帶有優化的 CPU。

**選擇其中一項：**
- **適用於 Intel GPU/CPU**：使用 PyTorch CPU 版本 + IPEX
- **適用於 NVIDIA GPU**：使用 PyTorch CUDA 版本（不需要 IPEX）

## 關於該錯誤的說明

`os.exit()` 錯誤表明你可能使用的是過時版本的 IPEX。最新版本應該已經修復了這個問題。在解決 PyTorch 版本不相容問題後，請確保安裝最新的 IPEX 版本。

你實際試圖使用什麼硬體 - Intel GPU、Intel CPU 還是 NVIDIA GPU？