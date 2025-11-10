---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CFFI Python C 介面指南
translated: true
type: note
---

### 什麼是 CFFI？
CFFI（C 語言外部函數介面）是一個用於從 Python 程式碼呼叫 C 函數的 Python 程式庫。它兼容 CPython 和 PyPy，提供了比 ctypes 等程式庫更安全、更便攜的替代方案。它支援兩種主要模式：ABI（呼叫現有共享程式庫）和 API（內聯編譯 C 程式碼）。

### 安裝
使用 pip 安裝 CFFI：
```bash
pip install cffi
```
CFFI 需要 C 編譯器（例如 Linux 上的 GCC、Windows 上的 Visual Studio）來建置模組。

### 基本使用範例
以下是一個簡單用例的逐步指南：使用 API 模式（建議用於新程式碼）呼叫一個將兩個整數相加的 C 函數。

1. **匯入並設定 FFI**：
   ```python
   from cffi import FFI
   ffibuilder = FFI()
   ```

2. **定義 C 宣告**：
   在字串中指定 C 函數簽章：
   ```python
   ffibuilder.cdef("""
       int add(int a, int b);
   """)
   ```

3. **提供 C 原始碼**：
   包含 C 實現：
   ```python
   ffibuilder.set_source("_example",
       """
       int add(int a, int b) {
           return a + b;
       }
       """)
   ```

4. **編譯模組**：
   執行此腳本一次以建置 C 擴充：
   ```python
   if __name__ == "__main__":
       ffibuilder.compile(verbose=True)
   ```
   這會生成一個編譯後的模組（例如 `_example.cpython-39-x86_64-linux-gnu.so`）。

5. **使用編譯後的模組**：
   在 Python 程式碼中，匯入並呼叫函數：
   ```python
   from _example import lib
   result = lib.add(5, 3)
   print(result)  # 輸出：8
   ```

### 關鍵概念
- **FFI 物件**：主要介面，使用 `FFI()` 建立。使用 `cdef()` 進行宣告，使用 `set_source()` 提供程式碼。
- **宣告**：告訴 Python 關於 C 類型、結構、函數等資訊。字串必須完全符合 C 語法。
- **類型轉換**：CFFI 自動處理基本類型（int、float、指標）。對於複雜情況，使用陣列、結構或回調。
- **錯誤處理**：無效的 C 定義會引發如 `CDefError` 的異常。C 運行時錯誤（例如透過 `errno`）可以使用 `ffi.errno` 檢查。
- **記憶體管理**：使用 `ffi.new()` 處理 C 結構/陣列，並確保適當釋放記憶體以避免洩漏。

### 模式：ABI 與 API
- **ABI 模式**（適用於現有程式庫）：載入共享程式庫（例如 `ffi.dlopen("mylib.so")`）並直接呼叫函數。範例：
  ```python
  from cffi import FFI
  ffi = FFI()
  ffi.cdef("int add(int a, int b);")
  lib = ffi.dlopen("/path/to/libmylib.so")
  result = lib.add(5, 3)
  ```
  這種模式對於預先建置的程式庫更快，但便攜性較差——需要確切的二進位檔案。

- **API 模式**（推薦）：如上例所示，內聯編譯 C 程式碼。它更安全、優化更好，並且跨平台工作。

### 進階功能
- **結構與聯合**：定義複雜類型，例如 `cdef("struct Point { int x, y; }")`。
- **陣列與指標**：使用 `ffi.new("int[10]")` 建立陣列，或使用 `ffi.cast("int*", ptr)` 進行轉型。
- **回調**：使用 `ffi.callback()` 將 Python 函數傳遞給 C。
- **與套件整合**：許多程式庫（例如 cryptography、NumPy）使用 CFFI 來提升效能。
- **效能提示**：編譯需要時間；對於分發，使用原地建置或 cffi 套件。避免在迴圈中進行繁重的 Python-C 轉換。

完整文件請參閱 [官方 CFFI 文件](https://cffi.readthedocs.io/)。這裡涵蓋了基礎知識——嘗試使用範例以適應你的需求。如果你有具體用例，請提供更多細節以獲得針對性建議。