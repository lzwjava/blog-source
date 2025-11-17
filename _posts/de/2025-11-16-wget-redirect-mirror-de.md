---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Normaler wget-Umleitungsspiegel von mirror.accum.se
translated: true
type: note
---

Ihr `wget`-Befehl ruft `https://mirror.accum.se/mirror/wikimedia.org/dumps/...` auf und erhält eine **302-Weiterleitung** zu `https://laotzu.ftp.acc.umu.se/...`. Dies ist ein völlig normales und erwartetes Verhalten für den **accum.se**-Mirror – hier ist der Grund, warum es passiert und was es bedeutet:

### Warum die Weiterleitung passiert
`mirror.accum.se` ist nur ein **Weiterleitungs-/Lastverteilungsdienst** (Redirector / Load-Balancer), der vom Academic Computer Club (ACC) an der Universität Umeå in Schweden betrieben wird.
Er hostet die Dateien **nicht** selbst. Stattdessen:

- Er ermittelt die Geolokation Ihrer IP-Adresse (oder manchmal die Auslastung)
- Er leitet Sie automatisch auf den schnellsten/nächstgelegenen tatsächlichen Speicherserver in ihrem Mirror-Farm weiter
- In Ihrem Fall wurde `laotzu.ftp.acc.umu.se` ausgewählt (dies ist der echte FTP/HTTP-Server, der die Daten bereitstellt)

Dies ist das gleiche System, das sie seit vielen Jahren verwenden. Andere gebräuchliche Hostnamen, auf die Sie weitergeleitet werden könnten, sind:

- `issac.ftp.acc.umu.se`
- `laotzu.ftp.acc.umu.se` (der, den Sie erhalten haben)
- `morpork.ftp.acc.umu.se`
- usw.

Auch wenn Sie in Ihrem Skript `mirror.accum.se` angegeben haben, laden Sie die Dateien fast immer von einem der `*.ftp.acc.umu.se` Back-End-Server herunter.

### Warum Sie „206 Partial Content“ bei der ersten Datei gesehen haben
Weil Sie (oder jemand/ein Skript) bereits zuvor mit dem Download genau dieser Datei begonnen hatten, hat `wget -c` die teilweise vorhandene lokale Datei erkannt und eine `Range`-Anfrage gesendet. Der Server hat den Download korrekt fortgesetzt → 206 Partial Content. Das ist gut!

### Gibt es ein Problem?
Nein. Alles funktioniert wie beabsichtigt.

- Die Weiterleitung ist normal und harmlos
- Der finale Server (`laotzu.ftp.acc.umu.se`) ist immer noch der offizielle ACC/Wikimedia-Mirror
- Die Prüfsummen sind identisch, unabhängig davon, auf welchen Back-End-Server Sie weitergeleitet werden

### Wenn Sie die Weiterleitung vermeiden möchten (optional)
Sie können den Redirector komplett umgehen und direkt auf einen der echten Hosts verweisen, z. B.:

```bash
# Diese drei sind hinter mirror.accum.se ohnehin per Round-Robin erreichbar
wget -c https://laotzu.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
# oder
wget -c https://issac.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
```

Die meisten Leute verwenden jedoch weiterhin `mirror.accum.se`, da der Redirector automatisch den besten Server für Sie auswählt.

### TL;DR
Ihr Skript ist in Ordnung. Die 302-Weiterleitung von `mirror.accum.se` → `laotzu.ftp.acc.umu.se` ist das normale, erwartete Verhalten dieses Mirrors. Es ist nichts falsch gelaufen und Sie laden immer noch das authentische Wikimedia-Dump herunter. Verwenden Sie weiterhin `mirror.accum.se` – es ist einer der schnellsten und zuverlässigsten Mirrors weltweit.