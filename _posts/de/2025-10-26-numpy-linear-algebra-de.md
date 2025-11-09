---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Taschenleitfaden Lineare Algebra mit NumPy
translated: true
type: note
---

Als Ihr technisch orientierter Tutor baut dieser Leitfaden auf den vorherigen indexexpliziten Formulierungen auf und integriert praktische NumPy-Demonstrationen via `import numpy as np` und `np.linalg`. Die gesamte Mathematik bleibt mit Indizes überprüfbar (z.B. \\( A = [a_{ij}]_{i=1}^2, j=1^2 \\)); der Code verwendet der Klarheit halber explizite Arrays. Die Ausgaben stammen aus verifizierten Ausführungen (z.B. für \\( A = \begin{pmatrix} a_{11}=1 & a_{12}=2 \\ a_{21}=3 & a_{22}=4 \end{pmatrix} \\), \\( B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \\)). Nutzen Sie diese für schnelle Berechnungen in der Prüfungsvorbereitung – konzentrieren Sie sich darauf, die Ausgaben anhand der Formeln zu interpretieren.

## 1. Matrixoperationen
Mathematik wie zuvor: \\( (AB)_{ij} = \sum_{k=1}^2 a_{ik} b_{kj} \\), usw.

**NumPy-Demo**:
```python
import numpy as np
A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)
```
- Addition: `A + B` ergibt \\( \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix} \\) (elementweise \\( a_{ij} + b_{ij} \\)).
- Skalarmultiplikation: `2 * A` ergibt \\( \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} \\) (\\( c a_{ij} \\)).
- Multiplikation: `A @ B` (oder `np.dot(A, B)`) ergibt \\( \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix} \\) (überprüfen: Zeile1-Spalte1 Summe \\( 1\cdot5 + 2\cdot7 = 19 \\)). Beachten Sie die Nichtkommutativität: `np.allclose(A @ B, B @ A)` ist `False`.
- Transponierte: `A.T` ergibt \\( \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \\) (\\( (A^T)_{ij} = a_{ji} \\)).
- Inverse: `np.linalg.inv(A)` ergibt \\( \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} \\) (überprüfen: `A @ inv_A` ≈ \\( I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \\), mit kleinen Float-Fehlern ~1e-16).

## 2. Determinanten
Mathematik: \\( \det A = \sum_{j=1}^2 a_{1j} C_{1j} \\), \\( C_{1j} = (-1)^{1+j} \det(M_{1j}) \\) (z.B. \\( M_{11} = [4] \\), also \\( C_{11} = 4 \\); vollständig \\( \det A = 1\cdot4 - 2\cdot3 = -2 \\)).

**NumPy-Demo** (Fortsetzung oben):
- `np.linalg.det(A)`: -2.0 (stimmt mit Formel überein; Float-Genauigkeit -2.0000000000000004).
- Produkt: `np.linalg.det(A @ B)` = 4.0; `det_A * np.linalg.det(B)` ≈ 4.0 (verifiziert \\( \det(AB) = \det A \cdot \det B \\)).
- Transponierte: `np.linalg.det(A.T)` = -2.0 (verifiziert \\( \det(A^T) = \det A \\)).

Für den Zusammenhang Adjunkte/Inverse: Die Inverse verwendet det im Nenner, wie in der Formel \\( A^{-1} = \frac{1}{\det A} \adj A \\).

## 3. Lineare Systeme & Gaußsches Eliminationsverfahren
Mathematik: Erweiterte Matrix \\( [A | b] \\) mit \\( b = [b_i]_{i=1}^2 = [5, 11]^T \\); lösen via Rückwärtseinsetzen nach Stufenform.

**NumPy-Demo**:
- `np.linalg.solve(A, b)` ergibt [1. 2.] (exakt: \\( x_1 = \frac{\det A_1}{\det A} \\), wobei \\( A_1 \\) Spalte1 mit b vertauscht, det= -2 gleich; verifiziert Cramer'sche Regel).
- Prüfung: `A @ x` = [5. 11.] (Residuum 0).
- Rang: `np.linalg.matrix_rank(A)` = 2 (voll; für singuläre Matrizen, Rang < 2 bedeutet unendlich/keine Lösungen).

NumPys `solve` führt intern eine LU-artige Faktorisierung durch (kein expliziter Gauß-Code nötig; für benutzerdefinierte Verfahren, verwenden Sie `scipy.linalg.lu`, aber bleiben Sie hier bei np.linalg).

## 4. Vektorräume
Mathematik: Rang A = # Pivots = dim Col(A); Nullität = 2 - Rang A.

**NumPy-Demo**:
- Rang wie oben: 2.
- Nullitätsschätzung via SVD: `U, S, Vt = np.linalg.svd(A)`; zähle singuläre Werte > 1e-10: 2, also Nullität = 2 - 2 = 0 (Nul(A) = {0}). Für Basis, Nullraumvektoren aus Vt-Zeilen mit kleinem S.

## 5. Lineare Transformationen
Mathematik: T(x)_i = \\( \sum_j a_{ij} x_j \\); Matrixdarstellung ist A.

**NumPy-Verbindung**: Gleich wie Matrixoperationen; z.B. wendet `T_x = A @ x` die Transformation an (vektorisiert).

## 6. Eigenwerte
Mathematik: Löse det(A - λ I) = 0, (A - λ I)_{ij} = a_{ij} - λ δ_{ij}; dann (A - λ I) v = 0 für v_j.

**NumPy-Demo**:
- `eigvals, eigvecs = np.linalg.eig(A)`: eigvals ≈ [-0.372, 5.372] (Wurzeln von λ² - tr(A)λ + det A = λ² - 5λ -2 =0).
- Eigenvektoren Spalten: z.B. Spalte0 ≈ [-0.825, 0.566]^T für λ≈-0.372.
- Prüfung: `A @ eigvecs[:,0]` ≈ λ eigvecs[:,0] (skalierte Verifikation: `A @ eigvecs[:,0] / eigvals[0]` stimmt mit eigvecs[:,0] überein).

Für diagonalisierbar: Vollrang Eigenvektoren (det ≠0).

## 7. Skalarprodukte & Orthogonalisierung
Mathematik: <u,v> = \\( \sum_i u_i v_i \\); proj = (<v,w>/<w,w>) w (skalare Multiplikation auf w_i).

**NumPy-Demo** (u=[1,2], v=[3,4]):
- `np.dot(u, v)` = 11 (oder `u @ v`).
- `np.linalg.norm(u)` ≈ 2.236 (√<u,u>).

Gram-Schmidt: Verwenden Sie `np.linalg.qr(V)` für Matrix V (Spalten als Basisvektoren); Q = orthonormal.
- Beispiel V = \\( \begin{pmatrix} 3 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \\) (Spalten v^{(1)}=[3,1,0]^T, etc.).
- `ortho = np.linalg.qr(V)[0]` ergibt ≈ \\( \begin{pmatrix} -0.949 & -0.316 & 0 \\ -0.316 & 0.949 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\) (Vorzeichenwechsel in Ordnung).
- Prüfung: `np.allclose(ortho.T @ ortho, np.eye(3))` = True (δ_{ij}).

Quadratische Form: `u @ A @ u` = 27.0 (x^T A x mit x_i = u_i; für positiv definit, alle Eigenwerte >0 – hier gemischte Vorzeichen).

**Schneller Verifikationstipp**: Immer `np.allclose` für Floats verwenden; für kleine n von Hand zeilenreduzieren, dann mit `solve` oder `eig` vergleichen. Übung: Setzen Sie Ihre eigenen 3×3-Matrizen ein.

[NumPy linalg Dokumentation](https://numpy.org/doc/stable/reference/routines.linalg.html)  
[Lineare Algebra in NumPy - SciPy Lecture Notes](https://scipy-lectures.org/intro/numpy/auto_examples/plot_linear_algebra.html)