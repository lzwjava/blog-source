---
audio: false
generated: true
lang: de
layout: post
title: Entscheidungsbaum
translated: true
type: note
---

Ein **Decision Tree** (Entscheidungsbaum) ist ein Werkzeug des Predictive Modeling, das im Machine Learning und in der Datenanalyse verwendet wird, um Entscheidungen auf der Grundlage von Eingabedaten zu treffen. Er stellt Entscheidungen und ihre möglichen Konsequenzen, einschließlich der Ergebnisse von Zufallsereignissen, in einer baumartigen Struktur dar. Decision Trees werden häufig für Aufgaben wie Klassifikation (z. B. Vorhersage, ob ein Kunde ein Produkt kaufen wird) und Regression (z. B. Vorhersage von Hauspreisen) verwendet. Sie sind intuitiv, leicht zu interpretieren und effektiv für sowohl einfache als auch komplexe Datensätze.

Dieser umfassende Leitfaden erklärt, was ein Decision Tree ist, wie er funktioniert, seine Komponenten, den Konstruktionsprozess, Vorteile, Einschränkungen und praktische Überlegungen, zusammen mit Beispielen.

---

### **Was ist ein Decision Tree?**

Ein Decision Tree ist eine flussdiagrammähnliche Darstellung von Entscheidungen und ihren möglichen Ergebnissen. Er besteht aus Knoten und Verzweigungen:
- **Knoten**: Stellen Entscheidungen, Bedingungen oder Ergebnisse dar.
- **Verzweigungen**: Stellen die möglichen Ergebnisse einer Entscheidung oder Bedingung dar.
- **Blätter**: Stellen die endgültige Ausgabe dar (z. B. ein Klassenlabel für die Klassifikation oder einen numerischen Wert für die Regression).

Decision Trees werden im Supervised Learning verwendet, bei dem das Modell aus gelabelten Trainingsdaten lernt, um Ergebnisse für neue, ungesehene Daten vorherzusagen. Sie sind vielseitig und können sowohl mit kategorialen als auch mit numerischen Daten umgehen.

---

### **Komponenten eines Decision Trees**

1. **Wurzelknoten (Root Node)**:
   - Der oberste Knoten des Baums.
   - Repräsentiert den gesamten Datensatz und den anfänglichen Entscheidungspunkt.
   - Er teilt die Daten basierend auf dem Merkmal auf, das die meisten Informationen liefert oder die Unsicherheit am meisten reduziert.

2. **Innere Knoten (Internal Nodes)**:
   - Knoten zwischen der Wurzel und den Blättern.
   - Stellen Zwischenentscheidungspunkte dar, basierend auf spezifischen Merkmalen und Bedingungen (z. B. "Ist das Alter > 30?").

3. **Verzweigungen (Branches)**:
   - Verbindungen zwischen Knoten.
   - Stellen das Ergebnis einer Entscheidung oder Bedingung dar (z. B. "Ja" oder "Nein" für eine binäre Aufteilung).

4. **Blattknoten (Leaf Nodes)**:
   - Terminalknoten, die die endgültige Ausgabe darstellen.
   - Bei der Klassifikation repräsentieren Blätter Klassenlabels (z. B. "Kaufen" oder "Nicht Kaufen").
   - Bei der Regression repräsentieren Blätter numerische Werte (z. B. einen vorhergesagten Preis).

---

### **Wie funktioniert ein Decision Tree?**

Ein Decision Tree funktioniert, indem er die Eingabedaten rekursiv in Regionen aufteilt, basierend auf Merkmalswerten, und dann eine Entscheidung basierend auf der Mehrheitsklasse oder dem Durchschnittswert in dieser Region trifft. Hier ist eine schrittweise Erklärung, wie er arbeitet:

1. **Eingabedaten**:
   - Der Datensatz enthält Merkmale (unabhängige Variablen) und eine Zielvariable (abhängige Variable).
   - In einem Datensatz zur Vorhersage, ob ein Kunde ein Produkt kaufen wird, könnten die Merkmale beispielsweise Alter, Einkommen und Browse-Zeit sein, wobei das Ziel "Kaufen" oder "Nicht Kaufen" ist.

2. **Aufteilen der Daten**:
   - Der Algorithmus wählt ein Merkmal und einen Schwellenwert (z. B. "Alter > 30"), um die Daten in Teilmengen aufzuspalten.
   - Das Ziel ist es, Aufteilungen zu erstellen, die die Trennung der Klassen (für Klassifikation) maximieren oder die Varianz (für Regression) minimieren.
   - Aufteilungskriterien umfassen Metriken wie **Gini Impurity**, **Information Gain** oder **Variance Reduction** (siehe unten).

3. **Rekursive Aufteilung**:
   - Der Algorithmus wiederholt den Aufteilungsprozess für jede Teilmenge und erstellt neue Knoten und Verzweigungen.
   - Dies wird fortgesetzt, bis ein Stoppkriterium erfüllt ist (z. B. maximale Tiefe, minimale Stichproben pro Knoten oder keine weitere Verbesserung).

4. **Zuweisen von Ausgaben**:
   - Sobald die Aufteilung stoppt, wird jedem Blattknoten eine endgültige Ausgabe zugewiesen.
   - Für die Klassifikation repräsentiert das Blatt die Mehrheitsklasse in dieser Region.
   - Für die Regression repräsentiert das Blatt den Durchschnitt (oder Median) der Zielwerte in dieser Region.

5. **Vorhersage**:
   - Um das Ergebnis für einen neuen Datenpunkt vorherzusagen, durchläuft der Baum von der Wurzel zu einem Blatt und folgt dabei den Entscheidungsregeln basierend auf den Merkmalswerten des Datenpunkts.
   - Der Blattknoten liefert die endgültige Vorhersage.

---

### **Aufteilungskriterien**

Die Qualität einer Aufteilung bestimmt, wie gut der Baum die Daten trennt. Häufige Kriterien sind:

1. **Gini Impurity (Klassifikation)**:
   - Misst die Unreinheit eines Knotens (wie gemischt die Klassen sind).
   - Formel: \( \text{Gini} = 1 - \sum_{i=1}^n (p_i)^2 \), wobei \( p_i \) der Anteil der Klasse \( i \) im Knoten ist.
   - Niedrigere Gini Impurity zeigt eine bessere Aufteilung an (homogenerer Knoten).

2. **Information Gain (Klassifikation)**:
   - Basierend auf **Entropie**, die die Zufälligkeit oder Unsicherheit in einem Knoten misst.
   - Entropie: \( \text{Entropy} = - \sum_{i=1}^n p_i \log_2(p_i) \).
   - Information Gain = Entropie vor der Aufteilung - Gewichtete durchschnittliche Entropie nach der Aufteilung.
   - Höherer Information Gain zeigt eine bessere Aufteilung an.

3. **Variance Reduction (Regression)**:
   - Misst die Reduktion der Varianz der Zielvariable nach einer Aufteilung.
   - Varianz: \( \text{Variance} = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 \), wobei \( y_i \) ein Zielwert und \( \bar{y} \) der Mittelwert ist.
   - Der Algorithmus wählt die Aufteilung, die die Varianzreduktion maximiert.

4. **Chi-Square (Klassifikation)**:
   - Testet, ob die Aufteilung die Verteilung der Klassen signifikant verbessert.
   - Wird in einigen Algorithmen wie CHAID verwendet.

Der Algorithmus bewertet alle möglichen Aufteilungen für jedes Merkmal und wählt diejenige mit der besten Bewertung aus (z. B. niedrigste Gini Impurity oder höchster Information Gain).

---

### **Wie wird ein Decision Tree aufgebaut?**

Der Aufbau eines Decision Trees umfasst die folgenden Schritte:

1. **Wähle das beste Merkmal**:
   - Bewerte alle Merkmale und möglichen Aufteilungspunkte mit dem gewählten Kriterium (z. B. Gini, Information Gain).
   - Wähle das Merkmal und den Schwellenwert, der die Daten am besten trennt.

2. **Teile die Daten**:
   - Teile den Datensatz in Teilmengen basierend auf dem ausgewählten Merkmal und Schwellenwert auf.
   - Erzeuge Kindknoten für jede Teilmenge.

3. **Wiederhole rekursiv**:
   - Wende denselben Prozess auf jeden Kindknoten an, bis eine Stoppbedingung erfüllt ist:
     - Maximale Baumtiefe erreicht.
     - Minimale Anzahl von Stichproben in einem Knoten.
     - Keine signifikante Verbesserung des Aufteilungskriteriums.
     - Alle Stichproben in einem Knoten gehören zur selben Klasse (für Klassifikation) oder haben ähnliche Werte (für Regression).

4. **Beschneide den Baum (Optional)**:
   - Um Overfitting zu verhindern, reduziere die Komplexität des Baums, indem du Verzweigungen entfernst, die wenig zur Vorhersagegenauigkeit beitragen.
   - Das Beschneiden kann **Pre-Pruning** (frühes Stoppen während der Konstruktion) oder **Post-Pruning** (Entfernen von Verzweigungen nach der Konstruktion) sein.

---

### **Beispiel: Klassifikations-Decision Tree**

**Datensatz**: Vorhersage, ob ein Kunde ein Produkt kaufen wird, basierend auf Alter, Einkommen und Browse-Zeit.

| Alter | Einkommen | Browse-Zeit | Kaufen? |
|-------|-----------|-------------|---------|
| 25    | Niedrig   | Kurz        | Nein    |
| 35    | Hoch      | Lang        | Ja      |
| 45    | Mittel    | Mittel      | Ja      |
| 20    | Niedrig   | Kurz        | Nein    |
| 50    | Hoch      | Lang        | Ja      |

**Schritt 1: Wurzelknoten**:
- Bewerte alle Merkmale (Alter, Einkommen, Browse-Zeit) für die beste Aufteilung.
- Angenommen, "Einkommen = Hoch" liefert den höchsten Information Gain.
- Teile die Daten:
  - Einkommen = Hoch: Alle "Ja" (reiner Knoten, stoppe hier).
  - Einkommen = Niedrig oder Mittel: Gemischt (fahre mit Aufteilung fort).

**Schritt 2: Kindknoten**:
- Für die Teilmenge "Niedriges oder mittleres Einkommen" bewerten die verbleibenden Merkmale.
- Angenommen, "Alter > 30" liefert die beste Aufteilung:
  - Alter > 30: Meistens "Ja".
  - Alter ≤ 30: Alle "Nein".

**Schritt 3: Stopp**:
- Alle Knoten sind rein (enthalten nur eine Klasse) oder erfüllen Stoppkriterien.
- Der Baum sieht wie folgt aus:
  - Wurzel: "Ist das Einkommen hoch?"
    - Ja → Blatt: "Kaufen"
    - Nein → "Ist das Alter > 30?"
      - Ja → Blatt: "Kaufen"
      - Nein → Blatt: "Nicht Kaufen"

**Vorhersage**:
- Neuer Kunde: Alter = 40, Einkommen = Mittel, Browse-Zeit = Kurz.
- Pfad: Einkommen ≠ Hoch → Alter = 40 > 30 → Vorhersage "Kaufen".

---

### **Beispiel: Regressions-Decision Tree**

**Datensatz**: Vorhersage von Hauspreisen basierend auf Größe und Lage.

| Größe (m²) | Lage    | Preis (Tsd. $) |
|------------|---------|----------------|
| 1000       | Urban   | 300            |
| 1500       | Suburban| 400            |
| 2000       | Urban   | 600            |
| 800        | Ländlich| 200            |

**Schritt 1: Wurzelknoten**:
- Bewerte Aufteilungen (z. B. Größe > 1200, Lage = Urban).
- Angenommen, "Größe > 1200" minimiert die Varianz.
- Aufteilung:
  - Größe > 1200: Preise = {400, 600} (Mittelwert = 500).
  - Größe ≤ 1200: Preise = {200, 300} (Mittelwert = 250).

**Schritt 2: Stopp**:
- Knoten sind klein genug oder die Varianzreduktion ist minimal.
- Baum:
  - Wurzel: "Größe > 1200?"
    - Ja → Blatt: Vorhersage 500 Tsd. $.
    - Nein → Blatt: Vorhersage 250 Tsd. $.

**Vorhersage**:
- Neues Haus: Größe = 1800, Lage = Urban → Größe > 1200 → Vorhersage 500 Tsd. $.

---

### **Vorteile von Decision Trees**

1. **Interpretierbarkeit**:
   - Leicht zu verstehen und zu visualisieren, ideal um Entscheidungen für nicht-technische Stakeholder zu erklären.
2. **Verarbeitet gemischte Daten**:
   - Funktioniert mit sowohl kategorialen als auch numerischen Merkmalen ohne aufwändige Vorverarbeitung.
3. **Nicht-parametrisch**:
   - Keine Annahmen über die zugrundeliegende Datenverteilung.
4. **Merkmalswichtigkeit**:
   - Identifiziert, welche Merkmale am meisten zu den Vorhersagen beitragen.
5. **Schnelle Vorhersage**:
   - Nach dem Training sind Vorhersagen schnell, da sie einfache Vergleiche beinhalten.

---

### **Einschränkungen von Decision Trees**

1. **Overfitting**:
   - Tiefe Bäume können die Trainingsdaten auswendig lernen, was zu einer schlechten Generalisierung führt.
   - Lösung: Verwende Pruning, begrenze die maximale Tiefe oder setze minimale Stichproben pro Knoten.
2. **Instabilität**:
   - Kleine Änderungen in den Daten können zu völlig anderen Bäumen führen.
   - Lösung: Verwende Ensemble-Methoden wie Random Forests oder Gradient Boosting.
3. **Verzerrung zu dominanten Klassen**:
   - Schwierigkeiten mit unausgeglichenen Datensätzen, bei denen eine Klasse dominiert.
   - Lösung: Verwende Techniken wie Class Weighting oder Oversampling.
4. **Greedy-Ansatz**:
   - Aufteilungen werden basierend auf lokaler Optimierung gewählt, was nicht unbedingt zum global optimalen Baum führt.
5. **Schlechte Handhabung linearer Beziehungen**:
   - Weniger effektiv für Datensätze, bei denen die Beziehungen zwischen Merkmalen und Ziel linear oder komplex sind.

---

### **Praktische Überlegungen**

1. **Hyperparameter**:
   - **Max Depth**: Begrenzt die Tiefe des Baums, um Overfitting zu verhindern.
   - **Min Samples Split**: Minimale Anzahl von Stichproben, die erforderlich sind, um einen Knoten aufzuteilen.
   - **Min Samples Leaf**: Minimale Anzahl von Stichproben in einem Blattknoten.
   - **Max Features**: Anzahl der Merkmale, die für jede Aufteilung berücksichtigt werden.

2. **Pruning**:
   - Pre-Pruning: Setze Einschränkungen während der Baumkonstruktion.
   - Post-Pruning: Entferne Verzweigungen nach dem Aufbau des Baums basierend auf der Validierungsleistung.

3. **Handhabung fehlender Werte**:
   - Einige Algorithmen (z. B. CART) weisen fehlende Werte dem Zweig zu, der den Fehler minimiert.
   - Alternativ: Imputiere fehlende Werte vor dem Training.

4. **Skalierbarkeit**:
   - Decision Trees sind recheneffizient für kleine bis mittlere Datensätze, können aber für sehr große Datensätze mit vielen Merkmalen langsam sein.

5. **Ensemble-Methoden**:
   - Um Einschränkungen zu überwinden, werden Decision Trees oft in Ensembles verwendet:
     - **Random Forest**: Kombiniert mehrere Bäume, die auf zufälligen Teilmengen von Daten und Merkmalen trainiert wurden.
     - **Gradient Boosting**: Baut Bäume sequentiell auf, wobei jeder die Fehler der vorherigen korrigiert.

---

### **Anwendungen von Decision Trees**

1. **Wirtschaft**:
   - Kundenabwanderungsvorhersage, Kreditbewertung, Marketing-Segmentierung.
2. **Gesundheitswesen**:
   - Krankheitsdiagnose, Risikovorhersage (z. B. Herzerkrankungen).
3. **Finanzen**:
   - Betrugserkennung, Kreditausfallvorhersage.
4. **Natural Language Processing**:
   - Textklassifikation (z. B. Sentiment Analysis).
5. **Regressionsaufgaben**:
   - Vorhersage kontinuierlicher Ergebnisse wie Hauspreise oder Umsatzprognosen.

---

### **Visualisierungsbeispiel**

Um zu veranschaulichen, wie ein Decision Tree Daten aufteilt, betrachten wir einen einfachen Klassifikationsdatensatz mit zwei Merkmalen (z. B. Alter und Einkommen) und zwei Klassen (Kaufen, Nicht Kaufen). Unten ist ein konzeptionelles Diagramm, das zeigt, wie der Decision Tree den Merkmalsraum partitioniert.

```
chartjs
{
  "type": "scatter",
  "data": {
    "datasets": [
      {
        "label": "Kaufen",
        "data": [
          {"x": 35, "y": 50000},
          {"x": 45, "y": 60000},
          {"x": 50, "y": 80000}
        ],
        "backgroundColor": "#4CAF50",
        "pointRadius": 6
      },
      {
        "label": "Nicht Kaufen",
        "data": [
          {"x": 20, "y": 20000},
          {"x": 25, "y": 30000}
        ],
        "backgroundColor": "#F44336",
        "pointRadius": 6
      }
    ]
  },
  "options": {
    "scales": {
      "x": {
        "title": { "display": true, "text": "Alter" },
        "min": 15,
        "max": 60
      },
      "y": {
        "title": { "display": true, "text": "Einkommen ($)" },
        "min": 10000,
        "max": 100000
      }
    },
    "plugins": {
      "title": { "display": true, "text": "Decision Tree Merkmalsraum" },
      "legend": { "display": true }
    }
  }
}
```

Dieses Diagramm zeigt die Datenpunkte in einem 2D-Merkmalsraum. Ein Decision Tree könnte diesen Raum aufteilen (z. B. bei Alter = 30 oder Einkommen = 40000), um "Kaufen" von "Nicht Kaufen" zu trennen.

---

### **Implementierung in der Praxis**

Decision Trees können mit Bibliotheken wie diesen implementiert werden:
- **Python**: Scikit-learn (`DecisionTreeClassifier`, `DecisionTreeRegressor`), XGBoost, LightGBM.
- **R**: `rpart`, `party`.
- **Andere Tools**: Weka, MATLAB oder Spark MLlib.

Beispiel in Python (Scikit-learn):
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Beispieldaten
X = [[25, 20000], [35, 50000], [45, 60000], [20, 30000], [50, 80000]]  # Merkmale: Alter, Einkommen
y = [0, 1, 1, 0, 1]  # Labels: 0 = Nicht Kaufen, 1 = Kaufen

# Daten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree trainieren
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Vorhersagen
y_pred = clf.predict(X_test)

# Auswerten
print("Genauigkeit:", accuracy_score(y_test, y_pred))
```

---

### **Schlussfolgerung**

Decision Trees sind leistungsstarke, interpretierbare Modelle für Klassifikations- und Regressionsaufgaben. Sie arbeiten durch rekursive Aufteilung von Daten basierend auf Merkmalsbedingungen und verwenden Kriterien wie Gini Impurity oder Information Gain. Obwohl sie einfach zu verwenden und zu visualisieren sind, können sie overfitten und instabil sein, was oft durch Pruning oder die Verwendung von Ensemble-Methoden wie Random Forests gemildert wird.

Für weitere Erkundungen experimentiere mit Decision Trees unter Verwendung realer Datensätze, optimiere die Hyperparameter und kombiniere sie mit Ensemble-Methoden für eine verbesserte Leistung. Wenn du einen spezifischen Datensatz oder Anwendungsfall im Sinn hast, kann ich ein maßgeschneidertes Beispiel oder eine Visualisierung bereitstellen!