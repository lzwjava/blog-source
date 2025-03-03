---
audio: false
generated: true
lang: hant
layout: post
title: 調試 Node.js 使用 Debug 套件
translated: true
---

### 主要要點
- "debug in npm" 似乎指的是在 npm 管理的 Node.js 專案中使用 "debug" 套件進行記錄。
- 研究建議使用 `npm install debug` 安裝套件，然後在程式碼中使用命名空間，例如 `require('debug')('myapp:component')`。
- 証據顯示，可以通過設置 `DEBUG` 環境變量來啟用調試輸出，例如 `DEBUG=myapp:component npm run start`。

### 安裝和使用 Debug 套件
要在 Node.js 專案中使用 "debug" 套件，首先使用 npm 安裝它：
- 在專案目錄中運行 `npm install debug`。

然後，在 JavaScript 程式碼中，要求套件並使用命名空間創建一個調試實例：
- 範例：`const debug = require('debug')('myapp:component'); debug('some message');`。

### 啟用調試輸出
要查看調試訊息，在運行應用程序時設置 `DEBUG` 環境變量：
- 例如，運行 `DEBUG=myapp:component node app.js` 或 `DEBUG=myapp:component npm run start`（如果使用 npm 腳本）。

### 控制命名空間
可以使用通配符或排除來控制顯示哪些調試訊息：
- 使用 `DEBUG=myapp:* node app.js` 啟用多個命名空間。
- 使用 `DEBUG=*,-myapp:exclude node app.js` 排除特定命名空間。

---

### 調查筆記：詳細探討在 npm 中使用 Debug

本節提供了在 npm 管理的 Node.js 專案中使用 "debug" 套件的全面概述，基於可用的文檔和資源。重點在於實際實施、高級功能以及開發者的考量，確保初學者和有經驗的用戶都能全面理解。

#### 在 npm 環境中介紹 Debug
"debug in npm" 這個短語最有可能指的是在 npm（Node Package Manager）管理的專案中使用 "debug" 套件，這是一個輕量級的調試工具，適用於 Node.js 和瀏覽器環境。根據 "debug" 套件在搜索結果中的突出地位以及其與 Node.js 開發的相關性，這種解釋符合開發者在 npm 管理的專案中進行記錄和調試的常見需求。該套件目前版本為 4.4.0，根據最近的更新，在 npm 註冊表中有超過 55,746 個其他專案採用它，這表明其在生態系統中的標準地位。

#### 安裝和基本使用
首先，使用 npm 安裝 "debug" 套件：
- 命令：`npm install debug`
- 這將套件添加到專案的 `node_modules` 並更新 `package.json`。

在 JavaScript 程式碼中，要求套件並使用命名空間初始化它，以分類調試訊息：
- 範例：`const debug = require('debug')('myapp:component');`。
- 使用調試實例記錄訊息：`debug('some message');`。
- 命名空間，例如 'myapp:component'，有助於識別訊息的來源，使得在大型應用程序中過濾日誌更加容易。

要查看這些調試訊息，在運行應用程序時設置 `DEBUG` 環境變量：
- 範例：`DEBUG=myapp:component node app.js`。
- 如果應用程序通過 npm 腳本啟動（例如 `npm run start`），使用：`DEBUG=myapp:component npm run start`。
- 這個環境變量控制啟用哪些命名空間，確保在不修改程式碼的情況下進行選擇性調試。

#### 高級功能和配置
"debug" 套件提供了幾個高級功能，以提高可用性：

##### 命名空間控制和通配符
- 使用通配符啟用多個命名空間：`DEBUG=myapp:* node app.js` 將顯示所有以 'myapp:' 開頭的命名空間的調試訊息。
- 使用減號排除特定命名空間：`DEBUG=*,-myapp:exclude node app.js` 啟用所有命名空間，但排除以 'myapp:exclude' 開頭的命名空間。
- 這種選擇性調試對於專注於應用程序的特定部分而不被日誌淹沒至關重要。

##### 顏色編碼和視覺解析
- 调试输出包括基于命名空间名称的颜色编码，有助于视觉解析。
- 默认情况下，当 stderr 是 Node.js 中的 TTY（终端）时，颜色是启用的，并且可以通过与 debug 一起安装 `supports-color` 套件来增强颜色调色板。
- 在浏览器中，颜色在基于 WebKit 的检查器、Firefox（版本 31 及以上）和 Firebug 中工作，增强了开发工具中的可读性。

##### 时间差异和性能见解
- 该套件可以显示调试调用之间的时间差异，前缀为 "+NNNms"，有助于性能分析。
- 该功能默认启用，并在 stdout 不是 TTY 时使用 `Date#toISOString()`，确保跨环境的一致性。

##### 环境变量和自定义
几个环境变量微调调试输出：
| 名稱             | 目的                              |
|------------------|--------------------------------------|
| DEBUG            | 啟用/禁用命名空間                  |
| DEBUG_HIDE_DATE  | 在非 TTY 输出中隱藏日期               |
| DEBUG_COLORS     | 强制在输出中使用颜色                 |
| DEBUG_DEPTH      | 设置对象检查深度                   |
| DEBUG_SHOW_HIDDEN| 在对象中显示隐藏属性               |

- 例如，設置 `DEBUG_DEPTH=5` 允許更深的對象檢查，對於複雜的數據結構非常有用。

##### 格式化器用於自定義輸出
Debug 支持不同數據類型的自定義格式化器，增強日誌的可讀性：
| 格式化器 | 表示                      |
|-----------|-------------------------------------|
| %O        | 美化打印对象（多行）|
| %o        | 美化打印对象（单行）   |
| %s        | 字符串                              |
| %d        | 数字（整数/浮点）              |
| %j        | JSON，处理循环引用   |
| %%        | 单个百分号                 |

- 自定義格式化器可以擴展，例如 `createDebug.formatters.h = (v) => v.toString('hex')` 以十六進制輸出。

#### 与 npm 脚本的集成
对于使用 npm 脚本的项目，集成 debug 是无缝的：
- 修改 `package.json` 脚本以包含调试设置（如果需要），但通常在运行时设置 `DEBUG` 即可。
- 示例脚本：`"start": "node app.js"`，运行 `DEBUG=myapp:component npm run start`。
- 对于 Windows 用户，使用 CMD 与 `set DEBUG=* & node app.js` 或 PowerShell 与 `$env:DEBUG='*';node app.js`，确保跨平台兼容性。

#### 浏览器支持和边缘情况
虽然主要用于 Node.js，但 debug 也支持浏览器环境：
- 使用工具如 Browserify 或服务如 [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) 进行客户端包含。
- 使用 `localStorage.debug` 在浏览器中保留启用状态，例如 `localStorage.debug = 'worker:*'`。
- 注意：基于 Chromium 的浏览器（Brave、Chrome、Electron）可能需要启用“详细”日志级别以获得完全功能。

#### 最佳实践和考虑
- 使用描述性命名空间，例如 "connect:bodyParser"，以保持日志的清晰度。
- 将 "*" 附加到命名空间以始终启用调试，例如 `DEBUG=connect:*`。
- 对于生产环境，确保 `DEBUG` 未设置以避免不必要的日志记录，因为调试语句在没有该变量的情况下是静默的。
- 考虑性能：debug 是轻量级的，只有在启用时才记录，因此适合开发而不会影响生产。

#### 意外细节：调试 npm 本身
虽然主要关注的是 "debug" 套件，但值得一提的是，"debug in npm" 可能会被误解为调试 npm 工具（例如 `npm install` 问题）。对于这种情况，使用 npm 的 `--verbose` 标志以获取详细输出，但这与使用 debug 套件不同。这种区别对于探索与 npm 相关的调试的用户很重要，尽管上下文表明套件更相关。

#### 结论
在 npm 管理的 Node.js 项目中使用 "debug" 套件提供了一种强大、灵活的实现选择性调试的方法。通过 `npm install debug` 安装、使用命名空间要求它，并通过 `DEBUG` 控制输出，开发者可以高效地管理日志、增强可读性并分析性能。这种方法符合现代开发实践，在调试工作流中提供了细节和控制的平衡。

**关键引用：**
- [debug npm 套件详细使用指南](https://www.npmjs.com/package/debug)