---
audio: false
generated: false
lang: hant
layout: post
title: Node.js OpenSSL 兼容性
translated: true
type: note
---

當使用 **Node.js 22.9.0** 和 **npm 10.8.3** 執行 `ng build` 時，您遇到以下錯誤：

```
error 0308010C digital envelope routines::unsupported
```

此錯誤通常是由於新版本的 Node.js（如 22.9.0，它使用 OpenSSL 3.0 或更高版本）與某些加密演算法之間的相容性問題所引起，這些演算法被像 Webpack 這樣的工具（Angular 在底層使用）所依賴。以下是一個逐步指南來解決此問題。

---

### 解決方案

#### 步驟 1：啟用 OpenSSL 傳統供應商
最簡單且最直接的解決方法是通過設置 `NODE_OPTIONS` 環境變數來啟用 OpenSSL 傳統供應商。這允許 Node.js 使用在 OpenSSL 3.0+ 中預設不再支援的舊版加密演算法。

- **適用於 macOS/Linux**：
  打開終端機並執行：
  ```bash
  export NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **適用於 Windows (命令提示字元)**：
  打開命令提示字元並執行：
  ```cmd
  set NODE_OPTIONS=--openssl-legacy-provider
  ng build
  ```

- **適用於 Windows (PowerShell)**：
  打開 PowerShell 並執行：
  ```powershell
  $env:NODE_OPTIONS="--openssl-legacy-provider"
  ng build
  ```

設置環境變數後，再次執行 `ng build`。這應該在大多數情況下通過允許 Node.js 處理不支援的常式來解決錯誤。

---

#### 步驟 2：驗證並更新 Angular CLI（如果需要）
如果在步驟 1 後錯誤仍然存在，您的 Angular CLI 版本可能與 Node.js 22.9.0 不完全相容。將其更新到最新版本可能會有所幫助。

- 檢查您當前的 Angular CLI 版本：
  ```bash
  ng --version
  ```

- 全域更新 Angular CLI：
  ```bash
  npm install -g @angular/cli
  ```

- 然後，再次嘗試執行 `ng build`。

---

#### 步驟 3：檢查並更新專案依賴項（可選）
如果問題仍未解決，您專案中過時的依賴項可能是問題所在。為了解決這個問題：

- 打開您的 `package.json` 檔案並檢視依賴項的版本（例如 `@angular/core`、`@angular/cli` 等）。
- 謹慎地將它們更新到最新的相容版本：
  ```bash
  npm install
  ```
  或者，如果您想更新所有依賴項：
  ```bash
  npm update
  ```

- 再次執行 `ng build` 進行測試。

*注意*：更新時請小心，因為它們可能會引入破壞性變更。之後請徹底測試您的應用程式。

---

#### 步驟 4：降級 Node.js（最後手段）
如果以上解決方案都無效，Node.js 22.9.0 可能尚未被您專案的當前配置完全支援。降級到 Node.js 的長期支援（LTS）版本，例如 **20.x** 或 **18.x**，可能會解決問題。

- 解除安裝您當前的 Node.js 版本。
- 從 [官方 Node.js 網站](https://nodejs.org/) 下載並安裝一個 LTS 版本。
- 驗證安裝的版本：
  ```bash
  node -v
  ```
- 重新安裝您的專案依賴項：
  ```bash
  npm install
  ```
- 再次執行 `ng build`。

---

### 推薦方法
從**步驟 1**（設置 `NODE_OPTIONS`）開始，因為這是最快的解決方法，並且允許您繼續使用 Node.js 22.9.0。如果無效，請繼續進行**步驟 2** 和**步驟 3**。僅在必要時使用**步驟 4**，因為降級 Node.js 可能會限制對新功能的訪問。

這應該能解決 "error 0308010C digital envelope routines::unsupported" 錯誤，並讓您的 `ng build` 指令再次正常運作！