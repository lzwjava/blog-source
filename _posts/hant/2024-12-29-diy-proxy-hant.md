---
audio: true
lang: hant
layout: post
title: 設置您的代理伺服器
translated: true
---

* 要設置伺服器，請使用Outline Manager：[https://getoutline.org](https://getoutline.org)。  

* 推薦的託管服務提供商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr或Linode。優先選擇新加坡或東京的地區。避免使用香港地區，因為像ChatGPT和Claude這樣的工具在那裡被禁止。  

* 如果您不介意ChatGPT和Claude在香港被禁止，香港仍然是一個很好的選擇。您可以使用Deepseek、Mistral、Grok和Gemini API等工具與香港伺服器配合使用。  

* Shadowsocks、VMess和Trojan等協議很容易被禁止。  

* 使用Linode進行快速伺服器遷移。  

* 您可能需要一個腳本每天自動續訂您的伺服器。  

* 如果代理伺服器被GFW禁止或遇到其他問題，您可以使用中國電信澳門SIM卡與筆記本電腦共享蜂窩數據。這使您可以設置新的伺服器。  

* 對於像Google Cloud Platform這樣的雲服務，配置新伺服器需要現有的代理伺服器。然而，像DigitalOcean或Vultr這樣的提供商可以直接設置，不需要代理伺服器。  

* 使用[Auto SS Config](https://github.com/lzwjava/auto-ss-config)生成並上傳Shadowsocks或Clash訂閱URL。  

* 使用Digital Ocean中的快照功能。如果伺服器的IP被禁止，從伺服器的快照創建新的droplet並再次運行`install.sh`。  

* 使用Digital Ocean中的保留IP功能。如果伺服器的IP被禁止，分配新的保留IP。  

* 我們使用Outline Manager設置自己的伺服器，因為它速度快且可以讓我們獨享伺服器。VPN提供商的節點通常不可靠。我們的伺服器也可能遇到問題，但我們對情況有更詳細的了解。我們還可以選擇不同的雲提供商。此外，我們知道我們使用的是中國電信還是中國移動，以及我們使用的是家庭Wi-Fi還是蜂窩數據。  

* 在路由器上安裝OpenWrt來設置代理可能沒有用。主要問題是GFW可以輕鬆禁止您的代理伺服器的IP地址。最好使用訂閱方法，如Clash，以便在路由器上輕鬆更改設置。