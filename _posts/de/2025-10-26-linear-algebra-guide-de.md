---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Präziser Lineare-Algebra-Taschenführer
translated: true
type: note
---

Als Ihr technisch orientierter Tutor betont dieser Leitfaden überprüfbare, indexexplizite Berechnungen für Matrizen \\( A = [a_{ij}]_{i=1}^m, j=1^n \in \mathbb{R}^{m \times n} \\) (Zeilen indiziert durch \\( i \\), Spalten durch \\( j \\), 1-basiert). Alle Schritte werden zur Verdeutlichung mit Indizes gezeigt; Beispiele kommentieren Einträge inline. Überprüfung mittels Zeilenreduktion und Eigenwertberechnungen an 2×2/3×3 Fällen.

## 1. Matrixoperationen
- **Addition**: \\( (A + B)_{ij} = a_{ij} + b_{ij} \\) für alle \\( i,j \\).
- **Skalare Multiplikation**: \\( (cA)_{ij} = c a_{ij} \\) für Skalar \\( c \\), alle \\( i,j \\).
- **Matrixmultiplikation** (falls \\( m \times p \\) und \\( p \times n \\)): \\( (AB)_{ij} = \sum_{k=1}^p a_{ik} b_{kj} \\) für alle \\( i=1^m \\), \\( j=1^n \\).
- **Transponierte**: \\( (A^T)_{ij} = a_{ji} \\); somit \\( (AB)^T_{ij} = \sum_k b_{ki} a_{kj} = (B^T A^T)_{ij} \\).
- **Inverse** (für quadratische \\( n \times n \\), \\( \det A \neq 0 \\)): \\( A^{-1} \\) erfüllt \\( \sum_k a_{ik} (A^{-1})_{kj} = \delta_{ij} \\) (Kronecker-Delta: 1 falls \\( i=j \\), sonst 0). Eigenschaften: \\( (AB)^{-1}_{ij} = \sum_k (B^{-1})_{ik} (A^{-1})_{kj} = (B^{-1} A^{-1})_{ij} \\); \\( (A^T)^{-1}_{ij} = \sum_k (A^{-1})_{ki} (A^T)_{kj} ? Moment, nein: (A^{-1})^T_{ij} = (A^{-1})_{ji} \\), also \\( [(A^T)^{-1}]_{ij} = (A^{-1})_{ji} \\).

**Beispiel (2×2 Inverse Annotation)**: Sei \\( A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \\). Dann ist \\( A^{-1} = \frac{1}{\det A} \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix} \\), wobei \\( \det A = a_{11} a_{22} - a_{12} a_{21} \\).

## 2. Determinanten
- **Definition**: Für quadratische \\( A \\) ist \\( \det A \\) via Kofaktorentwicklung entlang Zeile \\( i \\): \\( \det A = \sum_{j=1}^n a_{ij} C_{ij} \\), wobei Minor \\( M_{ij} \\) die Untermatrix ohne Zeile \\( i \\) und Spalte \\( j \\) ist (also \\( M_{ij} = [m_{pq}] \\) mit \\( p=1^{n-1} \setminus i \\), \\( q=1^{n-1} \setminus j \\), neu beschriftet 1-basiert), Kofaktor \\( C_{ij} = (-1)^{i+j} \det(M_{ij}) \\).
- **Eigenschaften**:
  - \\( \det(AB) = \det A \cdot \det B \\); \\( \det(A^T) = \det A \\) (da Entwicklung symmetrisch).
  - \\( \det(cA) = c^n \det A \\).
  - Zeilentausch: \\( \det \\) multipliziert mit -1; Vielfaches von Zeile \\( k \\) zu Zeile \\( i \neq k \\) addieren: unverändert; Zeile \\( i \\) mit \\( c \\) skalieren: multipliziert mit \\( c \\).
  - \\( \det I = 1 \\) (Diagonale 1en); singulär falls \\( \det A = 0 \\) (Rang < n).
- **Adjunkte**: \\( \adj(A)_{ij} = C_{ji} = [C^T]_{ij} \\), wobei \\( C = [C_{pq}] \\). Inverse: \\( A^{-1} = \frac{1}{\det A} \adj A \\), also \\( (A^{-1})_{ij} = \frac{1}{\det A} \sum_k \delta_{ik} C_{kj} ? Nein: Matrixform verifiziert \\( A \adj A = (\det A) I \\).

**Beispiel (2×2 Kofaktoren)**: Für obiges \\( A \\) ist \\( M_{11} = [a_{22}] \\), \\( C_{11} = (-1)^{1+1} a_{22} = a_{22} \\); \\( M_{12} = [a_{21}] \\), \\( C_{12} = (-1)^{1+2} a_{21} = -a_{21} \\); ähnlich \\( C_{21} = -a_{12} \\), \\( C_{22} = a_{11} \\). Somit ist \\( \adj A = \begin{pmatrix} C_{11} & C_{21} \\ C_{12} & C_{22} \end{pmatrix} = \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix} \\).

- **Cramersche Regel** (für \\( \sum_j a_{ij} x_j = b_i \\), \\( i=1^n \\), \\( \det A \neq 0 \\)): \\( x_r = \frac{\det A_r}{\det A} \\), wobei \\( A_r \\) Spalte \\( r \\) von \\( A \\) mit \\( [b_i]_{i=1}^n \\) ersetzt, also \\( (A_r)_{ij} = a_{ij} \\) falls \\( j \neq r \\), sonst \\( b_i \\).

## 3. Lineare Systeme & Gaußsches Eliminationsverfahren
- **Erweiterte Matrix**: \\( [A | b] = [a_{ij} | b_i] \\) für \\( i=1^m \\), \\( j=1^n \\).
- **Zeilenreduktion zu ZSF**: Wende elementare Operationen an (Vertausche Zeilen \\( p \leftrightarrow q \\); Skaliere Zeile \\( p \\) mit \\( c \neq 0 \\): Zeile \\( p \leftarrow c \\) Zeile \\( p \\); Addiere \\( c \\) Zeile \\( q \\) zu Zeile \\( p \\)), um Zeilenstufenform zu erhalten: führender Eintrag (Pivot) in Zeile \\( i \\) bei Spalte \\( p_i \geq p_{i-1} \\), Nullen unter Pivots.
- **Zu RZSF**: Fahre fort mit Nullen über Pivots, skaliere Pivots zu 1.
- **Rang**: Anzahl der Nichtnullzeilen in ZSF (oder Pivots).
- **Lösungen**:
  - Eindeutig falls Rang \\( A = n \\), Rang \\( [A|b] = n \\) (Nullität 0).
  - Unendlich viele falls Rang \\( A = \\) Rang \\( [A|b] = r < n \\) (n-r freie Variablen).
  - Inkonsistent falls Rang \\( A < \\) Rang \\( [A|b] \\).
- **Allgemeine Lösung**: \\( x = x_p + x_h \\), partikuläre Lösung \\( x_p \\) aus RZSF, homogene Lösung \\( x_h \\) spannt Nullraum (Basis der freien Variablen).
- **Schrittbeispiel (2×2 System Annotation)**: Löse \\( a_{11} x_1 + a_{12} x_2 = b_1 \\), \\( a_{21} x_1 + a_{22} x_2 = b_2 \\). Zeile2 ← Zeile2 - (a_{21}/a_{11}) Zeile1: neue Zeile2 = [0, a_{22} - (a_{21} a_{12}/a_{11}), b_2 - (a_{21} b_1 / a_{11}) ]. Rückwärtseinsetzen: \\( x_2 = \\) ... / det Term, etc.

## 4. Vektorräume
- **Unterräume**: Sp(A) = Span{ Spalte j von A, j=1^n } = { \\( \sum_j x_j \\) Spalte j | x }; dim = Rang A.
- **Zeilenraum**: ZR(A) = Sp(A^T); dim = Rang A.
- **Nullraum**: Kern(A) = { x | \\( \sum_j a_{ij} x_j = 0 \\) ∀ i }; Basis aus RZSF freien Spalten.
- **Rang-Nullitäts-Satz**: Rang A + dim Kern(A) = n.

## 5. Lineare Abbildungen
- **Matrixdarstellung**: T(x)_i = \\( \sum_j a_{ij} x_j \\).
- **Kern**: Ker T = Kern(A); Bild T = Sp(A).

## 6. Eigenwerte
- **Charakteristisches Polynom**: det(A - λ I) = 0, wobei (A - λ I)_{ij} = a_{ij} - λ δ_{ij}.
- **Eigenvektoren**: Für λ, löse \\( \sum_j (a_{ij} - λ δ_{ij}) v_j = 0 \\), v = [v_j] ≠ 0.
- **Diagonalisierbar**: Falls alg Vfh(λ_k) = geom Vfh(λ_k) ∀ k (volle Eigenraumdimension), dann A = P D P^{-1}, D_{ij} = λ_i δ_{ij}, P Spalten = Eigenvektoren.
- **Symmetrisch**: A = A^T ⇒ orthogonale Diagonalisierung: A = Q D Q^T, Q^T Q = I.

## 7. Skalarprodukte & Orthogonalisierung
- **Euklidisch**: <u,v> = \\( \sum_i u_i v_i = u^T v \\).
- **Gram-Schmidt Schritt**: Für Basis {v^{(k)}}, u^{(1)} = v^{(1)}; u^{(k)} = v^{(k)} - \sum_{m=1}^{k-1} \proj_{u^{(m)}} v^{(k)}, wobei \proj_w v = \frac{<v,w>}{<w,w>} w (Komponente \\( \sum_i ... \\)).

**Schneller Verifikationstipp**: Reduziere immer [A - λI | 0] für Eigenräume; prüfe det via Entwicklung falls n≤3.

[Linear Algebra Cheat Sheet - Indexed Formulas](https://laurentlessard.com/teaching/ece532/cheat_sheet.pdf)  
[Self-Exam 02198 Review](https://doc.quark.cn/preview/jiaoyukaoshi-shijuan-gaokao/1130FC966EE595249D3822AFF5DF0167)