---
audio: false
generated: false
lang: de
layout: post
title: Wie neuronale Netzwerke funktionieren
translated: true
usemathjax: true
---

Lassen Sie uns direkt den Kern der neuronalen Arbeit besprechen. Das heißt, den Backpropagation-Algorithmus:

1. Eingabe x: Setze die entsprechende Aktivierung $$a^{1}$$ für die Eingabeschicht.
2. Vorwärtsdurchlauf: Für jedes l=2,3,…,L berechne $$z^{l} = w^l a^{l-1}+b^l$$ und $$a^{l} = \sigma(z^{l})$$
3. Ausgabefehler $$\delta^{L}$$: Berechne den Vektor $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. Rückpropagierung des Fehlers: Für jedes l=L−1,L−2,…,2, berechne $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. Ausgabe: Der Gradient der Kostenfunktion ist gegeben durch $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ und $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

Dies ist aus Michael Nelsons Buch *Neural Networks and Deep Learning* übernommen. Ist es überwältigend? Vielleicht beim ersten Mal, wenn man es sieht. Aber nach einem Monat des Lernens und der Beschäftigung damit ist es das nicht mehr. Lassen Sie es mich erklären.

## Eingabe

Es gibt 5 Phasen. Die erste Phase ist die Eingabe. Hier verwenden wir handgeschriebene Ziffern als Eingabe. Unsere Aufgabe besteht darin, sie zu erkennen. Eine handgeschriebene Ziffer besteht aus 784 Pixeln, was 28*28 entspricht. In jedem Pixel gibt es einen Graustufenwert, der von 0 bis 255 reicht. Die Aktivierung bedeutet, dass wir eine Funktion verwenden, um sie zu aktivieren, um ihren ursprünglichen Wert in einen neuen Wert zu ändern, um die Verarbeitung zu erleichtern.

Angenommen, wir haben jetzt 1000 Bilder mit jeweils 784 Pixeln. Wir trainieren das Programm nun, um zu erkennen, welche Ziffern sie darstellen. Wir haben jetzt 100 Bilder, um diesen Lerneffekt zu testen. Wenn das Programm die Ziffern auf 97 Bildern korrekt erkennen kann, sagen wir, dass seine Genauigkeit bei 97 % liegt.

Wir würden also über die 1000 Bilder iterieren, um die Gewichte und Verzerrungen zu trainieren. Wir machen die Gewichte und Verzerrungen jedes Mal korrekter, wenn wir ihm ein neues Bild zum Lernen geben.

Ein Batch-Training-Ergebnis soll in 10 Neuronen widergespiegelt werden. Hier repräsentieren die 10 Neuronen die Zahlen von 0 bis 9, und ihr Wert liegt im Bereich von 0 bis 1, um anzuzeigen, wie sicher sie sich bezüglich ihrer Genauigkeit sind.

Und die Eingabe besteht aus 784 Neuronen. Wie können wir 784 Neuronen auf 10 Neuronen reduzieren? Hier ist die Sache. Nehmen wir an, wir haben zwei Schichten. Was bedeutet die Schicht? Das ist die erste Schicht, wir haben 784 Neuronen. In der zweiten Schicht haben wir 10 Neuronen.

Wir geben jedem Neuron in den 784 Neuronen ein Gewicht, sagen wir,

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

Und geben Sie der ersten Schicht einen Bias, also $$b_1$$.

Und so ist der Wert für das erste Neuron in der zweiten Schicht:

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

Aber diese Gewichte und ein Bias sind für $$neuron^2_{1}$$ (das erste Neuron in der zweiten Schicht). Für $$neuron^2_{2}$$ benötigen wir einen weiteren Satz von Gewichten und einen Bias.

Wie sieht es mit der Sigmoid-Funktion aus? Wir verwenden die Sigmoid-Funktion, um den obigen Wert auf einen Bereich von 0 bis 1 abzubilden.

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

Wir verwenden auch die Sigmoid-Funktion, um die erste Schicht zu aktivieren. Dadurch ändern wir den Graustufenwert in den Bereich von 0 bis 1. Jetzt hat also jedes Neuron in jeder Schicht einen Wert zwischen 0 und 1.

Für unser zweischichtiges Netzwerk hat die erste Schicht also 784 Neuronen und die zweite Schicht 10 Neuronen. Wir trainieren es, um die Gewichte und Bias-Werte zu erhalten.

Wir haben 784 * 10 Gewichte und 10 Bias-Werte. In der zweiten Schicht verwenden wir für jedes Neuron 784 Gewichte und 1 Bias-Wert, um seinen Wert zu berechnen. Der Code hier sieht so aus:

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

*Hinweis: Der Code wurde nicht übersetzt, da es sich um einen Python-Codeblock handelt, der in der Regel nicht übersetzt wird.*

## Feedforward

> Feedforward: Für jedes l=2,3,…,L berechne $$z^{l} = w^l a^{l-1}+b^l$$ und $$a^{l} = \sigma(z^{l})$$

Beachten Sie hier, dass wir den Wert der letzten Schicht, also $$a^{l-1}$$, und das Gewicht der aktuellen Schicht, $$w^l$$, sowie dessen Bias $$b^l$$ verwenden, um die Sigmoid-Funktion anzuwenden und den Wert der aktuellen Schicht, $$a^{l}$$, zu erhalten.

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
## Ausgabe-Fehler

> Ausgabefehler $$\delta^{L}$$: Berechne den Vektor $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

Schauen wir uns an, was das $$\nabla$$ bedeutet.

> Del, oder Nabla, ist ein Operator, der in der Mathematik (insbesondere in der Vektoranalysis) als vektorieller Differentialoperator verwendet wird und üblicherweise durch das Nabla-Symbol ∇ dargestellt wird.

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

Hier ist $$\eta $$ die Lernrate. Wir verwenden die Ableitung, die C in Bezug auf die Gewichte und den Bias darstellt, also die Änderungsrate zwischen ihnen. Dies ist `sigmoid_prime` im Folgenden.

Code:

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

(Beachten Sie, dass der Code in der Übersetzung unverändert bleibt, da es sich um eine Programmiersprache handelt und diese in der Regel nicht übersetzt wird.)

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

*Hinweis: Der Code wurde nicht übersetzt, da es sich um eine Programmiersprache handelt, die in der Regel nicht übersetzt wird.*

## Fehler rückwärts propagieren

> Fehler rückpropagieren: Für jedes l=L−1,L−2,…,2, berechne $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

(Der Code bleibt auf Englisch, da es sich um eine Programmiersprache handelt und die Übersetzung den Code unbrauchbar machen würde.)

## Ausgabe

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

## Abschließend

Es ist ein kurzer Artikel. Und zum größten Teil zeigt er nur den Code und mathematische Formeln. Aber das ist in Ordnung für mich. Bevor ich ihn geschrieben habe, habe ich nicht alles klar verstanden. Nachdem ich ihn geschrieben oder einfach Ausschnitte aus dem Code und dem Buch kopiert habe, verstehe ich das meiste davon. Nachdem ich durch das Vertrauen des Lehrers Yin Wang gestärkt wurde, etwa 30% des Buches *Neural Networks and Deep Learning* gelesen, die Vorlesungen von Andrej Karpathy an der Stanford University und die Kurse von Andrew Ng gehört, mit meinem Freund Qi diskutiert und mit Anaconda, numpy und den Theano-Bibliotheken herumgespielt habe, um den Code von vor Jahren zum Laufen zu bringen, verstehe ich es jetzt.

Einer der Schlüsselpunkte sind die Dimensionen. Wir sollten die Dimensionen jedes Symbols und jeder Variablen kennen. Und es führt lediglich die differenzierbare Berechnung durch. Lassen Sie uns mit einem Zitat von Yin Wang enden:

> Maschinelles Lernen ist wirklich nützlich, man könnte sogar sagen, es ist eine schöne Theorie, weil es im Grunde nichts anderes ist als Kalkül nach einer Verwandlung! Es ist die alte und großartige Theorie von Newton und Leibniz, aber in einer einfacheren, eleganten und kraftvolleren Form. Maschinelles Lernen ist im Wesentlichen die Anwendung von Kalkül, um Funktionen abzuleiten und anzupassen, und Deep Learning ist das Anpassen von komplexeren Funktionen.

> Es gibt keine „Intelligenz“ in der künstlichen Intelligenz, kein „Neuronales“ in neuronalen Netzen, kein „Lernen“ im maschinellen Lernen und keine „Tiefe“ im Deep Learning. Was in diesem Bereich wirklich funktioniert, nennt sich „Analysis“. Daher ziehe ich es vor, dieses Feld als „differenzierbare Berechnung“ zu bezeichnen, und den Prozess des Modellbaus als „differenzierbare Programmierung“.