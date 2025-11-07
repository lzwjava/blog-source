---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-4.5-sonnet
title: 為 PyTorch 啟用 Intel GPU 支援
translated: true
---

進展良好！PyTorch 與 IPEX 現已協同運作。不過，您的系統尚未啟用 Intel GPU 支援。讓我協助您了解當前狀況及解決方法：

## 目前狀態
- ✓ PyTorch + IPEX 已正確安裝
- ✗ Intel GPU (XPU) 支援不可用
- ✗ 缺少選用套件 (`dpctl`, `scikit-learn-intelex`)

## 啟用 Intel GPU 支援

### 1. **檢查是否配備 Intel GPU**
```bash
# 檢查 GPU 硬體
lspci | grep -i vga
# 或
lspci | grep -i display
```

### 2. **安裝 Intel GPU 驅動程式** (若使用 Intel Arc/Iris/UHD 顯示晶片)

適用 Ubuntu/Debian：
```bash
# 添加 Intel GPU 軟體庫
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# 安裝 Level Zero 與 OpenCL 運行環境
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **安裝額外 Python 套件**
```bash
# 安裝 dpctl 以管理 Intel GPU 裝置
pip install dpctl

# 安裝具 Intel 優化的 scikit-learn
pip install scikit-learn-intelex
```

### 4. **安裝具 XPU 支援的 PyTorch**
```bash
# 解除安裝僅限 CPU 的 PyTorch
pip uninstall torch torchvision torchaudio

# 安裝具 Intel XPU 支援的 PyTorch
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu

# 確保 IPEX 版本匹配
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **驗證安裝**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available()); print('XPU device count:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## 關於訓練錯誤

錯誤訊息 `"The optimizer should be given for training mode"` 是您腳本中的程式缺陷。訓練時需傳遞優化器參數。請檢查 `try_intel_gpu.py` 並確認訓練函式包含優化器參數。

**您使用的 Intel GPU 硬體型號為何？** 執行 `lspci | grep -i vga` 查詢，我將能提供更具體的指示。