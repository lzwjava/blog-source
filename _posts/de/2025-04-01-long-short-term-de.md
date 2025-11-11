---
audio: false
generated: true
lang: de
layout: post
title: Lange Kurzzeitgedächtnisnetzwerke
translated: true
type: note
---

Long Short-Term Memory (LSTM)-Netzwerke sind eine Art von rekurrenten neuronalen Netzwerkarchitekturen, die speziell entwickelt wurden, um das Problem des verschwindenden Gradienten zu adressieren und das Lernen von Langzeitabhängigkeiten in sequenziellen Daten zu ermöglichen. Sie erreichen dies durch eine anspruchsvollere interne Struktur, die **LSTM-Zelle** genannt wird.

Hier ist eine Aufschlüsselung, wie eine LSTM-Zelle funktioniert:

**Kernidee: Der Zellzustand**

Das zentrale Konzept in einem LSTM ist der **Zellzustand** (oft bezeichnet als 'C<sub>t</sub>'). Man kann sich den Zellzustand als ein Fließband vorstellen, das durch die gesamte Sequenz läuft. Er trägt Informationen, die für die Langzeithistorie der Sequenz relevant sind. Informationen können dem Zellzustand hinzugefügt oder von ihm entfernt werden, während er durch das Netzwerk fließt, und zwar über Strukturen, die **Gates** (Tore) genannt werden.

**Die Gates**

LSTM-Zellen haben drei Haupt-Gates, die den Informationsfluss regulieren:

1.  **Forget Gate (Vergess-Gate):** Dieses Gate entscheidet, welche Informationen aus dem vorherigen Zellzustand verworfen werden sollen.
    * Es empfängt den vorherigen verborgenen Zustand (h<sub>t-1</sub>) und die aktuelle Eingabe (x<sub>t</sub>).
    * Diese werden durch eine Neuronale-Netzwerk-Schicht gefolgt von einer **Sigmoid-Aktivierungsfunktion** geleitet.
    * Die Sigmoid-Funktion gibt Werte zwischen 0 und 1 aus. Ein Wert nahe 0 bedeutet "diese Information vollständig vergessen", während ein Wert nahe 1 bedeutet "diese Information vollständig behalten".
    * Mathematisch wird die Ausgabe des Forget Gates (f<sub>t</sub>) berechnet als:
        ```
        f_t = σ(W_f * [h_{t-1}, x_t] + b_f)
        ```
        wobei:
        * σ die Sigmoid-Funktion ist.
        * W<sub>f</sub> die Gewichtsmatrix für das Forget Gate ist.
        * [h<sub>t-1</sub>, x_t] die Verkettung des vorherigen verborgenen Zustands und der aktuellen Eingabe ist.
        * b<sub>f</sub> der Bias-Vektor für das Forget Gate ist.

2.  **Input Gate (Eingabe-Gate):** Dieses Gate entscheidet, welche neuen Informationen aus der aktuellen Eingabe dem Zellzustand hinzugefügt werden sollen. Dieser Prozess umfasst zwei Schritte:
    * **Input Gate Layer (Eingabe-Gate-Schicht):** Eine Sigmoid-Schicht entscheidet, welche Werte wir aktualisieren werden.
        ```
        i_t = σ(W_i * [h_{t-1}, x_t] + b_i)
        ```
        wobei:
        * σ die Sigmoid-Funktion ist.
        * W<sub>i</sub> die Gewichtsmatrix für das Input Gate ist.
        * [h<sub>t-1</sub>, x_t] die Verkettung des vorherigen verborgenen Zustands und der aktuellen Eingabe ist.
        * b<sub>i</sub> der Bias-Vektor für das Input Gate ist.
    * **Candidate Values Layer (Kandidatenwerte-Schicht):** Eine tanh-Schicht erzeugt einen Vektor neuer Kandidatenwerte (Kandidat-Zellzustand, bezeichnet als 'C̃<sub>t</sub>'), die dem Zellzustand hinzugefügt werden könnten. Die tanh-Funktion gibt Werte zwischen -1 und 1 aus, was zur Regulierung des Netzwerks beiträgt.
        ```
        C̃_t = tanh(W_C * [h_{t-1}, x_t] + b_C)
        ```
        wobei:
        * tanh die hyperbolische Tangens-Funktion ist.
        * W<sub>C</sub> die Gewichtsmatrix für den Kandidat-Zellzustand ist.
        * [h<sub>t-1</sub>, x_t] die Verkettung des vorherigen verborgenen Zustands und der aktuellen Eingabe ist.
        * b<sub>C</sub> der Bias-Vektor für den Kandidat-Zellzustand ist.

3.  **Output Gate (Ausgabe-Gate):** Dieses Gate entscheidet, welche Informationen aus dem aktuellen Zellzustand als verborgenen Zustand für den aktuellen Zeitschritt ausgegeben werden sollen.
    * Es empfängt den vorherigen verborgenen Zustand (h<sub>t-1</sub>) und die aktuelle Eingabe (x<sub>t</sub>).
    * Diese werden durch eine Neuronale-Netzwerk-Schicht gefolgt von einer **Sigmoid-Aktivierungsfunktion** geleitet, um zu bestimmen, welche Teile des Zellzustands ausgegeben werden sollen.
        ```
        o_t = σ(W_o * [h_{t-1}, x_t] + b_o)
        ```
        wobei:
        * σ die Sigmoid-Funktion ist.
        * W<sub>o</sub> die Gewichtsmatrix für das Output Gate ist.
        * [h<sub>t-1</sub>, x_t] die Verkettung des vorherigen verborgenen Zustands und der aktuellen Eingabe ist.
        * b<sub>o</sub> der Bias-Vektor für das Output Gate ist.
    * Der Zellzustand wird dann durch eine **tanh-Funktion** geleitet, um die Werte zwischen -1 und 1 zu skalieren.
    * Schließlich wird die Ausgabe des Sigmoid-Gates elementweise mit der Ausgabe der auf den Zellzustand angewendeten tanh-Funktion multipliziert. Dies wird der neue verborgene Zustand (h<sub>t</sub>), der an den nächsten Zeitschritt weitergegeben wird und auch für Vorhersagen verwendet werden kann.
        ```
        h_t = o_t * tanh(C_t)
        ```

**Aktualisierung des Zellzustands**

Der Zellzustand wird basierend auf den Entscheidungen der Forget- und Input-Gates aktualisiert:

```
C_t = f_t * C_{t-1} + i_t * C̃_t
```

* Das Forget Gate (f<sub>t</sub>) bestimmt, wie viel vom vorherigen Zellzustand (C<sub>t-1</sub>) behalten werden soll. Wenn f<sub>t</sub> nahe 0 ist, wird die Information größtenteils vergessen. Wenn es nahe 1 ist, wird die Information größtenteils behalten.
* Das Input Gate (i<sub>t</sub>) bestimmt, wie viel der neuen Kandidatenwerte (C̃<sub>t</sub>) dem Zellzustand hinzugefügt werden soll. Wenn i<sub>t</sub> nahe 0 ist, werden die neuen Informationen größtenteils ignoriert. Wenn es nahe 1 ist, werden die neuen Informationen größtenteils hinzugefügt.

**Wie LSTMs das Problem des verschwindenden Gradienten lösen:**

Der Schlüssel zur Fähigkeit von LSTMs, mit Langzeitabhängigkeiten umzugehen, liegt im Zellzustand und den Gating-Mechanismen. Der Zellzustand fungiert als direkter Pfad, auf dem Informationen über viele Zeitschritte hinweg fließen können, ohne wiederholt mit Gewichten multipliziert zu werden, was die Hauptursache für verschwindende Gradienten in traditionellen RNNs ist.

Die Gates ermöglichen es dem LSTM zu lernen, wann Informationen im Zellzustand gespeichert, abgerufen und vergessen werden sollen. Dieser selektive Gedächtnismechanismus ermöglicht es dem Netzwerk, relevante Informationen über lange Sequenzen hinweg zu behalten und bei Bedarf zu nutzen, wodurch das Problem des verschwindenden Gradienten effektiv gemildert und das Lernen von Langzeitabhängigkeiten ermöglicht wird.

Im Wesentlichen bieten LSTMs eine Möglichkeit für das Netzwerk, ein "Gedächtnis" über längere Zeiträume aufrechtzuerhalten, was sie sehr effektiv für Aufgaben macht, die sequenzielle Daten mit langreichweitigen Abhängigkeiten beinhalten.