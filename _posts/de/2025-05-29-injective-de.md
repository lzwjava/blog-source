---
audio: false
generated: true
lang: de
layout: post
title: Injektive Funktionen
translated: true
type: note
---

In der Mathematik bezeichnet der Begriff "injektiv" eine Funktion oder Abbildung zwischen zwei Mengen, bei der verschiedene Elemente der ersten Menge auf verschiedene Elemente der zweiten Menge abgebildet werden. Mit anderen Worten, keine zwei verschiedenen Elemente des Definitionsbereichs (der ersten Menge) werden auf dasselbe Element des Zielbereichs (der zweiten Menge) abgebildet.

Diese Eigenschaft wird auch als "eineindeutig" bezeichnet. Wenn eine Funktion \\( f \\) injektiv ist, dann gilt für zwei beliebige Elemente \\( x \\) und \\( y \\) im Definitionsbereich: Wenn \\( f(x) = f(y) \\) ist, dann muss \\( x = y \\) gelten. Dies stellt sicher, dass jedes Element im Zielbereich durch höchstens ein Element im Definitionsbereich abgebildet wird.

---

Um zu verstehen, warum eine lineare Transformation \\( T \\) injektiv ist, wenn ihr Kern nur den Nullvektor enthält, lassen Sie uns die Definitionen und Implikationen aufschlüsseln:

1.  **Kern einer Transformation**: Der Kern einer linearen Transformation \\( T: V \rightarrow W \\) (bezeichnet als \\( \ker(T) \\)) ist die Menge aller Vektoren in \\( V \\), die auf den Nullvektor in \\( W \\) abgebildet werden. Mathematisch ausgedrückt: \\( \ker(T) = \{ v \in V \mid T(v) = 0 \} \\).

2.  **Injektive Transformation**: Eine lineare Transformation \\( T \\) ist injektiv (oder eineindeutig), wenn verschiedene Vektoren in \\( V \\) auf verschiedene Vektoren in \\( W \\) abgebildet werden. Mit anderen Worten: Wenn \\( T(u) = T(v) \\) gilt, dann folgt \\( u = v \\).

Nun wollen wir diese beiden Konzepte verbinden:

*   Angenommen, \\( \ker(T) = \{0\} \\). Das bedeutet, dass der einzige Vektor in \\( V \\), der auf den Nullvektor in \\( W \\) abgebildet wird, der Nullvektor selbst ist.
*   Um zu zeigen, dass \\( T \\) injektiv ist, nehmen wir an, dass \\( T(u) = T(v) \\) gilt. Aufgrund der Linearität von \\( T \\) haben wir \\( T(u) - T(v) = T(u - v) = 0 \\).
*   Da \\( \ker(T) = \{0\} \\) ist, impliziert \\( T(u - v) = 0 \\), dass \\( u - v = 0 \\) ist, was \\( u = v \\) bedeutet.

Wenn also \\( \ker(T) = \{0\} \\) gilt, ist die Transformation \\( T \\) injektiv. Dies liegt daran, dass die einzige Lösung für \\( T(v) = 0 \\) \\( v = 0 \\) ist, was sicherstellt, dass keine zwei verschiedenen Vektoren in \\( V \\) auf denselben Vektor in \\( W \\) abgebildet werden.

---

Die Gleichung \\( T(u) - T(v) = T(u - v) \\) ist eine Folge der Linearitätseigenschaft einer linearen Transformation \\( T \\). Lassen Sie uns aufschlüsseln, warum dies gilt:

1.  **Linearität von \\( T \\)**: Eine lineare Transformation \\( T \\) erfüllt zwei Schlüsseleigenschaften für beliebige Vektoren \\( u \\) und \\( v \\) im Vektorraum und einen beliebigen Skalar \\( c \\):
    *   **Additivität**: \\( T(u + v) = T(u) + T(v) \\)
    *   **Homogenität**: \\( T(cu) = cT(u) \\)

2.  **Herleitung von \\( T(u) - T(v) = T(u - v) \\)**:
    *   Unter Verwendung der Additivitätseigenschaft können wir \\( T(u - v) \\) als \\( T(u + (-v)) \\) ausdrücken, was \\( T(u) + T(-v) \\) entspricht.
    *   Aufgrund der Homogenitätseigenschaft gilt \\( T(-v) = -T(v) \\).
    *   Daher ist \\( T(u - v) = T(u) + (-T(v)) = T(u) - T(v) \\).

Somit ist \\( T(u) - T(v) = T(u - v) \\) ein direktes Ergebnis der Linearität von \\( T \\). Diese Eigenschaft ist grundlegend in der linearen Algebra und wird häufig in Beweisen und Herleitungen im Zusammenhang mit linearen Transformationen verwendet.