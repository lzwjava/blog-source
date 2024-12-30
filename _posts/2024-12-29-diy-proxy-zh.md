---
audio: true
lang: zh
layout: post
title: 搭建代理服务器
---

* 要搭建服务器，请使用Outline Manager：[https://getoutline.org](https://getoutline.org)。  
* 推荐的托管服务提供商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr或Linode。优先选择新加坡或东京区域。避免使用香港区域，因为像ChatGPT和Claude等工具在那里被禁止。  
* Shadowsocks、VMess和Trojan等协议很容易被封禁。  
* 使用Linode可以快速迁移服务器。  
* 您可能需要编写脚本以每天自动更新服务器。  
* 如果代理服务器被GFW封禁或遇到其他问题，可以使用中国电信澳门SIM卡与笔记本电脑共享蜂窝数据，从而搭建新的服务器。  
* 对于Google Cloud Platform等云服务，配置新服务器需要现有的代理服务器。然而，像DigitalOcean或Vultr这样的提供商可以直接设置，无需代理服务器。