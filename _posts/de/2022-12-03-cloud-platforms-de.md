---
audio: false
generated: false
image: true
lang: de
layout: post
title: Einige Globale Cloud-Plattformen
translated: true
---

<div align="center"><img src="/assets/images/cloud/platform.jpg" width="400px"/><img/></div>

* [Azure](#azure)
* [AWS Lightsail](#aws-lightsail)
* [Digital Ocean](#digital-ocean)
* [Vultr](#vultr)
* [Google Cloud - Fehlschlag](#google-cloud---fail)
* [Überblick](#outline)
* [Zusammenfassung](#summary)

Ich habe kürzlich einige Cloud-Plattformen ausprobiert. Ich habe sie genutzt, um meinen eigenen Proxy-Server einzurichten. Zuvor hatte ich einen Proxy-Server eines Drittanbieters verwendet. Dieser Server wird von vielen Nutzern genutzt, weshalb die Geschwindigkeit manchmal langsam war. Ich habe versucht, meinen eigenen Server einzurichten, um dieses Problem zu beheben.

## Azure

Azure ist eine gute Option. Ich habe hier 3 virtuelle Maschinen erstellt. Weil die Plattform mir 200 Dollar Guthaben kostenlos zur Verfügung gestellt hat. Meine Maschinen befinden sich in Katar, den USA und Hongkong. Die Ping-Zeit von meinem Laptop in Guangzhou zum Server in Katar beträgt 150ms. Jetzt gehen die Ping-Pakete zum Server in den USA zu 100% verloren. Vor zwei Tagen konnte ich ihn noch erfolgreich anpingen. Und die Ping-Pakete zum Server in Hongkong gehen ebenfalls zu 100% verloren. Ich habe sie in meinem iOS-Proxy-Client getestet und sie konnten keine Verbindung herstellen. Ich muss sie abschalten. Obwohl die Kosten kostenlos sind, hat ein verlorener Server keinen Nutzen für mich.

<div align="center"><img src="/assets/images/cloud/azure.png" /><img/></div>

Schauen wir uns die Konsole und den Netzwerk-Tab an, oben und unten.

<div align="center"><img src="/assets/images/cloud/network.png" /><img/></div>

Meine benutzerdefinierten Netzwerkeinstellungen sind einfach. Ich lasse jeden Port zwischen 1024 und 65535 für jedes Protokoll offen. Da es mein Proxy-Server ist, habe ich keine geheimen Daten oder Programme darin. Daher folge ich dem Vorschlag der Outline App, dies so zu handhaben.

## AWS Lightsail

Lightsail ist ein leichtgewichtiges Produkt von AWS. AWS bietet eine Vielzahl von Produkten an. Manchmal möchten wir einfach nur einige virtuelle Maschinen darin erstellen. Deshalb stellt uns AWS Lightsail zur Verfügung.

<div align="center"><img src="/assets/images/cloud/lightsail.png" /><img/></div>

## Digital Ocean

Ich habe Digital Ocean auf ausländischen Cloud-Plattformen häufig genutzt, insbesondere von 2016 bis 2018. Ich habe jeden Monat 5 Dollar ausgegeben.

Wir erstellen einen Droplet wie folgt:

<div align="center"><img src="/assets/images/cloud/do.png" /><img/></div>

Dies ist meine Rechnungshistorie:

<div align="center"><img src="/assets/images/cloud/bill.png" /><img/></div>

## Vultr

Ich habe Vultr von 2018 bis 2020 genutzt.

<div align="center"><img src="/assets/images/cloud/vultr.png" /><img/></div>

## Google Cloud - Fehlschlag

Ich möchte auch Google Cloud ausprobieren. Allerdings bin ich gescheitert. Sie unterstützen keine Nutzer aus China. Obwohl wir falsche Informationen angeben könnten, als wären wir Bürger anderer Länder, haben wir nicht die entsprechende Kreditkarte, um uns erfolgreich zu registrieren.

<div align="center"><img src="/assets/images/cloud/google.png" /><img/></div>

## Gliederung

Outline ist keine Cloud-Plattform. Es ist ein Proxy-Tool. Da es mir hilft, meinen Proxy-Server einzurichten, muss ich einen separaten Absatz schreiben, um es zu loben. Es ist wirklich hilfreich. Du kannst mehr darüber erfahren, indem du es online suchst.

<div align="center"><img src="/assets/images/cloud/outline.png" /><img/></div>

## Zusammenfassung

Der günstigste Server mit der niedrigsten Konfiguration kostet normalerweise etwa 5 Dollar pro Monat. Dies reicht aus, um als Proxy-Server für einige Benutzer zu fungieren. Die Server in Singapur, Hongkong oder anderen asiatischen Regionen sind in der Regel schneller verbunden als die Server in den USA oder Europa. Manchmal funktioniert der Server, wenn Sie ihn gerade erst eingerichtet haben, einwandfrei. Nach ein paar Tagen kann er jedoch wie ein Zombie arbeiten. Was Geschwindigkeit und Stabilität betrifft, können Sie die Wahrheit also nur im täglichen Gebrauch herausfinden.