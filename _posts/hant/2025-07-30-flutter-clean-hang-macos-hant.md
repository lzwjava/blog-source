---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 解決 Flutter Clean 在 macOS 上的卡頓問題
translated: true
type: note
---

啊，我明白你的意思了 👍  
有時候在 macOS 上 `flutter clean` 看起來會「卡住」——特別是當有大量生成檔案，或是 Xcode 的 `DerivedData` 資料夾太大的時候。

---

### ✅ 嘗試以下步驟

1. **取消卡住的指令**
   按下 `CTRL + C`。

2. **手動清理（效果與 `flutter clean` 相同）**  
   你可以自行刪除這些建置/快取資料夾：
   ```bash
   rm -rf build/ .dart_tool/ ios/Pods ios/Podfile.lock ios/Flutter/Flutter.framework ios/Flutter/Flutter.podspec
   ```

   如果你也想清除 Xcode 的快取：
   ```bash
   rm -rf ~/Library/Developer/Xcode/DerivedData
   ```

3. **重新取得依賴項**
   ```bash
   flutter pub get
   ```

4. **重新安裝 CocoaPods（適用於 iOS）**
   ```bash
   cd ios
   pod install --repo-update
   cd ..
   ```

5. **再次建置/執行**
   ```bash
   flutter run
   ```

---

⚡ **提示：** 清理後的第一次建置可能會花費較長時間（因為 Flutter 需要重新生成 `.dart_tool`、`.pub-cache`、iOS Pods 等），但不應該永遠卡住。如果你持續看到它「卡住」，可能與以下原因有關：

- **過時的 Flutter SDK** → 執行 `flutter upgrade`
- **過時的 CocoaPods** → 執行 `sudo gem install cocoapods`  
- **Rosetta / M1 晶片問題**：如果你使用 Apple Silicon，根據你的設定，有時需要在 `ios` 資料夾內執行 `arch -x86_64 pod install`。

---

👉 需要我提供一個**一行指令腳本**來清除建置快取並重置 Pods（基本上就是「超級清理」），這樣你就不需要除錯 `flutter clean` 卡住的問題嗎？