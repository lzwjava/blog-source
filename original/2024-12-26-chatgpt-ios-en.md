---
audio: true
generated: false
lang: en
layout: post
title: Analysis of ChatGPT iOS VPN Detection
---

Today, I discovered that the ChatGPT iOS app now allows logging in with a VPN in China. Previously, it displayed a blocking prompt, like the one shown below.

However, as of today, it works fine with a VPN.  

I remember that when the ChatGPT iOS app was first released, using it with a VPN was not an issue. Later, VPN detection became more stringent, making it difficult to log in. Thankfully, it seems that this restriction has been eased recently.  

Upon further testing, I found that when using a DigitalOcean Singapore region VPN, I couldn't access the app. However, when using VPNs from Taiwan or the UK (provided by https://zhs.cloud), it worked perfectly.

It seems that ChatGPT iOS VPN detection is based on specific IP addresses. Some cloud providers or certain IP addresses are banned, which may explain the inconsistent behavior depending on the VPN server location.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }