---
audio: false
generated: false
lang: de
layout: post
title: EINRICHTEN SIE IHREN PROXY-SERVER
translated: true
---

* Um einen Server einzurichten, verwenden Sie den Outline Manager: [https://getoutline.org](https://getoutline.org).

* Empfohlene Hosting-Anbieter sind DigitalOcean, Google Cloud, Amazon Lightsail, Azure, Vultr und Linode. Für optimale Leistung wählen Sie Serverstandorte in Singapur oder Tokio. Während Hongkong ebenfalls eine Option ist, beachten Sie, dass bestimmte KI-Tools wie ChatGPT und Claude in dieser Region eingeschränkt sind.

* Sie können weiterhin Tools wie Deepseek, Mistral, Grok und die Gemini API (über Cursor) mit Hongkong-Servern verwenden. Da andere möglicherweise Hongkong-Server meiden, sind diese oft weniger überlastet.

* Berücksichtigen Sie den Serverstandort und die Entfernung. Für diejenigen in Guangzhou ist Hongkong eine gute Option für das Hosting eines Proxy-Servers. Verwenden Sie Speedtest, um die Netzwerkgeschwindigkeit zu messen.

* Wenn Ihnen Geschwindigkeit wichtig ist, ist die beste Option, von der ich weiß, die Verwendung eines Aliyun Hongkong-Servers mit einer BGP (Premium) elastischen IP. Die IP ist elastisch, was es einfach macht, eine neue zu binden, wenn die aktuelle IP gesperrt wird. Zusätzlich ist diese BGP (Premium) Verbindung von Aliyun Cloud optimiert, was schnelle Geschwindigkeiten bietet.

* Protokolle wie Shadowsocks, VMess und Trojan können leicht gesperrt werden.

* Verwenden Sie Linode für eine schnelle Server-Migration.

* Sie könnten ein Skript benötigen, um Ihren Server automatisch jeden Tag zu erneuern.

* Wenn der Proxy-Server vom GFW gesperrt wird oder andere Probleme auftreten, können Sie eine SIM-Karte von China Telecom Macau verwenden, um zellulare Daten mit Ihrem Laptop zu teilen. Dies ermöglicht Ihnen das Einrichten eines neuen Servers.

* Für Cloud-Dienste wie Google Cloud Platform erfordert die Konfiguration eines neuen Servers einen bestehenden Proxy-Server. Anbieter wie DigitalOcean oder Vultr können jedoch direkt eingerichtet werden, ohne dass ein Proxy-Server benötigt wird.

* Verwenden Sie [Auto SS Config](https://github.com/lzwjava/auto-ss-config), um Shadowsocks oder Clash Abonnement-URLs zu generieren und hochzuladen.

* Nutzen Sie die Snapshot-Funktionalität in DigitalOcean. Wenn die IP des Servers gesperrt wird, erstellen Sie einen neuen Droplet aus dem Snapshot des Servers und führen `install.sh` erneut aus.

* Nutzen Sie die reservierte IP-Funktionalität in DigitalOcean. Wenn die IP des Servers gesperrt wird, weisen Sie eine neue reservierte IP zu.

* Wir verwenden den Outline Manager, um unsere eigenen Server einzurichten, weil es schnell ist und uns ermöglicht, den Server selbst zu genießen. VPN-Anbieterknoten können oft unzuverlässig sein. Unsere Server können ebenfalls Probleme haben, aber wir haben viel detailliertere Kenntnisse über die Situation. Wir können auch verschiedene Cloud-Anbieter auswählen. Zudem wissen wir, ob wir China Telecom oder China Mobile verwenden und ob wir über Heim-WLAN oder zellulare Daten verbunden sind.

* Es ist wahrscheinlich nicht nützlich, OpenWrt auf einem Router zu installieren, um einen Proxy einzurichten. Das Hauptproblem ist, dass die GFW die IP-Adresse Ihres Proxy-Servers leicht sperren kann. Es ist besser, ein Abonnement-Verfahren wie mit Clash zu verwenden, um die Einstellungen auf Ihrem Router einfach zu ändern.