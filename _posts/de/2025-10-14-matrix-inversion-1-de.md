---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Invertieren einer 3x3-Matrix
translated: true
type: note
---

Gut — lassen Sie uns das klar und intuitiv aufschlüsseln, ohne Tabellenformatierung, damit es Zeile für Zeile leicht zu lesen ist.

---

### 1. Was das Ziel ist
Wir wollen die Inverse einer 3×3-Matrix finden, normalerweise geschrieben als A⁻¹.
Die Inverse ist die Matrix, die A "rückgängig macht", was bedeutet
A × A⁻¹ = I,
wobei I die Einheitsmatrix ist.

---

### 2. Die Kernformel
Die allgemeine Formel für jede invertierbare quadratische Matrix lautet

A⁻¹ = (1 / det(A)) × adj(A).

Wir benötigen also zwei Zutaten:
- die Determinante det(A), und
- die Adjunkte adj(A), welche die Transponierte der Kofaktormatrix ist.

---

### 3. Determinante einer 3×3-Matrix
Wenn
A =
[a  b  c]
[d  e  f]
[g  h  i],

dann ist

det(A) = a(ei − fh) − b(di − fg) + c(dh − eg).

Dieser Wert sagt Ihnen, ob die Matrix invertierbar ist:
- wenn det(A) = 0 → keine Inverse (Matrix ist singulär),
- wenn det(A) ≠ 0 → Inverse existiert.

---

### 4. Kofaktoren
Um adj(A) zu bilden, finden wir zuerst den Kofaktor jedes Elements.
Der Kofaktor des Elements aᵢⱼ ist
Cᵢⱼ = (−1)^(i+j) × Mᵢⱼ,
wobei Mᵢⱼ die Determinante der 2×2-Untermatrix ist, die Sie nach dem Löschen der Zeile i und Spalte j erhalten.

Wenn man dies für alle neun Positionen durchführt, erhält man die "Kofaktormatrix".
Für den allgemeinen Fall oben:

C₁₁ = ei − fh
C₁₂ = −(di − fg)
C₁₃ = dh − eg

C₂₁ = −(bi − ch)
C₂₂ = ai − cg
C₂₃ = −(ah − bg)

C₃₁ = bf − ce
C₃₂ = −(af − cd)
C₃₃ = ae − bd

---

### 5. Transponieren der Kofaktormatrix
Nehmen Sie nun diese Kofaktormatrix und transponieren Sie sie — das bedeutet, Zeilen und Spalten vertauschen.
Diese neue Matrix wird **Adjunkte** (oder adjungierte Matrix) von A genannt, geschrieben als adj(A).
Wenn Sie es sich visuell vorstellen, ist diese "Transponierung" wie das Drehen der Matrix: Was in der ersten Zeile war, wird zur ersten Spalte und so weiter.

---

### 6. Multiplizieren mit 1/det(A)
Skalieren Sie schließlich die Adjunkte-Matrix, indem Sie jeden Term durch det(A) teilen.
Das ergibt A⁻¹.

Symbolisch:
A⁻¹ = (1/det(A)) × adj(A).

---

### 7. Warum es funktioniert
Diese Formel kommt von einer grundlegenden Eigenschaft von Determinanten und Kofaktoren:

A × adj(A) = det(A) × I.

Wenn Sie beide Seiten durch det(A) teilen, erhalten Sie genau
A × [(1/det(A)) × adj(A)] = I.

Also muss der rechte Faktor die Inverse sein.

Der Grund, warum diese Identität gilt, ist, dass wenn Sie A mit seiner Kofaktormatrix multiplizieren, jeder Diagonaleintrag die Determinante selbst wird (da es die Entwicklung entlang dieser Zeile ist), und jeder Nicht-Diagonaleintrag wird aufgrund der alternierenden Kofaktorvorzeichen null — das ist die algebraische Aufhebung bei der Arbeit.

---

### 8. Beispiel
Sei
A =
[1  2  3]
[0  1  4]
[5  6  0].

Berechne det(A):
= 1(1×0 − 4×6) − 2(0×0 − 4×5) + 3(0×6 − 1×5)
= (−24) − (−40) + (−15)
= −24 + 40 − 15 = 1.

Also ist det(A) = 1.

Dann finden Sie alle Kofaktoren (etwas mühsam, aber unkompliziert), transponieren sie, um adj(A) zu erhalten, und da det(A) = 1, ist die Adjunkte bereits die Inverse.

---

### 9. Zusammenfassende Intuition
- Determinante → ein Maß dafür, wie die Matrix den "Raum skaliert".
- Kofaktor → erfasst den Beitrag jedes Elements zu dieser Skalierung.
- Transponieren → richtet diese Beiträge so aus, dass die Multiplikation die Einheitsmatrix rekonstruiert.
- Teilen durch die Determinante → normalisiert die Skalierung.

---

Möchten Sie, dass ich die detaillierten Kofaktorberechnungen für dieses Beispiel (die [1 2 3; 0 1 4; 5 6 0]) zeige, damit Sie jedes Unterdeterminante und Vorzeichen sehen können?