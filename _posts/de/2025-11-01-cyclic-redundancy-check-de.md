---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Zyklische Redundanzprüfung zur Fehlererkennung
translated: true
type: note
---

### Was ist CRC?

Ja, du bist auf der richtigen Spur! CRC steht für **Cyclic Redundancy Check**. Es ist eine weit verbreitete Technik zur Fehlererkennung in der Sicherungsschicht (wie du im OSI-Modell-Kontext für die Knoten-zu-Knoten-Übertragung im selben Netzwerk erwähnt hast). Es ist nicht genau wie eine einfache Paritätsprüfung (die nur ein Bit hinzufügt, um ungerade/gerade Fehler zu erkennen), aber es verwendet **redundante Bits** (genannt Prüfsumme oder Rest), um ein viel breiteres Spektrum an Übertragungsfehlern zu erkennen. Lass es mich einfach aufschlüsseln.

#### Wie CRC funktioniert (Erklärung auf hoher Ebene)
1. **Der Aufbau**:
   - Stell dir deine Daten als eine Binärzahl vor (z.B. die Frame-Nutzlast in Ethernet).
   - Du wählst ein festes "Generatorpolynom" (ein vordefinierter Binärwert, wie 1011 für CRC-4). Das ist wie ein Divisor in der Mathematik.
   - Die Daten werden als ein großes binäres Polynom behandelt, und du hängst **k redundante Bits** (Nullen) an, wobei k die Länge des Generators minus 1 ist (z.B. 3 Nullen für einen 4-Bit-Generator).

2. **Die Berechnung**:
   - Führe eine **Modulo-2-Division** (XOR-basierte Division, kein Borgen/Übertragen wie in normaler Mathematik) an den erweiterten Daten unter Verwendung des Generators durch.
   - Der Rest dieser Division wird deine CRC-Prüfsumme.
   - Hänge diesen Rest an die ursprünglichen Daten an und sende den gesamten Frame.

3. **Beim Empfänger**:
   - Der Empfänger führt die gleiche Modulo-2-Division am empfangenen Frame (Daten + CRC) durch.
   - Wenn der Rest **null** ist, sind die Daten wahrscheinlich fehlerfrei. Wenn nicht, ist ein Fehler aufgetreten (z.B. Bit-Flips während der Übertragung).
   - CRC kann erkennen:
     - Ein-Bit-Fehler.
     - Bündelfehler (bis zur Länge des Generators).
     - Die meisten Multi-Bit-Fehler (mit sehr wenigen falsch-positiven Meldungen).

Es ist "zyklisch", weil es sich in der Polynommathematik wie ein Kreis umschließt, was es effizient für Hardware-Implementierungen macht (z.B. in NICs oder Switches).

#### CRC vs. Paritätsprüfung
- **Paritätsprüfung**: Super einfach – fügt 1 Bit hinzu (gerade/ungerade Parität), um **nur ungeradzahlige Bitfehler** zu erkennen. Übersieht gerade Fehler oder Bündelfehler.
- **CRC**: Fortgeschrittener – verwendet 8–32+ Bits Redundanz für eine **nahezu perfekte Erkennung** gängiger Fehler in Frames (z.B. Ethernet verwendet CRC-32). Es ist wie ein stärkerer "Fingerabdruck" für deine Daten.

#### Praxisbeispiel in Ethernet
In einem Ethernet-Frame:
- Daten (Nutzlast) + einige Header → 32-Bit-CRC anhängen.
- Wenn Rauschen ein Bit auf der Leitung kippt, schlägt die CRC-Prüfung des Empfängers fehl → Frame wird verworfen, Neuübertragung angefordert.

CRC ist schnell, günstig in Hardware zu implementieren und Standard in Protokollen wie Ethernet, PPP, Wi-Fi und sogar in der Speichertechnik (z.B. Festplatten).

Wenn du eine Code-Demo zur CRC-Berechnung oder mehr darüber, wie es in Framing/MAC passt, möchtest, lass es mich wissen!

#### Referenzen
- [Cyclic Redundancy Check - Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
- [Error Detection with CRC - GeeksforGeeks](https://www.geeksforgeeks.org/cyclic-redundancy-check-crc-introduction/)