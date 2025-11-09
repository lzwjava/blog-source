---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 macOS 上安裝 Chromium
translated: true
type: note
---

是的，macOS 絕對可以安裝 Chromium 作為 Google Chrome 的替代瀏覽器。Chromium 是 Chrome 所基於的開源核心，因此功能非常相似，但缺少某些 Google 專有功能，例如自動更新和特定編解碼器。

### 安裝方法
有幾種簡單的安裝方式：

1. **透過 Homebrew（對多數用戶最簡便）**：
   - 若尚未安裝 Homebrew，請先執行：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - 接著執行：`brew install --cask chromium`
   - 此方法適用 Intel 和 Apple Silicon（M1/M2/M3）晶片的 Mac

2. **直接下載**：
   - 前往 Chromium 官方網站下載最新 Mac 版本
   - 解壓縮後將應用程式拖曳至「應用程式」資料夾

3. **開發者或自訂版本**：
   - 可使用 Woolyss 等工具取得預編譯版本，或需要時從原始碼編譯（需安裝 Xcode）

安裝完成後，您可於「系統設定」>「桌面與 Dock」>「預設網頁瀏覽器」中將 Chromium 設為預設瀏覽器。

[下載 Chromium](https://www.chromium.org/getting-involved/download-chromium/)  
[Homebrew 配方](https://formulae.brew.sh/cask/chromium)  
[Apple Silicon 安裝指南](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[MacUpdate 下載頁面](https://chromium.macupdate.com/)  
[最新版本發佈](https://chromium.woolyss.com/download/en/)