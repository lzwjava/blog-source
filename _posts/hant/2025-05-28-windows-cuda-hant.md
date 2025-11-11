---
audio: false
generated: true
lang: hant
layout: post
title: 在Windows中使用CUDA
translated: true
type: note
---

要在您的 HP ZBook Studio 16 G11 上使用 NVIDIA CUDA，您需要遵循以下步驟。CUDA 允許開發者透過利用 GPU 進行平行處理來加速應用程式。以下是入門指南：

### 步驟 1：驗證硬體相容性
- 確保您的 HP ZBook Studio 16 G11 配備相容的 NVIDIA GPU。ZBook Studio 16 G11 可搭載如 NVIDIA RTX 3000 Ada 世代或更高版本的 GPU，這些均支援 CUDA。

### 步驟 2：安裝 NVIDIA 驅動程式
- **下載驅動程式：** 前往 [NVIDIA 驅動程式下載頁面](https://www.nvidia.com/Download/index.aspx)，下載適合您特定 GPU 型號的最新驅動程式。
- **安裝驅動程式：** 執行安裝程式，並按照螢幕上的指示在系統上安裝驅動程式。

### 步驟 3：安裝 CUDA Toolkit
- **下載 CUDA Toolkit：** 前往 [NVIDIA CUDA Toolkit 網站](https://developer.nvidia.com/cuda-downloads)，下載與您作業系統版本相符的 CUDA Toolkit。
- **安裝 CUDA Toolkit：** 執行 CUDA Toolkit 安裝程式並按照指示操作。請確保為您的開發環境選擇適當選項。

### 步驟 4：設定環境變數
- 在安裝過程中，安裝程式應會自動設定必要的環境變數。但若未自動完成，您可能需要手動將 CUDA 二進位檔路徑加入系統的 PATH 中。
- 在 Windows 上，您可以透過「控制台 > 系統及安全性 > 系統 > 進階系統設定 > 環境變數」來操作，並新增 CUDA bin 目錄的路徑（例如 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.X\bin`）。

### 步驟 5：驗證安裝
- 開啟命令提示字元或終端機，輸入 `nvidia-smi`。此命令應顯示您的 GPU 資訊，確認驅動程式已正確安裝。
- 輸入 `nvcc --version` 以檢查 CUDA 編譯器版本。這將確認 CUDA Toolkit 是否正確安裝。

### 步驟 6：開發並執行 CUDA 應用程式
- **編寫 CUDA 程式碼：** 您可以使用 C、C++、Python 或 Fortran 編寫 CUDA 程式。NVIDIA 提供豐富的文件和範例程式碼協助您入門。
- **編譯 CUDA 程式碼：** 使用 `nvcc` 編譯器編譯您的 CUDA 程式。例如，若您有一個名為 `my_program.cu` 的 CUDA 程式，可以使用指令 `nvcc my_program.cu -o my_program` 進行編譯。
- **執行 CUDA 程式碼：** 從命令列執行已編譯的程式。例如，在 Linux 上使用 `./my_program`，在 Windows 上使用 `my_program.exe`。

### 步驟 7：使用 CUDA 函式庫
- NVIDIA 提供多個針對 CUDA 優化的函式庫，例如用於線性代數的 cuBLAS、用於傅立葉轉換的 cuFFT，以及用於深度神經網路的 cuDNN。您可以在專案中包含這些函式庫，以利用預先建置的優化功能。

### 其他資源
- **NVIDIA 開發者專區：** 前往 [NVIDIA 開發者專區](https://developer.nvidia.com/) 獲取教學課程、文件和社群支援。
- **CUDA 文件：** 參考 [CUDA 文件](https://docs.nvidia.com/cuda/) 獲取 CUDA 程式設計和最佳實踐的詳細資訊。

透過遵循這些步驟，您可以在 HP ZBook Studio 16 G11 上設定並開始使用 NVIDIA CUDA，以加速您的應用程式並充分利用 GPU 運算能力。