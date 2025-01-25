---
audio: true
lang: zh
layout: post
title: 设置您的代理服务器
translated: true
---

* 要设置服务器，请使用Outline Manager：[https://getoutline.org](https://getoutline.org)。  

* 推荐的托管服务提供商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr或Linode。首选新加坡或东京地区。避免使用香港地区，因为像ChatGPT和Claude这样的工具在那里被禁止。

* 如果您不介意ChatGPT和Claude在香港被禁，香港仍然是一个不错的选择。您可以使用Deepseek、Mistral、Grok和Gemini API等工具与香港服务器配合使用。

* Shadowsocks、VMess和Trojan等协议容易被封禁。  

* 使用Linode进行快速服务器迁移。  

* 您可能需要一个脚本来每天自动续订服务器。  

* 如果代理服务器被GFW封禁或遇到其他问题，您可以使用中国电信澳门SIM卡与笔记本电脑共享蜂窝数据。这样您就可以设置新的服务器。  

* 对于像Google Cloud Platform这样的云服务，配置新服务器需要现有的代理服务器。然而，像DigitalOcean或Vultr这样的提供商可以直接设置，无需代理服务器。

* 使用[Auto SS Config](https://github.com/lzwjava/auto-ss-config)生成并上传Shadowsocks或Clash订阅URL。

* 使用Digital Ocean的快照功能。如果服务器的IP被封禁，从服务器的快照创建新的droplet并再次运行`install.sh`。

* 使用Digital Ocean的保留IP功能。如果服务器的IP被封禁，分配一个新的保留IP。

* 我们使用Outline Manager来设置自己的服务器，因为它速度快，并且可以让我们独自享受服务器。VPN提供商的节点通常不可靠。我们的服务器也可能出现问题，但我们对情况有更详细的了解。我们还可以选择不同的云提供商。此外，我们知道我们使用的是中国电信还是中国移动，以及我们使用的是家庭Wi-Fi还是蜂窝数据。

* 在路由器上安装OpenWrt来设置代理可能没有用。主要问题是GFW可以轻松封禁您的代理服务器的IP地址。最好使用订阅方法，比如Clash，以便在路由器上轻松更改设置。