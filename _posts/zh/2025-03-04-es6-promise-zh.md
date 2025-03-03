---
audio: false
generated: true
lang: zh
layout: post
title: ES6 风格的 Promises
translated: true
---

### 关键点
- 要在 npm 中使用 `es6-promise` 包，首先使用 `npm install es6-promise` 安装它。
- 然后可以在 JavaScript 代码中 require 它，以便在本地使用 Promise 类或为更广泛的兼容性进行全局填充。
- 研究表明，现代环境支持本地承诺，因此该包主要用于较旧的系统或特定需求。

### 安装
在项目目录中使用 npm 安装包：
- 运行命令：`npm install es6-promise`。

### 使用
使用该包有两种主要选项：

#### 本地使用
如果要在代码中使用 Promise 类而不影响全局作用域：
- require 包并像这样使用它：
  ```javascript
  const Promise = require('es6-promise').Promise;
  // 然后根据需要使用 Promise，例如 new Promise((resolve, reject) => {...});
  ```

#### 全局填充
为了确保全局 Promise 设置为 `es6-promise` 实现，特别是对于较旧的环境：
- 使用填充方法：
  ```javascript
  require('es6-promise').polyfill();
  // 现在，全局 Promise 将使用 es6-promise 实现。
  ```
- 或者，进行自动填充：
  ```javascript
  require('es6-promise/auto');
  ```

### 意外细节
请注意，`es6-promise` 自六年前以来没有更新，这可能会引发安全和与较新 JavaScript 功能兼容性的问题，尽管它在其预期用途中仍然功能齐全。

---

### 调查说明：详细探讨在 npm 中使用 `es6-promise` 包

本节提供了在 npm 项目中使用 `es6-promise` 包的全面概述，扩展了直接答案，并提供了额外的上下文、技术细节和开发人员的考虑因素。信息结构模仿专业文章，确保包含分析中的所有相关详细信息，并使用表格以便于理解。

#### `es6-promise` 简介
`es6-promise` 包是一个轻量级库，作为 ES6 风格承诺的填充物，提供了组织异步代码的工具。它在缺乏或不可靠的本地 ES6 Promise 支持的环境中特别有用，例如较旧的浏览器或遗留的 Node.js 版本。鉴于其最后一次更新是在 2019 年，最新版本 4.2.8 发布于 2025 年 3 月 3 日，它是一个成熟但可能维护较少的解决方案，与现代替代方案相比。

#### 安装过程
将 `es6-promise` 集成到项目中，通过 npm 安装非常简单。命令是：
- `npm install es6-promise`

这将包安装到 `node_modules` 目录中，并将依赖项更新到 `package.json` 中。对于使用 Yarn 的用户，替代方案是 `yarn add es6-promise`，但由于用户的查询，npm 是重点。

| 安装方法 | 命令                     |
|---------------------|-----------------------------|
| npm                 | `npm install es6-promise`   |
| Yarn                | `yarn add es6-promise`      |

该包被广泛采用，npm 寄存器中有 5,528 个其他项目在使用它，这表明其在遗留或特定用例中的相关性。

#### JavaScript 中的使用
安装后，可以通过两种主要方式在 JavaScript 中使用 `es6-promise`：在代码中本地使用或作为全局填充。选择取决于项目的需求，特别是是否需要确保跨不同环境的兼容性。

##### 本地使用
对于本地使用，require 包并直接访问 Promise 类。语法是：
- `const Promise = require('es6-promise').Promise;`

这允许您在代码中使用 Promise 类而不修改全局作用域。例如：
```javascript
const Promise = require('es6-promise').Promise;
const myPromise = new Promise((resolve, reject) => {
  resolve('Success!');
});
myPromise.then(result => console.log(result)); // 输出：Success!
```

这种方法适用于项目已经支持本地承诺，但您希望使用 `es6-promise` 进行特定操作或一致性。

##### 全局填充
要填充全局环境，确保项目中所有 Promise 使用 `es6-promise` 实现，可以调用填充方法：
- `require('es6-promise').polyfill();`

这将全局 `Promise` 设置为 `es6-promise` 实现，这对于较旧的环境（如 IE<9 或遗留的 Node.js 版本）非常有用，其中本地承诺可能缺失或损坏。或者，进行自动填充：
- `require('es6-promise/auto');`

“auto” 版本，文件大小为 27.78 KB（7.3 KB gzipped），如果缺失或损坏，则自动提供或替换 `Promise`，简化了设置。例如：
```javascript
require('es6-promise/auto');
// 现在，全局 Promise 已填充，您可以在代码中使用 new Promise(...)。
```

##### 浏览器使用
虽然用户的查询集中在 npm，但值得一提的是，对于浏览器环境，可以通过 CDN 包含 `es6-promise`，例如：
- `<script src="https://cdn.jsdelivr.net/npm/es6-promise@4/dist/es6-promise.js"></script>`
- 也可以使用生产中的精简版本，例如 `es6-promise.min.js`。

然而，鉴于 npm 上下文，重点仍在 Node.js 使用。

#### 兼容性和考虑因素
该包是 rsvp.js 的子集，由 @jakearchibald 提取，旨在模仿 ES6 Promise 行为。然而，有兼容性注意事项需要考虑：
- 在 IE<9 中，`catch` 和 `finally` 是保留关键字，会导致语法错误。解决方法包括使用字符串表示法，例如 `promise['catch'](function(err) { ... });`，尽管大多数缩小器会自动修复这一点。
- 由于其最后一次更新是在 2019 年，开发人员应评估 `es6-promise` 是否满足当前的安全和兼容性需求，特别是针对目标现代 JavaScript 环境，其中本地承诺受支持。

npm 包健康分析表明，它每周下载超过 950 万次，被认为是关键生态系统项目，拥有 7,290 个 GitHub 星标，表明强大的历史社区。然而，过去 12 个月没有新版本，可能被视为已停止的项目，尽管根据存储库活动，维护被评为可持续。

#### TypeScript 和其他资源
对于 TypeScript 用户，虽然查询中没有明确提到，但请注意，可以通过 `@types/es6-promise` 安装类型定义，使用 `npm i @types/es6-promise`。这是一个存根包，因为 `es6-promise` 提供自己的类型，但它对于确保类型安全非常有用。

有关承诺的更多信息，文档建议 [JavaScript Promises HTML5Rocks 文章](http://www.html5rocks.com/en/tutorials/es6/promises/)，它提供了详细的 API 使用和模式。

#### 可能的陷阱和社区见解
一些用户可能会遇到安装问题，例如 404 错误，特别是在较旧的系统上或依赖项配置不正确时。例如，清除 `node_modules` 并重新安装可能会解决此类问题，如社区讨论中所见。此外，请确保您的 Node.js 版本支持 CommonJS requires，因为包的结构。

#### 结论
总之，`es6-promise` 是确保 npm 项目中 ES6 Promise 兼容性的有价值工具，特别是对于遗留环境。安装非常简单，使用 `npm install es6-promise`，并且可以通过 `require('es6-promise').Promise` 本地使用，或者通过 `require('es6-promise').polyfill()` 或 `require('es6-promise/auto')` 全局使用。鉴于其年龄，评估其是否适合项目的需求，特别是在现代 JavaScript 上下文中，其中本地承诺是标准。

#### 关键引用
- [es6-promise npm 包详细信息](https://www.npmjs.com/package/es6-promise)
- [es6-promise GitHub 存储库](https://github.com/stefanpenner/es6-promise)