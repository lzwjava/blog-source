---
audio: false
generated: true
lang: de
layout: post
title: Lineare Algebra Tutorial
translated: true
type: note
---

## 1. Einführung
### Definition & Bedeutung
Lineare Algebra ist der Zweig der Mathematik, der sich mit Vektorräumen und linearen Abbildungen zwischen ihnen befasst. Sie ist grundlegend für Ingenieurwesen, Physik, Informatik und Wirtschaftswissenschaften.

### Skalare, Vektoren und Matrizen
- **Skalare**: Einzelne Zahlen (z.B. reelle oder komplexe Zahlen)
- **Vektoren**: Geordnete Listen von Zahlen, die Betrag und Richtung darstellen
- **Matrizen**: Rechteckige Anordnungen von Zahlen, die Transformationen oder Systeme repräsentieren

### Anwendungen
- Physik (Quantenmechanik, Relativitätstheorie)
- Ingenieurwesen (Regelungstechnik, Schaltkreise)
- Wirtschaftswissenschaften (Optimierung, Spieltheorie)
- Data Science & Machine Learning

## 2. Lineare Gleichungssysteme
### Darstellung
Ein System linearer Gleichungen kann in Matrixform geschrieben werden als:
\\[ Ax = b \\]
wobei \\( A \\) eine Matrix ist, \\( x \\) ein Vektor von Variablen und \\( b \\) ein konstanter Vektor.

### Lösungsmethoden
- **Gaußsches Eliminationsverfahren**: Überführt das System in Zeilenstufenform, um Unbekannte zu lösen.
- **Zeilenreduktion (Reduzierte Zeilenstufenform, RREF)**: Reduziert die Matrix weiter, um Lösungen zu identifizieren.
- **Lösungstypen**:
  - **Eindeutige Lösung**: Ein Schnittpunkt
  - **Unendlich viele Lösungen**: Mehrere Schnittpunkte
  - **Keine Lösung**: Parallele Geraden (inkonsistentes System)
- **Homogen vs. Nicht-Homogen**:
  - Homogen: \\( Ax = 0 \\) (hat immer mindestens eine Lösung)
  - Nicht-Homogen: \\( Ax = b \\)

## 3. Matrizen und Operationen
### Notation & Typen
- **Quadratische Matrix**: Gleiche Anzahl von Zeilen und Spalten
- **Einheitsmatrix (I)**: Diagonalelemente sind 1, andere sind 0
- **Nullmatrix (0)**: Alle Elemente sind null

### Operationen
- **Addition & Subtraktion**: Elementweise
- **Skalarmultiplikation**: Multipliziere jedes Element mit einem Skalar
- **Matrixmultiplikation**: \\( (AB)_{ij} = \sum_{k} A_{ik} B_{kj} \\)
- **Transponierte**: Vertauschen von Zeilen und Spalten
- **Inverse (A\\(^-1\\))**: Existiert nur, wenn die Determinante ungleich null ist

## 4. Determinanten
### Definition
Ein Skalarwert, der einer quadratischen Matrix zugeordnet ist und nützlich für das Lösen linearer Gleichungen und das Verständnis von Matrixeigenschaften ist.

### Berechnung
- **2×2-Matrix**: \\( \text{det} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc \\)
- **3×3-Matrix**: Verwende Kofaktorentwicklung oder Sarrus-Regel
- **Matrizen höherer Ordnung**: Verwende Zeilenentwicklung oder Laplace-Entwicklung

### Eigenschaften & Anwendungen
- **Cramer'sche Regel**: Verwendet Determinanten, um Systeme \\( Ax = b \\) zu lösen
- **Singuläre vs. Nicht-singuläre Matrizen**: Determinante \\( = 0 \\) bedeutet nicht invertierbar

## 5. Vektorräume
### Definition
Eine Menge von Vektoren, die addiert und mit Skalaren multipliziert werden können, wobei sie in der Menge bleiben.

### Schlüsselkonzepte
- **Unterräume**: Eine Teilmenge eines Vektorraums, die Abgeschlossenheitseigenschaften erfüllt
- **Basis**: Eine minimale Menge linear unabhängiger Vektoren, die einen Raum aufspannen
- **Dimension**: Die Anzahl der Basisvektoren
- **Lineare Unabhängigkeit**: Eine Menge von Vektoren, bei der kein Vektor eine Linearkombination der anderen ist
- **Span (Spann)**: Alle möglichen Linearkombinationen einer gegebenen Menge von Vektoren
- **Basiswechsel**: Übergang zwischen verschiedenen Vektorraumdarstellungen

## 6. Lineare Transformationen
### Definition
Eine Funktion \\( T: V \to W \\), die Vektoraddition und Skalarmultiplikation erhält.

### Darstellung
Jede lineare Transformation kann als Matrix dargestellt werden.

### Eigenschaften
- **Kern (Nullraum)**: Menge der Vektoren, die auf null abgebildet werden
- **Bild (Wertebereich)**: Menge der Ausgabevektoren
- **Injektivität (Eineindeutigkeit)**: \\( \text{Ker}(T) = \{0\} \\)
- **Surjektivität (Onto)**: Das Bild umfasst den gesamten Zielbereich

## 7. Eigenwerte und Eigenvektoren
### Definitionen
- **Eigenwerte (λ)**: Skalare, für die \\( Av = \lambda v \\) gilt
- **Eigenvektoren (v)**: Vektoren ungleich null, die \\( Av = \lambda v \\) erfüllen

### Berechnung
- Löse die charakteristische Gleichung \\( \det(A - \lambda I) = 0 \\)
- Finde entsprechende Eigenvektoren aus \\( (A - \lambda I)v = 0 \\)

### Anwendungen
- Stabilitätsanalyse
- Markov-Prozesse
- Hauptkomponentenanalyse (PCA) im Machine Learning

## 8. Skalarprodukträume
### Skalarprodukt & Normen
- **Skalarprodukt**: \\( a \cdot b = \sum a_i b_i \\)
- **Norm (Betrag)**: \\( \|v\| = \sqrt{v \cdot v} \\)

### Orthogonalität & Orthonormale Basen
- **Orthogonale Vektoren**: Skalarprodukt = 0
- **Orthonormale Basis**: Basis, bei der alle Vektoren orthogonal sind und Einheitslänge haben
- **Gram-Schmidt-Verfahren**: Wandelt eine Basis in eine orthonormale um

## 9. Anwendungen
### Praktische Probleme
- **Netzwerkflüsse**: Optimierung mit linearer Algebra
- **Datenanpassung**: Regressionstechniken mit der Methode der kleinsten Quadrate

### Rechenmethoden
- **Matrizen in der Programmierung**: Werden in Python, MATLAB und NumPy für wissenschaftliches Rechnen verwendet