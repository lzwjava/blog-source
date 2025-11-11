---
audio: false
generated: true
lang: de
layout: post
title: Subraum
translated: true
type: note
---

Um zu bestimmen, welche der gegebenen Mengen ein Unterraum von $\mathbb{R}^2$ ist, müssen wir prüfen, ob sie die drei Bedingungen für einen Unterraum erfüllen:

1.  **Der Nullvektor ist im Unterraum.**
2.  **Der Unterraum ist abgeschlossen unter Vektoraddition.** Wenn $\mathbf{u}$ und $\mathbf{v}$ im Unterraum sind, dann ist $\mathbf{u} + \mathbf{v}$ auch im Unterraum.
3.  **Der Unterraum ist abgeschlossen unter Skalarmultiplikation.** Wenn $\mathbf{u}$ im Unterraum ist und $c$ ein beliebiger Skalar ist, dann ist $c\mathbf{u}$ auch im Unterraum.

Lassen Sie uns jede Option untersuchen:

**a) Die Gerade y = x + 1**

1.  **Nullvektor:** Der Nullvektor in $\mathbb{R}^2$ ist $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Damit dieser Vektor auf der Geraden liegt, muss er die Gleichung $y = x + 1$ erfüllen. Setzt man $x=0$ und $y=0$ ein, erhält man $0 = 0 + 1$, also $0 = 1$. Dies ist falsch, also liegt der Nullvektor nicht auf der Geraden $y = x + 1$.

Da die erste Bedingung nicht erfüllt ist, ist die Gerade $y = x + 1$ kein Unterraum von $\mathbb{R}^2$.

**b) Die Gerade y = 2x**

1.  **Nullvektor:** Damit der Nullvektor $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$ auf der Geraden liegt, muss er die Gleichung $y = 2x$ erfüllen. Setzt man $x=0$ und $y=0$ ein, erhält man $0 = 2(0)$, also $0 = 0$. Dies ist wahr, also liegt der Nullvektor auf der Geraden $y = 2x$.

2.  **Abgeschlossenheit unter Vektoraddition:** Seien $\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}$ und $\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}$ zwei Vektoren auf der Geraden $y = 2x$. Das bedeutet $y_1 = 2x_1$ und $y_2 = 2x_2$.
    Ihre Summe ist $\mathbf{u} + \mathbf{v} = \begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}$. Wir müssen prüfen, ob dieser Vektor auf der Geraden $y = 2x$ liegt. Setzt man die Komponenten ein, erhält man $y_1 + y_2 = 2(x_1 + x_2)$. Da $y_1 = 2x_1$ und $y_2 = 2x_2$ ist, haben wir $2x_1 + 2x_2 = 2x_1 + 2x_2$, was wahr ist. Somit ist die Gerade unter Vektoraddition abgeschlossen.

3.  **Abgeschlossenheit unter Skalarmultiplikation:** Sei $\mathbf{u} = \begin{pmatrix} x \\ y \end{pmatrix}$ ein Vektor auf der Geraden $y = 2x$, also $y = 2x$. Sei $c$ ein beliebiger Skalar. Dann ist $c\mathbf{u} = \begin{pmatrix} cx \\ cy \end{pmatrix}$. Wir müssen prüfen, ob dieser Vektor auf der Geraden $y = 2x$ liegt. Setzt man die Komponenten ein, erhält man $cy = 2(cx)$. Da $y = 2x$ ist, haben wir $c(2x) = 2(cx)$, also $2cx = 2cx$. Dies ist wahr, also ist die Gerade unter Skalarmultiplikation abgeschlossen.

Da alle drei Bedingungen erfüllt sind, ist die Gerade $y = 2x$ ein Unterraum von $\mathbb{R}^2$.

**c) Der Einheitskreis**

Der Einheitskreis in $\mathbb{R}^2$ ist durch die Gleichung $x^2 + y^2 = 1$ definiert.

1.  **Nullvektor:** Der Nullvektor ist $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Setzt man dies in die Gleichung ein, erhält man $0^2 + 0^2 = 1$, also $0 = 1$. Dies ist falsch, also liegt der Nullvektor nicht auf dem Einheitskreis.

Da die erste Bedingung nicht erfüllt ist, ist der Einheitskreis kein Unterraum von $\mathbb{R}^2$.

Endgültige Antwort: Die endgültige Antwort ist $\boxed{The line y = 2x}$

---

Die Anforderung, dass "Der Nullvektor im Unterraum ist", ist eine der **drei grundlegenden Bedingungen**, die eine Teilmenge eines Vektorraums erfüllen muss, um als **Unterraum** betrachtet zu werden. Lassen Sie uns aufschlüsseln, *warum* diese Bedingung notwendig ist.

Das Konzept eines Unterraums besteht darin, kleinere Mengen innerhalb eines größeren Vektorraums zu identifizieren, die sich selbst wie Vektorräume verhalten. Um sich wie ein Vektorraum zu verhalten, müssen diese kleineren Mengen bestimmte wesentliche Eigenschaften erben. Eine der grundlegendsten Eigenschaften eines jeden Vektorraums ist die Existenz eines **Nullvektors** (oft bezeichnet als $\mathbf{0}$). Dieser Vektor hat die entscheidende Eigenschaft, dass er, wenn er zu einem anderen Vektor im Raum addiert wird, diesen Vektor unverändert lässt: $\mathbf{v} + \mathbf{0} = \mathbf{v}$ für alle Vektoren $\mathbf{v}$ im Raum.

Hier ist der Grund, warum der Nullvektor in einem Unterraum sein muss:

1.  **Erben der Vektorraumstruktur:** Ein Unterraum soll ein "Mini-Vektorraum" innerhalb eines größeren sein. Wenn eine Teilmenge den Nullvektor nicht enthält, fehlt ihr ein entscheidendes Element, das erforderlich ist, um die Vektorraumaxiome zu erfüllen. Ohne einen Nullvektor wird das Konzept der additiven Inversen (ein weiteres wichtiges Axiom) problematisch.

2.  **Abgeschlossenheit unter Skalarmultiplikation:** Betrachten Sie eine nicht-leere Teilmenge $W$ eines Vektorraums $V$, die unter Skalarmultiplikation abgeschlossen ist. Wenn $\mathbf{w}$ ein beliebiger Vektor in $W$ ist und $W$ ein Unterraum ist, dann muss für jeden Skalar $c$ der Vektor $c\mathbf{w}$ auch in $W$ sein. Wenn wir den Skalar $c = 0$ wählen, dann ist $0\mathbf{w} = \mathbf{0}$ (dies ist eine Eigenschaft von Vektorräumen). Daher muss ein Unterraum, der unter Skalarmultiplikation abgeschlossen ist und mindestens einen Vektor enthält, *notwendigerweise* den Nullvektor enthalten.

3.  **Sicherstellung additiver Inversen:** Obwohl das Vorhandensein des Nullvektors allein nicht die Existenz additiver Inversen innerhalb des Unterraums garantiert, schafft seine Abwesenheit ein grundlegendes Problem. Wenn ein Vektor $\mathbf{v}$ im Unterraum ist und der Unterraum unter Skalarmultiplikation abgeschlossen ist, dann muss $(-1)\mathbf{v} = -\mathbf{v}$ auch im Unterraum sein (dies ist das additive Inverse von $\mathbf{v}$). Damit die Addition von $\mathbf{v}$ und $-\mathbf{v}$ zu einem Vektor *innerhalb* des Unterraums führt, muss dieser resultierende Vektor der Nullvektor sein. Wenn der Nullvektor nicht in der Teilmenge enthalten ist, könnte die Abgeschlossenheit unter Addition verletzt sein, selbst wenn additive Inverse innerhalb des größeren Vektorraums existieren.

Einfacher ausgedrückt: Wenn eine Teilmenge nicht einmal das "Identitätselement" für die Vektoraddition (welches der Nullvektor ist) enthält, kann sie nicht wirklich als ein in sich geschlossenes System unter Vektoraddition und Skalarmultiplikation fungieren, was die definierenden Operationen eines Vektorraums sind.

Daher ist die Bedingung, dass der Nullvektor im Unterraum sein muss, nicht willkürlich; sie ist eine direkte Folge der Anforderung, dass ein Unterraum die wesentliche algebraische Struktur des größeren Vektorraums, in dem er sich befindet, erben muss.