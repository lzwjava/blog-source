---
audio: false
generated: true
lang: de
layout: post
title: Fragen zur Linearen Algebra
translated: true
type: note
---

**18. Die Matrizen X und A erfüllen die Beziehung XA = X + A. Wenn $A = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$ ist, finde die Matrix X.**

**Antwort:**
Wir haben die Gleichung $XA = X + A$.
Wir können dies umschreiben als $XA - X = A$, also $X(A - I) = A$.
Wenn $(A - I)$ invertierbar ist, dann ist $X = A(A - I)^{-1}$.

Zuerst berechnen wir $A - I$:

$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$.

Als nächstes finden wir die Inverse von $(A - I)$. Sei $B = A - I$.
Die Determinante von B ist $\det(B) = 0(0 - 0) - (-3)(2 - 0) + 0(0 - 0) = 6$.
Da $\det(B) \neq 0$ ist, ist B invertierbar.

Die Adjunkte von B ist:
$adj(B) = \begin{pmatrix} C_{11} & C_{21} & C_{31} \\\ C_{12} & C_{22} & C_{32} \\\ C_{13} & C_{23} & C_{33} \end{pmatrix}$
$C_{11} = \begin{vmatrix} 0 & 0 \\\ 0 & 1 \end{vmatrix} = 0$
$C_{12} = -\begin{vmatrix} 2 & 0 \\\ 0 & 1 \end{vmatrix} = -2$
$C_{13} = \begin{vmatrix} 2 & 0 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{21} = -\begin{vmatrix} -3 & 0 \\\ 0 & 1 \end{vmatrix} = 3$
$C_{22} = \begin{vmatrix} 0 & 0 \\\ 0 & 1 \end{vmatrix} = 0$
$C_{23} = -\begin{vmatrix} 0 & -3 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{31} = \begin{vmatrix} -3 & 0 \\\ 0 & 0 \end{vmatrix} = 0$
$C_{32} = -\begin{vmatrix} 0 & 0 \\\ 2 & 0 \end{vmatrix} = 0$
$C_{33} = \begin{vmatrix} 0 & -3 \\\ 2 & 0 \end{vmatrix} = 6$

Die Kofaktormatrix ist $C = \begin{pmatrix} 0 & -2 & 0 \\\ 3 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$.
Die Adjunkte Matrix ist $adj(B) = C^T = \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$.

Dann ist $(A - I)^{-1} = \frac{1}{\det(B)} adj(B) = \frac{1}{6} \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$.

Jetzt berechnen wir $X = A(A - I)^{-1}$:
$X = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
$X = \begin{pmatrix} (1)(0) + (-3)(-1/3) + (0)(0) & (1)(1/2) + (-3)(0) + (0)(0) & (1)(0) + (-3)(0) + (0)(1) \\\ (2)(0) + (1)(-1/3) + (0)(0) & (2)(1/2) + (1)(0) + (0)(0) & (2)(0) + (1)(0) + (0)(1) \\\ (0)(0) + (0)(-1/3) + (2)(0) & (0)(1/2) + (0)(0) + (2)(0) & (0)(0) + (0)(0) + (2)(1) \end{pmatrix}$
$X = \begin{pmatrix} 0+1+0 & 1/2+0+0 & 0+0+0 \\\ 0-1/3+0 & 1+0+0 & 0+0+0 \\\ 0+0+0 & 0+0+0 & 0+0+2 \end{pmatrix}$
$X = \begin{pmatrix} 1 & 1/2 & 0 \\\ -1/3 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$.

**19. Bestimme den Wert von k, für den die Vektoren $\alpha_1 = (1, 1, k)^T$, $\alpha_2 = (1, k, 1)^T$, $\alpha_3 = (k, 1, 1)^T$ linear abhängig sind. Finde eine maximal linear unabhängige Menge und drücke die verbleibenden Vektor(en) als Linearkombination dieser Menge aus.**

**Antwort:**
Die Vektoren $\alpha_1, \alpha_2, \alpha_3$ sind linear abhängig, wenn die Determinante der aus diesen Vektoren gebildeten Matrix null ist.
Sei $A = \begin{pmatrix} 1 & 1 & k \\\ 1 & k & 1 \\\ k & 1 & 1 \end{pmatrix}$.
$\det(A) = 1(k - 1) - 1(1 - k) + k(1 - k^2)$
$= k - 1 - 1 + k + k - k^3$
$= -k^3 + 3k - 2$.
Wir müssen k so finden, dass $-k^3 + 3k - 2 = 0$, oder $k^3 - 3k + 2 = 0$.
Wir können nach ganzzahligen Wurzeln suchen, die Teiler von 2 sind (d.h. $\pm 1, \pm 2$).
Wenn $k=1$, $1^3 - 3(1) + 2 = 1 - 3 + 2 = 0$. Also ist $(k-1)$ ein Faktor.
Wenn $k=-2$, $(-2)^3 - 3(-2) + 2 = -8 + 6 + 2 = 0$. Also ist $(k+2)$ ein Faktor.
Polynomdivision oder synthetische Division für $(k^3 - 3k + 2) / (k-1)$:
$(k-1)(k^2+k-2) = 0$
$(k-1)(k+2)(k-1) = 0$
Die Wurzeln sind also $k=1$ (doppelte Wurzel) und $k=-2$.
Die Vektoren sind linear abhängig, wenn $k=1$ oder $k=-2$.

Fall 1: $k=1$
$\alpha_1 = (1, 1, 1)^T$, $\alpha_2 = (1, 1, 1)^T$, $\alpha_3 = (1, 1, 1)^T$.
In diesem Fall sind alle drei Vektoren identisch.
Eine maximal linear unabhängige Menge kann $\{\alpha_1\}$ sein.
Dann ist $\alpha_2 = 1 \cdot \alpha_1$ und $\alpha_3 = 1 \cdot \alpha_1$.

Fall 2: $k=-2$
$\alpha_1 = (1, 1, -2)^T$, $\alpha_2 = (1, -2, 1)^T$, $\alpha_3 = (-2, 1, 1)^T$.
Prüfen wir, ob $\alpha_1$ und $\alpha_2$ linear unabhängig sind. Sie sind keine skalaren Vielfachen voneinander, also sind sie linear unabhängig. Somit kann eine maximal linear unabhängige Menge $\{\alpha_1, \alpha_2\}$ sein.
Wir möchten $\alpha_3$ als Linearkombination von $\alpha_1$ und $\alpha_2$ ausdrücken:
$\alpha_3 = c_1 \alpha_1 + c_2 \alpha_2$
$(-2, 1, 1)^T = c_1 (1, 1, -2)^T + c_2 (1, -2, 1)^T$
Dies ergibt das Gleichungssystem:
1) $c_1 + c_2 = -2$
2) $c_1 - 2c_2 = 1$
3) $-2c_1 + c_2 = 1$
Subtrahiere (2) von (1): $(c_1 + c_2) - (c_1 - 2c_2) = -2 - 1 \Rightarrow 3c_2 = -3 \Rightarrow c_2 = -1$.
Setze $c_2 = -1$ in (1) ein: $c_1 - 1 = -2 \Rightarrow c_1 = -1$.
Prüfe mit (3): $-2(-1) + (-1) = 2 - 1 = 1$. Dies ist konsistent.
Also ist $\alpha_3 = -1 \cdot \alpha_1 - 1 \cdot \alpha_2$.

**20. Löse das lineare Gleichungssystem { $x_1 - x_2 - 3x_4 = -2$ ; $x_1 + 2x_3 - 2x_4 = -1$ ; $2x_1 - 2x_2 + x_3 - 6x_4 = -5$ ; $-x_1 + 2x_2 + 3x_3 + 4x_4 = 2$ } (Finde eine partikuläre Lösung und die fundamentale Basis von Lösungen für das entsprechende homogene System).**

**Antwort:**
Die erweiterte Matrix ist:
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 1 & 0 & 2 & -2 & | & -1 \\\ 2 & -2 & 1 & -6 & | & -5 \\\ -1 & 2 & 3 & 4 & | & 2 \end{pmatrix}$

$R_2 \leftarrow R_2 - R_1$
$R_3 \leftarrow R_3 - 2R_1$
$R_4 \leftarrow R_4 + R_1$
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 1 & 3 & 1 & | & 0 \end{pmatrix}$

$R_1 \leftarrow R_1 + R_2$
$R_4 \leftarrow R_4 - R_2$
$\begin{pmatrix} 1 & 0 & 2 & -2 & | & -1 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 1 & 0 & | & -1 \end{pmatrix}$

$R_1 \leftarrow R_1 - 2R_3$
$R_2 \leftarrow R_2 - 2R_3$
$R_4 \leftarrow R_4 - R_3$
$\begin{pmatrix} 1 & 0 & 0 & -2 & | & 1 \\\ 0 & 1 & 0 & 1 & | & 3 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 0 & 0 & | & 0 \end{pmatrix}$

Das System ist äquivalent zu:
$x_1 - 2x_4 = 1 \Rightarrow x_1 = 1 + 2x_4$
$x_2 + x_4 = 3 \Rightarrow x_2 = 3 - x_4$
$x_3 = -1$
Sei $x_4 = t$ (freie Variable).
Die allgemeine Lösung ist:
$x_1 = 1 + 2t$
$x_2 = 3 - t$
$x_3 = -1$
$x_4 = t$
In Vektorform: $X = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix} + t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$.

Eine partikuläre Lösung erhält man durch Setzen von $t=0$: $X_p = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix}$.

Das entsprechende homogene System hat die Lösung $X_h = t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$.
Die fundamentale Basis von Lösungen für das homogene System ist $\{\begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}\}$.

**21. Die Matrix A = \begin{pmatrix} x & 0 & y \\\ 0 & 2 & 0 \\\ y & 0 & -2 \end{pmatrix} habe einen Eigenwert von -3, und |A| = -12. Finde die Werte von x und y.**

**Antwort:**
Die charakteristische Gleichung ist $\det(A - \lambda I) = 0$.
$A - \lambda I = \begin{pmatrix} x-\lambda & 0 & y \\\ 0 & 2-\lambda & 0 \\\ y & 0 & -2-\lambda \end{pmatrix}$.
$\det(A - \lambda I) = (x-\lambda)[(2-\lambda)(-2-\lambda) - 0] - 0 + y[0 - y(2-\lambda)]$
$= (x-\lambda)(2-\lambda)(-2-\lambda) - y^2(2-\lambda)$
$= (2-\lambda)[(x-\lambda)(-2-\lambda) - y^2]$
$= (2-\lambda)[-2x - x\lambda + 2\lambda + \lambda^2 - y^2] = 0$.
Die Eigenwerte sind $\lambda_1 = 2$ und die Wurzeln von $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$.
Es ist gegeben, dass ein Eigenwert -3 ist.
Wenn $2 = -3$, ist dies falsch. Also muss -3 eine Wurzel von $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$ sein.
Setze $\lambda = -3$ ein:
$(-3)^2 + (2-x)(-3) - (2x+y^2) = 0$
$9 - 6 + 3x - 2x - y^2 = 0$
$3 + x - y^2 = 0 \Rightarrow x - y^2 = -3$ (Gleichung 1)

Es ist auch gegeben, dass $\det(A) = -12$.
$\det(A) = x(2(-2) - 0) - 0 + y(0 - 2y)$
$= -4x - 2y^2 = -12$
Teile durch -2: $2x + y^2 = 6$ (Gleichung 2)

Jetzt haben wir ein System von zwei Gleichungen mit x und y:
1) $x - y^2 = -3$
2) $2x + y^2 = 6$
Addiere Gleichung 1 und Gleichung 2:
$(x - y^2) + (2x + y^2) = -3 + 6$
$3x = 3 \Rightarrow x = 1$.
Setze $x=1$ in Gleichung 1 ein:
$1 - y^2 = -3$
$-y^2 = -4$
$y^2 = 4 \Rightarrow y = \pm 2$.

Die Werte sind also $x=1$ und $y=2$, oder $x=1$ und $y=-2$.

**22. Sei die quadratische Form mit 3 Variablen $f(x_1, x_2, x_3) = t(x_1^2 + x_2^2 + x_3^2) + 2x_1x_2 + 2x_1x_3 - 2x_2x_3$. Bestimme, für welchen Wert (welche Werte) von t diese quadratische Form positiv definit ist.**

**Antwort:**
Die Matrix der quadratischen Form A ist:
$A = \begin{pmatrix} t & 1 & 1 \\\ 1 & t & -1 \\\ 1 & -1 & t \end{pmatrix}$.
Damit die quadratische Form positiv definit ist, müssen alle führenden Hauptminoren von A positiv sein.

1. Der erste führende Hauptminor ist $M_1 = t$.
Für positive Definitheit muss $t > 0$ sein.

2. Der zweite führende Hauptminor ist $M_2 = \det \begin{pmatrix} t & 1 \\\ 1 & t \end{pmatrix} = t^2 - 1$.
Für positive Definitheit muss $t^2 - 1 > 0 \Rightarrow t^2 > 1$ sein.
Da wir bereits $t > 0$ haben, impliziert dies $t > 1$.

3. Der dritte führende Hauptminor ist $M_3 = \det(A)$.
$M_3 = t(t^2 - 1) - 1(t - (-1)) + 1(-1 - t)$
$= t(t^2 - 1) - (t + 1) - (1 + t)$
$= t^3 - t - t - 1 - 1 - t$
$= t^3 - 3t - 2$.
Für positive Definitheit muss $t^3 - 3t - 2 > 0$ sein.

Wir wissen aus Frage 19, dass $k^3 - 3k - 2 = (k+1)^2(k-2)$. (Hier ist $k$ gleich $t$)
Also ist $t^3 - 3t - 2 = (t+1)^2(t-2)$.
Wir benötigen $(t+1)^2(t-2) > 0$.
Da $(t+1)^2 \ge 0$ ist und um nicht null zu sein, $t \neq -1$.
Also benötigen wir $t-2 > 0$, was $t > 2$ bedeutet.

Kombiniere die Bedingungen:
1) $t > 0$
2) $t > 1$
3) $t > 2$

Der Schnitt dieser Bedingungen ist $t > 2$.
Daher ist die quadratische Form positiv definit, wenn $t > 2$.