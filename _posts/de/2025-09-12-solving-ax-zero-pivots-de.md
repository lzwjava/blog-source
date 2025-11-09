---
audio: false
date: 2025-09-12
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Lösen von Ax Gleich Null Pivotvariablen
translated: true
type: note
---

Dieses Video ist **Vorlesung 7** aus **MIT's *18.06 Lineare Algebra* Kurs (Frühjahr 2005)**, gelehrt von **Professor Gilbert Strang**. Das Thema ist:

### **"Lösen von \\( A\mathbf{x} = \mathbf{0} \\): Pivot-Variablen und spezielle Lösungen"**

---

### **Wichtige Konzepte, die in der Vorlesung behandelt werden:**
1. **Homogene Systeme (\\( A\mathbf{x} = \mathbf{0} \\))**
   - Ein System linearer Gleichungen, bei dem die rechte Seite der Nullvektor ist.
   - Hat immer mindestens die **triviale Lösung** \\( \mathbf{x} = \mathbf{0} \\).
   - Wenn es **freie Variablen** gibt, gibt es unendlich viele Lösungen.

2. **Pivot-Variablen vs. freie Variablen**
   - **Pivot-Variablen**: Entsprechen Spalten mit Pivots (führende Einträge ungleich Null) in der **Zeilenstufenform (RREF)** von \\( A \\).
   - **Freie Variablen**: Entsprechen Spalten **ohne Pivots** (können beliebige Werte annehmen).
   - Die Anzahl der freien Variablen = Anzahl der Spalten − Rang von \\( A \\).

3. **Spezielle Lösungen (Basis für den Nullraum)**
   - Für jede freie Variable setzt man sie auf **1** und die anderen auf **0** und löst dann nach den Pivot-Variablen auf.
   - Diese Lösungen bilden eine **Basis** für den **Nullraum** von \\( A \\) (alle Lösungen zu \\( A\mathbf{x} = \mathbf{0} \\)).
   - Der Nullraum ist ein **Unterraum** von \\( \mathbb{R}^n \\).

4. **Rang und der Nullraum**
   - Wenn \\( A \\) eine \\( m \times n \\) Matrix mit Rang \\( r \\) ist:
     - Anzahl der Pivot-Variablen = \\( r \\).
     - Anzahl der freien Variablen = \\( n - r \\).
     - Dimension des Nullraums = \\( n - r \\).

5. **Beispiel-Durchlauf**
   - Strang arbeitet ein Beispiel durch (wahrscheinlich eine Matrix mit Rang < Anzahl der Spalten), um zu veranschaulichen:
     - Finden der RREF.
     - Identifizieren von Pivot- und freien Variablen.
     - Konstruieren spezieller Lösungen.
     - Darstellen der allgemeinen Lösung als Linearkombination der speziellen Lösungen.

6. **Geometrische Interpretation**
   - Der Nullraum repräsentiert alle Vektoren \\( \mathbf{x} \\), die durch Multiplikation mit \\( A \\) auf Null "kollabiert" werden.
   - Für eine 3×3 Matrix mit Rang 2 ist der Nullraum eine **Gerade** durch den Ursprung.

---

### **Warum diese Vorlesung wichtig ist:**
- Führt den **Nullraum** ein (ein fundamentaler Unterraum in der linearen Algebra).
- Verbindet **Gauß-Elimination** mit der Struktur von Lösungen.
- Legt den Grundstein für das Verständnis von **linearer Unabhängigkeit**, **Basen** und **Dimension** in späteren Vorlesungen.
- Essentiell für das Lösen von Systemen, das Verständnis von Transformationen und Anwendungen wie **Differentialgleichungen** oder **Machine Learning**.

---
### **Wo man mehr findet:**
- **Vollständige Kursmaterialien**: [MIT OCW 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- **Lehrbuch**: Strangs *"Introduction to Linear Algebra"* (Kapitel 2 behandelt dieses Thema).
- **Folgevorlesungen**: Die nächsten Vorlesungen behandeln **das Lösen von \\( A\mathbf{x} = \mathbf{b} \\)** (nicht-homogene Systeme) und den **Spaltenraum**.

---
### **Zusammenfassung in einem Satz:**
Diese Vorlesung lehrt, wie man **alle Lösungen** für \\( A\mathbf{x} = \mathbf{0} \\) findet, indem man Pivot-/freie Variablen identifiziert und eine Basis für den Nullraum mithilfe spezieller Lösungen konstruiert.