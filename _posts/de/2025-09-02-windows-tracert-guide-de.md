---
audio: false
generated: true
image: false
lang: de
layout: post
title: Windows Tracert Netzwerkpfad-Diagnoseleitfaden
translated: true
type: note
---

Unter Windows ist **`tracert`** (kurz für *Trace Route*) ein diagnostisches Kommandozeilen-Tool, mit dem der Pfad verfolgt wird, den Pakete von Ihrem Computer zu einem Zielhost (wie einer Website oder IP-Adresse) nehmen. Es wird hauptsächlich verwendet, um zu identifizieren, wo Verzögerungen oder Verbindungsprobleme in einer Netzwerkroute auftreten.

So funktioniert es Schritt für Schritt:

### 1. ICMP Echo Requests mit inkrementellem TTL

* `tracert` sendet **ICMP Echo Request Pakete** (ähnlich wie `ping`).
* Es manipuliert das **Time-To-Live (TTL)**-Feld im IP-Header.
* TTL beginnt bei 1 und erhöht sich (2, 3, 4, …) mit jeder Sonde.

### 2. TTL-Ablauf und "Time Exceeded"-Antworten

* Wenn ein Router ein Paket empfängt, dekrementiert er den TTL-Wert um 1.
* Wenn TTL **0** erreicht, verwirft der Router das Paket und sendet eine **ICMP Time Exceeded**-Nachricht an den Absender.
* Dadurch erfährt `tracert` die Identität (IP/Hostname) dieses Routers.

### 3. Aufbau der Route

* Für TTL = 1 sehen Sie den ersten Hop (Ihr Standard-Gateway).
* Für TTL = 2 sehen Sie den nächsten Router, und so weiter.
* Dies wird so lange fortgesetzt, bis:

  * Der Zielhost mit einer **ICMP Echo Reply** antwortet, oder
  * das maximale Hop-Limit (standardmäßig 30) erreicht ist.

### 4. Messen der Latenz

* `tracert` sendet standardmäßig **drei Sonden** pro Hop.
* Es zeigt die **Round-Trip Time (RTT)** in Millisekunden für jede Sonde an.
* Wenn ein Router nicht antwortet, sehen Sie stattdessen `*`.

### 5. Beispielausgabe

```text
Tracing route to example.com [93.184.216.34]
over a maximum of 30 hops:

  1     1 ms    <1 ms     1 ms  192.168.1.1
  2    10 ms     9 ms    11 ms  isp-gateway.example.net [203.0.113.1]
  3    25 ms    23 ms    24 ms  core-router.example.net [198.51.100.1]
  ...
  8    45 ms    46 ms    47 ms  example.com [93.184.216.34]
```

### 6. Hinweise zum Verhalten

* Einige Router blockieren oder priorisieren ICMP-Antworten herab, was zu `* * *` führt.
* `tracert` unter **Windows** verwendet ICMP Echo Requests, während `traceroute` unter Linux/Unix oft **UDP-Sonden** verwendet (obwohl dies geändert werden kann).
* Firewalls oder ISP-Filterung können manchmal Teile der Route verbergen.

---

👉 Soll ich auch erklären, **wie man Fälle wie `* * *` oder große Verzögerungen** in einem `tracert`-Ergebnis interpretiert, damit Sie es für die echte Fehlerbehebung nutzen können?