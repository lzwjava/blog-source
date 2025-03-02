---
audio: false
generated: false
lang: hant
layout: post
title: ChatGPT iOS VPN 檢測分析
translated: true
---

今天發現，ChatGPT iOS 應用在中國使用 VPN 可以登錄了。之前會顯示封鎖提示，如下圖所示。

但截至今天，使用 VPN 可以正常登錄。

我記得 ChatGPT iOS 應用剛推出時，使用 VPN 登錄是沒有問題的。後來 VPN 檢測變得嚴格，難以登錄。幸好最近這個限制似乎有所放寬。

進一步測試發現，使用 DigitalOcean 新加坡區域的 VPN 無法訪問應用，但使用台灣或英國的 VPN（由 https://zhs.cloud 提供）則完全正常。

看來 ChatGPT iOS 的 VPN 檢測是基於特定 IP 地址的。某些雲服務提供商或特定 IP 地址被封禁，這可能解釋了根據 VPN 服務器位置不同而行為不一致的原因。

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }