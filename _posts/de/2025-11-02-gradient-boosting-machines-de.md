---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Vorstellung von Gradient Boosting Machines
translated: true
type: note
---

### Übersicht
Das 2001er Papier *"Greedy Function Approximation: A Gradient Boosting Machine"* von Jerome H. Friedman stellt Gradient Boosting Machines (GBMs) vor, eine leistungsstarke Ensemble-Lernmethode für überwachte Aufgaben wie Regression und Klassifikation. Es formuliert Boosting als eine Form des funktionalen Gradientenabstiegs, bei dem sequenziell einfache "schwache" Lerner (oft Entscheidungsbäume) zu einem additiven Modell hinzugefügt werden, um eine spezifizierte Verlustfunktion zu minimieren. Dieser Ansatz verallgemeinert frühere Boosting-Algorithmen (z.B. AdaBoost) und betont gierige Optimierung im Funktionsraum, was zu hochpräzisen, robusten und interpretierbaren Modellen führt.

### Abstrakt (Paraphrasiert)
GBMs erstellen flexible prädiktive Modelle, indem sie schwache Lerner sequenziell und additiv kombinieren, um den Minimierer einer differenzierbaren Verlustfunktion zu approximieren. Die Verwendung von Regressionsbäumen als Basis-Lerner ergibt wettbewerbsfähige, robuste Verfahren für Regression und Klassifikation. Die Methode übertrifft in empirischen Tests Alternativen wie multivariate adaptive Regressions-Splines (MARS) und weist niedrige Fehlerraten über diverse Datensätze hinweg auf.

### Schlüsselmethoden
Die Kernidee ist es, iterativ neue Lerner an den *negativen Gradienten* (Pseudo-Residuen) der Verlustfunktion bezüglich der Vorhersagen des aktuellen Modells anzupassen, was einem Gradientenabstieg im Funktionsraum entspricht.

- **Modellstruktur**: Das finale Modell ist \\( F_M(x) = \sum_{m=1}^M \beta_m h_m(x) \\), wobei jedes \\( h_m(x) \\) ein schwacher Lerner ist (z.B. ein kleiner Regressionsbaum).
- **Aktualisierungsregel**: In Iteration \\( m \\), berechne Residuen \\( r_{im} = -\left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]_{F=F_{m-1}} \\), passe dann \\( h_m \\) via Methode der kleinsten Quadrate an diese Residuen an. Die Schrittweite \\( \gamma_m \\) wird durch Liniensuche optimiert: \\( \gamma_m = \arg\min_\gamma \sum_i L(y_i, F_{m-1}(x_i) + \gamma h_m(x_i)) \\).
- **Shrinkage**: Skaliere die Additionen mit \\( \nu \in (0,1] \\) (z.B. \\( \nu = 0.1 \\)), um Overfitting zu reduzieren und mehr Iterationen zu ermöglichen.
- **Stochastische Variante**: Ziehe bei jedem Schritt eine Stichprobe der Daten (z.B. 50%) für schnellere Training und bessere Generalisierung.
- **TreeBoost-Algorithmus** (Pseudocode-Übersicht):
  1. Initialisiere \\( F_0(x) \\) als die Konstante, die den Verlust minimiert.
  2. Für \\( m = 1 \\) bis \\( M \\):
     - Berechne Pseudo-Residuen \\( r_{im} \\).
     - Passe Baum \\( h_m \\) an \\( \{ (x_i, r_{im}) \} \\) an.
     - Finde optimales \\( \gamma_m \\) via Liniensuche.
     - Aktualisiere \\( F_m(x) = F_{m-1}(x) + \nu \gamma_m h_m(x) \\).
  3. Stoppe basierend auf Iterationen oder Verlustverbesserung.

Unterstützte Verlustfunktionen beinhalten:
- Methode der kleinsten Quadrate (Regression): \\( L(y, F) = \frac{1}{2}(y - F)^2 \\), Residuen = \\( y - F \\).
- Minimale absolute Abweichung (robuste Regression): \\( L(y, F) = |y - F| \\).
- Log-Likelihood (binäre Klassifikation): \\( L = -\sum [y \log p + (1-y) \log(1-p)] \\), mit \\( p = \frac{1}{1 + e^{-F}} \\); Residuen = \\( y - p \\).
- Huber-Verlust (ausreißerrobust).

Varianten wie LogitBoost passen dies für spezifische Verlustfunktionen an (z.B. binomial deviance).

### Beiträge
- **Vereinheitlichtes Framework**: Erweitert Boosting auf beliebige differenzierbare Verlustfunktionen via Gradienten, vereinheitlicht AdaBoost (exponentieller Verlust) und LogitBoost.
- **Praktische Verbesserungen**: Führt Shrinkage und stochastisches Subsampling ein, um Overfitting und Rechenaufwand besser zu kontrollieren.
- **Flexibilität**: Funktioniert mit verschiedenen Basis-Lernern und Aufgaben (Regression, Klassifikation, Ranking); Bäume ermöglichen effiziente Handhabung hochdimensionaler Daten.
- **Interpretierbarkeitswerkzeuge**: Diskutiert Variablenwichtigkeit (via gesamter Unreinheitsreduktion) und partielle Abhängigkeitsplots.

### Hauptergebnisse
- **Leistung**: GBMs zeichnen sich empirisch aus und reduzieren Fehlerraten um 10-50% gegenüber Baseline-Methoden wie einzelnen Bäumen, Bagging, neuronalen Netzen und MARS auf realen Datensätzen (z.B. Finanzen, Physiksimulationen).
- **Robustheit**: Stochastisches GBM konvergiert schneller; tiefere Bäume (6-8 Ebenen) erhöhen die Genauigkeit, benötigen aber Regularisierung. LAD/Huber-Verluste mildern Ausreißer besser als die Methode der kleinsten Quadrate.
- **Effizienz**: Schnell für große Daten; optimale Setups verwenden \\( \nu = 0.1 \\), 1000+ Iterationen und Subsampling.
- Plots zeigen schnelle Verlustkonvergenz und niedrige Varianz/Bias im Vergleich zu Alternativen.

Dieses Papier legte den Grundstein für moderne Implementierungen wie XGBoost und LightGBM.

### Referenzen
- [Greedy Function Approximation: A Gradient Boosting Machine (PDF)](https://jerryfriedman.su.domains/ftp/trebst.pdf)