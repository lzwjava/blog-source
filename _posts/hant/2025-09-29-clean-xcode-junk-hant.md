---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 釋放磁碟空間清理 Xcode 暫存檔案
translated: true
type: note
---

好問題 👍 Xcode（和 iOS 模擬器）隨著時間會累積大量垃圾——建置快取、衍生資料、模擬器裝置、裝置支援檔案、日誌等。清理這些可以釋放數 GB 空間。以下是結構化的清理方法：

---

### 1. 清除衍生資料（建置快取）

這會移除舊的建置產物、中間檔案和索引。

* 透過 **Xcode 圖形介面**：
  `Xcode → Settings → Locations → Derived Data → 點擊箭頭 → 刪除資料夾。`
* 透過 **終端機**：

  ```bash
  rm -rf ~/Library/Developer/Xcode/DerivedData/*
  ```

---

### 2. 清理模擬器資料

* 重置或刪除模擬器內容：

  ```bash
  xcrun simctl erase all
  ```

  （會清除應用程式和資料，但保留裝置定義）

* 移除所有未使用的模擬器裝置（如果你累積了舊版 iOS）：

  ```bash
  xcrun simctl delete unavailable
  ```

* 刪除所有模擬器裝置（請小心，會移除所有內容）：

  ```bash
  xcrun simctl delete all
  ```

* 手動刪除佔用大量空間的目錄：

  ```bash
  rm -rf ~/Library/Developer/CoreSimulator/Devices/*
  ```

---

### 3. 移除舊版裝置支援檔案

當你連接實體裝置時，Xcode 會下載每個 iOS 版本的除錯符號。這些檔案會不斷累積。

```bash
rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/*
```

---

### 4. 清理封存檔案

來自「Product → Archive」的應用程式封存會佔用大量空間。

* 透過 Xcode Organizer → Archives → 刪除舊封存。
* 或透過終端機：

  ```bash
  rm -rf ~/Library/Developer/Xcode/Archives/*
  ```

---

### 5. 清理日誌

```bash
rm -rf ~/Library/Developer/Xcode/DocumentationCache/*
rm -rf ~/Library/Developer/Xcode/ios device logs/*
rm -rf ~/Library/Logs/CoreSimulator/*
```

---

### 6. 清理衍生索引與模組快取

```bash
rm -rf ~/Library/Developer/Xcode/DerivedDataModuleCache/*
```

---

### 7. 可選：完全重置

如果你想完全重置 Xcode 相關快取：

```bash
rm -rf ~/Library/Developer/Xcode/*
rm -rf ~/Library/Developer/CoreSimulator/*
```

（這會移除所有內容：模擬器、封存檔案、衍生資料等。下次啟動 Xcode 會像「全新安裝」一樣。）

---

⚠️ **提示**

* 執行這些指令前，請務必先關閉 Xcode 和模擬器。
* 使用 `du -sh ~/Library/Developer/*` 查看哪些資料夾佔用空間最大。
* 有時在 Xcode 中使用 `Clean Build Folder`（`⇧⌘K`）就足夠了，但深度清理能釋放更多空間。

---

需要我提供一個**單一指令稿**，讓你一次清理所有常見垃圾嗎（可選擇性加入旗標）？