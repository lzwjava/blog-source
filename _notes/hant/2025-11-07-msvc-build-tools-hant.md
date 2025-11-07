---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-4.5-sonnet
title: MSVC 建置工具用途與替代方案
translated: true
---

MSVC 建置工具確實非常龐大！以下是它們的實際用途：

## 主要用途

**針對 Rust 語言：**
- 建置具有 **C/C++ 依賴項** 的 Rust crate（非常常見）
- 編譯原生 Windows 系統 API
- 連結 Windows 函式庫
- 建置使用 `cc` crate 或 bindgen 的專案

**一般用途：**
- 在 Windows 上編譯 C/C++ 程式碼
- 建置具有原生擴充功能的 Python 套件（如 numpy、pandas）
- 編譯 Node.js 原生擴充模組
- 建置任何需要在 Windows 上使用 C/C++ 編譯器的軟體

## 為何如此龐大？

龐大的原因來自：
- Windows SDK（包含每個 Windows 版本的標頭檔和函式庫）
- 多重編譯器工具鏈（x86、x64、ARM、ARM64）
- ATL/MFC 函式庫
- 偵錯工具和符號檔
- 建置系統元件（MSBuild）

## 更輕量的替代方案

如果只需使用 Rust：
1. **改用 GNU 工具鏈** - 安裝 `rustup` 時選擇 `x86_64-pc-windows-gnu` 目標（需要 MinGW，約 2-3GB）
2. **WSL2** - 完全使用 Linux 工具鏈
3. **精簡版 MSVC 安裝** - 安裝時取消選取不需要的選用元件

對於沒有 C/C++ 依賴項的純 Rust 程式碼，完全不需要 MSVC。但實際上，許多熱門 crate（如 `openssl-sys`、`ring`、視窗函式庫）都需要 C 編譯器，因此大多數 Windows Rust 開發者最終還是會安裝它。

雖然令人困擾，但 Microsoft 的工具鏈向來都很龐大。GNU 替代方案雖然可用，但偶爾會與某些 crate 出現相容性問題。