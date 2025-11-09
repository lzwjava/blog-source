---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht des AVL-Baums
translated: true
type: note
---

### Was ist ein AVL-Baum?

Ein AVL-Baum ist eine Art **selbstbalancierender binärer Suchbaum (BST)**, erfunden im Jahr 1962 von Georgy Adelson-Velsky und Evgenii Landis (daher der Name). Wie jeder BST speichert er Daten sortiert: Alle Knoten im linken Teilbaum sind kleiner als der Elternknoten, und alle im rechten sind größer. Das Hauptmerkmal ist, dass er seine Struktur nach Einfüge- oder Löschoperationen automatisch anpasst, um balanciert zu bleiben.

### Wie funktioniert er?

- **Balance-Faktor**: Für jeden Knoten berechnet der Baum einen "Balance-Faktor" als die Höhe des linken Teilbaums minus die Höhe des rechten Teilbaums. Dieser muss immer -1, 0 oder +1 betragen (d.h., die Teilbäume unterscheiden sich um höchstens eine Ebene).
- **Rotationen zum Balancieren**: Wenn eine Einfüge- oder Löschoperation den Balance-Faktor verletzt:
  - **Einfache Rotationen** (links oder rechts) beheben Ungleichgewichte, bei denen die Verletzung im näheren Kind liegt.
  - **Doppelrotationen** (Links-Rechts oder Rechts-Links) behandeln Fälle, bei denen sie im entfernteren Kind liegt.
- Diese Rotationen bewahren die BST-Eigenschaft, während sie die Balance wiederherstellen, und sie laufen in O(1)-Zeit pro Operation ab.

Beispiel: Das Einfügen von Knoten in sortierter Reihenfolge in einen einfachen BST würde ihn zu einer verknüpften Liste machen (unbalanciert). In einem AVL-Baum halten Rotationen ihn in etwa höhenbalanciert, wie in diesem vereinfachten Vorher/Nachher:

```
Unbalanciert (nach Einfügen von: 1,2,3):
    2
   /
  1
 /
3  (eigentlich nach rechts abgewinkelt: 1->2->3)

Nach der Rotation:
  2
 / \
1   3
```

### Was macht ihn besonders?

- **Garantierte Effizienz**: Im Gegensatz zu regulären BSTs, die im schlimmsten Fall O(n) werden können (z.B. schief wie eine Liste), gewährleisten AVL-Bäume **O(log n)** durchschnittliche und schlimmstenfalls Zeit für Suche, Einfügen und Löschen. Das macht sie ideal für Anwendungen, die konsistente Leistung benötigen, wie Datenbanken oder Symboltabellen.
- **Kompromiss**: Sie sind strenger als andere balancierte Bäume (z.B. Rot-Schwarz-Bäume, die etwas mehr Ungleichgewicht für schnelleres Einfügen/Löschen erlauben). AVL priorisiert Suchgeschwindigkeit über Änderungsgeschwindigkeit.
- **Speicher**: Verwendet ein zusätzliches Feld pro Knoten für die Höhen-/Balancenachverfolgung, aber das ist geringfügig.

Kurz gesagt sind AVL-Bäume "besonders" aufgrund ihrer rigorosen Selbstbalancierung, die potentiell chaotische BSTs in zuverlässige, logarithmische Performer verwandelt.

Weitere Details: [AVL-Baum auf Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)