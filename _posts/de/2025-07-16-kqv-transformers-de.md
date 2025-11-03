---
audio: false
generated: false
image: false
lang: de
layout: post
title: Neuronales Netzwerk, Transformer und GPT
translated: true
---

### Inhaltsverzeichnis

1. [Wie ich den KQV-Mechanismus in Transformatoren gelernt habe](#how-i-learned-the-kqv-mechanism-in-transformers)
   - Query-, Key-, Value-Matrizen repräsentieren Token-Interaktionen
   - Das Verständnis erfordert Kenntnisse der Dimensionen und Formen
   - Erste Konzepte werden mit der Zeit klarer
   - Die KI-Ära bietet eine Fülle von Lernressourcen
   - Inspirierende Geschichten motivieren zum Weiterlernen

2. [Vom neuronalen Netzwerk zu GPT](#from-neural-network-to-gpt)
   - Neuronale Netze von Grund auf nachbilden, um sie zu verstehen
   - Transformatoren verarbeiten Text über Embedding und Encoding
   - Self-Attention berechnet Ähnlichkeiten zwischen Wörtern
   - Grundlegende Vorlesungen ansehen und Code lesen
   - Der Neugier durch Projekte und Veröffentlichungen folgen

3. [Wie neuronale Netze funktionieren](#how-neural-network-works)
   - Der Backpropagation-Algorithmus aktualisiert Gewichte und Biases
   - Eingabedaten werden durch Netzwerkschichten aktiviert
   - Feedforward berechnet Schichtausgaben über Sigmoid
   - Die Fehlerberechnung leitet die Lernanpassungen
   - Dimensionsverständnis ist entscheidend für das Verständnis


## Wie ich den KQV-Mechanismus in Transformatoren gelernt habe

*16.07.2025*

Nachdem ich [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en) gelesen hatte, verstand ich irgendwie, wie K, Q und V funktionieren.

Q steht für Query, K für Key und V für Value. Für einen Satz ist die Query eine Matrix, die den Wert eines Tokens speichert, nach dem es andere Tokens fragen muss. Der Key steht für die Beschreibung der Tokens, und der Value steht für die eigentliche Bedeutungsmatrix der Tokens.

Sie haben spezifische Formen, daher muss man ihre Dimensionen und Details kennen.

Ich verstand dies etwa Anfang Juni 2025. Ich hatte es erstmals Ende 2023 gelernt. Damals las ich Artikel wie [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), verstand aber nicht viel.

Nach etwa zwei Jahren fiel es mir nun leichter zu verstehen. In diesen zwei Jahren konzentrierte ich mich auf Backend-Arbeiten und die Vorbereitung auf meine Associate-Degree-Prüfungen, und ich las oder lernte nicht viel über maschinelles Lernen. Allerdings dachte ich von Zeit zu Zeit über diese Konzepte nach, wenn ich Auto fuhr oder andere Dinge tat.

Dies erinnert mich an den Effekt der Zeit. Wir mögen auf den ersten Blick viele Dinge lernen, auch wenn wir nicht viel verstehen. Aber irgendwie löst es einen Ausgangspunkt für unser Denken aus.

Im Laufe der Zeit stellte ich fest, dass es im Hinblick auf Wissen und Entdeckungen schwierig ist, Dinge beim ersten Mal zu durchdenken oder zu verstehen. Später scheint es jedoch leichter zu lernen und zu wissen.

Ein Grund dafür ist, dass das Lernen in der Ära der KI einfacher ist, weil man in jedes Detail oder jeden Aspekt eintauchen kann, um seine Zweifel zu beseitigen. Es gibt auch mehr verwandte KI-Videos. Noch wichtiger ist, dass man sieht, wie viele Leute lernen und Projekte darauf aufbauen, wie [llama.cpp](https://github.com/ggml-org/llama.cpp).

Die Geschichte von Georgi Gerganov ist inspirierend. Als neuer Lernender im Bereich maschinelles Lernen, der etwa 2021 begann, hatte er einen starken Einfluss in der KI-Gemeinschaft.

So etwas wird immer wieder passieren. Für Reinforcement Learning und die neuesten KI-Kenntnisse werde ich, obwohl ich ihnen immer noch nicht viel Zeit widmen kann, versuchen, etwas Zeit zu finden, um sie schnell zu lernen und viel darüber nachzudenken. Das Gehirn wird seine Arbeit tun.


---

## Vom neuronalen Netzwerk zu GPT

*28.09.2023*

### YouTube-Videos

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Model explanation (including math), Inference and Training

StatQuest with Josh Starmer - Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!

Pascal Poupart - CS480/680 Lecture 19: Attention and Transformer Networks

The A.I. Hacker - Michael Phi - Illustrated Guide to Transformers Neural Network: A step-by-step explanation

### Wie ich lerne

Nachdem ich die Hälfte des Buches "Neural Networks and Deep Learning" gelesen hatte, begann ich, das Beispiel eines neuronalen Netzes zur Erkennung handgeschriebener Ziffern nachzubilden. Ich erstellte ein Repository auf GitHub, https://github.com/lzwjava/neural-networks-and-zhiwei-learning.

Das ist der wirklich schwierige Teil. Wenn man es von Grund auf neu schreiben kann, ohne Code zu kopieren, versteht man es sehr gut.

Mein replizierter Code enthält immer noch nicht die Implementierung von update_mini_batch und backprop. Durch sorgfältiges Beobachten der Variablen in der Phase des Datenladens, Feed-Forwarding und Evaluierens erhielt ich jedoch ein viel besseres Verständnis der Vektor-, Dimensionalitäts-, Matrix- und Formeigenschaften der Objekte.

Und ich begann, die Implementierung von GPT und Transformer zu lernen. Durch Wort-Embedding und Positional Encoding ändern sich die Texte in Zahlen. Im Wesentlichen gibt es dann keinen Unterschied mehr zu einem einfachen neuronalen Netz zur Erkennung handgeschriebener Ziffern.

Andrej Karpathys Vorlesung "Let's build GPT" ist sehr gut. Er erklärt die Dinge gut.

Der erste Grund ist, dass es wirklich von Grund auf neu ist. Wir sehen zuerst, wie der Text generiert wird. Es ist irgendwie unscharf und zufällig. Der zweite Grund ist, dass Andrej die Dinge sehr intuitiv erklären konnte. Andrej hat das Projekt nanoGPT mehrere Monate lang durchgeführt.

Ich hatte gerade eine neue Idee, um die Qualität der Vorlesung zu beurteilen. Kann der Autor diese Codes wirklich schreiben? Warum verstehe ich nicht und welches Thema verpasst der Autor? Was sind neben diesen eleganten Diagrammen und Animationen ihre Mängel und Defekte?

Zurück zum Thema maschinelles Lernen selbst. Wie Andrej erwähnt, das Dropout, die Residual Connection, die Self-Attention, die Multi-Head Attention, die Masked Attention.

Indem ich mir weitere der oben genannten Videos ansah, begann ich etwas zu verstehen.

Durch Positional Encoding mit Sinus- und Kosinusfunktionen erhalten wir einige Gewichte. Durch Word Embedding ändern wir die Wörter in Zahlen.

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> The pizza came out of the oven and it tasted good.

In diesem Satz, wie weiß der Algorithmus, ob es sich auf Pizza oder Ofen bezieht? Wie berechnen wir die Ähnlichkeiten für jedes Wort im Satz?

Wir wollen einen Satz von Gewichten. Wenn wir das Transformer-Netzwerk für die Übersetzungsaufgabe verwenden, kann es jedes Mal, wenn wir einen Satz eingeben, den entsprechenden Satz in einer anderen Sprache ausgeben.

Über das Skalarprodukt hier. Ein Grund, warum wir das Skalarprodukt hier verwenden, ist, dass das Skalarprodukt jede Zahl im Vektor berücksichtigt. Was wäre, wenn wir das quadrierte Skalarprodukt verwenden? Wir berechnen zuerst das Quadrat der Zahlen und lassen sie dann das Skalarprodukt bilden. Was wäre, wenn wir ein umgekehrtes Skalarprodukt bilden?

Was die Maskierung hier betrifft, ändern wir die Zahlen der Hälfte der Matrix in negative Unendlichkeit. Und dann verwenden wir Softmax, um die Werte von 0 bis 1 zu bringen. Wie wäre es, wenn wir die Zahlen unten links in negative Unendlichkeit ändern?

### Plan

Lies weiterhin Code und Papers und schau Videos an. Habe einfach Spaß und folge meiner Neugier.

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch

---

## Wie neuronale Netze funktionieren

*30.05.2023*

Lassen Sie uns direkt den Kern der neuronalen Arbeit besprechen. Das heißt, den Backpropagation-Algorithmus:

1. Eingabe x: Setzen Sie die entsprechende Aktivierung $$a^{1}$$ für die Eingabeschicht.
2. Feedforward: Berechnen Sie für jedes l=2,3,…,L $$z^{l} = w^l a^{l-1}+b^l$$ und $$a^{l} = \sigma(z^{l})$$
3. Fehlererzeugung $$\delta^{L}$$: Berechnen Sie den Vektor $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. Fehler rückgängig machen: Berechnen Sie für jedes l=L−1,L−2,…,2 $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. Ausgabe: Der Gradient der Kostenfunktion ist gegeben durch $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ und $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

Dies ist aus Michael Nelsons Buch *Neural Networks and Deep Learning* kopiert. Ist es überwältigend? Das mag beim ersten Sehen der Fall sein. Aber nach einem Monat des Studierens ist es das nicht mehr. Lassen Sie mich erklären.

### Eingabe

Es gibt 5 Phasen. Die erste Phase ist die Eingabe. Hier verwenden wir handgeschriebene Ziffern als Eingabe. Unsere Aufgabe ist es, sie zu erkennen. Eine handgeschriebene Ziffer hat 784 Pixel, das sind 28*28. In jedem Pixel gibt es einen Graustufenwert, der von 0 bis 255 reicht. Die Aktivierung bedeutet also, dass wir eine Funktion verwenden, um sie zu aktivieren, um ihren ursprünglichen Wert in einen neuen Wert umzuwandeln, um die Verarbeitung zu erleichtern.

Nehmen wir an, wir haben jetzt 1000 Bilder mit 784 Pixeln. Wir trainieren es nun, um zu erkennen, welche Ziffern sie zeigen. Wir haben jetzt 100 Bilder, um diesen Lerneffekt zu testen. Wenn das Programm die Ziffern von 97 Bildern erkennen kann, sagen wir, dass seine Genauigkeit 97 % beträgt.

Wir würden also die 1000 Bilder durchlaufen, um die Gewichte und Biases zu trainieren. Wir korrigieren die Gewichte und Biases jedes Mal, wenn wir ein neues Bild zum Lernen geben.

Ein Batch-Trainingsergebnis soll sich in 10 Neuronen widerspiegeln. Hier repräsentieren die 10 Neuronen von 0 bis 9, und ihr Wert liegt zwischen 0 und 1, um anzuzeigen, wie hoch ihr Vertrauen in ihre Genauigkeit ist.

Und die Eingabe sind 784 Neuronen. Wie können wir 784 Neuronen auf 10 Neuronen reduzieren? Hier ist der Punkt. Nehmen wir an, wir haben zwei Schichten. Was bedeutet die Schicht? Das ist die erste Schicht, wir haben 784 Neuronen. In der zweiten Schicht haben wir 10 Neuronen.

Wir geben jedem Neuron in den 784 Neuronen ein Gewicht, sagen wir,

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

Und geben der ersten Schicht einen Bias, das ist $$b_1$$.

Und so ist für das erste Neuron in der zweiten Schicht sein Wert:

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

Aber diese Gewichte und ein Bias sind für $$neuron^2_{1}$$ (das erste in der zweiten Schicht). Für $$neuron^2_{2}$$ benötigen wir einen weiteren Satz Gewichte und einen Bias.

Wie wäre es mit der Sigmoidfunktion? Wir verwenden die Sigmoidfunktion, um den Wert des oben genannten Wertes von 0 auf 1 abzubilden.

$$
\begin{eqnarray}
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
\end{eqnarray}
$$

$$
\begin{eqnarray}
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}
\end{eqnarray}
$$

Wir verwenden auch die Sigmoidfunktion, um die erste Schicht zu aktivieren. Das heißt, wir ändern den Graustufenwert in den Bereich von 0 bis 1. So hat nun jedes Neuron in jeder Schicht einen Wert von 0 bis 1.

Für unser zweischichtiges Netzwerk hat die erste Schicht 784 Neuronen und die zweite Schicht 10 Neuronen. Wir trainieren es, um die Gewichte und Biases zu erhalten.

Wir haben 784 * 10 Gewichte und 10 Biases. In der zweiten Schicht verwenden wir für jedes Neuron 784 Gewichte und 1 Bias, um seinen Wert zu berechnen. Der Code hier sieht so aus:

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

### Feedforward

> Feedforward: Für jedes l=2,3,…,L berechne $$z^{l} = w^l a^{l-1}+b^l$$ und $$a^{l} = \sigma(z^{l})$$

Beachten Sie hier, dass wir den Wert der letzten Schicht, d.h. $$a^{l-1}$$, und das Gewicht der aktuellen Schicht, $$w^l$$, sowie ihren Bias $$b^l$$ verwenden, um die Sigmoidfunktion anzuwenden, um den Wert der aktuellen Schicht, $$a^{l}$$, zu erhalten.

Code:

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
### Ausgabe-Fehler

> Ausgabe-Fehler $$\delta^{L}$$: Berechne den Vektor $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

Sehen wir, was das $$\nabla$$ bedeutet.

> Del, oder Nabla, ist ein Operator, der in der Mathematik (insbesondere in der Vektorrechnung) als Vektordifferentialoperator verwendet wird, üblicherweise durch das Nabla-Symbol ∇ dargestellt.

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

Hier ist $$\eta$$ die Lernrate. Wir verwenden die Ableitung, bei der C die Gewichte bzw. den Bias berücksichtigt, das ist die Änderungsrate zwischen ihnen. Das ist `sigmoid_prime` unten.

Code:

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

### Fehler rückpropagieren

> Fehlerrückführung: Für jedes l=L−1,L−2,…,2 berechne $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

### Ausgabe

> Ausgabe: Der Gradient der Kostenfunktion ist gegeben durch $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
und $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

```python
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

### Finale

Es ist ein kurzer Artikel. Und im größten Teil zeigt er nur den Code und die mathematische Formel. Aber das ist für mich in Ordnung. Bevor ich ihn schrieb, verstand ich ihn nicht klar. Nachdem ich Snippets aus Code und Buch geschrieben oder einfach kopiert hatte, verstand ich das meiste davon. Nachdem ich von Lehrer Yin Wang Selbstvertrauen gewonnen, etwa 30 % des Buches *Neural Networks and Deep Learning* gelesen, Andrej Karpathys Stanford-Vorlesungen und Andrew Ngs Kurse gehört, mit meinem Freund Qi diskutiert und Anaconda, numpy und Theano-Bibliotheken angepasst hatte, um den Code von vor Jahren wieder funktionsfähig zu machen, verstehe ich es jetzt.

Einer der wichtigsten Punkte sind die Dimensionen. Wir sollten die Dimensionen jedes Symbols und jeder Variablen kennen. Und es führt einfach die differenzierbare Berechnung durch. Lassen Sie uns mit Yin Wangs Zitaten schließen:

> Maschinelles Lernen ist wirklich nützlich, man könnte sogar sagen, eine schöne Theorie, denn es ist einfach Analysis nach einem Makeover! Es ist die alte und große Theorie von Newton, Leibniz, in einer einfacheren, eleganteren und mächtigen Form. Maschinelles Lernen ist im Grunde die Verwendung von Analysis, um einige Funktionen abzuleiten und anzupassen, und Deep Learning ist das Anpassen komplexerer Funktionen.

> Es gibt keine "Intelligenz" in künstlicher Intelligenz, kein "neural" in neuronalem Netzwerk, kein "Lernen" in maschinellem Lernen und keine "Tiefe" in Deep Learning. Was in diesem Bereich wirklich funktioniert, nennt man "Analysis". Daher ziehe ich es vor, dieses Feld "differenzierbare Berechnung" und den Prozess des Aufbaus von Modellen "differenzierbare Programmierung" zu nennen.