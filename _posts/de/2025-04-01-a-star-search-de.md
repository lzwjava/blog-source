---
audio: false
generated: true
lang: de
layout: post
title: A-Stern-Suchalgorithmus
translated: true
type: note
---

Der **A* (A-Star)-Suchalgorithmus** ist ein beliebter Algorithmus zur Pfadsuche und zum Durchlaufen von Graphen, der in der Informatik und künstlichen Intelligenz verwendet wird. Er wird häufig eingesetzt, um den kürzesten Pfad von einem Startpunkt (oder Knoten) zu einem Zielpunkt (oder Ziel) in einem Graphen zu finden, während er mögliche Pfade effizient erkundet.

A* kombiniert Elemente des **Dijkstra-Algorithmus** (der den kürzesten Pfad garantiert) und der **Greedy-Best-First-Suche** (die versucht, das Ziel so schnell wie möglich zu finden). Das Hauptmerkmal von A* ist, dass es sowohl die tatsächlichen Kosten, um einen Knoten zu erreichen (vom Startknoten aus), als auch eine Heuristik verwendet, die die Kosten von diesem Knoten zum Ziel schätzt.

### So funktioniert A*:
1. **Beginnen mit einer offenen Liste**: Die offene Liste enthält Knoten, die noch erkundet werden müssen. Anfangs befindet sich nur der Startknoten auf dieser Liste.
2. **Berechnen der Bewertungen**: Jedem Knoten in der offenen Liste wird eine Bewertung zugewiesen, die auf zwei Faktoren basiert:
   - **g(n)**: Die Kosten, um den aktuellen Knoten vom Startknoten aus zu erreichen.
   - **h(n)**: Eine heuristische Schätzung der Kosten, um das Ziel vom aktuellen Knoten aus zu erreichen (dies ist domainspezifisch, z.B. die Luftlinienentfernung oder euklidische Distanz).
   - **f(n) = g(n) + h(n)**: Die gesamten geschätzten Kosten, die zur Priorisierung der Knoten verwendet werden. Knoten mit dem niedrigsten f(n) werden zuerst erkundet.
3. **Erweitern des vielversprechendsten Knotens**: Der Knoten mit der niedrigsten f(n)-Bewertung wird zur Erkundung ausgewählt. Er wird in eine "geschlossene Liste" von bereits untersuchten Knoten verschoben.
4. **Nachbarn überprüfen**: Der Algorithmus untersucht die Nachbarn des aktuellen Knotens. Wenn ein Nachbar noch nicht besucht wurde oder mit geringeren Kosten erreicht werden kann, wird er der offenen Liste hinzugefügt.
5. **Wiederholen**, bis das Ziel erreicht ist oder die offene Liste leer ist (was darauf hinweist, dass kein Pfad existiert).

### Wichtige Komponenten:
- **g(n)**: Die tatsächlichen Kosten vom Startknoten zum aktuellen Knoten.
- **h(n)**: Die heuristische Schätzung vom aktuellen Knoten zum Ziel (kann je nach Problem variieren).
- **f(n) = g(n) + h(n)**: Die Gesamtkosten, die zur Priorisierung der Knoten für die Erkundung dienen.

### Heuristiken:
Die Heuristikfunktion ist entscheidend für die Effizienz von A*. Eine gängige Heuristik für rasterbasierte Pfadsuche ist die **Manhattan-Distanz** (Summe der horizontalen und vertikalen Entfernungen) oder die **euklidische Distanz** (Luftlinienentfernung) für kontinuierliche Räume.

### Beispielanwendungen:
- **Navigationssysteme** (GPS)
- **Spiele und KI** (Pfadsuche für Charaktere oder Agenten)
- **Robotik** (zum Planen effizienter Pfade)

Zusammenfassend ist A* ein hocheffizienter Algorithmus, weil er Pfade systematisch auf der Grundlage sowohl der bekannten Kosten als auch der geschätzten zukünftigen Kosten erkundet und so sicherstellt, dass er, wenn möglich, die optimale Lösung findet.