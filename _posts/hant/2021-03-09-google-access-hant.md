---
audio: false
generated: false
image: true
lang: hant
layout: post
title: 如何使用 Google
translated: true
type: post
---

此篇文章最初以中文撰寫。

---

本課涵蓋以下內容：

1. 如何訪問VPN服務的官方網站。
2. 如何在Windows上使用VPN。
3. Clash軟體簡介。
3. 嘗試開啟Google、Twitter、YouTube和TikTok。

開始吧。以下是我教小王如何訪問Google的文字描述。

我們將使用一個名為「召喚師」的平台。其網站地址為`https://zhshi.gitlab.io`。

<img src="/assets/images/google/zhs.png" alt="zhs" />

但是，由於它可能被防火牆封鎖，所以未必能訪問。

![zhs_user](/assets/images/google/zhs_user.png)

這是登入後的樣子。

其實繞過防火牆的方法有兩種。一種是購買我們自己的海外伺服器。另一種是使用VPN平台，它提供許多海外伺服器地址。

「繞過防火牆」的意思是先從國內訪問海外伺服器。然後，這個海外伺服器就可以訪問被封鎖的網站了。

這樣的平台就叫做「召喚師」。但是如果官方網站無法訪問，我們如何獲得它提供的海外伺服器地址呢？小王是第一次使用VPN，我遠程教他。我應該如何教他？

此時，我想到了讓小王的Windows電腦繞過防火牆。我會給小王一個地址。然後小王就可以打開「召喚師」網站，註冊帳號，使用自己帳號下的海外伺服器地址。

![clash_win](/assets/images/google/clash_win.png)

![win_version](/assets/images/google/win_version.png)

接下來，檢查你的電腦是64位還是32位。如果是64位，下載`Clash.for.Windows.Setup.0.14.8.exe`。如果是32位，下載`Clash.for.Windows.Setup.0.14.8.ia32.exe`。

小王的電腦是64位的。但是他那邊下載速度很慢。所以我用我的電腦下載好，然後通過QQ郵件發給他。

他從QQ郵件下載，安裝，打開。

![clash_win_exe](/assets/images/google/clash_win_exe.png)

我先給他我的召喚師配置地址。這個配置地址會下載一個包含許多VPN伺服器地址的文件。在`Profiles`下，貼上地址並點擊`Download`。

![zhs_url](/assets/images/google/zhs_url.png)

看，下載好了。注意上面第二個配置。前面有一個綠色的勾，表示我們正在使用這個配置。

![zhs_proxy](/assets/images/google/zhs_proxy.png)

接下來，打開`Proxies`選項卡。你會看到一些東西。這些是`Clash`的一些配置。簡單來說，就是國內網站不使用VPN，國外網站使用。

注意`Proxy`目前的數值是`DIRECT`，表示直接連接。我們把它改成一個節點。

![zhs_node](/assets/images/google/zhs_node.png)

我們選擇了`US Rose`節點。

![clash_system](/assets/images/google/clash_system.png)

接下來，切換`System Proxy`設置以啟用它。這意味著將`Clash`軟體設置為系統的代理層。這樣，系統的流量就會先到`Clash`軟體，然後再訪問外部網路。

<img src="/assets/images/google/google.png" alt="google" style="zoom:40%;" />

小王打開了Google。接下來，他嘗試了TikTok、YouTube和Twitter。

好了，所以小王一直在使用我的召喚師帳號。他如何註冊呢？他需要打開召喚師官方網站。

<img src="/assets/images/google/zhs_register.png" alt="zhs_register" style="zoom:50%;" />

註冊後，他發現充值購買服務需要一些步驟。這是我的帳號截圖。

![zeng](/assets/images/google/zeng.png)

上面說需要綁定Telegram。

<img src="/assets/images/google/zhs_telegram.png" alt="zhs_telegram" style="zoom:50%;" />

小王去Telegram網站下載了Telegram Windows桌面版。

![telegram](/assets/images/google/telegram.png)

下載並安裝後，注意上面的文字。

> 安裝Telegram並註冊後，點擊與`小兔`或`城主`聊天，複製下面的二維碼發送給他們，或`點擊此處自動複製代碼並發送給機器人綁定`。

點擊`小兔`，就會自動跳轉到`Telegram`軟體，並開啟與`小兔`的聊天視窗。然後，把代碼發送給他們。

![telegram_username](/assets/images/google/telegram_username.png)

但是，小王的`Telegram`帳號是新註冊的，沒有`username`。這就像使用微信沒有設置微信號一樣。

找到Telegram選單並設置它。然後，再次發送代碼進行綁定。

<img src="/assets/images/google/zhs_set.png" alt="zhs_set" style="zoom:50%;" />

接下來，就可以捐款支持了。可以先充值30元，可以使用兩個月。

返回召喚師首頁。這裡，尋找「點擊複製」按鈕，獲取地址，然後在`Clash`軟體中下載配置。

然後小王就可以刪除我給他的地址了。小王現在有了自己的召喚師帳號。