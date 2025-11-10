---
audio: false
generated: true
image: false
lang: hant
layout: post
title: macOS Homebrew 上的 Nginx 配置
translated: true
type: note
---

對於透過 Homebrew 在 macOS 上安裝的 Nginx（如二進位檔案路徑 `/opt/homebrew/bin/nginx` 所示），主要設定檔通常位於：

```
/opt/homebrew/etc/nginx/nginx.conf
```

此目錄還包含其他相關檔案，例如位於 `servers/` 子目錄中的伺服器區塊（例如 `/opt/homebrew/etc/nginx/servers/`）。

要確認您的 Nginx 實例使用的確切設定檔路徑，請在終端機中執行以下指令：

```
nginx -t
```

這將測試設定並輸出正在使用的 `nginx.conf` 檔案路徑。或者，使用 `nginx -V` 查看編譯時詳細資訊，包括設定路徑前綴。

如果您使用的是較舊的 Intel 架構 Mac，Homebrew 會安裝到 `/usr/local` 目錄，此時路徑應為 `/usr/local/etc/nginx/nginx.conf`，但您提供的二進位檔案路徑確認了當前使用 `/opt/homebrew` 位置。

**參考資料**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)