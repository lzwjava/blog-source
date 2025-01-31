---
audio: true
lang: hant
layout: post
title: 設置您的代理伺服器
translated: true
---

* 設定伺服器，請使用 Outline Manager: [https://getoutline.org](https://getoutline.org)。

* 建議的主機提供商包括 DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr 和 Linode。為了獲得最佳性能，選擇新加坡或東京的伺服器位置。雖然香港也是一個可行的選擇，但請注意，某些人工智慧工具如 ChatGPT 和 Claude 在該地區受到限制。

* 您仍然可以在香港伺服器上使用 Deepseek、Mistral、Grok 和 Gemini API（通過 Cursor）。由於其他人可能會避免使用香港伺服器，因此這些伺服器通常不會擁擠。

* 考慮伺服器位置和距離。對於廣州的用戶來說，香港是設置代理伺服器的好選擇。使用 Speedtest 來測量網絡速度。

* 如果您關心速度，據我所知，最好的選擇是使用阿里雲香港伺服器和 BGP（高級）彈性 IP。這個 IP 是彈性的，這使得綁定新 IP 變得容易，如果當前的 IP 被封禁。此外，這個 BGP（高級）連接由阿里雲优化，提供快速速度。

* 如 Shadowsocks、VMess 和 Trojan 等協議可能會輕易被封禁。

* 使用 Linode 進行快速伺服器遷移。

* 您可能需要一個腳本來每天自動更新您的伺服器。

* 如果代理伺服器被 GFW 封禁或遇到其他問題，您可以使用中國電信澳門 SIM 卡與您的筆記本電腦共享流量。這使您能夠設置一個新伺服器。

* 對於 Google Cloud Platform 等雲服務，配置一個新伺服器需要一個現有的代理伺服器。然而，如 DigitalOcean 或 Vultr 等提供商可以直接設置而無需代理伺服器。

* 使用 [Auto SS Config](https://github.com/lzwjava/auto-ss-config) 生成和上傳 Shadowsocks 或 Clash 訂閱 URL。

* 使用 Digital Ocean 中的快照功能。如果伺服器的 IP 被封禁，從伺服器的快照創建一個新的 Droplet 並再次運行 `install.sh`。

* 使用 Digital Ocean 中的保留 IP 功能。如果伺服器的 IP 被封禁，分配一個新的保留 IP。

* 我們使用 Outline Manager 來設置我們的伺服器，因為它快速且讓我們能夠自己享受伺服器。 VPN 提供商的節點通常不可靠。我們的伺服器也可能會遇到問題，但我們對情況有更詳細的了解。我們還可以選擇不同的雲提供商。此外，我們知道我們是否使用中國電信或中國移動，以及我們是否使用家庭 Wi-Fi 或行動數據。

* 在路由器上安裝 OpenWrt 來設置代理可能沒有用。主要問題是 GFW 可以輕易封禁您的代理伺服器 IP 地址。最好使用訂閱方法，如與 Clash，輕鬆在您的路由器上更改設置。