---
audio: false
generated: true
lang: de
layout: post
title: Diagonalisierbar
translated: true
type: note
---

Um zu bestimmen, welche Option notwendig ist, damit eine Matrix diagonalisierbar ist, werde ich jede Aussage untersuchen.

Eine quadratische Matrix A ist genau dann diagonalisierbar, wenn es eine invertierbare Matrix P gibt, so dass P⁻¹AP eine Diagonalmatrix ist. Dies geschieht genau dann, wenn A einen vollständigen Satz linear unabhängiger Eigenvektoren besitzt.

Lassen Sie uns jede Option analysieren:

a) Die Matrix muss mindestens einen Eigenwert haben.
Während alle n×n-Matrizen mindestens einen Eigenwert haben (im komplexen Zahlenkörper), garantiert dies allein noch keine Diagonalisierbarkeit. Eine Matrix könnte Eigenwerte haben, aber dennoch nicht diagonalisierbar sein, wenn sie nicht genügend linear unabhängige Eigenvektoren besitzt.

b) Die Matrix muss verschiedene Eigenwerte haben.
Verschiedene Eigenwerte zu haben, ist hinreichend, aber nicht notwendig für Diagonalisierbarkeit. Eine Matrix mit wiederholten Eigenwerten kann immer noch diagonalisierbar sein, wenn sie genügend linear unabhängige Eigenvektoren besitzt, die diesen wiederholten Eigenwerten zugeordnet sind.

c) Die Matrix muss genügend linear unabhängige Eigenvektoren haben.
Dies ist genau die notwendige und hinreichende Bedingung für Diagonalisierbarkeit. Insbesondere ist eine n×n-Matrix genau dann diagonalisierbar, wenn sie n linear unabhängige Eigenvektoren besitzt, die eine Basis für den Vektorraum bilden.

Daher ist Option c) die richtige Antwort: Eine Matrix ist genau dann diagonalisierbar, wenn sie genügend linear unabhängige Eigenvektoren besitzt.

---

Ich werde erklären, warum Option (c) – das Vorhandensein von genügend linear unabhängigen Eigenvektoren – die notwendige Bedingung für Diagonalisierbarkeit ist.

Wenn wir sagen, eine Matrix A ist diagonalisierbar, meinen wir, dass wir eine invertierbare Matrix P finden können, so dass P⁻¹AP = D, wobei D eine Diagonalmatrix ist. Die Spalten von P sind die Eigenvektoren von A, und die Diagonaleinträge von D sind die entsprechenden Eigenwerte.

Hier ist der Grund, warum jede Option funktioniert oder nicht funktioniert:

Für Option (a): Während jede quadratische Matrix mindestens einen Eigenwert hat (im komplexen Zahlenkörper), garantiert das bloße Vorhandensein von Eigenwerten keine Diagonalisierbarkeit. Betrachten Sie die Matrix:
[1 1]
[0 1]

Sie hat einen Eigenwert (λ = 1) mit algebraischer Vielfachheit 2, aber nur einen linear unabhängigen Eigenvektor. Diese Matrix ist trotz vorhandener Eigenwerte nicht diagonalisierbar.

Für Option (b): Verschiedene Eigenwerte zu haben, ist hinreichend, aber nicht notwendig. Wenn eine Matrix verschiedene Eigenwerte hat, sind die Eigenvektoren automatisch linear unabhängig. Matrizen mit wiederholten Eigenwerten können jedoch immer noch diagonalisierbar sein, wenn sie genügend linear unabhängige Eigenvektoren besitzen.

Für Option (c): Dies ist genau die Definition von Diagonalisierbarkeit. Eine n×n-Matrix ist genau dann diagonalisierbar, wenn sie n linear unabhängige Eigenvektoren besitzt. Dies liegt daran, dass:
- Der Diagonalisierungsprozess erfordert, dass P invertierbar ist
- P ist genau dann invertierbar, wenn seine Spalten linear unabhängig sind
- Die Spalten von P sind die Eigenvektoren von A

Diese Bedingung adressiert direkt die grundlegende Anforderung für die Diagonalisierung – das Vorhandensein einer vollständigen Basis von Eigenvektoren für den Vektorraum.