---
audio: false
generated: true
lang: hant
layout: post
title: 在 Node.js 中使用 Debug 套件進行除錯
translated: true
type: note
---

### 重點摘要
- 「在 npm 中除錯」很可能是指於 npm 管理的 Node.js 專案中使用 debug 套件進行日誌記錄。
- 研究顯示需先透過 `npm install debug` 安裝套件，然後在程式碼中使用命名空間，例如 `require('debug')('myapp:component')`。
- 證據傾向透過設定 `DEBUG` 環境變數來啟用除錯輸出，例如 `DEBUG=myapp:component npm run start`。

### 安裝與使用 Debug 套件
要在 Node.js 專案中使用 debug 套件，請先透過 npm 安裝：
- 在專案目錄中執行 `npm install debug`。

接著在 JavaScript 程式碼中引入套件並建立帶有命名空間的 debug 實例：
- 範例：`const debug = require('debug')('myapp:component'); debug('some message');`。

### 啟用除錯輸出
要查看除錯訊息，請在執行應用程式時設定 `DEBUG` 環境變數：
- 例如執行 `DEBUG=myapp:component node app.js`，或若使用 npm 指令則執行 `DEBUG=myapp:component npm run start`。

### 控制命名空間
您可以使用萬用字元或排除語法來控制顯示哪些除錯訊息：
- 使用 `DEBUG=myapp:* node app.js` 啟用多個命名空間。
- 使用 `DEBUG=*,-myapp:exclude node app.js` 排除特定命名空間。

---

### 調查筆記：深入探索在 npm 中使用 Debug

本節基於現有文件與資源，提供在 npm 管理的 Node.js 專案中使用 debug 套件的全面概述。重點在於實務操作、進階功能及開發者注意事項，確保無論是初學者或資深使用者都能獲得透徹理解。

#### npm 環境下的 Debug 簡介
「在 npm 中除錯」這個說法很可能是指於 npm（Node Package Manager）管理的專案中使用 debug 套件——一個輕量級的 Node.js 與瀏覽器環境除錯工具。鑑於 debug 套件在搜尋結果中的突出地位及其與 Node.js 開發的關聯性，此解讀符合開發者在 npm 管理專案中對日誌記錄與除錯的常見需求。該套件目前版本為 4.4.0（截至近期更新），已被 npm 註冊表中超過 55,746 個其他專案採用，顯示其在生態系中的標準地位。

#### 安裝與基礎用法
首先使用 npm 安裝 debug 套件：
- 指令：`npm install debug`
- 這會將套件加入專案的 `node_modules` 並更新 `package.json`。

在 JavaScript 程式碼中引入套件，並使用命名空間初始化以分類除錯訊息：
- 範例：`const debug = require('debug')('myapp:component');`
- 使用 debug 實例記錄訊息：`debug('some message');`
- 命名空間（如 'myapp:component'）有助識別訊息來源，方便在大型應用中篩選日誌。

要查看這些除錯訊息，請在執行應用程式時設定 `DEBUG` 環境變數：
- 範例：`DEBUG=myapp:component node app.js`
- 若應用程式透過 npm 指令啟動（例如 `npm run start`），請使用：`DEBUG=myapp:component npm run start`
- 此環境變數控制啟用哪些命名空間，確保無需修改程式碼即可實現選擇性除錯。

#### 進階功能與設定
Debug 套件提供多項進階功能以提升可用性：

##### 命名空間控制與萬用字元
- 使用萬用字元啟用多個命名空間：`DEBUG=myapp:* node app.js` 將顯示所有以 'myapp:' 開頭的命名空間除錯訊息。
- 使用減號排除特定命名空間：`DEBUG=*,-myapp:exclude node app.js` 會啟用除 'myapp:exclude' 開頭外的所有命名空間。
- 這種選擇性除錯對於專注於應用程式的特定部分而不被日誌淹沒至關重要。

##### 色彩編碼與視覺解析
- 除錯輸出包含基於命名空間名稱的色彩編碼，輔助視覺解析。
- 在 Node.js 中，當 stderr 是 TTY（終端機）時預設啟用色彩，並可透過安裝 `supports-color` 套件與 debug 搭配使用以獲得更廣的色域。
- 在瀏覽器中，色彩適用於 WebKit 系檢查器、Firefox（31 版及以後）及 Firebug，提升開發工具中的可讀性。

##### 時間差與效能洞察
- 此套件可顯示除錯呼叫間的時間差，前綴為 "+NNNms"，對效能分析很有用。
- 此功能自動啟用，當 stdout 非 TTY 時使用 `Date#toISOString()`，確保跨環境一致性。

##### 環境變數與自訂設定
多個環境變數可微調除錯輸出：
| 名稱               | 用途                               |
|--------------------|------------------------------------|
| DEBUG              | 啟用/停用命名空間                  |
| DEBUG_HIDE_DATE    | 在非 TTY 輸出中隱藏日期            |
| DEBUG_COLORS       | 強制在輸出中使用色彩               |
| DEBUG_DEPTH        | 設定物件檢查深度                   |
| DEBUG_SHOW_HIDDEN  | 顯示物件中的隱藏屬性               |

- 例如，設定 `DEBUG_DEPTH=5` 允許更深層的物件檢查，對複雜資料結構很有用。

##### 自訂輸出的格式器
Debug 支援不同資料類型的自訂格式器，提升日誌可讀性：
| 格式器 | 呈現方式                           |
|--------|------------------------------------|
| %O     | 美化物件（多行顯示）               |
| %o     | 美化物件（單行顯示）               |
| %s     | 字串                               |
| %d     | 數字（整數/浮點數）                |
| %j     | JSON，處理循環參照                 |
| %%     | 單一百分比符號                     |

- 可擴充自訂格式器，例如 `createDebug.formatters.h = (v) => v.toString('hex')` 用於十六進位輸出。

#### 與 npm 指令的整合
對於使用 npm 指令的專案，整合 debug 十分順暢：
- 如有需要，可修改 `package.json` 中的指令以包含除錯設定，但通常於執行時設定 `DEBUG` 即可。
- 範例指令：`"start": "node app.js"`，執行時使用 `DEBUG=myapp:component npm run start`。
- Windows 使用者請使用 CMD 的 `set DEBUG=* & node app.js` 或 PowerShell 的 `$env:DEBUG='*';node app.js`，確保跨平台相容性。

#### 瀏覽器支援與特殊情況
雖然主要針對 Node.js，debug 也支援瀏覽器環境：
- 使用 Browserify 等工具建置，或透過 [browserify-as-a-service](https://wzrd.in/standalone/debug@latest) 服務進行客戶端引入。
- 在瀏覽器中使用 `localStorage.debug` 持久化啟用狀態，例如 `localStorage.debug = 'worker:*'`。
- 注意：Chromium 系瀏覽器（Brave、Chrome、Electron）可能需要啟用「Verbose」日誌等級以獲得完整功能。

#### 最佳實踐與注意事項
- 使用具描述性的命名空間（如 "connect:bodyParser"）以保持日誌清晰度。
- 在命名空間後附加 "*" 以實現始終啟用的除錯，例如 `DEBUG=connect:*`。
- 在生產環境中，確保未設定 `DEBUG` 以避免不必要的日誌記錄，因為除錯語句在未啟用變數時是靜默的。
- 考量效能：debug 是輕量級的，僅在啟用時記錄日誌，使其適用於開發環境且不影響生產環境。

#### 意外細節：除錯 npm 本身
雖然主要焦點是 debug 套件，但需注意「在 npm 中除錯」可能被誤解為除錯 npm 工具本身（例如 `npm install` 問題）。對此類情況，請使用 npm 的 `--verbose` 旗標獲取詳細輸出，但這與使用 debug 套件不同。此區別對於探索 npm 相關除錯的使用者很重要，儘管上下文顯示套件更為相關。

#### 結論
在 npm 管理的 Node.js 專案中使用 debug 套件，提供了強大且靈活的方式來實現選擇性除錯。透過 `npm install debug` 安裝、使用命名空間引入、並透過 `DEBUG` 控制輸出，開發者能有效管理日誌、以色彩提升可讀性並分析效能。此方法符合現代開發實踐，在除錯工作流程中提供了細節與控制間的平衡。

**主要參考文獻：**
- [debug npm 套件詳細使用指南](https://www.npmjs.com/package/debug)