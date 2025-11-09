---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 理解 atk-bridge 警告訊息
translated: true
type: note
---

這條警告訊息出現在 Linux 系統（特別是 Ubuntu）上基於 GTK 的應用程式（如 Firefox、Snap Store 或 GitHub CLI）中。這並非錯誤——僅為資訊性提示。「atk-bridge」模組曾用於連接無障礙功能工具包（ATK）以配合螢幕閱讀器及其他輔助功能，但較新版本的 GTK（約從 3.22 開始）已直接內建此功能。載入獨立模組變得多餘，因此 GTK 會跳過載入並記錄此提示。

此提示無害且不影響應用程式效能，但若它使終端機輸出雜亂，您可透過在執行應用程式前設定環境變數 `NO_AT_BRIDGE=1` 來隱藏它。例如：

```bash
export NO_AT_BRIDGE=1
firefox  # 或任何會觸發此提示的應用程式
```

若要永久設定，請將該 export 指令加入您的 `~/.bashrc` 或 `~/.profile` 檔案中。

### 參考資料
- [Not loading module "atk-bridge": The functionality is provided by GTK natively](https://stackoverflow.com/questions/75406844/not-loading-module-atk-bridge-the-functionality-is-provided-by-gtk-natively)
- [When launching firefox, get error Not loading module "atk-bridge"](https://askubuntu.com/questions/1462267/when-launching-firefox-get-error-not-loading-module-atk-bridge)
- [giving message when run any gh commad: Not loading module "atk-bridge"](https://github.com/cli/cli/issues/9043)