---
audio: false
generated: true
lang: hant
layout: post
title: Node.js OpenSSL 相容性
translated: true
---

當運行 `ng build` 時，使用 **Node.js 22.9.0** 和 **npm 10.8.3**，您會遇到以下錯誤：

```
error 0308010C digital envelope routines::unsupported
```

這個錯誤通常是由於 Node.js 的新版本（例如 22.9.0，使用 OpenSSL 3.0 或更高版本）與某些加密算法之間的兼容性問題引起的，這些加密算法是由 Angular 使用的工具（如 Webpack）所依賴的。以下是解決此問題的步驟指南。

---

### 解決方案

#### 步驟 1：啟用 OpenSSL 遺留提供者
最簡單且立即的修復方法是通過設置 `NODE_OPTIONS` 環境變量來啟用 OpenSSL 遺留提供者。這允許 Node.js 使用在 OpenSSL 3.0+ 中不再默認支持的較舊加密算法。

- **適用於 macOS/Linux**：
  打開終端並運行：
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **適用於 Windows（命令提示符）**：
  打開命令提示符並運行：
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **適用於 Windows（PowerShell）**：
  打開 PowerShell 並運行：
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

設置環境變量後，再次運行 `ng build`。這應該在大多數情況下通過允許 Node.js 處理不受支持的例程來解決錯誤。

---

#### 步驟 2：驗證並更新 Angular CLI（如果需要）
如果在步驟 1 後錯誤仍然存在，您的 Angular CLI 版本可能與 Node.js 22.9.0 並不完全兼容。將其更新到最新版本可能會有所幫助。

- 檢查當前的 Angular CLI 版本：
  ```bash
  ng --version
  ```

- 全局更新 Angular CLI：
  ```bash
  npm install -g @angular/cli
  ```

- 然後，再次嘗試運行 `ng build`。

---

#### 步驟 3：檢查並更新項目依賴項（可選）
如果問題仍未解決，項目中的過時依賴項可能會引起問題。為此：

- 打開 `package.json` 文件並檢查依賴項的版本（例如 `@angular/core`、`@angular/cli` 等）。
- 將其小心更新到最新的兼容版本：
  ```bash
  npm install
  ```
  或，如果您想更新所有依賴項：
  ```bash
  npm update
  ```

- 再次運行 `ng build` 進行測試。

*注意*：請謹慎更新，因為它們可能會引入中斷變更。更新後，請彻底測試您的應用程序。

---

#### 步驟 4：降級 Node.js（最後的手段）
如果以上解決方案都無效，Node.js 22.9.0 可能尚未完全支持您項目的當前配置。降級到 Node.js 的長期支持（LTS）版本，例如 **20.x** 或 **18.x**，可能會解決問題。

- 卸載當前的 Node.js 版本。
- 從 [官方 Node.js 網站](https://nodejs.org/) 下載並安裝 LTS 版本。
- 驗證已安裝的版本：
  ```bash
  node -v
  ```
- 重新安裝項目依賴項：
  ```bash
  npm install
  ```
- 再次運行 `ng build`。

---

### 推薦方法
從 **步驟 1**（設置 `NODE_OPTIONS`）開始，因為這是最快的修復方法，並允許您繼續使用 Node.js 22.9.0。如果這無效，請繼續進行 **步驟 2** 和 **步驟 3**。僅在必要時使用 **步驟 4**，因為降級 Node.js 可能會限制對新功能的訪問。

這應該解決 "error 0308010C digital envelope routines::unsupported" 並讓您的 `ng build` 命令再次運行！