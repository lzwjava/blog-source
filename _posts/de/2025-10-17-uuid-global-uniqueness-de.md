---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: UUIDs gewährleisten globale Einzigartigkeit ohne Koordinierung
translated: true
type: note
---

UUIDs können den Zweck der global eindeutigen Identifikation ohne zentrale Autorität erfüllen, da sie mit einem enormen Adressraum entworfen wurden: 128 Bit, die etwa 3,4 × 10^38 mögliche Werte bereitstellen. Dies ist deutlich größer als die Anzahl der UUIDs, die jemals in praktischen Szenarien über alle Systeme weltweit generiert werden. Bei Version-4-UUIDs (den zufälligen, wie die, die Sie geteilt haben) werden 122 dieser Bits mit hochwertigen Zufallsdaten gefüllt, was Duplikate extrem unwahrscheinlich macht.

Was Kollisionen betrifft: Ja, theoretisch ist es möglich, dass zwei UUIDs identisch sind, aber die Wahrscheinlichkeit ist so gering, dass sie für den praktischen Einsatz effektiv Null ist. Dies folgt dem "Geburtstagsparadoxon" in der Wahrscheinlichkeitstheorie – Kollisionen werden wahrscheinlicher, wenn die Anzahl der Elemente wächst, aber selbst dann:

- Die Chance, dass zwei zufällige Version-4-UUIDs kollidieren, beträgt etwa 1 zu 2,71 × 10^18.
- Sie müssten ungefähr 4,8 × 10^18 UUIDs generieren (das wäre, als ob jeder Mensch auf der Erde etwa 600 Millionen besäße) für eine 50%ige Chance auf nur *eine* Dublette.
- Zum Vergleich: Selbst die Generierung von 1 Billion (10^12) UUIDs ergibt ein Kollisionsrisiko von etwa 1 zu einer Milliarde oder weniger.

Verschiedene UUID-Versionen fügen Sicherheitsvorkehrungen hinzu: Version 1 verwendet Zeitstempel und MAC-Adressen, Version 5 hasht Namen mit Namensräumen usw. Aber die Zufälligkeit von Version 4 allein gewährleistet Eindeutigkeit in verteilten Systemen, Datenbanken oder Apps ohne Absprache.

[What are the odds?](https://jhall.io/archive/2021/05/19/what-are-the-odds/)  
[Universally unique identifier - Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)  
[How big is the chance to get a Java UUID.randomUUID collision?](https://stackoverflow.com/questions/24876188/how-big-is-the-chance-to-get-a-java-uuid-randomuuid-collision)