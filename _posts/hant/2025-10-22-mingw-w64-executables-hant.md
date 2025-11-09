---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: MinGW-w64 內含可執行檔
translated: true
type: note
---

### MinGW-w64 包含的可執行檔

MinGW-w64 主要是一個用於交叉編譯原生 Windows 應用程式的極簡化工具鏈，使用 GCC 及相關工具。它專注於開發工具，而非完整的類 Unix 指令集（例如，它預設**不**包含 `gpg` 或 GnuPG——這些可在如 MSYS2 等環境中作為獨立套件安裝）。核心安裝的 `bin` 目錄通常包含以下可執行檔（基於標準獨立下載，例如來自官方 SourceForge 發行版）。此列表可能因版本和建置而略有不同，但以下是常見項目：

| 可執行檔 | 描述 |
|------------|-------------|
| `gcc.exe` | GNU C 編譯器 |
| `g++.exe` | GNU C++ 編譯器 |
| `cpp.exe` | C 預處理器 |
| `gfortran.exe` | GNU Fortran 編譯器（若建置中包含） |
| `ld.exe` | GNU 連結器 |
| `as.exe` | GNU 組譯器 |
| `ar.exe` | 用於建立函式庫的封存工具 |
| `ranlib.exe` | 為封存函式庫產生索引 |
| `nm.exe` | 列出物件檔中的符號 |
| `objdump.exe` | 顯示物件檔資訊 |
| `objcopy.exe` | 複製並轉譯物件檔 |
| `strip.exe` | 從可執行檔中移除符號 |
| `size.exe` | 列出物件檔的區段大小 |
| `strings.exe` | 顯示檔案中的可列印字串 |
| `readelf.exe` | 顯示 ELF 檔案資訊（用於交叉工具） |
| `dlltool.exe` | 建立 DLL 匯入/匯出檔案 |
| `windres.exe` | 編譯 Windows 資源檔 |
| `gendef.exe` | 從 DLL 產生 .def 檔案 |
| `genidl.exe` | 從 DLL 產生 .idl 檔案 |
| `widl.exe` | 為 Wine/Winelib 編譯 IDL 檔案 |
| `gcc-ar.exe` | 用於 ar 的 GCC 封裝器 |
| `gcc-nm.exe` | 用於 nm 的 GCC 封裝器 |
| `gcc-ranlib.exe` | 用於 ranlib 的 GCC 封裝器 |

這些主要是來自 GCC 和 Binutils 的編譯器、連結器及二進位檔案操作工具。若需要更完整的類 Unix 環境（包含 `gpg`、`make`、`bash` 等工具），請考慮安裝 MSYS2（其包含 MinGW-w64 作為組件）並透過 `pacman` 添加套件。

[MinGW-w64 官方網站](https://www.mingw-w64.org/)  
[MSYS2 套件庫（用於擴充功能如 GnuPG）](https://packages.msys2.org/package/mingw-w64-x86_64-gnupg)  
[SourceForge MinGW-w64 下載頁面](https://sourceforge.net/projects/mingw-w64/files/)