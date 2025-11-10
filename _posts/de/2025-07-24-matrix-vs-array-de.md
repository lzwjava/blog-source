---
audio: false
generated: true
lang: de
layout: post
title: Matrizen vs. mehrdimensionale Arrays
translated: true
type: note
---

Hier ist ein einfaches mentales Modell, das Programmierern normalerweise hilft, die beiden auseinanderzuhalten.

---

### 1  Gemeinsame Kernidee

* **Rasterartige Speicherung** – Sowohl eine mathematische Matrix als auch ein mehrdimensionales Array organisieren Elemente durch mehrere ganzzahlige Indizes (Zeile/Spalte oder Zeile/Spalte/…/k).
* **Indexbasierter Zugriff** – Man greift auf ein Element mit einem Koordinatentripel wie `A[i][j]` zu (Matrix → zwei Indizes; allgemeines Array → beliebige Anzahl von Indizes).
* **Blockoperationen** – Das Denken in Blöcken anstelle von Skalaren fördert vektorisierten oder schleifenbasierten Code, cache-freundliche Speicherlayouts, GPU-Nutzung etc.

---

### 2  Wo sie sich unterscheiden

**a. Zweck & Semantik**

*Matrix*

* Rein **mathematisch**: Jedes Element ist eine Zahl aus einem Körper (ℝ, ℂ, …).
* Beinhaltet eine eingebaute Algebra: Addition, Skalarmultiplikation, Determinante, Inverse, Eigen-Stuff etc.
* Die Form ist immer 2-D; ein "Tensor dritter Stufe" wird nicht Matrix genannt.

*Mehrdimensionales Array*

* **Programmiercontainer**: Kann jeden Datentyp speichern, numerisch oder nicht.
* Keine inhärente Algebra; Operationen sind das, was man codiert (oder die Bibliothek bereitstellt).
* Der Rang ist beliebig: 1-D (Vektor), 2-D, 5-D, … sogar unregelmäßige Strukturen.

**b. Implementierungsdetails**

*Matrix-Bibliotheken* (NumPy `ndarray`, MATLAB, Eigen, BLAS, etc.)

* Achten normalerweise auf **Row-Major vs. Column-Major** Reihenfolge, da dies die Leistung algebraischer Kernel beeinflusst.
* Können Metadaten wie führende Dimension, Stride, Dreiecks-/gepackte Formen speichern.
* Bieten überladene Operatoren, so dass `C = A @ B` eine hochperformante Matrixmultiplikation auslöst.

*Allgemeine Arrays* (C-Arrays, Java-Arrays, Rust Slices, Python Listen von Listen)

* Das Speicherlayout ist sprachspezifisch: zusammenhängend, Array-von-Zeigern oder sogar fragmentiert (in Python-Listen).
* Fehlende automatische Algebra; um zwei 2-D-Arrays zu multiplizieren, schreibt man verschachtelte Schleifen oder ruft eine Mathebibliothek auf.
* Können in dynamisch typisierten Sprachen spärlich besetzt, gezackt oder gemischt typisiert sein.

**c. Typische Operationen**

*Matrix* – Punktprodukte, LU/QR-Zerlegung, Lösen linearer Systeme, SVD, Gradienten im ML, Grafiktransformationen.

*Mehrdimensionales Array* – Alles Mögliche: RGBA-Bildpixel, eine 3D-Voxel-Welt, eine Nachschlagetabelle mit Strings, Spielbrettzustände.

---

### 3  Analogie im Code

```python
# Matrix-Sichtweise (NumPy)
import numpy as np
A = np.array([[1, 2],
              [3, 4]])          # 2×2 Matrix
B = np.array([[5, 6],
              [7, 8]])
C = A @ B                       # Matrixmultiplikation, algebra-bewusst
detA = np.linalg.det(A)         # Determinante

# Reine mehrdimensionale Array-Sichtweise (Vanilla Python)
table = [[1, 2], [3, 4]]        # Liste von Listen
value = table[1][0]             # 3
# Multiplikation? Explizite Schleifen oder Comprehension nötig
product = [[sum(table[i][k]*B[k][j] for k in range(2))
           for j in range(2)] for i in range(2)]
```

---

### 4  TL;DR

* **Gleiche Form, unterschiedliche Bedeutung:** Eine Matrix ist ein 2-D numerisches Array *plus* ein Bündel von linearen Algebra-Gesetzen; ein mehrdimensionales Array ist nur ein indexierter Container – nicht mehr und nicht weniger.
* In der Praxis speichert man Matrizen oft *in* mehrdimensionalen Arrays und verlässt sich dann auf Bibliotheken, um ihnen Matrix-Semantik und Geschwindigkeit zu verleihen.