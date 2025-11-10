---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: NetzwerkX und Matplotlib Graph Tutorial
translated: true
type: note
---

### Installation der Bibliotheken
Um NetworkX und Matplotlib zum Zeichnen von Diagrammen zu verwenden, installieren Sie diese bei Bedarf:
- NetworkX: Verarbeitet die Erstellung und Manipulation von Graphen.
- Matplotlib: Bietet Plotting-Fähigkeiten.

Installation via pip:
```bash
pip install networkx matplotlib
```

Für schnelleres Rendering empfiehlt Matplotlib die Installation von NumPy (`pip install numpy`).

### Grundlegende Einrichtung und Beispiel
1. **Bibliotheken importieren**:  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **Einen Graphen erstellen**:  
   Verwenden Sie NetworkX, um einen einfachen ungerichteten Graphen zu erstellen (kann mit gerichteten Graphen, gewichteten Kanten usw. angepasst werden):
   ```python
   G = nx.Graph()  # Erstellt einen leeren Graphen
   G.add_nodes_from([1, 2, 3, 4, 5])  # Knoten hinzufügen (z.B. 5 Knoten)
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # Kanten hinzufügen (Verbindungen)
   ```

3. **Diagramm zeichnen und anzeigen**:  
   Verwenden Sie das Backend von Matplotlib für die Visualisierung:
   ```python
   nx.draw(G, with_labels=True)  # Zeichnet den Graphen mit Knotenbeschriftungen
   plt.show()  # Zeigt die Grafik an
   ```

Dies erzeugt ein grundlegendes kreisförmiges Layout des Graphen (ein Zyklus mit 5 Knoten).

### Erweiterte Anpassungen
- **Layouts**: Steuern Sie die Knotenpositionen (z.B. zufällig, Spring-Layout):
  ```python
  pos = nx.spring_layout(G)  # Kraftbasiertes Layout für realistische Netzwerke
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("Netzwerkdiagramm")
  plt.show()
  ```
- **Knoten- und Kantenstile**: Passen Sie das Erscheinungsbild an:
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **Gerichtete Graphen**: Für hierarchische Beziehungen verwenden Sie `nx.DiGraph`.
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **Diagramm speichern**: Exportieren Sie in eine Datei anstatt es anzuzeigen:
  ```python
  plt.savefig('diagram.png')
  ```

### Tipps und Ressourcen
- NetworkX-Dokumentation (networkx.org) für Graphentypen wie Bäume oder Gitter.
- Matplotlib-Dokumentation (matplotlib.org) für das Einbetten in GUIs oder Untergrafiken.
- Für große Graphen (>100 Knoten) verwenden Sie `nx.draw_networkx` oder externe Tools wie Graphviz für bessere Leistung.
- Experimentieren Sie in einem Jupyter Notebook für interaktives Plotten. Falls Probleme auftreten, stammen häufige Fehler von fehlenden Backends (installieren Sie z.B. via `pip install pyqt5` für interaktive Fenster).