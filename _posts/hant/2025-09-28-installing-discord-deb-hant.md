---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: 安裝 Discord DEB 檔案的方法
translated: true
type: note
---

要安裝 `discord-0.0.111.deb` 檔案，你可以使用以下幾種方法：

**方法一：使用 dpkg（指令行）**
```bash
sudo dpkg -i discord-0.0.111.deb
```

如果遇到依賴性問題，請執行：
```bash
sudo apt-get install -f
```

**方法二：使用 apt（推薦）**
```bash
sudo apt install ./discord-0.0.111.deb
```

此方法比 dpkg 能更好地自動處理依賴性問題。

**方法三：使用 gdebi（如已安裝）**
```bash
sudo gdebi discord-0.0.111.deb
```

**方法四：圖形介面方法**
如果你使用桌面環境，通常可以雙擊 .deb 檔案，它會在套件管理程式（例如軟體中心）中開啟以供安裝。

**必要條件：**
- 請確保你位於包含 .deb 檔案的目錄中
- 你需要擁有 sudo 權限
- 如果你尚未取得該檔案，可以從 Discord 官方網站下載

**安裝後：**
你應該可以從應用程式選單啟動 Discord，或在終端機中執行 `discord` 指令來啟動。

你比較想使用哪種方法，或是需要任何特定步驟的協助嗎？