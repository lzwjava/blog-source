---
audio: false
generated: true
lang: hant
layout: post
title: Hugo 中的 LaTeX 渲染
translated: true
type: note
---

您所描述的問題出現在使用 **Jekyll** 並以 **MathJax** 作為數學引擎的 **Kramdown** 環境中。當 Kramdown 配置了 `math_engine: mathjax` 時，它會將 Markdown 內容中的括號 `( )` 解讀為 LaTeX 的行內數學分隔符（例如 `\( \)`），這可能會破壞包含括號的正常文本。這是因為 MathJax 根據您的配置設定為解析 `\( \)` 或 `$ $` 作為行內數學符號。

在 **Hugo** 中，預設情況下較少出現此問題，但這取決於您如何配置 Hugo 的 Markdown 處理器及 MathJax 整合。以下我將解釋為何 Hugo 在多數情況下能避免此問題、如何在 Jekyll 中預防或修復此問題，以及如何確保在 Hugo 中不會發生此情況。

---

### **Hugo 會遇到此問題嗎？**
Hugo 通常能避免此問題，原因如下：
1. **Markdown 處理器**：Hugo 預設使用 **Goldmark**（或可選的 Blackfriday）作為其 Markdown 渲染器，該渲染器預設不啟用 MathJax 或 LaTeX 解析。除非您明確配置 Hugo 使用 MathJax 並設定行內數學分隔符如 `\( \)`，否則內容中的普通括號 `( )` 不會被誤解為 LaTeX。
2. **MathJax 整合**：Hugo 本身不解析 LaTeX。如果您需要 MathJax 支援，必須手動將 MathJax 腳本（如您提供的）添加到主題模板中（例如在 `layouts/partials/head.html`）並配置分隔符。Hugo 的靈活性讓您能控制 MathJax 如何處理內容，避免自動解析 `( )`，除非明確啟用。
3. **數學短代碼**：Hugo 使用者通常使用短代碼（例如 `{{< math >}}...{{< /math >}}`）來實現 LaTeX 渲染，這能明確標記數學內容，防止普通括號被誤認為 LaTeX。

總之，除非您配置 MathJax 使用相同的行內分隔符（`\( \)`）並在沒有適當保護措施的情況下啟用自動解析，否則 Hugo 不會遇到此問題。通過使用短代碼或避免使用 `\( \)` 作為分隔符，Hugo 可以完全避開此問題。

---

### **在 Jekyll 中修復此問題**
在 Jekyll 中，此問題的發生是因為 Kramdown 的 `math_engine: mathjax` 設定與您的 MathJax 配置結合，導致 `( )` 被解析為 LaTeX。以下是修復方法：

#### **1. 變更 MathJax 行內分隔符**
修改 MathJax 配置，使用不同的行內數學分隔符，例如 `$ $`，以代替 `\( \)`，避免與普通括號衝突。更新您 Jekyll 網站 HTML 中的腳本（例如在 `_includes/head.html`）：

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // 使用 $ $ 作為行內數學符號
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // 允許使用 \$ 來顯示字面意義的 $
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

- **為何有效**：通過從 `inlineMath` 中移除 `['\(','\)']`，MathJax 不再將 `( )` 解讀為 LaTeX 分隔符，從而保留它們用於普通文本。`processEscapes: true` 設定允許您在 Markdown 中寫入 `\$` 來顯示字面意義的 `$`。
- **在您的 Markdown 中**：使用 `$x^2$` 作為行內數學符號，而不是 `\(x^2\)`。例如：
  ```markdown
  這是一個公式：$x^2 + y^2 = z^2$。普通文本（不會被解析）。
  ```

#### **2. 在 Markdown 中跳脫括號**
如果您想保留 `\( \)` 作為分隔符，請在 Markdown 內容中跳脫括號，以防止 Kramdown/MathJax 將其解析為 LaTeX。在每個括號前使用反斜線 `\`：

```markdown
普通文本 \(not a formula\)。這是一個真正的公式：\(x^2 + y^2\)。
```

- **輸出**：跳脫後的 `\(not a formula\)` 會渲染為 `(not a formula)`，而 `\(x^2 + y^2\)` 會渲染為 LaTeX 公式。
- **缺點**：這需要手動跳脫內容中的每一個 `( )` 實例，對於大型網站來說可能很繁瑣。

#### **3. 對特定頁面停用 MathJax**
如果您僅在特定頁面（例如數學內容較多的文章）需要 MathJax，請預設停用它，並僅在需要時啟用：
- 從全域的 `_layouts/default.html` 或 `_includes/head.html` 中移除 MathJax 腳本。
- 在您的佈局或頁面 front matter 中添加條件式包含。例如，在 `_layouts/post.html` 中：

```html
{% if page.mathjax %}
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$']],
        displayMath: [['$$','$$'], ['\[','\]']],
        processEscapes: true
      }
    });
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

- 在您的 Markdown 文件的 front matter 中，僅對特定頁面啟用 MathJax：
  ```yaml
  ---
  title: 我的數學文章
  mathjax: true
  ---
  ```

- **為何有效**：沒有 `mathjax: true` 的頁面不會載入 MathJax，因此 `( )` 不會被解析為 LaTeX。

#### **4. 使用不同的數學引擎**
從 MathJax 切換到 Kramdown 支援的其他數學引擎，例如 **KaTeX**，它速度更快，且除非明確配置，否則不太可能誤解括號。在您的 Jekyll 網站中安裝 KaTeX：
- 將 KaTeX 腳本添加到 `_includes/head.html`：
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      renderMathInElement(document.body, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false }
        ]
      });
    });
  </script>
  ```
- 更新 `_config.yml`：
  ```yaml
  kramdown:
    math_engine: katex
    input: GFM
    syntax_highlighter: rouge
  ```

- **為何有效**：KaTeX 對解析更嚴格，且預設使用 `$ $` 作為行內數學符號，減少了與 `( )` 的衝突。它也比 MathJax 更快。

---

### **確保 Hugo 避免此問題**
要在 Hugo 中使用 MathJax 而不遇到 `( )` 解析問題，請遵循以下步驟：

1. **將 MathJax 添加到 Hugo**：
   - 將 MathJax 腳本放置於您主題的 partials 中（例如 `layouts/partials/head.html`）：
     ```html
     {{ if .Params.mathjax }}
     <script type="text/x-mathjax-config">
       MathJax.Hub.Config({
         tex2jax: {
           inlineMath: [['$','$']],
           displayMath: [['$$','$$'], ['\[','\]']],
           processEscapes: true
         },
         "HTML-CSS": { linebreaks: { automatic: true } },
         "CommonHTML": { linebreaks: { automatic: true } },
         TeX: { equationNumbers: { autoNumber: "AMS" } }
       });
     </script>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
     {{ end }}
     ```
   - 通過在 front matter 中添加以下內容來啟用特定頁面的 MathJax：
     ```yaml
     ---
     title: 我的數學文章
     mathjax: true
     ---
     ```

2. **使用數學短代碼**：
   創建一個短代碼（例如 `layouts/shortcodes/math.html`）來明確包裹數學內容：
   ```html
   {{ if .IsNamedParams }}
     <span class="math">{{ .Get "content" | safeHTML }}</span>
   {{ else }}
     <span class="math">{{ .Inner | safeHTML }}</span>
   {{ end }}
   ```
   在您的 Markdown 中使用它：
   ```markdown
   普通文本（不會被解析）。公式：{{< math >}}$x^2 + y^2${{< /math >}}。
   ```
   - **為何有效**：短代碼確保僅明確標記的內容被處理為數學，使普通文本中的 `( )` 保持原樣。

3. **改用 KaTeX**：
   Hugo 使用者通常偏愛 KaTeX 因為其速度。將 KaTeX 添加到 `layouts/partials/head.html`：
   ```html
   {{ if .Params.math }}
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
   <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
   <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
   <script>
     document.addEventListener("DOMContentLoaded", function() {
       renderMathInElement(document.body, {
         delimiters: [
           { left: "$$", right: "$$", display: true },
           { left: "$", right: "$", display: false }
         ]
       });
     });
   </script>
   {{ end }}
   ```
   在 front matter 中啟用它：
   ```yaml
   math: true
   ```
   使用 `$ $` 作為行內數學符號以避免 `( )` 衝突。

---

### **建議**
- **對於 Jekyll**：切換到使用 `$ $` 分隔符的 MathJax 或使用 KaTeX，以避免 `( )` 解析問題。跳脫括號是一種備用方案，但對於大型網站來說較不實用。
- **對於 Hugo**：除非您明確配置 MathJax 使用 `\( \)` 分隔符，否則您不太可能遇到此問題。使用短代碼或 KaTeX 進行數學渲染，以確保普通括號的安全。

如果您正在從 Jekyll 遷移到 Hugo 並希望保留數學內容，我建議在 Hugo 中使用 KaTeX 並配合短代碼以實現明確控制。如果您需要協助設定 Hugo 的 MathJax/KaTeX 整合或轉換 Jekyll 網站的數學內容，請告訴我！