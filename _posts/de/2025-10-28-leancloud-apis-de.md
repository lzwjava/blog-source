---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: LeanCloud-APIs nicht Uluru genannt
translated: true
type: note
---

Nein, LeanCloud bezeichnet seine öffentliche API nicht als "Uluru API". Die offiziellen APIs werden als LeanCloud REST API (für Datenspeicherung, Abfragen usw.), Cloud Engine REST API (für serverseitige Funktionen und Hooks) und ähnliche dienstspezifische Endpunkte wie für Push-Benachrichtigungen oder Dateispeicherung bezeichnet. Diese sind umfassend auf ihrer Entwickler-Website (docs.leancloud.cn) dokumentiert, ohne jeglichen Verweis auf "Uluru".

Allerdings scheint "Uluru" ein interner oder früher Codename zu sein, der mit ihrer Produkt- oder SDK-Entwicklung in Verbindung steht. Dies basiert auf einem archivierten npm-Paket namens **uluru-js-sdk** (Version 0.1.0, veröffentlicht vor ~12 Jahren unter dem "avos"-Publisher-Account). AVOS Cloud war der ursprüngliche Name von LeanCloud vor der Umbenennung, und dieses Paket wird als "JavaScript SDK for PAAS" (Platform as a Service) beschrieben, was zu LeanClouds Backend-Diensten passt. Es unterstützt sowohl Browser- als auch Node.js-Umgebungen für Kernfunktionen wie Datenoperationen – was LeanClouds frühen Angeboten entspricht – wurde aber niemals öffentlich als das Haupt-SDK beworben. Aktuelle SDKs sind als "LeanCloud SDK" gebrandet (z.B. für Java, Python, JavaScript usw.) und auf GitHub unter leancloud/ verfügbar.

Falls sich dies auf etwas Aktuelleres oder Spezifischeres bezieht (z.B. ein privates/internes Tool), ist es nicht öffentlich dokumentiert. Für offizielle API-Details besuchen Sie die [LeanCloud Docs](https://docs.leancloud.cn/en/).