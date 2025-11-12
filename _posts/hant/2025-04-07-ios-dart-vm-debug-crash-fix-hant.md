---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: iOS Dart 虛擬機除錯崩潰修復
translated: true
type: note
---

你遇到的是 iOS 與 Dart VM 互動的已知問題：在 **除錯（JIT）模式** 下的 Dart VM 需要在運行時將記憶體頁面設為可執行，而近期 iOS 版本收緊了政策，導致 `mprotect(..., PROT_EXEC)` 失敗並返回 `13（權限不足）`。這會使 Dart VM 在完成程式碼時中止，並產生你貼上的崩潰記錄（SIGABRT）。這並非你的 Flutter 應用程式程式碼錯誤，而是平台（iOS／系統政策）與 VM 模式不匹配所致。（[GitHub][1]）

### 快速總結／根本原因

* 除錯版本使用 Dart **JIT**（熱重載／熱重啟），需要變更記憶體保護以讓生成的機器碼可執行。近期 iOS 版本封鎖了此操作，導致 `mprotect failed: 13（權限不足）` 及 Dart VM 中的斷言失敗。（[GitHub][1]）

---

### 立即解決方案（選擇適合你工作流程的一種）

1. **在模擬器上運行** — 模擬器運行 x86／arm 模擬器程式碼，JIT 限制不會生效，因此除錯與熱重載功能正常。
   指令：`flutter run -d <模擬器-id>`（或從 Xcode 開啟）。（[GitHub][1]）

2. **在裝置上使用 profile 或 release（AOT）模式** — 建置 AOT 程式碼，使 VM 無需在運行時使用 mprotect 變更頁面權限。你將失去熱重載功能，但應用程式可在裝置上運行。

   * 如需測試安裝：執行 `flutter build ios --release`，然後透過 Xcode 或 `flutter install --release` 安裝。
   * 或直接執行 `flutter run --profile`／`flutter run --release`。（[GitHub][1]）

3. **使用較舊的 iOS 裝置／作業系統**（僅作為臨時測試）：此限制出現在某些 iOS 測試版／版本中；運行在政策收緊前 iOS 版本的裝置不會觸發此斷言。（不適合長期使用。）（[Stack Overflow][2]）

---

### 長期解決方案／建議

* **更新 iOS／Xcode** — Apple 在不同測試版中調整了行為；有時後續的 iOS 測試版修復了行為或變更了政策。如果你正在使用引入此限制的 iOS 測試版，請更新至包含修復的版本。（有報告指出某些 iOS 測試版引入／回歸了此問題，而後續測試版已修復或變更了行為。）（[Stack Overflow][2]）

* **將 Flutter／Dart 升級至最新穩定版** — Flutter／Dart 團隊在 GitHub 問題中追蹤此問題，並在平台變更後發布了更新／解決方案；請確保你的 Flutter 與 Dart 為最新版本。升級後，執行 `flutter clean` 並重新建置。（[GitHub][3]）

* **關注上游問題** — 存在關於 iOS JIT／mprotect 失敗的活躍 Flutter 問題與 PR。訂閱 Flutter 問題討論串以獲取永久修復或推薦的開發工作流程。（如需連結我可提供。）（[GitHub][1]）

---

### 關於你同時看到的 `UIScene` 訊息的補充說明

頂部的 `UIScene` 生命週期訊息（「`UIScene lifecycle will soon be required`…」）是 iOS 關於遷移至現代基於場景的應用程式生命週期（iOS 13+）的**警告**。它與 `mprotect` 崩潰無關。你可暫時忽略它，或若想消除警告可遷移至使用 Scenes（實作 `SceneDelegate`／更新 `Info.plist`）。這並非 SIGABRT 的成因。（[GitHub][1]）

---

### 我目前推薦的具體步驟

1. 若需保留熱重載功能：在**模擬器**上運行。
   `flutter run -d <模擬器-id>`

2. 若想立即在實體裝置上測試：建置 **release／profile**（AOT）版本。
   `flutter run --release`（或 `flutter build ios --release` + 安裝）

3. 更新你的環境：升級 iOS（若正在使用有問題的測試版）、更新 Xcode、升級 Flutter／Dart、執行 `flutter clean`，然後在裝置上重試。

4. 若你願意，可貼上 `flutter doctor -v` 的輸出及你測試所用的確切 iOS／裝置版本，我將提供最具體的後續步驟（例如：「此 iOS 版本已知有問題 — 請更新至 X.Y.Z 或使用 release 版本建置」）。

---

### 連結／參考資料（以便你追蹤上游討論）

* GitHub Flutter 問題追蹤除錯模式 JIT／`mprotect failed: 13`（討論與解決方案）。（[GitHub][1]）
* StackOverflow 討論串報告相同 `mprotect failed: 13` 於 iOS 測試版 — 指出平台回歸問題及 iOS 測試版修復。（[Stack Overflow][2]）
* 解釋 iOS 26／Flutter 摩擦及推薦開發選項的部落格／總結。（[Medium][4]）

---

若你需要，我可以：

* 提供用於建置 release IPA 並安裝到你裝置的確切 `flutter` 指令，或
* 檢查你的 `flutter doctor -v` 及裝置作業系統版本，以推薦當前最佳單一行動。

你傾向哪一種？

[1]: https://github.com/flutter/flutter/issues/163984?utm_source=chatgpt.com "Debug mode and hot reload fail on iOS 26 due to JIT ..."
[2]: https://stackoverflow.com/questions/79473408/flutter-ios-18-4-debug-build-error-mprotect-failed-13-permission-denied?utm_source=chatgpt.com "Flutter iOS 18.4 Debug Build Error: mprotect failed"
[3]: https://github.com/flutter/flutter/actions/runs/15564769770?utm_source=chatgpt.com "Debug mode and hot reload fail on iOS 26 due to JIT ..."
[4]: https://vijay-mishra.medium.com/flutter-vs-ios26-what-broke-and-what-to-do-36c6d6bf1e16?utm_source=chatgpt.com "Flutter vs iOS 26: What Broke and How to Fix It - Vijay Mishra"