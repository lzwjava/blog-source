---
audio: true
lang: hant
layout: post
title: 設置您的代理伺服器
---

* 要設置伺服器，請使用Outline Manager：[https://getoutline.org](https://getoutline.org)。  
* 推薦的託管服務提供商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr或Linode。建議選擇新加坡或東京地區。避免使用香港地區，因為像ChatGPT和Claude這樣的工具在那裡被禁止。  
* Shadowsocks、VMess和Trojan等協議容易被封禁。  
* 使用Linode可以快速遷移伺服器。  
* 您可能需要一個腳本每天自動續訂伺服器。  
* 如果代理伺服器被GFW封禁或遇到其他問題，您可以使用中國電信澳門SIM卡與筆記本電腦共享移動數據。這樣可以設置新的伺服器。  
* 對於像Google Cloud Platform這樣的雲服務，配置新伺服器需要現有的代理伺服器。然而，像DigitalOcean或Vultr這樣的提供商可以直接設置，不需要代理伺服器。
* 使用[Auto SS Config](https://github.com/lzwjava/auto-ss-config)生成並上傳Shadowsocks或Clash訂閱URL。
* 使用Digital Ocean的快照功能。如果伺服器的IP被封禁，從伺服器的快照創建新的droplet並再次運行`install.sh`。