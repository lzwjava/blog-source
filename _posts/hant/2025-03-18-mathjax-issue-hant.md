---
audio: false
generated: true
lang: hant
layout: post
title: 數學公式問題疑難排解
translated: true
type: note
---

您的 MathJax 配置似乎未能正常運作。讓我們根據您提供的程式碼來找出並解決問題。

### 您目前的配置
您目前的 MathJax 設定如下：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\[","\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

此配置旨在：
- 在 `\( ... \)` 分隔符之間渲染行內數學公式。
- 在 `$$ ... $$` 或 `\[ ... \]` 分隔符之間渲染展示型數學公式。
- 啟用長公式的自動換行功能。
- 使用 CommonHTML 輸出處理器將數學輸出縮放至 85% 大小。
- 使用 AMS 樣式自動為方程式編號。

然而，您回報它「無法正常運作」，這可能意味著數學公式未能正確渲染，或是特定功能（如換行）未如預期般運作。

### 問題所在
主要問題在於 `displayMath` 分隔符的配置：

```javascript
displayMath: [ ['$$','$$'], ["\[","\]"] ]
```

在 JavaScript 中，字串 `"["` 會被直譯為 `[`，因為 `\[` 並非特殊的跳脫序列——它只是一個反斜線後跟一個方括號。同樣地，`"\]"` 會變成 `]`。結果，MathJax 被配置為將 `[ ... ]` 識別為展示型數學公式的分隔符，**而非** `\[ ... \]`。由於您的數學表達式（例如範例 `\[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]`）使用了 `\[ ... \]`，MathJax 在目前的設定下無法將其識別為展示型數學公式。

行內數學公式的分隔符 `["\\(","\\)"]` 是正確的，因為在 JavaScript 字串中，`\\(` 和 `\\)` 代表 `\(` 和 `\)`——這是行內數學公式的標準 LaTeX 分隔符。然而，展示型數學公式的分隔符需要調整。

### 解決方案
為修正此問題，請更新 `displayMath` 配置，使 MathJax 能正確識別 `\[ ... \]` 為展示型數學公式的分隔符。在 JavaScript 中，要表示字串 `\[`，您需要寫成 `"\\["`，因為每個反斜線都必須被跳脫。同樣地，`\]` 應寫成 `"\\]"`。以下是修正後的配置：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

#### 關鍵變更
- 將 `displayMath` 陣列中的 `["\[","\]"]` 更改為 `["\\[","\\]"]`。
- 這確保分隔符設定為 `\[ ... \]`（以及 `$$ ... $$`），符合標準的 LaTeX 表示法。

### 其他注意事項
1. **換行問題**：您提到某些表達式過長並導致溢位，特別是在行動裝置檢視時。`"CommonHTML"` 輸出處理器中的 `linebreaks: { automatic: true }` 設定應能處理此問題，但它要求數學公式位於具有定義寬度的容器內（例如 `width: 100%`）。請確保您的 HTML 結構包含類似以下的內容：

   ```html
   <div style="width: 100%; overflow-x: auto;">
     \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   </div>
   ```

   這允許 MathJax 根據容器的寬度進行換行，以適應螢幕尺寸。

2. **輸出處理器**：您的腳本載入了 `TeX-MML-AM_CHTML`，該配置預設使用 CommonHTML 輸出。`"CommonHTML"` 設定（例如 `scale: 85`、`linebreaks: { automatic: true }`）將會生效，但 `"HTML-CSS"` 設定可能不會，因為該輸出處理器並未啟用。由於 CommonHTML 是現代且廣泛支援的輸出方式，這沒有問題——只需確保您的設定與其一致。

3. **測試**：更新配置後，請使用您的範例表達式進行測試：

   ```html
   \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   ```

   它現在應正確渲染為展示型數學公式，並在需要時進行適當的換行。

4. **瀏覽器相容性**：MathJax 2.7.7 應在大多數現代瀏覽器中運作。若問題仍然存在，請確保主控台中沒有 JavaScript 錯誤或衝突的 CSS 規則（例如 `white-space: nowrap`）覆寫了數學渲染。

### 最終修正後的程式碼
以下是完整且修正後的設定：

```html
<!-- MathJax Configuration -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<!-- Load MathJax -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<!-- Example Math -->
<div style="width: 100%; overflow-x: auto;">
  \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
</div>
```

### 為何此解決方案有效
- **分隔符修正**：`["\\[","\\]"]` 確保 MathJax 能識別 `\[ ... \]` 為展示型數學公式，符合您的內容。
- **換行功能**：`CommonHTML` 設定與適當的容器結合，可為長表達式啟用自動換行。
- **渲染**：CDN 腳本與配置共同確保數學公式能正確處理和顯示。

請使用此修正更新您的程式碼，您的 MathJax 設定應能如預期般運作！若問題仍然存在，請分享未能正常運作的數學表達式具體範例或您遇到的任何錯誤訊息。

---

為了讓 MathJax 能妥善渲染所提供內容中的數學表達式，您需要確保它能正確處理像 \( T_p \) 和 \( 2 \times T_p \) 這樣的行內數學表達式，這些表達式是用 LaTeX 風格的分隔符包圍的。內容使用 `\( ... \)` 表示行內數學，雖然它不包含展示型數學（例如單獨成行的方程式），但為了靈活性，配置 MathJax 以同時支援行內和展示型數學是良好的做法。以下是實現此目標的逐步指南。

### 步驟 1：在 HTML 中包含 MathJax
首先，您需要載入 MathJax 函式庫。您可以使用內容傳遞網路 (CDN) 將其包含在您的 HTML 檔案中。將以下 script 標籤添加到您的 HTML `<head>` 或包含數學公式的內容之前：

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

這會載入 MathJax 2.7.9 版及其 `TeX-AMS_CHTML` 配置，該配置支援 LaTeX 輸入並將數學公式渲染為 HTML 與 CSS，適用於大多數網路應用程式。

### 步驟 2：配置 MathJax 分隔符
MathJax 需要知道應識別哪些分隔符來處理數學表達式。內容使用 `\( ... \)` 表示行內數學，這是標準的 LaTeX 分隔符。為確保 MathJax 能正確處理這些分隔符，請在 MathJax 函式庫腳本之前添加一個配置腳本。以下是一個基本配置：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    }
  });
</script>
```

- **`inlineMath`**：告訴 MathJax 將 `\( ... \)` 之間的文字視為行內數學。使用雙重方括號 `[ ['\\(', '\\)'] ]` 是因為 MathJax 接受一個分隔符對的陣列。
- **`displayMath`**：配置 MathJax 識別 `$$ ... $$` 和 `\[ ... \]` 為展示型數學，即使目前的內容未使用這些分隔符。這能確保與未來內容的相容性。
- **`processEscapes`**：允許跳脫分隔符（例如使用 `\$` 來顯示字面上的美元符號），但對於此特定內容而言並非關鍵。

### 步驟 3：增強渲染以適應響應式設計
為了使渲染的數學公式能適應不同的螢幕尺寸（例如防止在行動裝置上溢位），請為長表達式啟用自動換行功能。更新配置如下：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
```

- **`HTML-CSS`、`CommonHTML`、`SVG`**：這些是 MathJax 用來渲染數學公式的輸出處理器。啟用 `linebreaks: { automatic: true }` 可確保長表達式能自然換行，儘管此內容中的表達式（\( T_p \)、\( 2 \times T_p \)）很短，不太可能需要換行。

### 步驟 4：整合所有內容
以下是應在內容之前包含在 HTML 檔案中的完整設定：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

### 步驟 5：驗證內容是否正確渲染
透過此配置，您內容中的行內數學——例如 \( T_p \) 和 \( 2 \times T_p \)——將被渲染為格式正確的數學表達式。例如：
- \( T_p \) 會變成帶下標的變數。
- \( 2 \times T_p \) 會顯示為帶有乘號 (×) 和下標 \( T_p \) 的表達式。

### 補充說明
- **無展示型數學**：由於您的內容僅使用行內數學，因此 `displayMath` 設定並非嚴格必要，但為了完整性而包含在內。
- **CSS 樣式**：請確保您內容的 HTML 容器（例如 `<div>`）具有 `width: 100%` 或適當的樣式，以保持佈局的響應性。
- **測試**：添加此配置後，請在瀏覽器中載入您的頁面，確認 \( T_p \) 和 \( 2 \times T_p \) 能如預期般渲染。

此設定確保 MathJax 能清晰且專業地渲染您 CSMA/CD 說明中的數學表達式，從而提升使用者的閱讀體驗。

---

為了解決 MathJax 在渲染括號 `\(...\)` 和其他 LaTeX 分隔符時的問題，請調整您的配置，以在 JavaScript 字串中正確跳脫反斜線。以下是修正後的設定：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(','\\)'] ],  // 在 JavaScript 中正確跳脫
      displayMath: [ ['$$','$$'], ['\\[','\\]'] ],  // 修正了 \[ 和 \] 的跳脫
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

### 關鍵修正：
1. **已跳脫的反斜線**：
   - 將 `["\\(","\\)"]` 更改為 `['\\(','\\)']`（使用單引號可避免額外的跳脫）。
   - 將 `["\[","\]"]` 修正為 `['\\[','\\]']`，以確保 `\[...\]` 能用於展示型方程式。

2. **建議**：
   - 使用 `'$$...$$'` 或 `\\[...\\]` 表示展示型方程式。
   - 使用 `\\(...\\)` 表示行內方程式。
   - 確保沒有衝突的 Markdown 處理器會更改您的 LaTeX。

### 使用範例：
```html
<p>行內數學：\( E = mc^2 \)。</p>

<p>展示型數學：</p>
\[
  \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}
\]
```

此配置確保 MathJax 能正確解析所有 LaTeX 分隔符。

---

我了解您正在使用 Jekyll 與 Kramdown 來渲染 Markdown 文章，並希望配置 MathJax 以正確顯示數學表達式。您已提供了一個 MathJax 配置，並注意到您是在 Markdown 文章內渲染數學公式，而非使用 HTML 標籤。讓我們確保 MathJax 能與您的設定無縫協作。

### 您目前的設定
您正在使用：
- **Jekyll 與 Kramdown**：Kramdown 是 Jekyll 預設的 Markdown 解析器，並支援 LaTeX 風格的數學表達式。
- **MathJax**：您的配置指定了行內和展示型數學公式的分隔符：
  - 行內：`\( ... \)`
  - 展示型：`$$ ... $$` 和 `\[ ... \]`

您還包含了一個 `marked.min.js` 腳本，但由於 Jekyll 是使用 Kramdown 在伺服器端渲染 Markdown，而非在客戶端渲染，因此該腳本可能不相關。

### 渲染可能無法運作的原因
Kramdown 和 MathJax 需要就數學分隔符的處理方式達成一致。您的 MathJax 設定能識別 `\( ... \)` 為行內數學，以及 `$$ ... $$` 和 `\[ ... \]` 為展示型數學。然而，Kramdown 的預設行為可能無法將所有這些分隔符正確傳遞給 MathJax，除非進行適當配置，特別是在 Markdown 中出現跳脫問題時。

### 解決方案：配置 MathJax 與 Kramdown 協作
以下是使其運作的方法：

#### 1. 在 Jekyll 中配置 Kramdown
確保您的 Jekyll `_config.yml` 檔案啟用了 MathJax 作為 Kramdown 的數學引擎。添加或驗證以下內容：

```yaml
markdown: kramdown
kramdown:
  math_engine: mathjax
```

這會告訴 Kramdown 處理數學表達式並將其傳遞給 MathJax。預設情況下，Kramdown 能識別：
- `\( ... \)` 用於行內數學。
- `$$ ... $$` 用於展示型數學。

雖然您的 MathJax 配置也支援 `\[ ... \]` 用於展示型數學，但 Kramdown 並未原生使用此分隔符，除非正確處理，否則可能導致問題。

#### 2. 在 Markdown 中使用一致的數學分隔符
為避免混淆或跳脫問題，請在您的 Markdown 文章中堅持使用 Kramdown 的預設分隔符：
- **行內數學**：使用 `\( ... \)`。
  範例：`這是行內：\( E = mc^2 \)` 渲染為「這是行內：\( E = mc^2 \)」。
- **展示型數學**：使用 `$$ ... $$`。
  範例：
  ```markdown
  $$
  \int_0^1 x^2 \, dx = \frac{1}{3}
  $$
  ```
  這會渲染為置中的方程式：\( \int_0^1 x^2 \, dx = \frac{1}{3} \)。

如果您偏好使用 `\[ ... \]`，您可以使用它，但 Markdown 的反斜線跳脫可能需要特別注意（例如 `\\[ ... \\]`）。然而，使用 `$$ ... $$` 更簡單且符合 Kramdown 的預設值，能減少潛在錯誤。

#### 3. 簡化您的 MathJax 配置
由於 Kramdown 會預先處理數學公式，您的 MathJax 配置可以專注於渲染。以下是基於您的設定簡化後的版本：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(','\\)'] ],
      displayMath: [ ['$$','$$'] ], // 堅持使用 $$ 以簡化
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

- 我已從 `displayMath` 中移除 `['\\[','\\]']`，以符合 Kramdown 對 `$$ ... $$` 的偏好。如果您仍想使用 `\[ ... \]`，請保留它，但需徹底測試。
- 移除了 `"HTML-CSS"`，因為對於現代的 MathJax 渲染而言，`"CommonHTML"` 已足夠。

請將此內容置於您的 Jekyll 佈局檔案的 `<head>` 區段中。

#### 4. 移除不必要的腳本
您已包含 `<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>`，但 Jekyll 是在伺服器端使用 Kramdown，因此 Marked.js（一個客戶端解析器）並非必需，除非您有特定用途。如果沒有，請移除它以避免潛在的衝突或混淆。

#### 5. 測試您的設定
在 Markdown 文章中添加這些範例以確認渲染正常：
- 行內：`能量是 \( E = mc^2 \)。`
- 展示型：
  ```markdown
  $$
  \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bps}
  $$
  ```

執行 `jekyll serve`，在瀏覽器中開啟網站，並檢查數學公式是否正確渲染。如果沒有，請檢查瀏覽器主控台是否有 MathJax 錯誤。

### 最後說明
- **一致性**：使用 `\( ... \)` 和 `$$ ... $$` 能確保 Kramdown 和 MathJax 之間的相容性，無需額外的跳脫麻煩。
- **疑難排解**：如果數學公式仍然無法渲染，請驗證：
  - MathJax 腳本是否載入無誤（檢查瀏覽器主控台）。
  - 您的 Jekyll 建置是否成功完成。
  - 分隔符或配置中沒有拼寫錯誤。

此設定應能在您的 Jekyll Markdown 文章中完美渲染數學表達式！如果您在嘗試渲染特定範例時遇到問題，請告知我。