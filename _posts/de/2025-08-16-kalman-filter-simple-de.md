---
audio: false
generated: true
image: false
lang: de
layout: post
title: 'Einfach erklärt: Der Kalman-Filter'
translated: true
type: note
---

Hier ist ein **umfassender Leitfaden zur Kalman-Filterung (卡尔曼滤波)** auf Englisch, strukturiert für Klarheit:

---

# 1. Einführung

Der **Kalman-Filter** ist ein **Algorithmus**, der Schätzungen unbekannter Variablen liefert, indem er verrauschte Sensormessungen mit Vorhersagen aus einem Systemmodell kombiniert. Er wird häufig in **Regelungssystemen, Navigation, Robotik, Computer Vision und Finanzen** eingesetzt.

Grundidee:
Er arbeitet rekursiv – das bedeutet, er aktualisiert kontinuierlich seine Schätzung, sobald neue Messwerte eintreffen, anstatt auf den gesamten Datensatz zu warten.

---

# 2. Grundkonzepte

### Zustand

Die Menge der Variablen, die wir schätzen möchten (z. B. Position, Geschwindigkeit).

### Prozessmodell

Beschreibt, wie sich der Zustand über die Zeit entwickelt, normalerweise mit einer gewissen Unsicherheit.

### Messmodell

Bezieht die tatsächlichen Sensormessungen auf den zugrunde liegenden Zustand.

### Rauschen

Sowohl der Prozess als auch die Messungen weisen Unsicherheiten (zufälliges Rauschen) auf. Der Kalman-Filter modelliert dies explizit unter Verwendung von Wahrscheinlichkeiten.

---

# 3. Mathematische Formulierung

Der Kalman-Filter geht von einem **linearen System** mit gaußschem Rauschen aus.

* **Zustandsgleichung (Prädiktion):**

  $$
  x_k = A x_{k-1} + B u_k + w_k
  $$

  * $x_k$: Zustand zum Zeitpunkt $k$
  * $A$: Zustandsübergangsmatrix
  * $B u_k$: Steuereingabe
  * $w_k$: Prozessrauschen (Gaußsch, Kovarianz $Q$)

* **Messgleichung (Beobachtung):**

  $$
  z_k = H x_k + v_k
  $$

  * $z_k$: Messung
  * $H$: Beobachtungsmatrix
  * $v_k$: Messrauschen (Gaußsch, Kovarianz $R$)

---

# 4. Die zwei Hauptschritte

### Schritt 1: Prädiktion

* Den Zustand für einen zukünftigen Zeitpunkt vorhersagen.
* Die Unsicherheit (Fehlerkovarianz) vorhersagen.

### Schritt 2: Update (Korrektur)

* Die vorhergesagte Messung mit der tatsächlichen Messung vergleichen.
* Die **Kalman-Verstärkung** berechnen (wie viel Vertrauen in die Messung vs. die Vorhersage gesetzt wird).
* Die Schätzung aktualisieren und die Unsicherheit reduzieren.

---

# 5. Kalman-Filter-Gleichungen (Linearer Fall)

1. **Zustand vorhersagen:**

   $$
   \hat{x}_k^- = A \hat{x}_{k-1} + B u_k
   $$

2. **Kovarianz vorhersagen:**

   $$
   P_k^- = A P_{k-1} A^T + Q
   $$

3. **Kalman-Verstärkung:**

   $$
   K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}
   $$

4. **Zustand aktualisieren:**

   $$
   \hat{x}_k = \hat{x}_k^- + K_k (z_k - H \hat{x}_k^-)
   $$

5. **Kovarianz aktualisieren:**

   $$
   P_k = (I - K_k H) P_k^-
   $$

Wo:

* $\hat{x}_k^-$: Vorhergesagter Zustand vor dem Update
* $\hat{x}_k$: Aktualisierter Zustand
* $P_k$: Kovarianzmatrix (Unsicherheit in der Schätzung)

---

# 6. Intuition

* Wenn die Messung **sehr verrauscht** ist (großes $R$), wird die Kalman-Verstärkung klein → verlasse dich mehr auf die Vorhersage.
* Wenn das Modell **unsicher** ist (großes $Q$), erhöht sich die Kalman-Verstärkung → verlasse dich mehr auf die Messungen.
* Im Laufe der Zeit findet es die **optimale Balance** zwischen dem Vertrauen in das Modell und dem Vertrauen in die Sensoren.

---

# 7. Varianten

* **Erweiterter Kalman-Filter (EKF):** Für nichtlineare Systeme, verwendet Linearisierung (Jacobimatrix).
* **Unscented Kalman Filter (UKF):** Für nichtlineare Systeme, verwendet deterministisches Sampling.
* **Information Filter:** Arbeitet mit inverser Kovarianz für Effizienz.
* **Ensemble Kalman Filter:** Wird in der Wettervorhersage und bei hochdimensionalen Systemen eingesetzt.

---

# 8. Anwendungen

* **Navigation:** GPS + Beschleunigungsmesser-Fusion für Positionsverfolgung.
* **Robotik:** SLAM (Simultaneous Localization and Mapping).
* **Finanzen:** Schätzung versteckter Variablen wie Volatilität.
* **Computer Vision:** Objektverfolgung in Videos.
* **Regelungssysteme:** Stabilisierung von Flugzeugen und Raumfahrzeugen.

---

# 9. Beispielszenario

Stellen Sie sich ein selbstfahrendes Auto vor, das seine Position schätzt:

* Das Modell sagt die Position unter Verwendung der Geschwindigkeit + vorherigen Zustands vorher.
* GPS liefert eine verrauschte Messung der Position.
* Der Kalman-Filter kombiniert Vorhersage und GPS, um eine glattere, genauere Position zu erhalten.

Im Laufe der Zeit kann das Auto seinen Standort verfolgen, selbst wenn das GPS kurzzeitig ausfällt.

---

# 10. Wichtige Stärken und Einschränkungen

**Stärken:**

* Rekursiv, effizient (benötigt nur den letzten Zustand, nicht die gesamte Historie).
* Optimal für lineare Gauß-Systeme.
* Weitgehend erprobt und robust.

**Einschränkungen:**

* Erfordert genaue Modelle der Dynamik und des Rauschens.
* Rein linear – nichtlineare Fälle benötigen EKF/UKF.
* Kann divergieren, wenn die Annahmen verletzt werden.

---

✅ Kurz gesagt: Der **Kalman-Filter** ist eine mathematisch elegante Methode, um Vorhersagen und Messungen unter Unsicherheit zu fusionieren, indem er das Vertrauen zwischen Modellen und Sensoren ausbalanciert, um die bestmögliche Schätzung in Echtzeit zu erzeugen.

---

Möchten Sie, dass ich Ihnen auch ein **schrittweises Python-Implementierungsbeispiel** gebe (z. B. zur Positionsverfolgung mit Rauschen), damit Sie sehen können, wie es in der Praxis funktioniert?