---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Deep-Learning-Buch von Goodfellow Bengio Courville
translated: true
type: note
---

**Ian Goodfellow**  
**Yoshua Bengio**  
**Aaron Courville**

## Inhaltsverzeichnis

- Website viii  
- Danksagungen ix  
- Notation xiii  

### 1 Einführung 1

- 1.1 Für wen ist dieses Buch? 8  
- 1.2 Historische Trends im Deep Learning 12  

## I Angewandte Mathematik und Grundlagen des maschinellen Lernens 27

### 2 Lineare Algebra 29

- 2.1 Skalare, Vektoren, Matrizen und Tensoren 29  
- 2.2 Multiplikation von Matrizen und Vektoren 32  
- 2.3 Einheitsmatrix und inverse Matrizen 34  
- 2.4 Lineare Abhängigkeit und Span 35  
- 2.5 Normen 37  
- 2.6 Besondere Arten von Matrizen und Vektoren 38  
- 2.7 Eigenzerlegung 40  
- 2.8 Singulärwertzerlegung 42  
- 2.9 Die Moore-Penrose-Pseudoinverse 43  
- 2.10 Die Spur einer Matrix 44  
- 2.11 Die Determinante 45  
- 2.12 Beispiel: Hauptkomponentenanalyse 45  

### 3 Wahrscheinlichkeitsrechnung und Informationstheorie 51

- 3.1 Warum Wahrscheinlichkeitsrechnung? 52  
- 3.2 Zufallsvariablen 54  
- 3.3 Wahrscheinlichkeitsverteilungen 54  
- 3.4 Randwahrscheinlichkeit 56  
- 3.5 Bedingte Wahrscheinlichkeit 57  
- 3.6 Die Kettenregel für bedingte Wahrscheinlichkeiten 57  
- 3.7 Unabhängigkeit und bedingte Unabhängigkeit 58  
- 3.8 Erwartungswert, Varianz und Kovarianz 58  
- 3.9 Gängige Wahrscheinlichkeitsverteilungen 60  
- 3.10 Nützliche Eigenschaften gebräuchlicher Funktionen 65  
- 3.11 Satz von Bayes 68  
- 3.12 Technische Details stetiger Variablen 69  
- 3.13 Informationstheorie 71  
- 3.14 Strukturierte probabilistische Modelle 73  

### 4 Numerische Berechnung 78

- 4.1 Overflow und Underflow 78  
- 4.2 Schlechte Konditionierung 80  
- 4.3 Gradientenbasierte Optimierung 80  
- 4.4 Optimierung unter Nebenbedingungen 91  
- 4.5 Beispiel: Lineare Methode der kleinsten Quadrate 94  

### 5 Grundlagen des maschinellen Lernens 96

- 5.1 Lernalgorithmen 97  
- 5.2 Kapazität, Overfitting und Underfitting 108  
- 5.3 Hyperparameter und Validierungsmengen 118  
- 5.4 Schätzer, Bias und Varianz 120  
- 5.5 Maximum-Likelihood-Schätzung 129  
- 5.6 Bayesianische Statistik 133  
- 5.7 Algorithmen für überwachtes Lernen 137  
- 5.8 Algorithmen für unüberwachtes Lernen 142  
- 5.9 Stochastic Gradient Descent 149  
- 5.10 Einen Machine-Learning-Algorithmus entwickeln 151  
- 5.11 Herausforderungen, die Deep Learning motivieren 152  

## II Tiefe Netzwerke: Moderne Praktiken 162

### 6 Tiefe vorwärtsgerichtete Netzwerke 164

- 6.1 Beispiel: Lernen von XOR 167  
- 6.2 Gradientenbasiertes Lernen 172  
- 6.3 Versteckte Einheiten 187  
- 6.4 Architekturentwurf 193  
- 6.5 Backpropagation und andere Differenzierungsalgorithmen 200  
- 6.6 Historische Anmerkungen 220  

### 7 Regularisierung für Deep Learning 224

- 7.1 Parameter-Norm-Strafen 226  
- 7.2 Norm-Strafen als eingeschränkte Optimierung 233  
- 7.3 Regularisierung und unterbestimmte Probleme 235  
- 7.4 Datensatzerweiterung 236  
- 7.5 Rauschrobustheit 238  
- 7.6 Halbüberwachtes Lernen 240  
- 7.7 Multitask-Learning 241  
- 7.8 Early Stopping 241  
- 7.9 Parameter Binding und Parameter Sharing 249  
- 7.10 Sparsity in Darstellungen 251  
- 7.11 Bagging und andere Ensemble-Methoden 253  
- 7.12 Dropout 255  
- 7.13 Adversarial Training 265  
- 7.14 Tangent Distance, Tangent Prop und Manifold Tangent Classifier 267  

### 8 Optimierung für das Training tiefer Modelle 271

- 8.1 Wie sich Lernen von reiner Optimierung unterscheidet 272  
- 8.2 Herausforderungen bei der Optimierung neuronaler Netzwerke 279  
- 8.3 Grundlegende Algorithmen 290  
- 8.4 Strategien zur Parameterinitialisierung 296  
- 8.5 Algorithmen mit adaptiven Lernraten 302  
- 8.6 Approximative Methoden zweiter Ordnung 307  
- 8.7 Optimierungsstrategien und Metaalgorithmen 313  

### 9 Faltungsnetzwerke 326

- 9.1 Die Faltungsoperation 327  
- 9.2 Motivation 329  
- 9.3 Pooling 335  
- 9.4 Faltung und Pooling als unendlich starker Prior 339  
- 9.5 Varianten der grundlegenden Faltungsfunktion 342  
- 9.6 Strukturierte Ausgaben 352  
- 9.7 Datentypen 354  
- 9.8 Effiziente Faltungsalgorithmen 356  
- 9.9 Zufällige oder unüberwachte Merkmale 356  
- 9.10 Die neurowissenschaftliche Basis für Faltungsnetzwerke 358  
- 9.11 Faltungsnetzwerke und die Geschichte des Deep Learning 365  

### 10 Sequenzmodellierung: Rekurrente und rekursive Netze 367

- 10.1 Entfaltung von Berechnungsgraphen 369  
- 10.2 Rekurrente neuronale Netze 372  
- 10.3 Bidirektionale RNNs 388  
- 10.4 Encoder-Decoder Sequence-to-Sequence-Architekturen 390  
- 10.5 Tiefe rekurrente Netzwerke 392  
- 10.6 Rekursive neuronale Netze 394  
- 10.7 Die Herausforderung langfristiger Abhängigkeiten 396  
- 10.8 Echo State Networks 399  
- 10.9 Leaky Units und andere Strategien für multiple Zeitskalen 402  
- 10.10 Long Short-Term Memory und andere gated RNNs 404  
- 10.11 Optimierung für langfristige Abhängigkeiten 408  
- 10.12 Expliziter Speicher 412  

### 11 Praktische Methodik 416

- 11.1 Leistungsmetriken  
- 11.2 Standard-Baselinemodelle  
- 11.3 Entscheidung, ob mehr Daten gesammelt werden sollen  
- 11.4 Auswahl von Hyperparametern  
- 11.5 Debugging-Strategien  
- 11.6 Beispiel: Erkennung mehrstelliger Zahlen  

## III Deep Learning Forschung 482

### 12 Lineare Faktormodelle 485

- 12.1 Probabilistisches PCA und Faktorenanalyse  
- 12.2 Independent Component Analysis (ICA)  
- 12.3 Slow Feature Analysis  
- 12.4 Sparse Coding  
- 12.5 Manifold-Interpretation von PCA  

### 13 Autoencoder 500

- 13.1 Untervollständige Autoencoder  
- 13.2 Regularisierte Autoencoder  
- 13.3 Repräsentationsstärke, Schichtgröße und Tiefe  
- 13.4 Stochastische Encoder und Decoder  
- 13.5 Denoising Autoencoders  
- 13.6 Lernen von Mannigfaltigkeiten mit Autoencodern  
- 13.7 Kontraktive Autoencoder  
- 13.8 Predictive Sparse Decomposition  
- 13.9 Anwendungen von Autoencodern  

### 14 Repräsentationslernen 525

- 14.1 Greedy Layer-Wise Unsupervised Pretraining  
- 14.2 Transfer Learning und Domain Adaptation  
- 14.3 Halbüberwachtes Entwirren kausaler Faktoren  
- 14.4 Distributed Representation  
- 14.5 Exponentielle Gewinne durch Tiefe  
- 14.6 Bereitstellung von Hinweisen zur Entdeckung zugrunde liegender Ursachen  

### 15 Strukturierte probabilistische Modelle für Deep Learning 540

- 15.1 Die Herausforderung unstrukturierter Modellierung  
- 15.2 Verwendung von Graphen zur Beschreibung der Modellstruktur  
- 15.3 Sampling von graphischen Modellen  
- 15.4 Vorteile strukturierter Modellierung  
- 15.5 Lernen von Abhängigkeiten  
- 15.6 Inferenz und approximative Inferenz  
- 15.7 Der Deep-Learning-Ansatz für strukturierte probabilistische Modelle  

### 16 Monte-Carlo-Methoden 557

- 16.1 Sampling und Monte-Carlo-Methoden  
- 16.2 Importance Sampling  
- 16.3 Markov Chain Monte Carlo Methods  
- 16.4 Gibbs Sampling  
- 16.5 Die Herausforderung des Mixings zwischen getrennten Modi  

### 17 Konfrontation mit der Partition Function 567

- 17.1 Der Log-Likelihood-Gradient  
- 17.2 Stochastic Maximum Likelihood und Contrastive Divergence  
- 17.3 Pseudolikelihood  
- 17.4 Score Matching und Ratio Matching  
- 17.5 Denoising Score Matching  
- 17.6 Noise-Contrastive Estimation  
- 17.7 Schätzung der Partition Function  

### 18 Approximative Inferenz 579

- 18.1 Inferenz als Optimierung  
- 18.2 Expectation Maximization  
- 18.3 MAP-Inferenz und Sparse Coding  
- 18.4 Variationelle Inferenz und Lernen  
- 18.5 Gelernte approximative Inferenz  

### 19 Tiefe generative Modelle 594

- 19.1 Boltzmann-Maschinen  
- 19.2 Restricted Boltzmann Machines  
- 19.3 Deep Belief Networks  
- 19.4 Deep Boltzmann Machines  
- 19.5 Boltzmann-Maschinen für reellwertige Daten  
- 19.6 Convolutional Boltzmann Machines  
- 19.7 Boltzmann-Maschinen für strukturierte oder sequentielle Ausgaben  
- 19.8 Andere Boltzmann-Maschinen  
- 19.9 Backpropagation durch zufällige Operationen  
- 19.10 Gerichtete generative Netze  
- 19.11 Ziehen von Stichproben aus Autoencodern  
- 19.12 Generative Stochastic Networks  
- 19.13 Andere Generierungsschemata  
- 19.14 Auswertung generativer Modelle  
- 19.15 Schlussfolgerung  

[Deep Learning Inhaltsverzeichnis](https://www.deeplearningbook.org/contents/toc.html)