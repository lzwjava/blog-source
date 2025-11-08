---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-4.5-sonnet
title: PyTorchでIntel GPUサポートを有効にする
translated: true
type: note
---

順調に進んでいます！PyTorchとIPEXが連携して動作しています。ただし、お使いのシステムではIntel GPUサポートが有効になっていません。現状と解決方法について説明します：

## 現在の状況
- ✓ PyTorch + IPEX 正しくインストール済み
- ✗ Intel GPU（XPU）サポートが利用不可
- ✗ オプションパッケージが不足（`dpctl`、`scikit-learn-intelex`）

## Intel GPUサポートを有効にする方法

### 1. **Intel GPUの有無を確認**
```bash
# GPUハードウェアを確認
lspci | grep -i vga
# または
lspci | grep -i display
```

### 2. **Intel GPUドライバーをインストール**（Intel Arc/Iris/UHDグラフィックスをお持ちの場合）

Ubuntu/Debianの場合：
```bash
# Intel GPUリポジトリを追加
wget -qO - https://repositories.intel.com/gpu/intel-graphics.key | \
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/gpu/ubuntu jammy client" | \
  sudo tee /etc/apt/sources.list.d/intel-gpu-jammy.list

sudo apt update

# Level ZeroとOpenCLランタイムをインストール
sudo apt install -y \
  intel-opencl-icd \
  intel-level-zero-gpu \
  level-zero \
  level-zero-dev
```

### 3. **追加のPythonパッケージをインストール**
```bash
# Intel GPUデバイス管理用のdpctlをインストール
pip install dpctl

# Intel最適化版scikit-learnをインストール
pip install scikit-learn-intelex
```

### 4. **XPUサポート付きPyTorchをインストール**
```bash
# CPU専用PyTorchをアンインストール
pip uninstall torch torchvision torchaudio

# Intel XPUサポート付きPyTorchをインストール
pip install torch==2.8.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu

# IPEXのバージョン整合性を確認
pip install intel-extension-for-pytorch==2.8.0
```

### 5. **インストールを確認**
```bash
python -c "import torch; import intel_extension_for_pytorch as ipex; print('XPU available:', torch.xpu.is_available()); print('XPU device count:', torch.xpu.device_count() if torch.xpu.is_available() else 0)"
```

## トレーニングエラーについて

エラー `"The optimizer should be given for training mode"` はスクリプトのバグです。トレーニング時にはオプティマイザを渡す必要があります。`try_intel_gpu.py`を確認し、トレーニング関数にオプティマイザパラメータが含まれていることを確認してください。

**お使いのIntel GPUハードウェアは何ですか？** `lspci | grep -i vga` を実行して確認していただければ、より具体的な指示をお伝えできます。