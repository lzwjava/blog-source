---
audio: false
generated: true
lang: hant
layout: post
title: 在 Jekyll 中使用 KaTeX
translated: true
type: note
---

若要在您現有的 Jekyll 設定中使用 KaTeX 替代 MathJax，您需要將 MathJax 腳本替換為 KaTeX 並調整 Jekyll 配置。KaTeX 比 MathJax 更快速輕量，但需採用不同方法，因為它不支援 MathJax 的所有功能（例如自動方程式編號需手動處理）。以下是在 Jekyll 網站中切換至 KaTeX 的逐步指南：

### 1. 更新 Jekyll 配置
修改 `_config.yml` 以設定 Kramdown 使用 KaTeX 作為數學引擎。更新 `kramdown` 區段如下：

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

這會指示 Kramdown 使用 KaTeX 而非 MathJax 來渲染 LaTeX 數學表達式。

### 2. 在 HTML 中引入 KaTeX
從 HTML 中移除 MathJax 腳本並替換為 KaTeX。您可透過 CDN 引入 KaTeX。將以下代碼添加到 Jekyll 佈局文件（例如 `_layouts/default.html`）的 `<head>` 區段：

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- 自動渲染擴展（可選，用於數學表達式自動渲染） -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- 自動渲染配置 -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // 區塊數學
        {left: "\\[", right: "\\]", display: true}, // 區塊數學
        {left: "\\(", right: "\\)", display: false}, // 行內數學
        {left: "$", right: "$", display: false} // 行內數學
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. 移除 MathJax 配置
從佈局文件中刪除與 MathJax 相關的代碼，包括 `<script type="text/x-mathjax-config">` 區塊和 MathJax CDN 腳本。KaTeX 不像 MathJax 的 `tex2jax` 那樣需要配置，上述自動渲染腳本已處理類似功能。

### 4. 在 Markdown 中編寫數學公式
配置好 KaTeX 和 Kramdown 後，您可使用與之前相同的分隔符在 Markdown 文件中編寫 LaTeX 數學公式：

- **行內數學**：使用 `$...$` 或 `\(...\)`（例如 `$E=mc^2$` 或 `\(E=mc^2\)`）。
- **區塊數學**：使用 `$$...$$` 或 `\[...\]`（例如 `$$E=mc^2$$` 或 `\[E=mc^2\]`）。

例如：

```markdown
行內數學：$E=mc^2$ 或 \(E=mc^2\)。

區塊數學：
$$E=mc^2$$

或

\[E=mc^2\]
```

Kramdown 配合 KaTeX 數學引擎會將這些內容處理成 KaTeX 可渲染的 HTML。

### 5. KaTeX 與 MathJax 對比須知
- **自動方程式編號**：KaTeX 不支援像 MathJax 的 `autoNumber: "AMS"` 那樣的自動編號功能。若需要方程式編號，必須在 LaTeX 代碼中手動使用 `\tag{}` 添加（例如 `$$E=mc^2 \tag{1}$$`）。
- **效能**：KaTeX 比 MathJax 快得多，非常適合像 Jekyll 這樣的靜態網站。
- **功能集**：KaTeX 支援的 LaTeX 指令比 MathJax 少。請查閱 [KaTeX 支援函數列表](https://katex.org/docs/supported.html)以確保您的數學表達式相容。
- **渲染**：上述自動渲染腳本透過在指定分隔符內自動渲染數學表達式來模擬 MathJax 的行為。若需變更或限制分隔符，請調整腳本中的 `delimiters` 陣列。

### 6. 測試設定
在本地運行 Jekyll 網站（`jekyll serve`）並驗證數學表達式是否正確渲染。若遇到問題：
- 檢查瀏覽器控制台是否有 KaTeX 相關錯誤。
- 確認 KaTeX CDN 網址為最新版本（以上使用的是 0.16.11 版，截至本文撰寫時為最新）。
- 確保您的 Markdown 文件使用有效的 KaTeX 相容 LaTeX 語法。

### 7. 可選：本地 KaTeX 文件
若希望避免 CDN 依賴而本地托管 KaTeX 文件：
1. 從 [KaTeX GitHub 發布頁](https://github.com/KaTeX/KaTeX/releases)下載 `katex.min.css`、`katex.min.js` 和 `auto-render.min.js`。
2. 將它們放入 Jekyll 資源資料夾（例如 `assets/katex/`）。
3. 更新 `<link>` 和 `<script>` 標籤以指向本地文件（例如 `/assets/katex/katex.min.css`）。

### 8. 疑難排解
- **數學公式未渲染**：確認 KaTeX 腳本正確加載且 `kramdown.math_engine` 設為 `katex`。
- **分隔符問題**：驗證自動渲染腳本中的分隔符與 Markdown 中的使用是否匹配。
- **不支援的指令**：若 LaTeX 指令失效，請查閱 KaTeX 文件了解支援的指令，或改寫表達式。

若需要針對特定數學表達式或配置的具體協助，請提供詳細資訊，我將為您提供量身訂製的指導！