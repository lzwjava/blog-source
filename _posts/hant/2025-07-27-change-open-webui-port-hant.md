---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 變更 Open WebUI 連接埠
translated: true
type: note
---

若要變更執行 Open WebUI 時使用的連接埠（通常透過 pip 安裝後使用 `open-webui serve` 指令），請使用 `--port` 參數並指定您想要的連接埠號碼。預設連接埠為 8080。

### 步驟：
1. 確保已安裝 Open WebUI：  
   ```
   pip install open-webui
   ```

2. 在不同連接埠上執行伺服器（例如 3000）：  
   ```
   open-webui serve --port 3000
   ```

   - 這將使 WebUI 可透過 `http://localhost:3000`（或您的伺服器 IP 地址加上新連接埠）存取。
   - 注意：使用 `serve` 指令時會忽略 `PORT` 環境變數；您必須改用 `--port` 參數。

若您使用 Docker 而非直接安裝：
- 設定 `PORT` 環境變數，例如 `docker run -e PORT=3000 ...`。
- 使用 `-p <主機連接埠>:3000` 對外映射連接埠（請根據需要調整）。

完整安裝與設定詳情，請參閱官方文件。

[環境變數設定 | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[快速開始 | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)