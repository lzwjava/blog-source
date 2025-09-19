---
audio: false
generated: false
image: true
lang: hant
layout: post
title: 一些全球雲端平台
translated: true
---

<div align="center"><img src="/assets/images/cloud/platform.jpg" width="400px"/><img/></div>

* [Azure](#azure)
* [AWS Lightsail](#aws-lightsail)
* [Digital Ocean](#digital-ocean)
* [Vultr](#vultr)
* [Google Cloud - 失敗](#google-cloud---失敗)
* [Outline](#outline)
* [總結](#總結)

最近我嘗試了一些雲平台，用來設置我的代理伺服器。之前，我使用的是第三方代理伺服器，由於該伺服器被許多用戶使用，所以速度有時會很慢。為了解決這個問題，我嘗試自己設置一個。

## Azure

Azure 是一個不錯的選擇。我在這裡創建了3台虛擬機，因為這個平台免費給了我200美元的信用額。我的機器分別位於卡塔爾、美國和香港。從我的廣州筆記本電腦到卡塔爾伺服器的ping時間是150毫秒。現在到美國伺服器的ping包100%丟失。兩天前，我還能成功ping通。而到香港伺服器的ping包也100%丟失。我在iOS代理客戶端測試後發現無法連接。我需要關閉它們。雖然成本是免費的，但無法使用的伺服器對我來說毫無用處。

<div align="center"><img src="/assets/images/cloud/azure.png" /><img/></div>

讓我們看看控制台和網絡選項卡，上下兩張圖。

<div align="center"><img src="/assets/images/cloud/network.png" /><img/></div>

我的自定義網絡設置很簡單。我只是讓任何協議的1024到65535端口都開放。因為這是我的代理伺服器，裡面沒有任何秘密數據或程序。所以我按照Outline App的建議來做。

## AWS Lightsail

Lightsail 是 AWS 的一個輕量級產品。AWS 有很多產品，有時我們只想在裡面創建一些虛擬機。所以他們提供了 AWS Lightsail。

<div align="center"><img src="/assets/images/cloud/lightsail.png" /><img/></div>

## Digital Ocean

我在海外雲平台中使用 Digital Ocean 很多，尤其是從2016年到2018年。我每個月花費5美元。

我們像這樣創建一個 droplet：

<div align="center"><img src="/assets/images/cloud/do.png" /><img/></div>

這是我的賬單歷史：

<div align="center"><img src="/assets/images/cloud/bill.png" /><img/></div>

## Vultr

我從2018年到2020年使用 Vultr。

<div align="center"><img src="/assets/images/cloud/vultr.png" /><img/></div>

## Google Cloud - 失敗

我也想試試 Google Cloud。然而，我失敗了。他們不支持中國用戶。雖然我們可以提供虛假信息，假裝是其他國家的公民。但我們沒有相應的信用卡來成功註冊。

<div align="center"><img src="/assets/images/cloud/google.png" /><img/></div>

## Outline

Outline 不是一個雲平台。它是一個代理工具。因為它幫助我設置了我的代理伺服器，所以我必須單獨寫一段來讚揚它。它真的很有幫助。你可以通過在線搜索來了解它。

<div align="center"><img src="/assets/images/cloud/outline.png" /><img/></div>

## 總結

最低配置的最便宜伺服器通常每月花費約5美元。對於作為代理伺服器供少數用戶使用來說已經足夠了。位於新加坡、香港或其他亞洲地區的伺服器通常比位於美國或歐洲的伺服器連接速度更快。有時，當你剛設置好伺服器時，它運行得非常順暢。然而，幾天後，它就像殭屍一樣無法使用。所以關於速度和穩定性，你只能在日常使用中找到真相。