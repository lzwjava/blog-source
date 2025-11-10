---
audio: false
generated: true
image: false
lang: hant
layout: post
title: PyTorch 的 Rust 綁定
translated: true
type: note
---

### tch-rs 簡介

tch-rs 是一個 Rust 套件，提供 PyTorch C++ API 的綁定，專門封裝了 libtorch 函式庫。其主要目的是讓 Rust 開發者能夠在 Rust 應用程式中直接利用 PyTorch 強大的張量計算、自動微分和機器學習功能。透過提供與原始 C++ API 對應的輕量級底層封裝，tch-rs 允許在其基礎上建立更符合 Rust 慣用語法的抽象層，讓開發者無需離開 Rust 生態系統就能輕鬆執行模型訓練、推論和張量操作等任務。

#### 主要功能
- **張量操作與 Autograd**：支援核心張量運算、梯度計算，以及透過 Adam 等優化器進行模型訓練的反向傳播
- **神經網路 API**：包含用於建構和訓練神經網路架構的工具，附有在 MNIST 資料集上實現簡單前饋網路的範例
- **模型載入**：允許使用 safetensors 格式匯入預先訓練的 PyTorch 模型，這種格式效率高且無需 Python 依賴
- **範例與使用場景**：提供實用演示，包括張量建立基礎、梯度下降訓練、自訂神經網路，以及執行預訓練模型（如用於影像分類的 ResNet18）
- **跨平台支援**：可在多種系統上運行，並提供 CPU 或 GPU（CUDA）加速選項

該項目採用 Apache-2.0 和 MIT 雙重授權，持續積極維護，部分程式碼生成參考了 ocaml-torch 等相關項目。

#### 快速開始
使用 tch-rs 前，需在系統中安裝 libtorch（PyTorch 的 C++ 發行版）。透過 Cargo 將其加入您的 Rust 專案：
```
[dependencies]
tch = "0.17.2"  # 請檢查最新版本
```
可透過手動下載、使用系統安裝或啟用 `download-libtorch` 等功能來自動獲取 libtorch。如需 GPU 支援，請指定 CUDA 版本（例如透過 `TORCH_CUDA_VERSION=cu117`）。執行範例可使用 `cargo run --example basics` 等指令。請注意 Windows 使用者建議優先使用 MSVC 工具鏈，並可透過環境變數啟用靜態連結。

更多詳細資訊，請參閱專案儲存庫中提供的說明文件和範例。

[tch-rs GitHub 儲存庫](https://github.com/LaurentMazare/tch-rs)  
[tch-rs 說明文件](https://docs.rs/tch)