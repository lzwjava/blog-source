---
audio: false
generated: true
lang: hant
layout: post
title: Xvfb：無頭 X11 顯示伺服器
translated: true
type: note
---

### 什麼是 Xvfb？

Xvfb（X Virtual Framebuffer）是一個 X11 顯示伺服器，可在無需實體顯示器或硬體圖形加速的情況下執行圖形應用程式。它本質上是一個「無頭」X 伺服器，在記憶體中模擬顯示器，讓需要圖形環境的程式（例如瀏覽器、GUI 測試或渲染工具）能在沒有顯示器、鍵盤或滑鼠的伺服器或環境中執行。

它常用於自動化測試（例如使用 Selenium 進行網頁爬取或 UI 測試）、CI/CD 流程，或任何需要在背景執行 X11 應用程式且不在螢幕上顯示內容的場景。

### Xvfb 如何運作？

1. **虛擬顯示器建立**：
   - 啟動 Xvfb 時，它會建立一個完全存在於 RAM 中的虛擬顯示器（例如 `:99` 或其他顯示器編號）。該顯示器具有您在啟動時指定的解析度、色深等參數。
   - 範例指令：`Xvfb :99 -screen 0 1024x768x24`（啟動一個解析度為 1024x768、24 位元色的虛擬顯示器）。

2. **處理圖形操作**：
   - Xvfb 攔截來自應用程式的 X11 協定請求（例如繪製視窗、渲染影像或處理事件）。
   - 它不會將輸出傳送到實體螢幕，而是在記憶體緩衝區（「framebuffer」）中執行所有操作。此緩衝區就像一個虛擬螢幕，像素被寫入但從不顯示。
   - 它支援基本的 X11 功能，但缺乏硬體加速，因此不適用於高效能圖形（如遊戲）— 更適用於簡單渲染或測試。

3. **事件模擬**：
   - Xvfb 可以模擬輸入事件（例如滑鼠/鍵盤），但通常應用程式會像在真實顯示器上一樣執行。
   - 輸出不可見，但您可以擷取螢幕截圖或將 framebuffer 轉儲到檔案中（使用 `xwd` 或 ImageMagick 的 `import` 等工具）進行驗證。

4. **與工具整合**：
   - 像 pyvirtualdisplay（如錯誤追蹤中所示）這樣的函式庫封裝了 Xvfb，使其更容易從程式碼中啟動/停止。例如，在 Python 中：
     ```python
     from pyvirtualdisplay import Display
     display = Display(visible=0, size=(1024, 768))
     display.start()
     # 在此執行您的圖形應用程式
     display.stop()
     ```
   - 它在背景執行，您的應用程式設定 `DISPLAY` 環境變數（例如 `export DISPLAY=:99`）以指向虛擬伺服器。

5. **限制**：
   - 無真實硬體互動，因此不支援 GPU 或直接視訊輸出。
   - 記憶體使用量可能隨解析度提高或長時間執行而增加。
   - 它是 X.org 專案的一部分，可在 Linux/Unix 系統上使用；不原生支援 macOS 或 Windows（儘管 Windows 有像 Xming 這樣的替代方案）。

關於您貼上的錯誤：似乎您的系統未安裝 Xvfb（`FileNotFoundError` 針對 'Xvfb'）。在 macOS 上（根據您的 Homebrew 路徑），您可以透過 `brew install --cask xvfb` 或類似指令安裝，但請確認它已在您的 PATH 中。pyvirtualdisplay 依賴於它作為可執行檔可用。

[Xvfb 手冊頁](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml)  
[維基百科：Xvfb](https://en.wikipedia.org/wiki/Xvfb)  
[如何使用 Xvfb 進行無頭測試](https://www.browserstack.com/guide/what-is-xvfb)