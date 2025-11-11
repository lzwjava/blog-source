---
audio: false
generated: false
lang: de
layout: post
title: Maschinelles Lernen, Deep Learning und GPT
translated: true
type: note
---

1. Machine Learning (ML) ist ein Bereich der Informatik, der es Systemen ermöglicht, aus Daten zu lernen und ihre Leistung ohne explizite Programmierung zu verbessern.

2. Deep Learning (DL) ist ein Teilgebiet des ML, das mehrschichtige neuronale Netze verwendet, um komplexe Muster in Daten zu modellieren.

3. Neuronale Netze sind Rechenmodelle, die vom menschlichen Gehirn inspiriert sind und aus miteinander verbundenen Knoten (Neuronen) bestehen, die Informationen in Schichten verarbeiten.

4. Trainingsdaten sind der gelabelte oder ungelabelte Datensatz, der verwendet wird, um einem Machine-Learning-Modell beizubringen, wie es eine Aufgabe ausführt.

5. Supervised Learning beinhaltet das Trainieren eines Modells auf gelabelten Daten, wobei jedes Beispiel eine Eingabe und einen zugehörigen korrekten Ausgabewert hat.

6. Unsupervised Learning verwendet ungelabelte Daten, sodass das Modell verborgene Muster oder Gruppierungen ohne explizite Anweisung entdecken kann.

7. Reinforcement Learning (RL) trainiert Agenten, Entscheidungen zu treffen, indem erwünschtes Verhalten belohnt und unerwünschtes bestraft wird.

8. Generative Modelle lernen, neue Daten zu erzeugen, die ihren Trainingsbeispielen ähneln (z.B. Text, Bilder).

9. Diskriminative Modelle konzentrieren sich darauf, Eingaben in Kategorien einzuteilen oder spezifische Ergebnisse vorherzusagen.

10. Transfer Learning ermöglicht es, ein für eine Aufgabe trainiertes Modell für eine verwandte Aufgabe wiederzuverwenden oder feinzutunen.

11. GPT (Generative Pre-trained Transformer) ist eine Familie großer Sprachmodelle, die von OpenAI entwickelt wurden und menschenähnlichen Text generieren können.

12. ChatGPT ist eine interaktive Variante von GPT, die für Konversationen und Aufgaben zur Befolgung von Anweisungen feingetunt wurde.

13. Die Transformer-Architektur wurde im Paper "Attention Is All You Need" eingeführt und revolutionierte die natürliche Sprachverarbeitung durch die Verlassenschaft auf Aufmerksamkeitsmechanismen.

14. Self-Attention-Mechanismen ermöglichen es dem Modell, verschiedene Teile der Eingabesequenz bei der Konstruktion einer Ausgabedarstellung unterschiedlich zu gewichten.

15. Positional Encoding in Transformern hilft dem Modell, die Reihenfolge der Tokens in einer Sequenz zu identifizieren.

16. Pre-training ist die anfängliche Phase, in der ein Modell allgemeine Merkmale aus großen Datenmengen lernt, bevor es auf spezifische Aufgaben feingetunt wird.

17. Fine-tuning ist der Prozess, bei dem ein vortrainiertes Modell genommen und mit einem kleineren, aufgabenspezifischen Datensatz an eine speziellere Aufgabe angepasst wird.

18. Language Modeling ist die Aufgabe, den nächsten Token (Wort oder Subwort) in einer Sequenz vorherzusagen; sie ist grundlegend für GPT-ähnliche Modelle.

19. Zero-shot Learning ermöglicht es einem Modell, Aufgaben ohne explizite Trainingsbeispiele zu bewältigen, indem es auf erlerntes Allgemeinwissen zurückgreift.

20. Few-shot Learning nutzt eine begrenzte Anzahl aufgabenspezifischer Beispiele, um Modellvorhersagen oder -verhalten zu steuern.

21. RLHF (Reinforcement Learning from Human Feedback) wird verwendet, um Modellausgaben an menschliche Präferenzen und Werte anzupassen.

22. Human Feedback kann Rankings oder Labels umfassen, die die Generierung des Modells in Richtung erwünschterer Antworten lenken.

23. Prompt Engineering ist die Kunst, Eingabeanfragen oder Anweisungen so zu formulieren, dass große Sprachmodelle effektiv geführt werden.

24. Context Window bezieht sich auf die maximale Textmenge, die das Modell auf einmal verarbeiten kann; GPT-Modelle haben eine begrenzte Kontextlänge.

25. Inference ist die Phase, in der ein trainiertes Modell bei neuen Eingaben Vorhersagen trifft oder Ausgaben generiert.

26. Die Parameteranzahl ist ein Schlüsselfaktor für die Modellkapazität; größere Modelle können komplexere Muster erfassen, benötigen aber mehr Rechenleistung.

27. Model-Compression-Techniken (z.B. Pruning, Quantization) verringern die Größe eines Modells und beschleunigen die Inferenz bei minimalem Genauigkeitsverlust.

28. Attention Heads in Transformatoren verarbeiten verschiedene Aspekte der Eingabe parallel und verbessern so die Darstellungskraft.

29. Masked Language Modeling (z.B. in BERT) beinhaltet das Vorhersagen fehlender Tokens in einem Satz, was dem Modell hilft, Kontext zu lernen.

30. Causal Language Modeling (z.B. in GPT) beinhaltet das Vorhersagen des nächsten Tokens basierend auf allen vorherigen Tokens.

31. Die Encoder-Decoder-Architektur (z.B. T5) verwendet ein Netzwerk zum Kodieren der Eingabe und ein anderes, um sie in eine Zielsequenz zu dekodieren.

32. Convolutional Neural Networks (CNNs) sind hervorragend geeignet für die Verarbeitung gitterartiger Daten (z.B. Bilder) über Faltungsschichten.

33. Recurrent Neural Networks (RNNs) verarbeiten sequentielle Daten, indem sie versteckte Zustände entlang der Zeitschritte weitergeben, können jedoch mit langfristigen Abhängigkeiten kämpfen.

34. Long Short-Term Memory (LSTM) und GRU sind RNN-Varianten, die entwickelt wurden, um Abhängigkeiten über lange Distanzen besser zu erfassen.

35. Batch Normalization hilft, das Training zu stabilisieren, indem sie die Ausgaben zwischengeschalteter Schichten normalisiert.

36. Dropout ist eine Regularisierungstechnik, die während des Trainings Neuronen zufällig "ausblendet", um Overfitting zu verhindern.

37. Optimizer-Algorithmen wie Stochastic Gradient Descent (SGD), Adam und RMSProp aktualisieren Modellparameter basierend auf Gradienten.

38. Die Learning Rate ist ein Hyperparameter, der bestimmt, wie drastisch die Gewichte während des Trainings aktualisiert werden.

39. Hyperparameter (z.B. Batch-Größe, Anzahl der Schichten) sind Konfigurationseinstellungen, die vor dem Training gewählt werden, um zu steuern, wie das Lernen abläuft.

40. Model Overfitting tritt auf, wenn ein Modell die Trainingsdaten zu gut lernt und sich nicht auf neue Daten verallgemeinern lässt.

41. Regularizationstechniken (z.B. L2-Gewichtsdecay, Dropout) helfen, Overfitting zu reduzieren und die Generalisierung zu verbessern.

42. Der Validation Set wird verwendet, um Hyperparameter abzustimmen, während der Test Set die endgültige Leistung des Modells bewertet.

43. Cross-validation teilt Daten in mehrere Teilmengen auf, trainiert und validiert systematisch, um eine robustere Leistungsschätzung zu erhalten.

44. Gradient Exploding und Vanishing Probleme treten in tiefen Netzen auf und machen das Training instabil oder ineffektiv.

45. Residual Connections (Skip Connections) in Netzen wie ResNet helfen, das Verschwinden von Gradienten zu mildern, indem sie Datenpfade abkürzen.

46. Scaling Laws legen nahe, dass eine Erhöhung der Modellgröße und der Datenmenge im Allgemeinen zu einer besseren Leistung führt.

47. Compute Efficiency ist kritisch; das Training großer Modelle erfordert optimierte Hardware (GPUs, TPUs) und Algorithmen.

48. Ethische Überlegungen umfassen Bias, Fairness und potenziellen Schaden – ML-Modelle müssen sorgfältig getestet und überwacht werden.

49. Data Augmentation erweitert Trainingsdatensätze künstlich, um die Robustheit des Modells zu verbessern (besonders bei Bild- und Sprachaufgaben).

50. Data Preprocessing (z.B. Tokenisierung, Normalisierung) ist essenziell für effektives Modelltraining.

51. Tokenisierung teilt Text in Tokens (Wörter oder Subwörter) auf, die grundlegenden Einheiten, die von Sprachmodellen verarbeitet werden.

52. Vector Embeddings repräsentieren Tokens oder Konzepte als numerische Vektoren und bewahren semantische Beziehungen.

53. Positional Embeddings fügen Informationen über die Position jedes Tokens hinzu, um einem Transformer zu helfen, die Sequenzreihenfolge zu verstehen.

54. Attention Weights zeigen, wie ein Modell den Fokus auf verschiedene Teile der Eingabe verteilt.

55. Beam Search ist eine Decoding-Strategie in Sprachmodellen, die bei jedem Schritt mehrere Kandidatenausgaben beibehält, um die beste Gesamtsequenz zu finden.

56. Greedy Search wählt bei jedem Schritt den wahrscheinlichsten Token aus, kann aber zu suboptimalen Endergebnissen führen.

57. Temperature beim Sampling passt die Kreativität der Sprachgeneration an: höhere Temperatur = mehr Zufälligkeit.

58. Top-k und Top-p (Nucleus) Sampling-Methoden schränken die Kandidatentokens auf die k wahrscheinlichsten oder eine kumulative Wahrscheinlichkeit p ein und balancieren so Vielfalt und Kohärenz.

59. Perplexity misst, wie gut ein Wahrscheinlichkeitsmodell eine Stichprobe vorhersagt; niedrigere Perplexity zeigt eine bessere Vorhersageleistung an.

60. Precision und Recall sind Metriken für Klassifikationsaufgaben, die sich jeweils auf Korrektheit und Vollständigkeit konzentrieren.

61. Der F1-Score ist das harmonische Mittel aus Precision und Recall und vereint beide Metriken in einem einzigen Wert.

62. Accuracy ist der Anteil der korrekten Vorhersagen, kann aber bei unausgeglichenen Datensätzen irreführend sein.

63. Area Under the ROC Curve (AUC) misst die Leistung eines Klassifikators über verschiedene Schwellenwerte hinweg.

64. Die Confusion Matrix zeigt die Anzahl der True Positives, False Positives, False Negatives und True Negatives.

65. Uncertainty-Estimation-Methoden (z.B. Monte Carlo Dropout) schätzen ab, wie sicher ein Modell in seinen Vorhersagen ist.

66. Active Learning beinhaltet das Abfragen neuer Datenbeispiele, bei denen das Modell am unsichersten ist, und verbessert so die Dateneffizienz.

67. Online Learning aktualisiert das Modell inkrementell, wenn neue Daten eintreffen, anstatt von Grund auf neu zu trainieren.

68. Evolutionary Algorithms und Genetic Algorithms optimieren Modelle oder Hyperparameter mittels bio-inspirierter Mutation und Selektion.

69. Bayesian Methods integrieren Vorwissen und aktualisieren Überzeugungen mit eingehenden Daten; nützlich für die Unsicherheitsquantifizierung.

70. Ensemble Methods (z.B. Random Forest, Gradient Boosting) kombinieren mehrere Modelle, um Leistung und Stabilität zu verbessern.

71. Bagging (Bootstrap Aggregating) trainiert mehrere Modelle auf verschiedenen Teilmengen der Daten und mittelt dann ihre Vorhersagen.

72. Boosting trainiert iterativ neue Modelle, um Fehler zu korrigieren, die von zuvor trainierten Modellen gemacht wurden.

73. Gradient Boosted Decision Trees (GBDTs) sind leistungsstark für strukturierte Daten und übertreffen oft einfache neuronale Netze.

74. Autoregressive Models sagen den nächsten Wert (oder Token) basierend auf vorherigen Ausgaben in einer Sequenz vorher.

75. Autoencoder ist ein neuronales Netz, das entwickelt wurde, um Daten in eine latente Darstellung zu kodieren und dann zurück zu dekodieren, und so komprimierte Datenrepräsentationen lernt.

76. Variational Autoencoder (VAE) führt eine probabilistische Wendung ein, um neue Daten zu generieren, die dem Trainingsset ähneln.

77. Generative Adversarial Network (GAN) lässt einen Generator gegen einen Diskriminator antreten und erzeugt realistische Bilder, Texte oder andere Daten.

78. Self-Supervised Learning nutzt große Mengen ungelabelter Daten, indem es künstliche Trainingsaufgaben erstellt (z.B. das Vorhersagen fehlender Teile).

79. Foundation Models sind große vortrainierte Modelle, die an eine Vielzahl von Downstream-Aufgaben angepasst werden können.

80. Multimodal Learning integriert Daten aus mehreren Quellen (z.B. Text, Bilder, Audio), um reichhaltigere Repräsentationen zu erstellen.

81. Data Labeling ist oft der zeitaufwändigste Teil des ML und erfordert eine sorgfältige Annotation für Genauigkeit.

82. Edge Computing bringt ML-Inferenz näher an die Datenquelle, reduziert Latenz und Bandbreitennutzung.

83. Federated Learning trainiert Modelle über dezentralisierte Geräte oder Server hinweg, die lokale Datenproben halten, ohne diese auszutauschen.

84. Privacy-Preserving ML umfasst Techniken wie Differential Privacy und Homomorphic Encryption, um sensible Daten zu schützen.

85. Explainable AI (XAI) zielt darauf ab, die Entscheidungen komplexer Modelle für Menschen interpretierbarer zu machen.

86. Bias und Fairness im ML benötigen sorgfältige Überwachung, da Modelle unbeabsichtigt gesellschaftliche Vorurteile lernen und verstärken können.

87. Concept Drift tritt auf, wenn sich die statistischen Eigenschaften der Zielvariable im Laufe der Zeit ändern und sich auf die Modellleistung auswirken.

88. AB Testing vergleicht zwei oder mehr Versionen eines Modells, um zu sehen, welche in einer realen Umgebung besser abschneidet.

89. GPU-Beschleunigung nutzt paralleles Rechnen auf Grafikkarten, um das ML-Training drastisch zu beschleunigen.

90. TPUs (Tensor Processing Units) sind spezialisierte Hardwarebeschleuniger von Google für effiziente Deep-Learning-Workloads.

91. Open-Source-Frameworks (z.B. TensorFlow, PyTorch) bieten Bausteine und Tools für die ML-Modellentwicklung.

92. Model Serving ist die Praxis, trainierte Modelle so bereitzustellen, dass sie Echtzeit- oder Batch-Vorhersagen verarbeiten können.

93. Skalierbarkeit ist entscheidend für die Handhabung großer Datensätze oder hohen Datenverkehrs und erfordert verteilte Trainings- und Inferenzstrategien.

94. MLOps kombiniert ML-Entwicklung mit Operations-Praktiken und konzentriert sich auf Reproduzierbarkeit, Testing und Continuous Integration.

95. Version Control für Daten und Modelle gewährleistet konsistentes Experiment-Tracking und Zusammenarbeit.

96. Deployment-Strategien (z.B. Container, Microservices) organisieren, wie Modelle verpackt und im großen Maßstab bereitgestellt werden.

97. Monitoring verfolgt die Modellleistung nach dem Deployment und beobachtet sie auf Verschlechterungen oder Anomalien.

98. Retraining und Model Updates halten Modelle aktuell, wenn neue Daten und sich ändernde Bedingungen auftreten.

99. Time Complexity (O-Notation) misst, wie sich die Laufzeit eines Algorithmus mit der Eingabegröße skaliert; O(1) bezeichnet konstante Zeit.

100. Die Zukunft des ML verspricht zunehmend ausgefeilte und allgemeine Modelle, muss jedoch ethische, soziale und ökologische Überlegungen adressieren.