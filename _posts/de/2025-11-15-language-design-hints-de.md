---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Hinweise zum Entwurf von Programmiersprachen
translated: true
type: note
---

### Überblick
„Hints on Programming Language Design“ ist ein klassisches, einflussreiches Papier von Sir Tony Hoare (C. A. R. Hoare), das ursprünglich als Hauptvortrag auf dem **SIGACT/SIGPLAN Symposium on Principles of Programming Languages** im Oktober 1973 vorgestellt und später 1974 veröffentlicht wurde.

Es ist keine formale akademische Arbeit mit Theoremen – es ist eine persönliche, meinungsstarke und bemerkenswert weitsichtige Sammlung von „Hinweisen“ (Ratschlägen) eines der größten Köpfe der Informatik darüber, wie Programmiersprachen entworfen werden sollten (und wie nicht).

### Kernaussage
Hoares zentrale These ist, dass **das Design von Programmiersprachen zu sehr von hastiger Implementierung dominiert wurde und nicht genug von sorgfältiger, langfristiger intellektueller Disziplin**. Er ist der Ansicht, dass die meisten Sprachen der frühen 1970er Jahre (PL/I, ALGOL 68, Pascal, etc.) unter Überkomplexität, willkürlichen Entscheidungen und schlechter Abstraktion litten – und dass zukünftige Sprachen radikal einfacher und prinzipienorientierter sein müssen.

### Wichtige Hinweise / Ideen im Papier

1.  **Vorzeitige Optimierung ist die Wurzel allen Übels** (im Sprachdesign)
    Fügen Sie keine Funktionen hinzu, nur weil sie 10–20 % Leistungssteigerung bringen, wenn sie die Sprache für immer komplizierter machen.

2.  **Einfachheit vor Leistungsfähigkeit**
    „Der Preis für Zuverlässigkeit ist das Streben nach größter Einfachheit.“
    Eine Sprache sollte so wenige Konzepte wie möglich haben. Komplexität sollte in Bibliotheken ausgelagert werden, nicht in die Kernsprache.

3.  **Vermeiden Sie „eine Sprache, um sie alle zu beherrschen“**
    Er kritiert große Allzwecksprachen (insbesondere PL/I und ALGOL 68). Besser sind kleine, saubere Sprachen, die auf bestimmte Domänen zugeschnitten sind.

4.  **Orthogonalität und Regularität**
    Sprachfeatures sollten sich auf vorhersehbare, nicht überraschende Weise kombinieren lassen (ein Prinzip, das später durch Perls „Es gibt mehr als einen Weg, es zu tun“ berühmt wurde – was Hoare verabscheut hätte).

5.  **Abstraktion und Information Hiding**
    Starke Unterstützung für Module, abstrakte Datentypen und Kapselung – Ideen, die CLU, Modula-2 und später Ada und objektorientierte Sprachen direkt beeinflussten.

6.  **Sicherheit und Zuverlässigkeit zuerst**
    Sprachen sollten es einfach machen, korrekte, beweisbare Programme zu schreiben. Er setzte sich bereits für starke Typisierung, Korrektheitsbeweise ein und forderte, Features zu vermeiden, die die Verifikation erschweren.

7.  **Konkrete Syntax ist wichtig, aber nicht so wichtig, wie die Leute denken**
    Geschweifte Klammern vs. BEGIN/END ist relativ unwichtig im Vergleich zur semantischen Klarheit.

8.  **Historische Bedauern**
    Er reflektiert über ALGOL 60 (das er wegen seiner Eleganz liebte) im Vergleich zu ALGOL 68 (das er für eine Katastrophe der Übertechnisierung hielt).

9.  **Vision einer idealen Sprache (1973!)**
    - Sehr kleiner Kern
    - Leistungsfähiges Modul-/Abstraktionssystem
    - Starke statische Typisierung
    - Separate Kompilierung
    - Einrichtungen für nebenläufige Programmierung (Communicating Sequential Processes – CSP – wird hier bereits angedeutet; er veröffentlichte CSP fünf Jahre später, 1978)

### Berühmte Zitate aus dem Papier
-   „Es gibt zwei Wege, ein Softwaredesign zu konstruieren: Der eine ist, es so einfach zu machen, dass es offensichtlich keine Mängel gibt, und der andere, es so kompliziert zu machen, dass es keine offensichtlichen Mängel gibt. Die erste Methode ist bei weitem schwieriger.“
-   „Ich schließe daraus, dass es zwei Wege gibt, Programmiersprachen zu entwerfen: Macht sie so kompliziert, dass es keine offensichtlichen Mängel gibt, oder macht sie so einfach, dass es offensichtlich keine Mängel gibt.“

### Wirkung & Vermächtnis
Dieser Vortrag von 1973 sagte im Grunde die Philosophie des Sprachdesigns der nächsten 30–40 Jahre voraus:
-   Beeinflusste Simula → Smalltalk → modernes OO
-   Inspirierte direkt Modula, Ada, ML, Haskells Modulsystem
-   Die gesamte „Einfachheit-zuerst“-Bewegung (Go, Rusts ursprüngliche Philosophie, etc.) ist ihm zu großem Dank verpflichtet
-   Seine Kritik an ALGOL 68 und PL/I wird immer noch zitiert, wenn Leute sich über C++, Java oder Scala-Bloat beschweren

### Wo man es lesen kann
Die ursprüngliche Version des Stanford Technical Reports von 1973 (am häufigsten zitiert):
[Hints on Programming Language Design – C. A. R. Hoare (1973)](http://i.stanford.edu/pub/cstr/reports/cs/tr/73/403/CS-TR-73-403.pdf)

Eine leicht überarbeitete Version erscheint in dem Buch *Programming Language Design and Implementation* und in Hoares gesammelten Werken.

Es ist nur etwa 25 Seiten lang und auch mehr als 50 Jahre später bemerkenswert lesbar – sehr zu empfehlen, wenn Sie sich für Sprachdesign interessieren.