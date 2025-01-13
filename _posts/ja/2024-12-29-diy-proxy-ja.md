---
audio: true
lang: ja
layout: post
title: プロキシサーバーのセットアップ
translated: true
---

* サーバーをセットアップするには、Outline Managerを使用します: [https://getoutline.org](https://getoutline.org)。  
* 推奨されるホスティングプロバイダーには、DigitalOcean、Google Cloud、Amazon Lightsail、Azure、Vultr、またはLinodeがあります。シンガポールや東京のリージョンを優先してください。香港リージョンは避けてください。なぜなら、ChatGPTやClaudeなどのツールが禁止されているからです。  
* Shadowsocks、VMess、Trojanなどのプロトコルは簡単にブロックされる可能性があります。  
* サーバーの高速移行にはLinodeを使用します。  
* サーバーを毎日自動的に更新するスクリプトが必要になる場合があります。  
* プロキシサーバーがGFWによってブロックされたり、他の問題が発生した場合、中国電信マカオのSIMカードを使用して、ノートパソコンと携帯データを共有することができます。これにより、新しいサーバーをセットアップできます。  
* Google Cloud Platformのようなクラウドサービスでは、新しいサーバーを設定するために既存のプロキシサーバーが必要です。しかし、DigitalOceanやVultrのようなプロバイダーは、プロキシサーバーなしで直接設定できます。
* [Auto SS Config](https://github.com/lzwjava/auto-ss-config)を使用して、ShadowsocksまたはClashのサブスクリプションURLを生成およびアップロードします。
* Digital Oceanのスナップショット機能を使用します。サーバーのIPがブロックされた場合、サーバーのスナップショットから新しいドロップレットを作成し、再度`install.sh`を実行します。
* Digital Oceanの予約済みIP機能を使用します。サーバーのIPがブロックされた場合、新しい予約済みIPを割り当てます。