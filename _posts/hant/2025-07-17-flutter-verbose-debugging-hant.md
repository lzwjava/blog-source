---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Flutter 詳細模式除錯指南
translated: true
type: note
---

啊，明白了 👍 — 沒錯，Flutter 有個 **詳細模式**，會把幕後執行的*所有*操作都列印出來，這樣你就能看到它在哪個步驟卡住了。

---

### ✅ 使用詳細日誌執行 `flutter` 指令

只需加上 `-v`（或 `--verbose`）參數：

- 執行 `flutter clean`：
  ```bash
  flutter clean -v
  ```

- 獲取依賴項：
  ```bash
  flutter pub get -v
  ```

- 運行應用程式：
  ```bash
  flutter run -v
  ```

這會將詳細日誌（網絡請求、檔案刪除、pod 指令等）輸出到終端機。

---

### 📌 閱讀詳細日誌的小技巧
- 查看停止回應前顯示的**最後幾行** → 這會告訴你卡在哪個步驟。
- 通常卡頓發生在：
  - **CocoaPods** 解析階段（網絡緩慢／資源庫過時）。
  - **Gradle sync** 階段（Android 建置時）。
  - 權限問題（如果 Flutter 無法存取某些目錄）。

---

👉 如果 `flutter clean -v` 仍然看似卡住，請將它列印的最後約 20 行內容貼到這裡 ⬇️，我可以幫你分析具體卡住的位置。

需要我幫你寫一個**帶有詳細輸出的快捷清理腳本**嗎？這樣你就能直接執行 `./super_clean.sh`，而不用逐個輸入指令了。