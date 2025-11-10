---
audio: false
generated: true
image: false
lang: ja
layout: post
title: TypeScriptローカルセットアップガイド手順
translated: true
type: note
---

TypeScriptをローカルで実行するには、通常**npm**とTypeScriptコンパイラ（`tsc`）を使用します。以下にステップバイステップのガイドを示します：

---

### 1. プロジェクトの初期化

`package.json`がまだない場合：

```bash
npm init -y
```

これにより依存関係を管理できる`package.json`が作成されます。

---

### 2. TypeScriptのインストール

開発依存関係としてインストール：

```bash
npm install typescript --save-dev
```

TypeScriptコンパイラ（`tsc`）をグローバルで利用可能にしたい場合：

```bash
npm install -g typescript
```

---

### 3. tsconfig.jsonの作成

デフォルトの設定ファイルを生成：

```bash
npx tsc --init
```

これにより`tsconfig.json`が作成され、TypeScriptがファイルをコンパイルする方法（ターゲット、モジュールシステム、strictモードなど）を制御します。

---

### 4. TypeScriptファイルの作成

例 `index.ts`：

```ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("World"));
```

---

### 5. TypeScriptのコンパイル

実行：

```bash
npx tsc
```

これにより`tsconfig.json`に従ってすべての`.ts`ファイルがコンパイルされます。

または、単一ファイルのみをコンパイルする場合：

```bash
npx tsc index.ts
```

これにより`.js`ファイル（例：`index.js`）が生成されます。

---

### 6. コンパイルされたJavaScriptの実行

Node.jsを使用：

```bash
node index.js
```

---

### 7. オプション：保存時の自動コンパイル

`--watch`フラグ付きで実行すると、編集時に自動的に再コンパイル：

```bash
npx tsc --watch
```

---

👉 これが標準的なワークフローです：
`npm install` → `tsc`（コンパイル） → `node`（コンパイルされたコードの実行）。

---

手動コンパイルをスキップして`ts-node`でTypeScriptを直接実行する方法も紹介しましょうか？