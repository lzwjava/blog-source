---
audio: false
generated: false
image: true
lang: ja
layout: post
title: Googleへのアクセス方法
translated: true
---

この記事は中国語で書かれました。

---

このレッスンでは、以下の内容を扱います。

1. VPNサービスの公式ウェブサイトへのアクセス方法
2. WindowsでのVPNの使い方
3. Clashソフトウェアの紹介
4. Google、Twitter、YouTube、TikTokを開こうとする試み

始めましょう。私が小王にGoogleにアクセスする方法を教えた様子を記述します。

「Summoner」というプラットフォームを使用します。ウェブサイトは`https://zhshi.gitlab.io`です。

<img src="/assets/images/google/zhs.png" alt="zhs" />

しかし、Great Firewallによってブロックされているため、アクセスできない可能性があります。

![zhs_user](/assets/images/google/zhs_user.png)

ログインするとこのような表示になります。

ファイアウォールを回避するには、実際には2つの方法があります。1つは独自の海外サーバーを購入することです。もう1つは、多くの海外サーバーアドレスを提供するVPNプラットフォームを使用することです。

「ファイアウォールを回避する」とは、まず国内から海外サーバーにアクセスすることを意味します。この海外サーバーは、ブロックされているウェブサイトにアクセスできます。

そのようなプラットフォームが「Summoner」です。しかし、公式ウェブサイトにアクセスできない場合、どのようにして提供される海外サーバーアドレスを取得するのでしょうか？小王は初めてVPNを使用しており、私はリモートで彼に教えています。どのように教えるべきでしょうか？

この時点で、小王のWindowsコンピューターでファイアウォールを回避できるようにすることを考えました。小王にアドレスを提供します。その後、小王は「Summoner」ウェブサイトを開き、アカウントを登録し、自分のアカウントの下にある海外サーバーアドレスを使用できます。

![clash_win](/assets/images/google/clash_win.png)

![win_version](/assets/images/google/win_version.png)

次に、コンピューターが64ビットか32ビットかを確認します。64ビットの場合は`Clash.for.Windows.Setup.0.14.8.exe`を、32ビットの場合は`Clash.for.Windows.Setup.0.14.8.ia32.exe`をダウンロードします。

小王のコンピューターは64ビットです。しかし、彼の側ではダウンロードが非常に遅いので、私のコンピューターでダウンロードしてQQメールで彼に送りました。

彼はQQメールからダウンロードしてインストールし、開きました。

![clash_win_exe](/assets/images/google/clash_win_exe.png)

最初に、私のSummoner設定アドレスを彼に渡しました。この設定アドレスは、多くのVPNサーバーアドレスを含むファイルをダウンロードします。「Profiles」でアドレスを貼り付けて「Download」をクリックします。

![zhs_url](/assets/images/google/zhs_url.png)

ご覧の通り、ダウンロードされました。上の2番目の設定に注目してください。緑色のチェックマークが表示されており、この設定を使用していることを示しています。

![zhs_proxy](/assets/images/google/zhs_proxy.png)

次に、「Proxies」タブを開きます。ここにいくつかのものがあります。これらは`Clash`の一部の設定です。簡単に言えば、国内のウェブサイトはVPNを使用せず、海外のウェブサイトは使用するという意味です。

「Proxy」の現在の値は「DIRECT」であり、直接接続であることを示しています。これをノードに変更します。

![zhs_node](/assets/images/google/zhs_node.png)

「US Rose」ノードを選択しました。

![clash_system](/assets/images/google/clash_system.png)

次に、「System Proxy」設定を切り替えて有効にします。これは、`Clash`ソフトウェアをシステムのプロキシレイヤーとして設定することを意味します。その後、システムのトラフィックは最初に`Clash`ソフトウェアに送られ、その後外部ネットワークにアクセスします。

<img src="/assets/images/google/google.png" alt="google" style="zoom:40%;" />

小王はGoogleを開きました。次に、TikTok、YouTube、Twitterを試しました。

さて、小王は私のSummonerアカウントを使用していました。彼はどのように登録するのでしょうか？彼はSummonerの公式ウェブサイトを開く必要があります。

<img src="/assets/images/google/zhs_register.png" alt="zhs_register" style="zoom:50%;" />

登録後、サービスを購入するためのチャージにはいくつかの手順が必要であることがわかりました。これが私のアカウントのスクリーンショットです。

![zeng](/assets/images/google/zeng.png)

Telegramにリンクする必要があると記載されています。

<img src="/assets/images/google/zhs_telegram.png" alt="zhs_telegram" style="zoom:50%;" />

小王はTelegramのウェブサイトに行き、Telegram Windowsデスクトップ版をダウンロードしました。

![telegram](/assets/images/google/telegram.png)

ダウンロードしてインストールしたら、上のテキストに注意してください。

> Telegramをインストールして登録したら、`小兔`または`城主`とチャットをクリックするか、下のQRコードをコピーして送信するか、`こちらをクリックしてコードを自動的にコピーし、Botに送信してバインドします`。

`小兔`をクリックすると、`Telegram`ソフトウェアに自動的にジャンプし、`小兔`とのチャットウィンドウが開きます。その後、彼らにコードを送信します。

![telegram_username](/assets/images/google/telegram_username.png)

しかし、小王の`Telegram`アカウントは新しく登録されたもので、`username`がありません。WeChat IDを設定せずにWeChatを使用するようなものです。

Telegramメニューを見つけて設定します。その後、コードを再度送信してバインドします。

<img src="/assets/images/google/zhs_set.png" alt="zhs_set" style="zoom:50%;" />

次に、寄付してサポートできます。2ヶ月間30元をチャージすることから始められます。

Summonerのホームページに戻ります。「クリックしてコピー」ボタンを探し、アドレスを取得して、`Clash`ソフトウェアで設定をダウンロードします。

その後、小王は私が彼に与えたアドレスを削除できます。小王は自分のSummonerアカウントを持つようになりました。
