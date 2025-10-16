---
audio: false
generated: false
image: true
lang: de
layout: post
title: Der Weg zur Verfolgung der Internetfreiheit
translated: true
---

### Inhaltsverzeichnis

1. [Proxy-Lösungen in China](#proxy-solutions-in-china)
   - Verwendung einer Macao SIM-Karte für direkten Zugriff
   - Empfehlung erschwinglicher Proxy-Server-Anbieter
   - Konfiguration von Apps mit globalen Routing-Regeln
   - Vermeidung selbst gehosteter Proxy-Server-Setups
   - App Store-Region mit Proxy wechseln

2. [Die Reise zur Internetfreiheit](#the-journey-to-pursue-internet-freedom)
   - Zeitlinie der Proxy-Methodenentwicklung
   - Vergleich des GFW-Kampfes mit der Myopie-Reversion
   - Aktuelles Setup verwendet mehrere Proxy-Server
   - Automatisierte Proxy-Auswahl basierend auf Geschwindigkeit
   - Bedauern, dass Anbietertechniken nicht früher gelernt wurden

3. [Macau SIM-Karten](#macau-sim-cards)
   - Details zur China Telecom Easy+ SIM-Karte
   - Blue Macau SIM-Karte Pay-as-you-go
   - Verschiedene Tagesgebühren und Datentarife
   - Erfordert ein kompatibles 4G-unterstütztes Gerät
   - Keine Vertrags- oder Kündigungsgebühren

4. [Shadowsocks Proxy-Probleme](#shadowsocks-proxy-issues)
   - Netzwerk-spezifische Konnektivitätsprobleme treten auf
   - 5G- versus 4G-Leistungsunterschiede
   - Carrier-Richtlinien können Proxy-Traffic blockieren
   - Serverstandort beeinflusst Latenz
   - Fehlerbehebung mit verschiedenen Servern

5. [Registrierung auf jeder Plattform unabhängig von der Identität](#registering-on-any-platform-regardless-of-identity)
   - Verwendung mehrerer E-Mail-Konten für die Registrierung
   - Telefonnummern über Online-Dienste mieten
   - Apple Store-Region mit Proxy wechseln
   - Zahlungsbeschränkungen mit chinesischen Visa-Karten
   - Chinesische Ausweisdokumente helfen manchmal


## Proxy-Lösungen in China

*2024.12.29*

* Der beste Weg ist, eine China Macau SIM-Karte zu besorgen, um bei Bedarf direkt mobile Daten zu nutzen. Besuchen Sie [https://www.1888.com.mo](https://www.1888.com.mo). Es kostet etwa 80 CNY für 10 GB mobile Daten und bietet eine schnelle und reibungslose Erfahrung.

* China Telecom Macau SIM-Karten sind in zwei Typen erhältlich: rot und blau. Rote Karten bieten Tagespläne, die typischerweise 2, 3 oder 5 Macau-Dollar pro Tag kosten. Blaue Karten bieten Datentarife, wie 10 GB für 98 Macau-Dollar oder 20 GB für 198 Macau-Dollar, ohne monatliche Gebühren.

* Wenn Sie mehr Netzwerkdaten benötigen oder häufig einen Laptop verwenden, ziehen Sie [zhs.cloud](https://zhs.cloud) in Betracht. Es bietet Zugang zu etwa 15 globalen Proxy-Servern für nur 30 CNY pro Monat.

* Auf iOS verwenden Sie Shadowrocket mit Shadowsocks-Regeln: [https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever). Konfigurieren Sie das globale Routing, um den China-Verkehr vom Übersee-Verkehr zu trennen.

* Auf Android verwenden Sie V2Ray. Auf Fire TV verwenden Sie die V2Ray-App. Auf Apple TV verwenden Sie die Shadowrocket-App. Auf Mac verwenden Sie die ShadowsocksX-NG- oder ClashX-App.

* Es wird nicht empfohlen, selbst einen Proxy-Server einzurichten. Protokolle wie Shadowsocks, VMess oder Trojan werden leicht gesperrt, unabhängig vom verwendeten Server.

* Um den App Store in die USA-Region zu wechseln, schalten Sie einen globalen Proxy (USA) ein, und es wird die Zahlungsoption „Keine“ angezeigt, sodass Sie frei wechseln können.

* Verwenden Sie eine Visa-Karte, um Geschenkkarten von Amazon zu kaufen oder verwenden Sie das Apple Geschenkkartenportal, um Ihr App Store-Konto aufzuladen.

---

## Die Reise zur Internetfreiheit

*2025.02.03, Dieser Beitrag wurde zuletzt im August 2025 aktualisiert.*

#### Die Reise

Von 2010 bis 2013 nutzte ich Goagent und das SwitchyOmega Proxy-Tool, um die GFW zu umgehen.

Zwischen 2014 und 2015 nutzte ich Qujing (曲径) für Proxys und folgte deren Autor auf Twitter, der jetzt in Japan lebt.

Von Juni 2016 bis Juli 2018 nutzte ich Digital Ocean, um meinen Shadowsocks-Proxy-Server zu hosten.

Ab 2019 begann ich https://zhs.cloud zu nutzen.

Im März 2023 begann ich, eine Macau-SIM-Karte in meinem Mobiltelefon für den Internetzugang ohne Proxy oder VPN zu verwenden. Dies kostete etwa 150 CNY pro Monat für 20 GB mobile Daten, und ich nutzte diese Methode etwa ein Jahr lang.

Im Jahr 2024 begann ich wieder, Outline Manager mit meinem Shadowsocks-Proxy-Server zu verwenden und experimentierte mit verschiedenen Cloud-Anbietern.

Im Februar 2025 ist mein bevorzugtes Setup Outline Manager mit einem Aliyun Hong Kong Server für den täglichen Gebrauch und einem Nicht-Hong Kong Server (wie Singapur oder Japan) für AI-Tools. Ich verwende immer noch dieselbe Proxy-Regelkonfiguration, die in Shadowrocket oder Clash verwendet wird.

Ab Juni 2025 begann ich, ein Python-Skript auf meinem Laptop zu verwenden, um alle 10 Minuten automatisch einen Proxy-Server basierend auf Speedtest-Ergebnissen auszuwählen. Das Skript priorisiert Singapur-Server gegenüber Hong Kong-Servern für die Nutzung von AI-Tools. Weitere Details finden Sie unter [Automating Clash Proxy Management](/clash-en). Für den VPN-Cloud-Anbieter nutzte ich weiterhin https://zhs.cloud.

Zusätzlich wechselte ich auf iOS wieder zur Verwendung einer Macau-SIM-Karte, die 150 CNY pro Monat für 20 GB Daten kostet. Ich kaufte auch dreimal zusätzliche 5 GB Daten für jeweils 20 MOP, was insgesamt etwa 200 CNY für 35 GB Daten auf meinem Mobiltelefon ausmachte.

Ab Mitte Oktober 2025 habe ich meinen Macau-SIM-Kartentarif nicht mehr verwendet, da ich in den letzten Monaten etwa 35 GB pro Monat verbraucht habe. Die Nutzung chinesischer Apps, die etwa ein Drittel meines Datenverbrauchs ausmachen – hauptsächlich in WeChat – würde mobile Daten kosten.

Ich begann wieder, die iOS Shadowsocks-App mit Proxy-Servern von https://zhs.cloud zu verwenden. Und ich begann, Wissen über CN2-Kabel zu erlernen.

#### Der Unterschied im Vergleich zur Myopie-Reversion

Eine Herausforderung ist der Kampf gegen die GFW, die von Menschen gemacht ist. Die andere ist die Auseinandersetzung mit den Prinzipien der Augenmuskelfunktion.

Die Effektivität einer Proxy-Lösung lässt sich leicht messen. Die Reversion der Myopie erfordert jedoch Zeit, um festzustellen, ob sich der Augapfel verändert.

#### Ähnlichkeiten zur Myopie-Reversion

Eine Ähnlichkeit besteht darin, dass sowohl eine Proxy-Lösung als auch Brillen mit einer Reduzierung um 200 Grad oft gut funktionieren. Das eine beinhaltet den Internetzugang, das andere die Verbesserung des Sehvermögens. Beide lösen sehr wichtige Probleme.

Das zugrunde liegende Prinzip ist, dass, wenn wir verstehen, wie die GFW funktioniert und einen Weg finden, sie zu umgehen, die Lösung einfach sein sollte.

#### Begründung und Nuance

Ich verstehe immer noch nicht vollständig, wie die GFW funktioniert. Wenn die IP meines Proxy-Servers blockiert wird, habe ich jetzt mehr Möglichkeiten, die Ursache zu untersuchen.

Ich kann überprüfen, ob die Blockierung im Mobilfunknetz oder im Heim-Breitband erfolgt. Wenn es das Mobilfunknetz ist, kann ich überprüfen, ob es sich um 4G oder 5G handelt.

Ähnlich, wenn sich meine Myopie nach sechs Monaten oder einem Jahr nicht verbessert, muss ich untersuchen, ob es Unterschiede zwischen meinen Augen gibt. Ich muss auch bedenken, ob ich die meiste Zeit des Jahres Dinge gerade noch klar gesehen habe, ohne meine Augen zu belasten.

#### Aktueller Status

Mein Proxy-Server funktioniert derzeit sehr gut. Die Download-Geschwindigkeit auf meinem Telefon erreicht 80 Mbps und die Upload-Geschwindigkeit 50 Mbps, wenn ich mit dem Hong Kong Proxy-Server verbunden bin. Das Gleiche gilt für meinen Laptop.

Ich verwende dieselben Proxy-Konfigurationen auf meinem Laptop und meinen Telefonen, und sie funktionieren perfekt. Normalerweise verwende ich einen Proxy-Server, um Websites außerhalb Chinas zu besuchen, und einen Nicht-HK-Server für AI-Tools.

#### Wiederherstellung

Wenn etwas kaputt ist, ist meine Wiederherstellungsmethode einfach. Ich muss nur die elastische IP meines Aliyun Hong Kong Proxy-Servers ändern und die neue Proxy-URL in den Cloud-Speicher hochladen. Das bedeutet, dass ich zwei Skripte ausführen muss, was etwa 1 Minute dauert, und mein Laptop und meine Telefone können die Proxy-Server-Adresse aktualisieren.

#### Bedauern

Ich habe zu oft und zu lange mit der GFW gekämpft. Ich habe viele Proxy-Protokolle ausprobiert, wohlwissend, dass sie von der GFW erkannt und gesperrt würden. Ohne einen zuverlässigen Proxy-Server ist es schwierig, einen Proxy auf einem OpenWrt-Router einzurichten.

Eine Sache, die ich bedauere, ist, die Techniken von Proxy-Anbietern wie [zhs.cloud](https://zhs.cloud) nicht früher gelernt zu haben. Ich kenne jetzt die meisten ihrer Geheimnisse.

Die andere Sache ist, dass ich, wann immer mein Proxy-Server gesperrt wurde, nicht zu tief nachgedacht habe. Es schien, dass man nur einen neuen Proxy-Server einrichten musste, um eine neue IP-Adresse zu erhalten, die nicht gesperrt worden war. Aber das war oberflächliches Denken.

#### Metriken

Ich bedauere, Speedtest nicht früher verwendet zu haben. Ich kannte den Namen des Tools schon lange, aber ich habe nicht gelernt, es sorgfältig zu verwenden.

Es ist gut, Speedtest häufig zu verwenden, wenn man mit 5G- oder 4G-Mobilfunkstationen oder einem Heim-Breitbandnetzwerk verbunden ist.

Für die Reversion der Myopie ist es dasselbe. Ich habe eine C-förmige Sehtafel und eine Standard-Sehtafel gekauft.

Kein Messen, keine Verbesserung. Das Messen von Dingen hilft beim Lernen. Die häufige Verwendung von Speedtest hilft mir festzustellen, dass man in einem 5G-Netzwerk leicht 100 Mbps überschreiten kann, während es in einem Heim-Breitbandnetzwerk schwierig ist, 100 Mbps zu überschreiten.

#### Es ist noch früh

Wird die GFW-Mauer in den nächsten Jahren fallen? Das ist schwer zu sagen.

Als ich, nachdem ich zwei Jahre lang meine Myopie rückgängig gemacht hatte, meinem Freund erzählte, dass meine Reversionsmethode verbessert werden müsste und dass ich eine Brille mit 200 Grad weniger als meiner tatsächlichen Sehstärke statt 150 Grad weniger tragen müsste.

Er sagte, das sei kein Problem, es sei in Ordnung, keine Zeitverschwendung, und es sei noch früh. Ja. Diese Dinge sind grundlegend. Wie Myopie sollten die Menschen es früher entdecken. Todd Becker teilte diese Entdeckung 2014 auf YouTube, und die Videos erhielten über 1 Million Aufrufe. Und jetzt ist es 2025, wie viele Menschen wissen wirklich davon auf der Welt? Ich schätze, es werden weniger als 10 Tausend sein.

---

## Macau SIM-Karten

*2023.04.20*

#### Meine Erfahrung mit Macau SIM-Karten

Während meines Wochenendbesuchs in Macau im Jahr 2023 kaufte ich eine China Telecom Easy+ SIM Macau Card. Nach meiner Ankunft in Guangzhou stellte ich fest, dass sie immer noch perfekt funktionierte und mir half, Englisch zu lernen und viele ausländische Apps herunterzuladen. Es fühlte sich an, als wäre ich immer noch in Macau. Ich kann sie wärmstens empfehlen. Später probierte ich die Blue Macau SIM Card aus, die ebenfalls gut war. Hier ist ein kurzer Überblick über beide:

#### China Telecom Easy+ SIM-Karte

Jederzeit einfach zu bedienen!

### Hauptpunkte
- Keine Kaution; automatische Aktivierung für Festlandchina, Macau und Hongkong.
- Kein Vertrag oder Kündigungsgebühr; sofort nach dem Kauf einsatzbereit.
- Macau-Nummer enthalten; optionale Festlandchina-Nummer für Dual-Nummern-Nutzung.
- Online aufladen oder mit Wertkarten.

### Optionen für tägliche Gebühren
- 2 $/Tag: 4 GB High-Speed, danach unbegrenzt mit reduzierter Geschwindigkeit; 5.000 Minuten lokale Anrufe.
- 3 $/Tag: 10 GB High-Speed, danach unbegrenzt mit reduzierter Geschwindigkeit; 5.000 Minuten lokale Anrufe.
- 5 $/Tag: 20 GB High-Speed, danach unbegrenzt mit reduzierter Geschwindigkeit; 5.000 Minuten lokale Anrufe.

### Extras
- Datennutzung in Hongkong: 0,1 $/MB.
- Tarife jederzeit per SMS ändern.

#### Blue Macau SIM-Karte

### Hauptpunkte
- Keine monatliche Miete; Pay-as-you-go.
- Lokale Anrufe: 0,39 MOP/Minute; Internet: 0,1 MOP/MB; SMS: 1 MOP/Nachricht.
- Optionale Datenpakete ohne Ablaufdatum: 10 GB für 98 MOP, 20 GB für 188 MOP, 40 GB für 288 MOP.
- Alle 180 Tage aufladen, um aktiv zu bleiben.

#### Kompatible Geräte

- Erfordert ein 4G-Full-Network- oder China Telecom-unterstütztes Telefon.

Weitere Informationen finden Sie unter [China Telecom Macau](https://www.1888.com.mo/).

---

Diese finden Sie auch auf Taobao:

<div align="center"><img src="/assets/images/macao/easy.jpg" width="300px" /><img/></div>

---

## Shadowsocks Proxy-Probleme

*2025.01.03*

Zhiwei:

Ich bin mit einem Freund zum Grillen gegangen und habe Shadowsocks mit einem Server in Singapur als Proxy verwendet, um die Große Firewall (GFW) zu umgehen. Als ich draußen 5G nutzte, konnte ich keine Verbindung herstellen, und der Test schlug fehl, als ich versuchte, auf YouTube zuzugreifen. Wenn ich jedoch zu Hause 4G oder mein China Telecom Heimnetzwerk nutze, funktioniert Shadowsocks einwandfrei. Warum passiert das?

Mistral:

Es hört sich so an, als hätten Sie Konnektivitätsprobleme mit Ihrem Shadowsocks-Proxy, wenn Sie 5G draußen nutzen, aber nicht, wenn Sie 4G oder Ihr Heimnetzwerk nutzen. Dafür könnte es mehrere Gründe geben:

1. Unterschiede in der Netzwerkkonfiguration:
   - 5G-Netzwerk: Das 5G-Netzwerk könnte andere Konfigurationen oder Einschränkungen im Vergleich zu 4G haben. Einige Anbieter könnten strengere Firewall-Regeln oder ein anderes Netzwerk-Routing für 5G haben, was die Leistung Ihres Shadowsocks-Proxys beeinträchtigen könnte.
   - 4G-Netzwerk: Das 4G-Netzwerk könnte entspanntere Einstellungen oder ein besseres Routing haben, das es Ihrem Shadowsocks-Proxy ermöglicht, korrekt zu funktionieren.

2. ISP-Einschränkungen:
   - Carrier-Richtlinien: Verschiedene Anbieter könnten unterschiedliche Richtlinien bezüglich der Verwendung von VPNs oder Proxys haben. Ihr 5G-Anbieter könnte strengere Richtlinien haben, die VPN-Verkehr, einschließlich Shadowsocks, blockieren oder drosseln.
   - Heimnetzwerk: Ihr Heimnetzwerk, bereitgestellt von China Telecom, könnte weniger Einschränkungen haben, wodurch Shadowsocks ohne Probleme funktioniert.

3. Signalstärke und -stabilität:
   - 5G-Signal: Die Stabilität und Stärke des 5G-Signals kann variieren, insbesondere in Außenbereichen. Schwache oder instabile Signale können Konnektivitätsprobleme verursachen, einschließlich Timeouts.
   - 4G-Signal: Das 4G-Signal könnte stabiler und konsistenter sein und eine bessere Verbindung für Ihren Shadowsocks-Proxy bieten.

4. Proxy-Server-Standort:
   - Singapur-Server: Der Standort Ihres Shadowsocks-Servers in Singapur könnte die Latenz und Konnektivität beeinflussen. Das 5G-Netzwerk könnte eine höhere Latenz oder ein weniger optimales Routing zum Singapur-Server im Vergleich zum 4G-Netzwerk oder Ihrem Heimnetzwerk haben.

5. Geräteeinstellungen:
   - Konfiguration: Stellen Sie sicher, dass Ihre Geräteeinstellungen für die Verwendung von Shadowsocks korrekt konfiguriert sind. Manchmal kann das Wechseln von Netzwerken (von 5G zu 4G oder Heim-WLAN) dazu führen, dass Einstellungen zurückgesetzt oder geändert werden.
   - App-Berechtigungen: Stellen Sie sicher, dass die Shadowsocks-App die erforderlichen Berechtigungen zum Betrieb in verschiedenen Netzwerken hat.

### Schritte zur Fehlerbehebung:

1. Netzwerkeinstellungen überprüfen:
   - Stellen Sie sicher, dass Ihre Shadowsocks-Einstellungen sowohl für 5G- als auch für 4G-Netzwerke korrekt konfiguriert sind.
   - Überprüfen Sie, ob es keine spezifischen Einschränkungen oder Einstellungen in Ihrem 5G-Netzwerk gibt, die den Proxy blockieren könnten.

2. Verschiedene Server testen:
   - Versuchen Sie, sich mit verschiedenen Shadowsocks-Servern zu verbinden, um zu sehen, ob das Problem spezifisch für den Singapur-Server ist.
   - Überprüfen Sie die Latenz und Stabilität der Verbindung zum Server.

3. Wenden Sie sich an Ihren Anbieter:
   - Wenn das Problem weiterhin besteht, wenden Sie sich an Ihren 5G-Anbieter, um Informationen zu Einschränkungen oder Einstellungen zu erhalten, die Ihre Shadowsocks-Verbindung beeinträchtigen könnten.

4. Software aktualisieren:
   - Stellen Sie sicher, dass Ihre Shadowsocks-App und Gerätesoftware auf dem neuesten Stand sind. Manchmal können Updates Konnektivitätsprobleme beheben.

5. Alternative Proxys verwenden:
   - Erwägen Sie die Verwendung alternativer Proxy-Dienste oder VPNs, die möglicherweise eine bessere Kompatibilität mit Ihrem 5G-Netzwerk aufweisen.

Durch die systematische Überprüfung dieser Faktoren sollten Sie in der Lage sein, die Ursache des Konnektivitätsproblems zu identifizieren und eine geeignete Lösung zu finden.

---
Update:

Tatsächlich verwendet mein Heim-WLAN China Mobile Communications Corporation, und seine Adresse ist wie 120.235.8.xx.

Interessanterweise habe ich unregelmäßige Verbindungsmuster beobachtet – obwohl mein Proxy-Server im Mobilfunknetz und in China Telecom-Netzwerken normal funktioniert, stellt er gelegentlich keine Verbindung her, wenn ich mein Heim-WLAN-Netzwerk verwende.

---

## Registrierung auf jeder Plattform unabhängig von der Identität

Ich bin ein chinesischer Staatsbürger und ein Software-Ingenieur, der sich auf die neueste Technologie konzentriert. Es ist frustrierend zu sehen, dass viele Produkte den Zugang aus China verbieten. Obwohl ich noch an meinem Associate Degree arbeite und hoffe, eines Tages außerhalb Chinas zu arbeiten, werde ich noch einige Jahre in China bleiben. In der Zwischenzeit möchte ich einige Informationen über die Überwindung von Internetbarrieren aufgrund der Nationalität teilen.

#### E-Mail

Mehrere E-Mail-Konten zu haben, ist besser. Claude hat mein Gmail wegen VPN-Zugriff gesperrt, also habe ich eine neue Outlook-E-Mail registriert und es funktionierte einwandfrei.

#### Telefonnummer

Über [http://sms-activate.org](http://sms-activate.org) ist es möglich, eine Telefonnummer zur Registrierung zu mieten. Das Problem ist jedoch, dass Konten, die mit solchen Telefonnummern registriert sind, gewisse Risiken bergen können.

In China empfehle ich persönlich [https://www.1888.com.mo](https://www.1888.com.mo) für eine China Telecom Macau Karte. Ich habe auch die Giffgaff UK SIM-Karte ausprobiert und kürzlich eine PayGo T-Mobile USA SIM-Karte bestellt.

#### Apple Store Region

Um den App Store in die USA-Region zu wechseln, schalten Sie einen globalen Proxy (USA) ein, und es wird die Zahlungsoption „Keine“ angezeigt, sodass Sie frei wechseln können.

Sie können eine Visa-Karte verwenden, um Geschenkkarten von Amazon zu kaufen oder das Apple Geschenkkartenportal nutzen, um Ihr App Store-Konto aufzuladen.

Die gleiche Methode gilt für Singapur oder andere Regionen.

#### Zahlung

Eine Visa-Karte zu haben, ist praktisch. Allerdings haben Visa-Karten, die von China ausgestellt werden, immer noch einige Einschränkungen. Zum Beispiel akzeptieren Anthropic oder OpenAI keine von China ausgestellten Visa-Karten.

#### VPN

Sie könnten [Proxy-Lösungen in China](./proxy-en) und [Einrichtung Ihres Proxy-Servers](./diy-proxy-en) prüfen.

#### Identität

Ich besitze einen chinesischen Personalausweis und Reisepass, die in bestimmten Situationen hilfreich sein können.