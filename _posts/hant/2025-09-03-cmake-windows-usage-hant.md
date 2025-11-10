---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Windows 上的 CMake 使用與解說
translated: true
type: note
---

很好的問題！讓我們來了解什麼是 **CMake**、如何在 **Windows** 上使用它，以及像 `cmake --build` 這樣的命令實際上是什麼意思。

---

### 🔹 什麼是 CMake？
- **CMake** 是一個跨平台的建置系統產生器。
- 它本身**並不建置**專案，而是為你的平台和編譯器建立適當的建置檔案（例如 Visual Studio 解決方案、Makefiles、Ninja 檔案等）。
- 然後，你使用這些生成的檔案（或 CMake 自己的建置驅動程式）來實際編譯你的專案。

---

### 🔹 在 Windows 上安裝 CMake
1. 從此處下載：[https://cmake.org/download/](https://cmake.org/download/)
2. 安裝時，請確保勾選 **「Add CMake to system PATH」**（或手動添加）。
3. 在終端機（PowerShell 或 CMD）中驗證：
   ```sh
   cmake --version
   ```

---

### 🔹 在 Windows 上的典型 CMake 工作流程

假設你的專案結構如下：
```
project_root/
 ├─ CMakeLists.txt
 └─ src/
     └─ main.cpp
```

#### 1. 開啟終端機
（如果使用 MSVC，可以使用 **x64 Native Tools Command Prompt for VS**；如果使用 `MinGW`/`Ninja`，使用一般的 PowerShell 即可。）

#### 2. 建立建置目錄
最好將原始碼和建置檔案分開：
```sh
cd project_root
mkdir build
cd build
```

#### 3. 生成建置系統檔案
使用 Visual Studio 的範例：
```sh
cmake .. -G "Visual Studio 17 2022" -A x64
```

使用 Ninja 的範例：
```sh
cmake .. -G Ninja
```

此步驟會讀取 `../CMakeLists.txt` 並生成必要的建置定義。

#### 4. 建置專案
現在你可以使用：
```sh
cmake --build .
```

- 在 Windows 上使用 Visual Studio 時，這實際上會呼叫 `MSBuild`。
- 使用 Ninja 時，則會呼叫 `ninja` 工具。

你也可以告訴 CMake 以 **Release** 模式建置：
```sh
cmake --build . --config Release
```
⚠ 注意：`--config` 僅用於多配置產生器（Visual Studio、Xcode）。如果使用 Ninja 或 Makefiles，你需要在配置時指定：
```sh
cmake .. -DCMAKE_BUILD_TYPE=Release
```

#### 5. 執行你的可執行檔
建置完成後，在相應的目錄中尋找：
- 對於 **Visual Studio**：`build/Debug/` 或 `build/Release/`
- 對於 **Ninja**：直接在 `build/` 目錄內

---

### 🔹 常用命令速查表
```sh
# 配置專案（生成建置檔案）
cmake -S . -B build

# 配置並指定 Release 建置類型（單一配置產生器）
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release

# 建置專案
cmake --build build

# 使用特定配置建置（適用於 Visual Studio/Xcode）
cmake --build build --config Release

# 安裝編譯輸出（如果在 CMakeLists 中有定義）
cmake --install build
```

---

✅ **總結**：  
- **`cmake ..`** → 配置並生成平台特定的專案/建置檔案。  
- **`cmake --build .`** → 使用選擇的建置工具實際編譯。  
- 在 Windows 上，你通常會使用 **Visual Studio 產生器** 或 **Ninja** 以獲得更好的效能。  

---

需要我提供一個**最簡範例 CMakeLists.txt**，並逐步指導你在 Windows 上建置一個簡單的 C++「Hello World」專案嗎？