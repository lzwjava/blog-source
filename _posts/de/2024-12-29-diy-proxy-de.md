---
audio: true
lang: de
layout: post
title: Richten Sie Ihren Proxy-Server ein
translated: true
---

* Um einen Server einzurichten, verwenden Sie den Outline Manager: [https://getoutline.org](https://getoutline.org).  
* Empfohlene Hosting-Anbieter sind DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr oder Linode. Bevorzugen Sie Regionen in Singapur oder Tokio. Vermeiden Sie die Region Hongkong, da Tools wie ChatGPT und Claude dort gesperrt sind.  
* Protokolle wie Shadowsocks, VMess und Trojan können leicht gesperrt werden.  
* Verwenden Sie Linode für eine schnelle Server-Migration.  
* Möglicherweise benötigen Sie ein Skript, um Ihren Server täglich automatisch zu erneuern.  
* Wenn der Proxy-Server von der GFW gesperrt wird oder andere Probleme auftreten, können Sie eine China Telecom Macau SIM-Karte verwenden, um Mobilfunkdaten mit Ihrem Laptop zu teilen. Dies ermöglicht es Ihnen, einen neuen Server einzurichten.  
* Für Cloud-Dienste wie Google Cloud Platform ist für die Konfiguration eines neuen Servers ein bestehender Proxy-Server erforderlich. Anbieter wie DigitalOcean oder Vultr können jedoch direkt eingerichtet werden, ohne einen Proxy-Server zu benötigen.
* Verwenden Sie [Auto SS Config](https://github.com/lzwjava/auto-ss-config), um Shadowsocks- oder Clash-Abonnement-URLs zu generieren und hochzuladen.
* Nutzen Sie die Snapshot-Funktion in Digital Ocean. Wenn die IP des Servers gesperrt wird, erstellen Sie einen neuen Droplet aus dem Snapshot des Servers und führen Sie `install.sh` erneut aus.
* Verwenden Sie die reservierte IP-Funktion in Digital Ocean. Wenn die IP des Servers gesperrt wird, weisen Sie eine neue reservierte IP zu.