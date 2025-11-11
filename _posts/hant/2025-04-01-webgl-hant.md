---
audio: false
generated: true
lang: hant
layout: post
title: WebGL 指南
translated: true
type: note
---

讓我們深入探討 WebGL（Web Graphics Library）的完整指南。這將涵蓋它的定義、運作原理、應用優勢、入門方法及其更廣泛的應用場景——非常適合理解它在 Figma 等工具或更多領域中的角色。準備好，開始吧！

---

### **1. 什麼是 WebGL？**
WebGL 是一種 JavaScript API，能將硬體加速的 2D 和 3D 圖形帶到網絡上。它基於 OpenGL ES（嵌入式系統），是原生應用中使用的 OpenGL 標準的子集，並針對瀏覽器進行了調整。透過 WebGL，你可以直接使用 GPU 將圖形渲染到 `<canvas>` 元素上，繞過傳統 HTML/CSS 基於 CPU 的較慢渲染方式。

- **主要特性：**
  - **硬體加速：** 利用 GPU 實現快速渲染。
  - **跨平台：** 在所有主流瀏覽器（Chrome、Firefox、Safari、Edge）中運行。
  - **可編程：** 使用著色器（小型程式）來定義外觀和動畫效果。
  - **無需插件：** 瀏覽器原生支援，不同於 Flash 或舊技術。

- **歷史背景：**
  - 由 Khronos Group（OpenGL 的背後團隊）於 2011 年推出。
  - WebGL 1.0 基於 OpenGL ES 2.0；WebGL 2.0（2017 年）則基於 OpenGL ES 3.0。

- **應用場景：**
  - 遊戲（例如，基於瀏覽器的 3D 遊戲）。
  - 數據可視化（例如，互動式圖表或地圖）。
  - 創意工具（例如，Figma 的向量渲染）。
  - 模擬（例如，物理引擎或 3D 建模）。

---

### **2. WebGL 的運作原理**
WebGL 透過 JavaScript API 提供對 GPU 的低階存取。它圍繞著**渲染管線**運作——這是一系列將程式碼轉換為螢幕上像素的步驟。

1. **設定：**
   - 在 HTML 中創建一個 `<canvas>` 元素。
   - 取得 WebGL 上下文：`canvas.getContext('webgl')`（或 `'webgl2'` 用於 2.0）。

2. **著色器：**
   - **頂點著色器：** 定義點（頂點）在 3D 空間中的位置。
   - **片段著色器：** 為頂點之間的每個像素上色。
   - 使用 GLSL（OpenGL Shading Language）編寫，在運行時編譯。

3. **緩衝區：**
   - 數據（例如，頂點位置、顏色）透過緩衝區儲存在 GPU 記憶體中。
   - 例如：三角形的三個角點以座標陣列形式傳送。

4. **渲染：**
   - 綁定緩衝區、設定著色器，並發出繪製呼叫（例如，`gl.drawArrays()`）。
   - GPU 以平行方式處理，輸出到 canvas 上。

- **座標系統：** WebGL 使用標準化的 3D 空間（x、y、z 軸範圍為 -1 到 1），並透過矩陣進行變換（例如，用於透視或旋轉）。

- **狀態機：** WebGL 是無狀態的——你需要在每次繪製呼叫前設定參數（例如，紋理、混合模式）。

---

### **3. 為什麼使用 WebGL？**
- **效能：** 對於複雜圖形，GPU 加速優於 CPU 渲染。
- **靈活性：** 著色器讓你可以自訂視覺效果到像素級別。
- **網絡整合：** 與 JavaScript、DOM 事件及其他 API 無縫協作。
- **無需安裝：** 在任何有瀏覽器的地方都能運行。

**權衡之處：**
- 學習曲線陡峭——相比 HTML5 Canvas 2D 更為低階。
- 除錯困難（GLSL 錯誤訊息難以理解）。
- 瀏覽器兼容性可能有所不同（尤其是 WebGL 2.0）。

---

### **4. WebGL 入門**
讓我們渲染一個簡單的彩色三角形來體驗 WebGL 的實際運作。

#### **步驟 1：HTML 設定**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <canvas id="glCanvas" width="400" height="400"></canvas>
    <script>
        // JavaScript 程式碼放在這裡
    </script>
</body>
</html>
```

#### **步驟 2：JavaScript 基礎**
在 `<script>` 標籤內加入以下程式碼：
```javascript
// 取得 canvas 和上下文
const canvas = document.getElementById('glCanvas');
const gl = canvas.getContext('webgl');
if (!gl) {
    alert('不支援 WebGL！');
}

// 頂點著色器原始碼（GLSL）
const vsSource = `
    attribute vec2 a_position;
    void main() {
        gl_Position = vec4(a_position, 0.0, 1.0);
    }
`;

// 片段著色器原始碼（GLSL）
const fsSource = `
    void main() {
        gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); // 紅色
    }
`;

// 編譯著色器
function createShader(gl, type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error(gl.getShaderInfoLog(shader));
        gl.deleteShader(shader);
        return null;
    }
    return shader;
}

const vertexShader = createShader(gl, gl.VERTEX_SHADER, vsSource);
const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fsSource);

// 連結成程式
const program = gl.createProgram();
gl.attachShader(program, vertexShader);
gl.attachShader(program, fragmentShader);
gl.linkProgram(program);
if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    console.error(gl.getProgramInfoLog(program));
}

// 頂點數據（一個三角形）
const positions = new Float32Array([
    0.0,  0.5,  // 頂部
   -0.5, -0.5,  // 左下
    0.5, -0.5   // 右下
]);

// 緩衝區設定
const positionBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);

// 告訴 WebGL 如何讀取緩衝區
const positionLocation = gl.getAttribLocation(program, 'a_position');
gl.enableVertexAttribArray(positionLocation);
gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

// 清除並繪製
gl.clearColor(0.0, 0.0, 0.0, 1.0); // 黑色背景
gl.clear(gl.COLOR_BUFFER_BIT);
gl.useProgram(program);
gl.drawArrays(gl.TRIANGLES, 0, 3); // 繪製 3 個頂點
```

#### **步驟 3：測試**
- 儲存為 `index.html`，啟動伺服器（例如，`python -m http.server 8080`），並在瀏覽器中開啟。
- 你將看到黑色背景上有一個紅色三角形。

---

### **5. 核心概念**
- **著色器：** 頂點著色器定位幾何形狀；片段著色器為其上色。GLSL 類似 C 語言，但針對 GPU 特定。
- **緩衝區：** 在 GPU 記憶體中儲存頂點數據（位置、法線、顏色）。
- **紋理：** 映射到 3D 物件上的 2D 圖像（例如，`gl.texImage2D()`）。
- **矩陣：** 用於變換（平移、旋轉、縮放），可透過 `glMatrix` 等函式庫實現。
- **繪製呼叫：** `gl.drawArrays()` 用於簡單形狀；`gl.drawElements()` 用於索引幾何。

**WebGL 2.0 新增功能：**
- 更好的紋理（例如，3D 紋理）。
- 多重渲染目標。
- 增強著色器功能（例如，uniform buffer objects）。

---

### **6. 生態系統與工具**
- **函式庫：**
  - **Three.js：** 高階 3D 框架（隱藏了原始 WebGL 的複雜性）。
  - **Babylon.js：** 專注於遊戲的 3D 引擎。
  - **PixiJS：** 2D 渲染，帶有 WebGL 後備支援。
  - **glMatrix：** 用於變換的數學工具。

- **瀏覽器支援：**
  - WebGL 1.0：幾乎普遍支援。
  - WebGL 2.0：大多數現代瀏覽器（請查閱 caniuse.com）。

- **除錯：**
  - 瀏覽器開發者工具（例如，Chrome 的 WebGL Inspector）。
  - 擴充功能如 Spector.js。

---

### **7. WebGL 的實際應用**
- **Figma：** 使用 WebGL 進行向量圖形渲染，並結合 WebAssembly 進行計算。
- **遊戲：** Unity 和 Unreal Engine 可導出為 WebGL，在瀏覽器中遊玩。
- **地圖：** Google Maps 和 Mapbox 使用它實現平滑縮放和 3D 地形。

---

### **8. 未來發展**
- **WebGPU：** 下一代 API（基於 Vulkan/Metal）正在興起，承諾更好的效能和現代功能。它目前並非替代品，而是補充。
- **更廣泛的應用：** WebGL 目前仍佔主導地位，尤其是隨著 WebGL 2.0 的升級。

---

### **9. 資源**
- **官方資源：** [webglfundamentals.org](https://webglfundamentals.org/)——優秀的初學者教程。
- **MDN：** [WebGL 文檔](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)。
- **書籍：** Kouichi Matsuda 的《WebGL Programming Guide》。
- **X 推文：** 搜尋 #WebGL 以獲取範例和社群提示。

---

### **總結**
WebGL 是你進入瀏覽器中 GPU 驅動圖形世界的入口。它低階、強大，且有些令人畏懼——但透過練習（和函式庫），你可以從簡單動畫到完整 3D 世界無所不建。想嘗試特定項目或深入研究著色器嗎？告訴我！