---
audio: false
generated: true
image: false
lang: hant
layout: post
title: TypeScript 本地安裝指南步驟
translated: true
type: note
---

要在本地執行 TypeScript，通常會使用 **npm** 和 TypeScript 編譯器 (`tsc`)。以下是逐步指南：

---

### 1. 初始化專案

如果還沒有 `package.json`：

```bash
npm init -y
```

這會建立一個 `package.json`，方便你管理依賴項。

---

### 2. 安裝 TypeScript

將其安裝為開發依賴項：

```bash
npm install typescript --save-dev
```

如果還想讓 TypeScript 編譯器 (`tsc`) 在全局可用：

```bash
npm install -g typescript
```

---

### 3. 建立 tsconfig.json

生成默認配置檔案：

```bash
npx tsc --init
```

這會建立 `tsconfig.json`，用於控制 TypeScript 如何編譯你的檔案（目標、模組系統、嚴格模式等）。

---

### 4. 編寫 TypeScript 檔案

範例 `index.ts`：

```ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("World"));
```

---

### 5. 編譯 TypeScript

執行：

```bash
npx tsc
```

這會根據 `tsconfig.json` 編譯所有 `.ts` 檔案。

或者，僅編譯單一檔案：

```bash
npx tsc index.ts
```

這會生成一個 `.js` 檔案（例如 `index.js`）。

---

### 6. 執行編譯後的 JavaScript

使用 Node.js：

```bash
node index.js
```

---

### 7. 可選：儲存時自動編譯

使用 `--watch` 參數執行，以便在編輯時重新編譯：

```bash
npx tsc --watch
```

---

👉 這就是標準工作流程：
`npm install` → `tsc`（編譯）→ `node`（執行編譯後的程式碼）。

---

需要我示範如何使用 `ts-node` **跳過手動編譯**直接執行 TypeScript 嗎？