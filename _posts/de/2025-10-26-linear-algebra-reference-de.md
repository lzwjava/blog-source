---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Schnellreferenz für Lineare Algebra-Prüfung
translated: true
type: note
---

Schnellreferenz für Schlüsselkonzepte und Formeln. Fokus auf Matrizen, Determinanten, lineare Systeme, Vektorräume, Transformationen, Eigenwerte und quadratische Formen – zentrale Themen aus früheren Prüfungen. Wiederhole Definitionen, Eigenschaften und Berechnungen.

## 1. Matrizen
- **Definition**: \\( A = [a_{ij}] \in \mathbb{R}^{m \times n} \\).
- **Operationen**:
  - Addition: \\( (A + B)_{ij} = a_{ij} + b_{ij} \\).
  - Skalarmultiplikation: \\( (cA)_{ij} = c a_{ij} \\).
  - Multiplikation: \\( (AB)_{ij} = \sum_k a_{ik} b_{kj} \\) (bei kompatiblen Größen).
- **Transponierte**: \\( (A^T)_{ij} = a_{ji} \\); \\( (AB)^T = B^T A^T \\), \\( (A^T)^T = A \\).
- **Inverse** (quadratisch): \\( AA^{-1} = I \\); \\( (AB)^{-1} = B^{-1} A^{-1} \\); \\( (A^T)^{-1} = (A^{-1})^T \\).
- **Typen**:
  - Diagonal: Nur auf der Diagonale von Null verschieden.
  - Ober-/Untere Dreiecksmatrix: Nullen unter-/oberhalb der Diagonale.
  - Symmetrisch: \\( A = A^T \\).
  - Orthogonal: \\( A^T A = I \\) (Spalten orthonormal).

## 2. Determinanten (det A)
- **Eigenschaften**:
  - \\( \det(AB) = \det A \cdot \det B \\); \\( \det(A^T) = \det A \\); \\( \det(cA) = c^n \det A \\).
  - Zeilen-/Spaltentausch: Multipliziert mit -1.
  - Addition eines Vielfachen einer Zeile/Spalte: Keine Änderung.
  - Skalieren einer Zeile/Spalte mit c: Multipliziert mit c.
  - \\( \det I = 1 \\); \\( \det A = 0 \\) wenn singulär (linear abhängige Zeilen/Spalten).
- **Berechnung**:
  - 2x2: \\( \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc \\).
  - Kofaktor-Entwicklung (Zeile i): \\( \det A = \sum_j a_{ij} C_{ij} \\), wobei \\( C_{ij} = (-1)^{i+j} M_{ij} \\) (Minor-Det).
  - Dreiecksmatrix: Produkt der Diagonaleinträge.
- **Adjunkte/Inverse**: \\( A^{-1} = \frac{1}{\det A} \adj A \\), wobei \\( \adj A = C^T \\) (transponierte Kofaktormatrix).
- **Cramer's Regel** (für \\( Ax = b \\), det A ≠ 0): \\( x_i = \frac{\det A_i}{\det A} \\) (A_i ersetzt i-te Spalte durch b).

## 3. Lineare Systeme (Ax = b)
- **Gaußsches Eliminationsverfahren**: Zeilenreduktion von [A | b] auf ZSF/ERZF.
  - ZSF: Pivots (führende Einsen) Treppe rechts-unten; Nullen unter Pivots.
  - Rückwärtseinsetzen für eindeutige Lösung.
- **Lösungen**:
  - Eindeutig: Rang A = n (voller Spaltenrang), Nullraum {0}.
  - Unendlich viele: Rang A = Rang [A|b] < n (freie Variablen).
  - Keine: Rang A < Rang [A|b].
- **Vollständige Lösung**: Partikuläre Lösung + Nullraum-Basis (homogene Lösungen).
- **LU-Zerlegung** (ohne Pivotisierung): A = LU (L untere Einheits-Dreiecksmatrix, U obere Dreiecksmatrix); löse Ly = b, Ux = y.
- **Methode der kleinsten Quadrate** (überbestimmt): \\( \hat{x} = (A^T A)^{-1} A^T b \\) (bei vollem Rang).

## 4. Vektorräume & Unterräume
- **Vektorraum**: Abgeschlossen unter Addition/Skalarmultiplikation; Axiome (z.B. Nullvektor, Inverse).
- **Unterräume**: Spann von Vektoren; abgeschlossen, enthält 0.
  - Spaltenraum: Col(A) = Spann(Spalten von A); dim = Rang A.
  - Zeilenraum: Row(A) = Col(A^T); dim = Rang A.
  - Nullraum: Nul(A) = {x | Ax = 0}; dim = n - Rang A.
  - Links-Nullraum: Nul(A^T).
- **Lineare Unabhängigkeit**: c1 v1 + ... + ck vk = 0 ⇒ alle ci = 0.
- **Basis**: Lin. unabh. Erzeugendensystem.
- **Dimension**: # Vektoren in Basis; dim Col(A) + dim Nul(A) = n (Rang-Nullitäts-Satz).
- **Rang**: # Pivotspalten = dim Col(A) = dim Row(A).

## 5. Lineare Transformationen
- **Definition**: T: V → W linear wenn T(u + v) = T u + T v, T(cu) = c T u.
- **Matrixdarst.**: [T] bezüglich Basen = A wobei T(x) = A x (Standardbasis).
- **Kern**: Ker T = Nul(A); Bild: Im T = Col(A).
- **Isomorphismus**: 1-1 und onto (invertierbare Matrix).
- **Rang-Nullitäts-Satz**: dim Ker T + dim Im T = dim V.

## 6. Eigenwerte & Eigenvektoren
- **Definition**: A v = λ v (v ≠ 0 Eigenvektor, λ Eigenwert).
- **Charakteristische Gl.**: det(A - λ I) = 0; Wurzeln λi (algebraische Vielfachheit).
- **Eigenvektoren**: Löse (A - λ I) v = 0; geometrische Vielf. = Dim. Eigenraum.
- **Diagonalisierbar**: n lin. unabh. Eigenvektoren ⇒ A = X Λ X^{-1} (Λ diag(λi), X = [v1 ... vn]).
  - Symmetrisches A: Immer diagonalisierbar; orthogonale Eigenvektoren (A = Q Λ Q^T, Q orthogonal).
- **Spur**: tr A = ∑ λi.
- **Det**: det A = ∏ λi.
- **Ähnliche Matrizen**: A ~ B wenn A = P B P^{-1}; gleiche Eigenwerte, Spur, Det.

## 7. Skalarprodukte & Quadratische Formen
- **Skalarprodukt**: <u, v> = u^T v (Euklidisch); ||v|| = √<v,v>.
- **Orthogonal**: <u,v> = 0; Orthonormalbasis: <ei, ej> = δij.
- **Gram-Schmidt**: Orthogonalisiere Basis {v1,...,vn} → {u1,...,un}.
  - u1 = v1; uk = vk - proj_{span(u1..u_{k-1})} vk; proj_w v = (<v,w>/<w,w>) w.
- **Quadratische Form**: q(x) = x^T A x (A symmetrisch).
  - Positiv definit: q(x) > 0 für x ≠ 0 (alle λi > 0).
  - Diagonalisieren: q(x) = ∑ λi yi^2 (y = Q^T x).

## Schnelle Tipps
- Rang berechnen: Zeilenreduktion für # Pivots.
- Diagonalisierbarkeit prüfen: Geometrische Vielf. = algebraische Vielf. für jedes λ.
- Für Prüfungen: Übe Zeilenreduktion, Det-Entwicklung, Eigenwertprobleme an 2x2/3x3 Matrizen.
- Häufige Fehler: Vielfachheit vergessen; Vorzeichen bei Kofaktoren; nicht-kommutative Multiplikation.

Viel Glück für morgen – konzentriere dich auf Verständnis statt Auswendiglernen!

[Linear Algebra Cheat Sheet - Laurent Lessard](https://laurentlessard.com/teaching/ece532/cheat_sheet.pdf)  
[Linear Algebra Review - Yiping Lu](https://2prime.github.io/files/linear/finalsheet.pdf)  
[2023 Self-Exam Linear Algebra Questions](https://doc.quark.cn/preview/jiaoyukaoshi-shijuan-gaokao/1130FC966EE595249D3822AFF5DF0167)