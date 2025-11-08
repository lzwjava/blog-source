---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Bereich von IP-Adressen-Subnetzen erklärt
translated: true
type: note
---

Ja, das ist korrekt. Die IP-Adresse `192.168.1.35/24` gehört zum Subnetz `192.168.1.0/24`, das den gesamten Bereich von 256 Adressen umfasst: von `192.168.1.0` (Netzwerkadresse) bis `192.168.1.255` (Broadcast-Adresse).

### Kurze Übersicht:
- **/24** bedeutet eine Subnetzmaske von `255.255.255.0`, die die ersten drei Oktette (`192.168.1`) festlegt und das letzte Oktett von 0 bis 255 variieren lässt.
- Verwendbare Host-Adressen: `192.168.1.1` bis `192.168.1.254` (ohne Netzwerk- und Broadcast-Adresse).
- Ihr spezifischer Host (`192.168.1.35`) ist nur eine Adresse innerhalb dieses Bereichs.

Wenn Sie Subnetze für ein anderes Präfix berechnen oder die Adresse mit einem Tool überprüfen müssen, lassen Sie es mich wissen!