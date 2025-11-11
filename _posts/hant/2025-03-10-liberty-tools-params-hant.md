---
audio: false
generated: true
lang: hant
layout: post
title: 在 Liberty Tools 插件中傳遞自訂 JVM 參數
translated: true
type: note
---

您可以透過在 VS Code 的 Liberty 開發模式啟動設定中新增自訂 JVM 參數（例如 `-Dversion=5.1`）。通常，您需要編輯（或建立）專案中的 `.vscode/launch.json` 檔案，並將參數包含在 `"vmArgs"` 屬性下（如果您的設定預期是 Maven 目標參數，則使用 `"args"`）。

舉例來說，如果您使用 Liberty Tools 擴充套件進行開發模式，您的設定可能如下所示：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "liberty",
      "request": "launch",
      "name": "Liberty Dev Mode",
      "goal": "dev",
      "vmArgs": "-Dversion=5.1"
    }
  ]
}
```

### 步驟：
1. **開啟或建立啟動設定：**
   - 在 VS Code 中開啟您的專案。
   - 導航至 `.vscode` 資料夾並開啟（或建立）`launch.json` 檔案。

2. **新增您的開發模式設定：**
   - 如上所示新增設定項目。關鍵屬性 `"vmArgs"` 可讓您指定在開發模式啟動時傳遞給伺服器的 JVM 選項。

3. **儲存並啟動：**
   - 儲存檔案。
   - 使用「執行與偵錯」視窗來啟動「Liberty Dev Mode」設定。

如果您直接使用 Maven，也可以透過命令列啟動開發模式：

```bash
mvn liberty:dev -Dversion=5.1
```

這會在啟動伺服器時將自訂屬性傳遞給 JVM。

透過這種方式設定，Liberty Tools 擴充套件將在每次啟動開發模式時包含您的自訂參數（`-Dversion=5.1`）。