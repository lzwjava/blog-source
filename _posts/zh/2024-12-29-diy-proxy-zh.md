---
audio: true
lang: zh
layout: post
title: 设置您的代理服务器
translated: true
---

* 要设置服务器，请使用Outline Manager: [https://getoutline.org](https://getoutline.org)。

* 推荐的托管提供商包括DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr和Linode。为了获得最佳性能，选择新加坡或东京的服务器位置。虽然香港也是一个可行的选项，但请注意，某些AI工具如ChatGPT和Claude在该地区受到限制。

* 你仍然可以在香港服务器上使用Deepseek、Mistral、Grok和Gemini API（通过Cursor）。由于其他人可能会避开香港服务器，它们往往不太拥堵。

* 考虑服务器位置和距离。对于广州的人来说，香港是托管代理服务器的好选择。使用Speedtest测量网络速度。

* 如果你在乎速度，据我所知，最好的选择是使用阿里云香港服务器和BGP（高级）弹性IP。IP是弹性的，这使得如果当前IP被封禁，绑定新的IP变得容易。此外，这种BGP（高级）连接由阿里云优化，提供快速速度。

* 协议如Shadowsocks、VMess和Trojan很容易被封禁。

* 使用Linode进行快速服务器迁移。

* 你可能需要一个脚本来每天自动续订你的服务器。

* 如果代理服务器被GFW封禁或遇到其他问题，你可以使用中国电信澳门SIM卡与你的笔记本电脑共享移动数据。这使你能够设置一个新的服务器。

* 对于像Google Cloud Platform这样的云服务，配置新服务器需要现有的代理服务器。但是，像DigitalOcean或Vultr这样的提供商可以直接设置，而不需要代理服务器。

* 使用[Auto SS Config](https://github.com/lzwjava/auto-ss-config)生成和上传Shadowsocks或Clash订阅URL。

* 使用Digital Ocean中的快照功能。如果服务器的IP被封禁，从服务器的快照创建一个新的droplet，然后再次运行`install.sh`。

* 使用Digital Ocean中的保留IP功能。如果服务器的IP被封禁，分配一个新的保留IP。

* 我们使用Outline Manager设置我们自己的服务器，因为它速度快，并且允许我们自己享受服务器。VPN提供商的节点往往不可靠。我们的服务器也可能会出现问题，但我们对情况有更详细的了解。我们也可以选择不同的云提供商。此外，我们知道我们是使用中国电信还是中国移动，是使用家庭Wi-Fi还是移动数据。

* 将OpenWrt安装在路由器上设置代理可能不太有用。主要问题是GFW可以轻易封禁你的代理服务器的IP地址。最好使用订阅方法，例如Clash，以轻松在路由器上更改设置。