---
audio: true
lang: ja
layout: post
title: プロキシサーバーの設定
translated: true
---

* サーバーをセットアップするには、Outline Managerを使用します: [https://getoutline.org](https://getoutline.org)。  
* 推奨されるホスティングプロバイダーには、DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr、Linodeなどがあります。シンガポールや東京のリージョンを優先してください。香港リージョンは避けてください。なぜなら、ChatGPTやClaudeなどのツールが禁止されているからです。  
* Shadowsocks、VMess、Trojanなどのプロトコルは簡単に禁止される可能性があります。  
* サーバーの高速移行にはLinodeを使用します。  
* サーバーを毎日自動的に更新するスクリプトが必要になる場合があります。  
* プロキシサーバーがGFWによって禁止されたり、他の問題が発生した場合、中国電信マカオのSIMカードを使用して、ラップトップと携帯データを共有することができます。これにより、新しいサーバーをセットアップできます。  
* Google Cloud Platformなどのクラウドサービスでは、新しいサーバーを設定するために既存のプロキシサーバーが必要です。しかし、DigitalOceanやVultrなどのプロバイダーは、プロキシサーバーを必要とせずに直接設定できます。
* [Auto SS Config](https://github.com/lzwjava/auto-ss-config)を使用して、ShadowsocksまたはClashのサブスクリプションURLを生成してアップロードします。
* Digital Oceanのスナップショット機能を使用します。サーバーのIPが禁止された場合、サーバーのスナップショットから新しいドロップレットを作成し、再度`install.sh`を実行します。