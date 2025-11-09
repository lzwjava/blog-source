---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 文件類型宣告參考
translated: true
type: note
---

### 概述
這是一個來自 CodeIgniter 框架（一個開源網頁應用程式框架）的 PHP 陣列，它定義了各種標記語言的 DOCTYPE 宣告。DOCTYPE 是一種文件類型宣告，用於告知瀏覽器和驗證器有關 HTML 文件中使用的標記語言的版本和標準。它能確保正確的渲染和驗證。這些宣告基於官方的 W3C 標準。下面，我將按主題分組逐一解釋，包括它們的用途和典型使用場景。

### XHTML 文件類型
XHTML（可延伸超文字標記語言）是將 HTML 重新制定為 XML，強制執行更嚴格的語法（例如，要求閉合標籤和小寫元素）。
- **xhtml11**：宣告 XHTML 1.1，這是最新的 XHTML 版本，具有模組化功能，適用於進階網頁應用程式。嚴格、符合 XML 規範；用於現代、語義化的網頁，不含框架或舊式元素。
- **xhtml1-strict**：XHTML 1.0 Strict；強制使用乾淨、語義化的標記，不含已棄用的元素（例如，沒有 `<font>`）。適用於需要向後兼容的標準合規網站。
- **xhtml1-trans**：XHTML 1.0 Transitional；允許一些舊式 HTML 元素，以便從 HTML 3.2/4.0 更容易遷移。適用於混合新舊標記的現有網站。
- **xhtml1-frame**：XHTML 1.0 Frameset；支援使用 `<frameset>` 的框架佈局。由於可用性問題和 SEO 缺點，在現代網頁設計中已過時。
- **xhtml-basic11**：XHTML Basic 1.1；一個輕量級配置，適用於移動裝置和簡單應用程式，排除進階功能如表單或樣式表。

### HTML 文件類型
HTML 是網頁的標準標記語言，從寬鬆標準演進到嚴格標準。
- **html5**：現代 HTML5 DOCTYPE；簡單且面向未來，所有瀏覽器均以標準模式解析。支援多媒體、API 和語義元素（例如 `<article>`、`<header>`）。建議用於新網站。
- **html4-strict**：HTML 4.01 Strict；強制語義嚴謹性，不含已棄用的元素。用於需要嚴格合規的舊專案。
- **html4-trans**：HTML 4.01 Transitional；寬鬆，允許舊式標籤以便逐步更新。常見於過渡到標準的舊網站。
- **html4-frame**：HTML 4.01 Frameset；用於框架頁面，現已因加載速度慢和可訪問性問題而被棄用。

### MathML 文件類型
MathML（數學標記語言）用於在網路上顯示數學符號。
- **mathml1**：MathML 1.0；以 XML 格式進行基本數學渲染。用於教育工具或包含簡單方程的檔案。
- **mathml2**：MathML 2.0；增強對複雜數學的支援，更好地與其他標記整合。現代數學網路顯示的基礎。

### SVG 文件類型
SVG（可縮放向量圖形）在 XML 中定義向量圖像，用於網頁圖形。
- **svg10**：SVG 1.0；基本的 2D 向量圖形。用於靜態插圖。
- **svg11**：SVG 1.1；完整的 2D 圖形，支援動畫和濾鏡。動態網頁圖形的標準。
- **svg11-basic**：SVG 1.1 Basic；針對移動裝置的精簡子集，功能較少。適用於裝置上的輕量級 SVG。
- **svg11-tiny**：SVG 1.1 Tiny；針對低功耗裝置（如手機）的最小配置。支援基本形狀和動畫。

### 複合文件類型
這些結合了多個標準，用於豐富的多媒體內容。
- **xhtml-math-svg-xh**：XHTML 1.1 與 MathML 2.0 和 SVG 1.1；用於混合文字、數學和圖形的檔案（例如科學論文）。
- **xhtml-math-svg-sh**：與上述類似，但基於 SVG（`<svg:svg>`），用於以 SVG 為主的檔案，並嵌入 XHTML 和 MathML。
- **xhtml-rdfa-1**：XHTML 與 RDFa 1.0（屬性中的資源描述框架）；增強語義網資料嵌入，適用於富含元資料的網站。
- **xhtml-rdfa-2**：XHTML 與 RDFa 1.1；改進的 RDFa，用於在 HTML 屬性中連結資料，應用於資料網應用程式。

### 使用說明
- 這些在 CodeIgniter 中預定義，可透過其 `doctype()` 輔助函數輕鬆插入。
- 現代網頁開發傾向使用 HTML5（`html5`），因為其靈活性和瀏覽器支援。舊的文件類型（例如 HTML 4 或框架版本）大多已過時。
- 如 W3C 規範（例如 w3.org/TR/html5/、w3.org/TR/xhtml11/）所示，這些確保一致的解析：瀏覽器使用它們來觸發標準模式或怪異模式，影響佈局和腳本。根據專案的標記需求選擇最適合的類型以獲得最佳驗證（透過如 W3C Validator 等工具）。如果您在 CodeIgniter 中工作，請在視圖中使用陣列鍵來輸出宣告。