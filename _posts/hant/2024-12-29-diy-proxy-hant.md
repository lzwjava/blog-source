---
audio: true
lang: hant
layout: post
title: 设置您的代理服务器
---

* 要设置服务器，请使用Outline Manager：[https://getoutline.org](https://getoutline.org)。  
* 推荐的托管服务提供商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr或Linode。优先选择新加坡或东京地区。避免使用香港地区，因为像ChatGPT和Claude这样的工具在那里被禁止。  
* Shadowsocks、VMess和Trojan等协议容易被封禁。  
* 使用Linode可以快速迁移服务器。  
* 您可能需要一个脚本来每天自动续订服务器。  
* 如果代理服务器被GFW封禁或遇到其他问题，您可以使用中国电信澳门SIM卡与笔记本电脑共享蜂窝数据。这样您就可以设置一个新的服务器。  
* 对于像Google Cloud Platform这样的云服务，配置新服务器需要现有的代理服务器。然而，像DigitalOcean或Vultr这样的提供商可以直接设置，不需要代理服务器。
* 使用[Auto SS Config](https://github.com/lzwjava/auto-ss-config)生成并上传Shadowsocks或Clash订阅URL。
* 使用Digital Ocean的快照功能。如果服务器的IP被封禁，从服务器的快照创建一个新的droplet并再次运行`install.sh`。