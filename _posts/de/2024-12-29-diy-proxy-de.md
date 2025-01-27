---
audio: true
lang: de
layout: post
title: Richten Sie Ihren Proxy-Server ein
translated: true
---

* Um einen Server einzurichten, verwenden Sie den Outline Manager: [https://getoutline.org](https://getoutline.org).  

* Empfohlene Hosting-Anbieter sind DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr oder Linode. Bevorzugen Sie Regionen in Singapur oder Tokio. Vermeiden Sie die Hongkong-Region, da Tools wie ChatGPT und Claude dort verboten sind.

* Wenn es Ihnen nichts ausmacht, dass ChatGPT und Claude in Hongkong verboten sind, ist es dennoch eine praktikable Option. Sie können Tools wie Deepseek, Mistral, Grok und die Gemini-API mit Hongkong-Servern nutzen. Nutzen Sie umgekehrtes Denken; andere könnten Hongkong-Server meiden, was sie weniger überlastet lässt.

* Berücksichtigen Sie den Standort und die Entfernung des Servers. Für diejenigen in Guangzhou ist Hongkong eine gute Option für das Hosting eines Proxy-Servers. Verwenden Sie Speedtest, um die Netzgeschwindigkeit zu messen.

* Protokolle wie Shadowsocks, VMess und Trojan können leicht gesperrt werden.  

* Verwenden Sie Linode für eine schnelle Server-Migration.  

* Möglicherweise benötigen Sie ein Skript, um Ihren Server täglich automatisch zu erneuern.  

* Wenn der Proxy-Server von der GFW gesperrt wird oder auf andere Probleme stößt, können Sie eine China Telecom Macau-SIM-Karte verwenden, um Mobilfunkdaten mit Ihrem Laptop zu teilen. Dies ermöglicht es Ihnen, einen neuen Server einzurichten.  

* Für Cloud-Dienste wie Google Cloud Platform erfordert die Konfiguration eines neuen Servers einen bestehenden Proxy-Server. Anbieter wie DigitalOcean oder Vultr können jedoch direkt eingerichtet werden, ohne einen Proxy-Server zu benötigen.

* Verwenden Sie [Auto SS Config](https://github.com/lzwjava/auto-ss-config), um Shadowsocks- oder Clash-Abonnement-URLs zu generieren und hochzuladen.

* Verwenden Sie die Snapshot-Funktion in Digital Ocean. Wenn die IP des Servers gesperrt wird, erstellen Sie einen neuen Droplet aus dem Snapshot des Servers und führen Sie `install.sh` erneut aus.

* Verwenden Sie die reservierte IP-Funktion in Digital Ocean. Wenn die IP des Servers gesperrt wird, weisen Sie eine neue reservierte IP zu.

* Wir verwenden den Outline Manager, um unsere eigenen Server einzurichten, da er schnell ist und es uns ermöglicht, den Server allein zu nutzen. Die Knoten von VPN-Anbietern sind oft unzuverlässig. Unsere Server können ebenfalls Probleme haben, aber wir haben ein viel detaillierteres Wissen über die Situation. Wir können auch verschiedene Cloud-Anbieter auswählen. Darüber hinaus wissen wir, ob wir China Telecom oder China Mobile nutzen und ob wir Heim-Wi-Fi oder Mobilfunkdaten verwenden.

* Es ist wahrscheinlich nicht sinnvoll, OpenWrt auf einem Router zu installieren, um einen Proxy einzurichten. Das Hauptproblem ist, dass die GFW die IP-Adresse Ihres Proxy-Servers leicht sperren kann. Es ist besser, eine Abonnementmethode wie mit Clash zu verwenden, um die Einstellungen auf Ihrem Router leicht ändern zu können.