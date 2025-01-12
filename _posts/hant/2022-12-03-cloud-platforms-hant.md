---
lang: hant
layout: post
title: 部分全球云平台
---

<div align="center"><img src="/assets/images/cloud/platform.jpg" width="400px"/></div>

* [Azure](#azure)
* [AWS Lightsail](#aws-lightsail)
* [Digital Ocean](#digital-ocean)
* [Vultr](#vultr)
* [Google Cloud - 失败](#google-cloud---fail)
* [概述](#outline)
* [总结](#summary)

最近我尝试了一些云平台，用来搭建自己的代理服务器。之前，我使用的是第三方代理服务器，由于该服务器用户众多，有时速度会变得很慢。为了解决这个问题，我决定自己搭建一个。

## 天蓝

Azure 是一个不错的选择。我在这里创建了3台虚拟机。因为平台免费给了我200美元的信用额度。我的机器分别位于卡塔尔、美国和香港。从我的广州笔记本电脑到卡塔尔服务器的 ping 时间是150毫秒。现在到美国服务器的 ping 包100%丢失。两天前，我还能成功 ping 通它。而到香港服务器的 ping 包也是100%丢失。我在我的iOS代理客户端中测试了它们，发现无法连接。我需要关闭它们。尽管成本是免费的，但丢失的服务器对我来说没有用处。

<div align="center"><img src="/assets/images/cloud/azure.png" /></div>

让我们看看控制台和网络标签，上下对照。

<div align="center"><img src="/assets/images/cloud/network.png" /></div>

我的自定义网络设置很简单。我只是开放了1024到65535之间的所有端口，无论使用何种协议。因为这是我的代理服务器，里面没有存放任何机密数据或程序。因此，我遵循了Outline App的建议来这样设置。

## AWS Lightsail 简介

Lightsail 是 AWS 的一款轻量级产品。AWS 提供了众多服务，而有时我们仅需在其中创建一些虚拟机。为此，他们为我们提供了 AWS Lightsail。

<div align="center"><img src="/assets/images/cloud/lightsail.png" alt="Lightsail 云服务" /></div>

## 数字海洋

在海外云平台中，我大量使用了Digital Ocean，尤其是在2016至2018年间，每月花费5美元。

我们创建一个这样的液滴：

<div align="center"><img src="/assets/images/cloud/do.png" /></div>

这是我的账单历史记录：

<div align="center"><img src="/assets/images/cloud/bill.png" alt="账单图片" /></div>

## Vultr 云服务器

我从2018年到2020年使用Vultr。

<div align="center"><img src="/assets/images/cloud/vultr.png" /></div>

## 谷歌云 - 失败

我也想尝试谷歌云，但未能成功。他们不支持中国用户。尽管我们可以提供虚假信息，假装是其他国家的公民。然而，我们没有相应的信用卡来完成注册。

<div align="center"><img src="/assets/images/cloud/google.png" alt="Google"/></div>

## 大纲

Outline并非云服务平台，而是一款代理工具。鉴于它助我搭建了个人代理服务器，我不得不单独用一段话来赞美它。它的确非常实用。你可以通过在线搜索来了解更多关于它的信息。

<div align="center"><img src="/assets/images/cloud/outline.png" alt="云服务概述图" /></div>

## 总结

配置最低、价格最便宜的服务器通常每月费用约为5美元。对于作为代理服务器供少数用户使用来说，这已经足够了。位于新加坡、香港或其他亚洲地区的服务器，通常比美国或欧洲的服务器连接速度更快。有时，刚设置好服务器时，它运行得非常好，但几天后，可能就会变得像僵尸一样缓慢。因此，关于速度和稳定性，只有在日常使用中才能发现真相。