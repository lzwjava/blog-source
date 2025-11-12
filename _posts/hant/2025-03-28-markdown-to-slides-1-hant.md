---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Markdown 簡報輕鬆製作
translated: true
type: note
---

Marp CLI 讓你能將 Markdown 檔案轉換成簡報（HTML、PDF、PPTX）。如果你希望以純 Markdown 編寫簡報並盡量減少格式調整，它尤其實用。

以下是逐步指南：

---

### 1. 安裝 Marp CLI

你需要先安裝 Node.js。

```bash
npm install -g @marp-team/marp-cli
```

檢查安裝：

```bash
marp --version
```

---

### 2. 編寫 Markdown 簡報

建立檔案，例如 `slides.md`。

```markdown
---
marp: true
theme: default
paginate: true
---

# Hello, Marp!

---

## 第二頁

- 項目 1
- 項目 2
```

重點：

* `---`（YAML frontmatter）啟用 Marp 和配置。
* `---`（內容之間）分隔簡報頁。

---

### 3. 在瀏覽器預覽

執行帶自動重新載入的本地伺服器：

```bash
marp -p slides.md
```

在瀏覽器中開啟 [http://localhost:8080](http://localhost:8080)。

---

### 4. 匯出簡報

生成不同格式：

* HTML（自包含）：

  ```bash
  marp slides.md -o slides.html
  ```

* PDF：

  ```bash
  marp slides.md -o slides.pdf
  ```

* PowerPoint（PPTX）：

  ```bash
  marp slides.md -o slides.pptx
  ```

---

### 5. 實用選項

* **監聽變更**（自動重建）：

  ```bash
  marp -w slides.md
  ```

* **設定主題**（default、gaia、uncover 或自訂 CSS）：

  ```bash
  marp --theme-set ./my-theme.css slides.md -o slides.html
  ```

* **包含演講者備註**：

  ```markdown
  ---
  marp: true
  ---

  # 標題

  <!--
  這是演講者備註
  -->
  ```

---

### 6. 編輯器整合

* VSCode 有 [Marp 擴充功能](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)。
* 它能在編輯 Markdown 時顯示即時預覽。

---

👉 透過此設定，你可以在幾分鐘內從純 `.md` 檔案生成精美的簡報。

需要我提供**即用型 Markdown 範本檔案**（包含標題頁、議程、內容和結尾頁）讓你立即開始嗎？