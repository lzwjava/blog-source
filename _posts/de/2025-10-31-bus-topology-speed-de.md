---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Geschwindigkeitsbegrenzungen der Bus-Topologie erklärt
translated: true
type: note
---

### Einschränkungen der Bustopologie

Du liegst genau richtig mit den Hauptmerkmalen: Die Bustopologie verwendet ein einziges gemeinsames Kabel (wie Koaxialkabel in klassischen Ethernet-Setups), das einfach und billig, aber anfällig für Kollisionen ist. Wenn mehrere Geräte gleichzeitig senden wollen, überlappen sich die Signale und verursachen "Zusammenstöße", die eine erneute Übertragung über Protokolle wie CSMA/CD (Carrier Sense Multiple Access with Collision Detection) erfordern.

#### Warum ~100 Mbps wie eine praktische Grenze wirken (auch wenn das Kabel mehr kann)
Die Kabel selbst – ob Kupfer (z.B. Twisted-Pair oder Koax) oder optische Glasfasern – sind hier nicht der Engpass. Glasfaser kann problemlos Gigabits pro Sekunde (oder Terabits in modernen Setups) über lange Strecken mit minimalem Verlust übertragen. Die wirklichen Grenzen ergeben sich aus der **Natur des gemeinsamen Mediums des Busses** und dem physikalischen/Protokoll-Overhead. Hier ist der Grund, warum die Geschwindigkeit in traditionellen Bus-Designs bei etwa 10–100 Mbps gedeckelt ist:

1.  **Ausbreitungsverzögerung und Kollisionserkennung**:
    *   Signale brauchen Zeit, um das Kabel entlang zu laufen (z.B. ~5 ns/Meter in Koax oder ~5 ns/km in Glasfaser).
    *   In einem Bus muss jedes Gerät über die *gesamte Netzwerklänge* hinweg auf Kollisionen "lauschen". Das Protokoll definiert eine "Slot Time" (minimale Zeit zur Erkennung einer Kollision), die länger sein muss als die Round-Trip-Ausbreitungsverzögerung (RTT) für den Worst-Case (Signal von einem Ende zum anderen und zurück).
    *   Für 10 Mbps Ethernet (klassischer Bus) war die maximale Segmentlänge ~500m, um die RTT unter 51,2 μs (512-Bit-Slot-Zeit) zu halten.
    *   Bei 100 Mbps schrumpft die Slot-Zeit proportional (auf ~5,12 μs), was die maximale Länge auf ~100m zwingt. Darüber hinaus bleiben Kollisionen unerkannt, was zu endlosen Fehlern führt.
    *   Auf 1 Gbps erhöhen? Die Slot-Zeit sinkt auf ~0,512 μs, was Segmente auf ~10–20m begrenzt – unpraktisch für einen "Bus", der mehrere Geräte verbindet.

2.  **Kollisions-Overhead und Effizienz**:
    *   CSMA/CD fügt Wiederholungsversuche hinzu: Eine Kollision verschwendet Bandbreite (bis zu 50% Effizienzverlust unter hoher Last).
    *   Höhere Geschwindigkeiten verstärken dies – häufigere Kollisionen bedeuten mehr verschwendete Zyklen, was den effektiven Durchsatz reduziert.
    *   Gemeinsames Medium bedeutet, dass die Gesamtbandbreite auf alle Geräte aufgeteilt wird; keine dedizierte Bandbreite pro Port.

3.  **Signalintegrität und Rauschen**:
    *   Während Glasfaser elektromagnetische Störungen (EMI) besser widersteht als Kupfer, benötigen Bus-Setups dennoch eine präzise Takterkennung.
    *   Bei hohen Geschwindigkeiten verschlechtern Reflexionen, Dämpfung oder Übersprechen auf einer gemeinsamen Leitung die Signale schneller, was mehr Repeater erfordert (die Verzögerung und Kosten hinzufügen).

#### Warum der Weweg vom Bus für höhere Geschwindigkeiten?
Deshalb hat sich Ethernet weiterentwickelt: Nach 100 Mbps (Fast Ethernet) wurde der reine Bus zugunsten einer **Stern-Topologie mit Switches** (z.B. 1 Gbps+) aufgegeben. Switches erstellen Vollduplex-Punkt-zu-Punkt-Verbindungen – keine Kollisionen, volle Bandbreite pro Gerät und längere Reichweiten. Busse sind heute außerhalb von Nischen-/Industrieanwendungen selten.

Wenn du an ein bestimmtes Setup denkst (z.B. CAN-Bus in Autos oder altes 10BASE-T), sind die Prinzipien ähnlich: Protokoll + Physik > Kabelkapazität.

Für vertiefende Informationen:  
[Ethernet Bustopologie Grundlagen](https://en.wikipedia.org/wiki/Bus_network)  
[CSMA/CD Einschränkungen](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html)