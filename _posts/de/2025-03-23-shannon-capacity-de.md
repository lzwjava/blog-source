---
audio: false
generated: true
lang: de
layout: post
title: Shannons Kapazitätsformel
translated: true
type: note
---

Die Shannon-Kapazitätsformel lautet eigentlich:

C = B log₂(1 + S/N)

Dabei gilt:
- C ist die Kanalkapazität in Bits pro Sekunde
- B ist die Bandbreite in Hertz
- S/N ist das Signal-Rausch-Verhältnis (Leistungsverhältnis)
- log₂ ist der Logarithmus zur Basis 2

Diese Formel repräsentiert die theoretische maximale Datenrate, die zuverlässig über einen Kommunikationskanal mit Bandbreite B und einem Signal-Rausch-Verhältnis von S/N übertragen werden kann.

Um zu verstehen, warum dies korrekt ist:

1. **Bandbreitenfaktor (B)**: Die Bandbreite skaliert die Kapazität direkt - eine Verdopplung der Bandbreite verdoppelt die Kapazität.

2. **Logarithmische Beziehung**: Der log₂ zeigt, dass die Kapazität logarithmisch mit S/N zunimmt, nicht linear. Das bedeutet:
   - Eine Verdopplung von S/N verdoppelt nicht die Kapazität
   - Jedes zusätzliche "Bit" an Kapazität erfordert eine Verdopplung des S/N

3. **1 + S/N Term**: Die Addition von 1 stellt sicher, dass die Kapazität immer positiv ist, selbst bei sehr kleinen S/N-Werten.

Diese Formel ist grundlegend für die Informationstheorie, da sie die theoretische Obergrenze dafür festlegt, wie viel Information über einen verrauschten Kanal übertragen werden kann, unabhängig vom verwendeten Kodierungsschema.

Möchten Sie, dass ich einen bestimmten Aspekt dieser Formel genauer erkläre?