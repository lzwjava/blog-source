---
audio: false
generated: true
lang: hant
layout: post
title: WebAssembly
translated: true
type: note
---

讓我們深入探討 WebAssembly (Wasm) 的完整指南。我將把它分解成幾個容易消化的部分：它是什麼、如何運作、為何重要、如何使用以及未來發展。閱讀完畢後，你將對 WebAssembly 及其入門方法有扎實的理解。

---

### **1. 什麼是 WebAssembly？**
WebAssembly 是一種二進制指令格式，設計為程式語言的便攜高效編譯目標。它是一種低階、類似組合語言的格式，具有緊湊的二進制表示法，但並非直接供人類編寫——而是透過編譯 C、C++、Rust、Go 甚至 Python 等高階語言生成。

- **主要特性：**
  - **高效能：** 透過利用硬體能力，以接近原生速度執行。
  - **可攜性：** 跨平台（瀏覽器、伺服器、物聯網裝置等）一致運行。
  - **安全性：** 在沙盒環境中運行，與主機系統隔離。
  - **互通性：** 與 JavaScript 協同工作，而非對立。

- **歷史：**
  - 2015 年由 Mozilla、Google、Microsoft 和 Apple 合作推出。
  - 2019 年成為 W3C 推薦標準，標誌著其成為官方網絡標準。

- **使用案例：**
  - 網頁遊戲（例如 Unity 或 Unreal Engine 輸出）。
  - 效能關鍵型應用（例如 Figma 等視頻編輯器或類似 Photoshop 的工具）。
  - 伺服器端應用（例如與 Node.js 配合使用）。
  - 在現代環境中運行遺留程式碼庫。

---

### **2. WebAssembly 如何運作？**
WebAssembly 橋接了高階程式碼與機器執行之間的差距。流程如下：

1. **原始碼：** 使用 C++ 或 Rust 等語言編寫程式碼。
2. **編譯：** 編譯器（例如 C/C++ 的 Emscripten 或 Rust 的 `wasm-pack`）將其轉譯為 WebAssembly 的二進制格式（`.wasm` 檔案）。
3. **執行：**
   - 在瀏覽器中，`.wasm` 檔案被獲取（通常透過 JavaScript），驗證後由瀏覽器的 Wasm 運行時編譯為機器碼。
   - 運行時在沙盒中執行，確保安全性。

- **文字格式 (WAT)：** WebAssembly 還具有人類可讀的文字表示法（`.wat`），適用於除錯或學習。例如：
  ```wat
  (module
    (func (export "add") (param i32 i32) (result i32)
      local.get 0
      local.get 1
      i32.add)
  )
  ```
  這定義了一個 `add` 函數，接受兩個 32 位元整數並返回它們的和。

- **記憶體模型：** Wasm 使用線性記憶體模型——一個程式可讀寫的位元組平面陣列。它透過手動管理或原始語言的運行時進行管理。

- **與 JavaScript 互動：** 使用 `WebAssembly.instantiate()` 或 `fetch()` 在 JavaScript 中載入 Wasm 模組，並呼叫匯出的函數。Wasm 也可以回呼 JavaScript。

---

### **3. 為何使用 WebAssembly？**
- **速度：** 預編譯的二進制檔案比解釋型 JavaScript 運行更快。
- **語言靈活性：** 使用 C、Rust 等語言，而非局限於 JavaScript。
- **大小效率：** `.wasm` 檔案比等效的 JavaScript 更小，減少載入時間。
- **跨平台：** 編寫一次，隨處運行——瀏覽器、伺服器或嵌入式裝置。
- **安全性：** 沙盒化防止惡意程式碼存取主機系統。

**權衡取捨：**
- 無法直接存取 DOM（需透過 JavaScript 處理）。
- 對初學者而言，工具鏈可能較複雜。
- 除錯比 JavaScript 更困難。

---

### **4. WebAssembly 入門指南**
讓我們透過一個簡單範例：將 C 函數編譯為 WebAssembly 並在瀏覽器中運行。

#### **步驟 1：安裝工具**
- **Emscripten：** 用於將 C/C++ 編譯為 WebAssembly 的工具鏈。
  - 安裝：遵循 [Emscripten 指南](https://emscripten.org/docs/getting_started/downloads.html)（需要 Python、CMake 等）。
- **Node.js：** 可選，用於在瀏覽器外運行 Wasm。
- **網頁伺服器：** 瀏覽器要求 `.wasm` 檔案需透過 HTTP 提供（例如使用 `python -m http.server`）。

#### **步驟 2：編寫程式碼**
建立檔案 `add.c`：
```c
int add(int a, int b) {
    return a + b;
}
```

#### **步驟 3：編譯為 WebAssembly**
執行此 Emscripten 指令：
```bash
emcc add.c -s EXPORTED_FUNCTIONS='["_add"]' -s EXPORT_ES6=1 -s MODULARIZE=1 -o add.js
```
- 輸出 `add.js`（粘合腳本）和 `add.wasm`（二進制檔案）。

#### **步驟 4：在 HTML 中使用**
建立 `index.html`：
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <script type="module">
        import init, { add } from './add.js';
        async function run() {
            await init();
            console.log(add(5, 3)); // 輸出 8
        }
        run();
    </script>
</body>
</html>
```

#### **步驟 5：提供服務並測試**
- 啟動本地伺服器：`python -m http.server 8080`
- 在瀏覽器中開啟 `http://localhost:8080`，並檢查控制台。

對於 Rust，你會使用 `cargo` 和 `wasm-pack`——流程類似，工具鏈不同。

---

### **5. 生態系統與工具**
- **語言：**
  - **C/C++：** Emscripten。
  - **Rust：** `wasm-pack`、`wasm-bindgen`。
  - **Go：** 內建 Wasm 支援（`GOOS=js GOARCH=wasm`）。
  - **AssemblyScript：** 類似 TypeScript 語法的 Wasm。

- **運行時：**
  - **瀏覽器：** Chrome、Firefox、Safari、Edge。
  - **Node.js：** 使用 `--experimental-wasm-modules`。
  - **獨立運行時：** Wasmtime、Wasmer、WasmEdge。

- **函式庫：**
  - **WebGL：** 用於圖形處理（例如遊戲）。
  - **WASI：** WebAssembly 系統介面，用於非網絡使用案例（檔案 I/O 等）。

---

### **6. 進階功能**
- **執行緒：** 支援 SharedArrayBuffer 以實現並行處理。
- **SIMD：** 向量指令用於數學密集型任務（例如影像處理）。
- **WASI：** 將 Wasm 擴展至網絡之外，增加系統呼叫。
- **動態連結：** 載入多個 `.wasm` 模組並在運行時連結它們。

---

### **7. WebAssembly 的未來**
- **更廣泛的應用：** 更多語言和框架正在加入 Wasm 支援。
- **無伺服器運算：** Wasm 的輕量特性適合邊緣運算。
- **標準化：** 垃圾回收和異常處理等提案正在進行中。
- **非網絡領域增長：** WASI 及 Wasmer 等運行時正將 Wasm 推向物聯網、桌面應用等領域。

---

### **8. 進一步學習資源**
- **官方網站：** [webassembly.org](https://webassembly.org/)
- **MDN 文檔：** [MDN 上的 WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)
- **教學：** 《Rust and WebAssembly》書籍 (rustwasm.github.io/book) 或 Emscripten 文檔。
- **X 推文：** 在 X 上搜尋 #WebAssembly 以獲取真實範例和討論。

---

### **快速回顧**
WebAssembly 在效能和可攜性方面改變了遊戲規則。你可以用喜愛的語言編寫，編譯為 `.wasm`，並在任何地方快速運行。它並非萬能解藥（JavaScript 仍主導網絡互動性），但它是現代開發者工具包中的強大工具。

想嘗試特定範例、探索使用案例或解決問題嗎？告訴我！