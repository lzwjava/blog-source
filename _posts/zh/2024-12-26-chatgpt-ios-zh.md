---
audio: true
generated: false
lang: zh
layout: post
title: ChatGPT iOS VPN 检测分析
translated: true
---

今天，我发现 ChatGPT iOS 应用现在可以在中国使用 VPN 登录。之前，它会显示如下的阻止提示。

然而，今天开始，使用 VPN 登录已经没有问题了。  

我记得在 ChatGPT iOS 应用最初发布时，使用 VPN 是没有问题的。后来，VPN 检测变得更加严格，导致登录变得困难。幸运的是，这个限制似乎已经有所放宽。  

在进一步测试时，我发现使用 DigitalOcean 新加坡地区的 VPN 时，无法访问该应用。但当使用台湾或英国地区的 VPN（由 https://zhs.cloud 提供）时，则可以正常使用。

看起来，ChatGPT iOS 的 VPN 检测是基于某些 IP 地址的。一些云服务提供商或特定的 IP 地址被封禁，这可能解释了根据 VPN 服务器位置不同，访问的行为不一致。

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }