---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 建立您的代理伺服器
translated: true
type: post
---

* 設定伺服器，請使用Outline Manager: [https://getoutline.org](https://getoutline.org)。

* 推薦的託管供應商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr和Linode。為達到最佳效能，選擇新加坡或東京的伺服器位置。雖然香港也是一個可行的選項，但請注意，像ChatGPT和Claude這樣的某些AI工具在該地區受到限制。

* 您仍然可以在香港伺服器上使用Deepseek、Mistral、Grok和Gemini API（通過Cursor）。由於其他人可能會避開香港伺服器，因此它們往往不會擁擠。

* 考慮伺服器位置和距離。對於廣州的用戶來說，香港是託管代理伺服器的好選擇。使用Speedtest測量網絡速度。

* 為了獲得最佳速度，我建議使用含有BGP（高級）彈性IP的阿里雲香港伺服器。彈性IP功能允許快速替換當前IP。阿里雲雲的優化BGP（高級）連接確保快速性能。該服務每1GB流量收費3元人民幣。

* 如Shadowsocks、VMess和Trojan等協議很容易被禁止。

* Linode的IP轉移功能允許您快速將伺服器遷移到新位置，從而獲得新的IP地址。

* 您可能需要一個腳本來每天自動更新伺服器。

* 如果代理伺服器被GFW封禁或遇到其他問題，可以使用中國電信澳門SIM卡與您的筆記本電腦共享蜂窩數據。這樣可以設置新的伺服器。

* 對於像Google Cloud Platform這樣的雲服務，配置新伺服器需要現有的代理伺服器。然而，像DigitalOcean或Vultr這樣的供應商可以直接設置而不需要代理伺服器。

* 使用[Auto SS Config](https://github.com/lzwjava/lzwjava.github.io/blob/main/scripts/auto-ss-config/upload_configs.py)生成並上傳Shadowsocks或Clash訂閱URL。

* 使用DigitalOcean中的快照功能。如果伺服器的IP被封禁，從伺服器的快照創建一個新的Droplet並再次運行`install.sh`。

* 使用DigitalOcean中的保留IP功能。如果伺服器的IP被封禁，分配一個新的保留IP。

* 我們使用Outline Manager設置我們自己的伺服器，因為它快速且允許我們獨享伺服器。VPN提供商的節點往往不可靠。我們的伺服器也可能會出現問題，但我們對情況有更詳細的了解。我們還可以選擇不同的雲服務供應商。此外，我們知道我們是否使用中國電信還是中國移動，以及我們是否使用家庭Wi-Fi還是蜂窩數據。

* 在路由器上安裝OpenWrt設置代理可能不會有用。主要問題是GFW可以輕易封禁您的代理伺服器的IP地址。最好使用訂閱方法，例如Clash，以便在路由器上輕鬆更改設置。