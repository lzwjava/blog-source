---
audio: false
generated: true
image: false
lang: zh
layout: post
title: TypeScript本地环境搭建指南
translated: true
type: note
---

要在本地运行 TypeScript，通常需要使用 **npm** 和 TypeScript 编译器（`tsc`）。以下是详细步骤：

---

### 1. 初始化项目

如果尚未创建 `package.json` 文件：

```bash
npm init -y
```

这将创建用于管理依赖项的 `package.json` 文件。

---

### 2. 安装 TypeScript

作为开发依赖项安装：

```bash
npm install typescript --save-dev
```

如需全局安装 TypeScript 编译器（`tsc`）：

```bash
npm install -g typescript
```

---

### 3. 创建 tsconfig.json

生成默认配置文件：

```bash
npx tsc --init
```

这将创建控制 TypeScript 编译方式的 `tsconfig.json` 文件（包括编译目标、模块系统、严格模式等配置）。

---

### 4. 编写 TypeScript 文件

示例 `index.ts`：

```ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

console.log(greet("World"));
```

---

### 5. 编译 TypeScript

执行命令：

```bash
npx tsc
```

这将根据 `tsconfig.json` 编译所有 `.ts` 文件。

若只需编译单个文件：

```bash
npx tsc index.ts
```

编译后将生成对应的 `.js` 文件（如 `index.js`）。

---

### 6. 运行编译后的 JavaScript

使用 Node.js 运行：

```bash
node index.js
```

---

### 7. 可选：保存时自动编译

使用 `--watch` 参数实现编辑时自动重新编译：

```bash
npx tsc --watch
```

---

👉 这就是标准工作流程：
`npm install` → `tsc`（编译）→ `node`（运行编译后的代码）。

---

需要我继续演示如何通过 `ts-node` **跳过手动编译步骤**直接运行 TypeScript 吗？