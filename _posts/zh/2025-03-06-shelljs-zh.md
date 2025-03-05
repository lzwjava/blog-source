---
audio: false
generated: true
lang: zh
layout: post
title: 使用 ShellJS 执行 Shell 命令
translated: true
---

ShellJS 是一个为 Node.js 项目提供 Unix 命令行命令（如 `cp`、`mkdir`、`exec` 等）的 JavaScript 库。它通过允许你在 JavaScript 中直接执行熟悉的命令行命令，简化了跨平台脚本的编写。然而，在前端开发中——通常指在浏览器中运行的代码——ShellJS 不能直接应用，因为它依赖于浏览器环境中不可用的 Node.js API。

### 为什么 ShellJS 不能在浏览器中运行
- **Node.js 依赖**：ShellJS 基于 Node.js 运行时，提供文件系统访问、进程执行和其他系统级操作的 API。这些 API 在浏览器中不可用，因为其沙盒安全模型。
- **浏览器安全限制**：浏览器防止 JavaScript 访问本地文件系统或执行任意命令，以保护用户免受恶意脚本的侵害。由于 ShellJS 命令如 `exec`（运行外部进程）或 `cp`（复制文件）依赖这些功能，因此它们在浏览器环境中无法正常工作。

因此，你不能在浏览器中运行的客户端 JavaScript 中直接使用 ShellJS。然而，ShellJS 仍然可以在前端开发工作流中发挥有价值的作用，通过将其集成到你的构建过程或开发工具中，这些工具通常在 Node.js 上运行。

### 如何在前端开发工作流中使用 ShellJS
虽然 ShellJS 不能在浏览器中执行，但你可以在 Node.js 脚本中利用它来自动化支持前端开发的任务。前端项目通常依赖于 Webpack、Gulp 或 Grunt 等构建工具，这些工具在 Node.js 上运行，并且可以集成 ShellJS 来简化工作流程。以下是如何做到这一点的方法：

#### 1. 安装 ShellJS
首先，确保你的系统上安装了 Node.js。然后，使用 npm 或 yarn 将 ShellJS 添加到你的项目中：

```bash
npm install shelljs
```

或

```bash
yarn add shelljs
```

#### 2. 创建一个使用 ShellJS 的 Node.js 脚本
编写一个使用 ShellJS 执行与前端项目相关任务的脚本，例如复制文件、创建目录或运行命令行工具。将此脚本保存为 `.js` 文件（例如 `build.js`）。

以下是一个准备前端资产的示例脚本：

```javascript
const shell = require('shelljs');

// 如果不存在，创建一个构建目录
shell.mkdir('-p', 'build');

// 将 HTML 文件复制到构建目录
shell.cp('-R', 'src/*.html', 'build/');

// 将 Sass 编译为 CSS
shell.exec('sass src/styles.scss build/styles.css');

// 复制 JavaScript 文件
shell.cp('-R', 'src/*.js', 'build/');
```

- **`shell.mkdir('-p', 'build')`**：创建一个 `build` 目录，`-p` 确保如果它已经存在则不会出错。
- **`shell.cp('-R', 'src/*.html', 'build/')`**：将所有 HTML 文件从 `src` 复制到 `build`，`-R` 用于递归复制。
- **`shell.exec('sass src/styles.scss build/styles.css')`**：运行 Sass 编译器生成 CSS。

#### 3. 将脚本集成到你的工作流中
你可以通过以下几种方式运行此脚本：
- **直接通过 Node.js**：
  ```bash
  node build.js
  ```
- **作为 npm 脚本**：将其添加到你的 `package.json` 中：
  ```json
  "scripts": {
    "build": "node build.js"
  }
  ```
  然后运行：
  ```bash
  npm run build
  ```
- **与构建工具一起使用**：将 ShellJS 集成到 Gulp 等工具中。例如：
  ```javascript
  const gulp = require('gulp');
  const shell = require('shelljs');

  gulp.task('build', function(done) {
    shell.exec('sass src/styles.scss build/styles.css');
    shell.cp('-R', 'src/*.js', 'build/');
    done();
  });
  ```

#### 4. 前端开发中的使用场景
ShellJS 可以自动化前端工作流中的各种任务：
- **资产管理**：将图像、字体或其他静态文件复制到构建目录。
- **CSS/JavaScript 处理**：通过 `shell.exec` 运行 Sass、PostCSS 或 UglifyJS 等工具。
- **测试和代码检查**：执行测试运行器或代码检查工具（例如 `shell.exec('eslint src/*.js')`）。
- **部署准备**：打包文件或清理目录（例如 `shell.rm('-rf', 'build/*')`）。

### 示例：自动化前端构建过程
假设你正在构建一个使用 HTML、Sass 和 JavaScript 的简单 Web 应用程序。以下是你如何使用 ShellJS 来自动化构建的方法：

**目录结构**：
```
project/
├── src/
│   ├── index.html
│   ├── styles.scss
│   └── app.js
├── build.js
└── package.json
```

**build.js**：
```javascript
const shell = require('shelljs');

// 清理构建目录
shell.rm('-rf', 'build/*');

// 创建构建目录
shell.mkdir('-p', 'build');

// 复制 HTML
shell.cp('src/index.html', 'build/');

// 编译 Sass
shell.exec('sass src/styles.scss build/styles.css');

// 复制 JavaScript
shell.cp('src/app.js', 'build/');
```

**package.json**：
```json
{
  "scripts": {
    "build": "node build.js"
  },
  "dependencies": {
    "shelljs": "^0.8.5"
  }
}
```

运行 `npm run build`，ShellJS 将准备好 `build` 目录中的编译和复制文件，准备部署。

### 关键要点
- **不适用于浏览器**：由于其依赖于 Node.js 和系统级操作，ShellJS 不能在浏览器中运行。
- **适用于构建脚本**：在 Node.js 脚本中使用它来自动化前端任务，如文件操作和命令执行。
- **跨平台**：ShellJS 确保你的脚本在 Windows、Linux 和 macOS 上一致工作，使其适合多样化的开发环境。

通过将 ShellJS 集成到你的 Node.js 电源构建过程中，你可以通过强大的自动化增强前端开发工作流，即使它不能直接在浏览器中运行。