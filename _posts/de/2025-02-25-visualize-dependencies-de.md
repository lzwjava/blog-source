---
audio: false
generated: true
lang: de
layout: post
title: Visualisieren Sie Abhängigkeiten
translated: true
type: note
---

Um den Maven-Abhängigkeitsgraphen zu visualisieren, der durch das bereitgestte Python-Skript generiert wird, können Sie **Graphviz** verwenden, ein weit verbreitetes und unkompliziertes Grafik-Tool, das Graphen rendert, die in der DOT-Sprache beschrieben sind. Das Skript gibt einen Abhängigkeitsgraphen im DOT-Format aus, der Abhängigkeiten zwischen Modulen innerhalb Ihres Maven-Projekts als einen gerichteten Graphen darstellt, wobei Knoten durch `artifactId`s beschriftet sind und Kanten die Abhängigkeitsbeziehungen zeigen. Im Folgenden finden Sie die Schritte, um diesen Graphen mit Graphviz zu zeichnen und zu visualisieren, zusammen mit Erwähnungen alternativer Tools wie Polyglot oder anderen, falls Sie andere Optionen bevorzugen.

---

### Graphviz verwenden (Empfohlener Ansatz)

Graphviz ist hier ideal, weil das Skript direkt eine Ausgabe im DOT-Format erzeugt, das von Graphviz nativ unterstützt wird. Folgen Sie diesen Schritten:

1. **Skript ausführen**  
   Führen Sie das Python-Skript aus und übergeben Sie das Root-Verzeichnis Ihres Maven-Projekts als Argument. Dies generiert die DOT-Ausgabe für den Abhängigkeitsgraphen.
   ```bash
   python script.py /pfad/zum/maven/projekt
   ```

2. **DOT-Ausgabe in einer Datei speichern**  
   Leiten Sie die Ausgabe des Skripts in eine Datei um, zum Beispiel `dependencies.dot`. Diese Datei enthält die Graph-Beschreibung im DOT-Format.
   ```bash
   python script.py /pfad/zum/maven/projekt > dependencies.dot
   ```

3. **Graphviz installieren (falls noch nicht installiert)**  
   Graphviz ist für Windows, macOS und Linux verfügbar. Installieren Sie es mit Ihrem Paketmanager:
   - **Ubuntu/Debian**:  
     ```bash
     sudo apt-get install graphviz
     ```
   - **macOS (mit Homebrew)**:  
     ```bash
     brew install graphviz
     ```
   - **Windows**: Laden Sie es von der [Graphviz-Website](https://graphviz.org/download/) herunter und installieren Sie es.

4. **Ein visuelles Bild generieren**  
   Verwenden Sie den `dot`-Befehl von Graphviz, um die DOT-Datei in ein Bild zu konvertieren. Um zum Beispiel eine PNG-Datei zu erstellen:
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   - Sie können `-Tpng` durch andere Formate wie `-Tsvg` für SVG oder `-Tpdf` für PDF ersetzen, je nach Präferenz.

5. **Den Graphen anzeigen**  
   Öffnen Sie die generierte Datei `dependencies.png` mit einem beliebigen Bildbetrachter, um den Abhängigkeitsgraphen zu sehen. Jeder Knoten repräsentiert die `artifactId` eines Moduls, und Pfeile zeigen die Abhängigkeiten zwischen den Modulen an.

---

### Alternative Tools

Falls Sie Graphviz nicht verwenden möchten oder andere gängige Grafik-Tools erkunden möchten, hier einige Optionen:

#### Polyglot Notebooks (z.B. mit Jupyter)
Polyglot Notebooks visualisieren DOT-Dateien nicht direkt, aber Sie können Graphviz in einer Jupyter Notebook-Umgebung integrieren:
- **Schritte**:
  1. Installieren Sie Graphviz und das `graphviz` Python-Paket:
     ```bash
     pip install graphviz
     sudo apt-get install graphviz  # Für Ubuntu, passen Sie für Ihr Betriebssystem an
     ```
  2. Modifizieren Sie das Skript so, dass es die `graphviz`-Bibliothek von Python verwendet, anstatt rohes DOT auszugeben. Fügen Sie dies am Ende Ihres Skripts hinzu:
     ```python
     from graphviz import Digraph

     dot = Digraph()
     for from_module, to_module in sorted(dependencies):
         dot.edge(from_module, to_module)
     dot.render('dependencies', format='png', view=True)
     ```
  3. Führen Sie das modifizierte Skript aus, um `dependencies.png` direkt zu generieren und anzuzeigen.
- **Hinweis**: Dies basiert weiterhin auf Graphviz, es ist also kein völlig separates Tool.

#### Gephi
Gephi ist ein Open-Source-Tool zur Netzwerkvisualisierung, das DOT-Dateien importieren kann:
- **Schritte**:
  1. Laden Sie Gephi von [gephi.org](https://gephi.org/) herunter und installieren Sie es.
  2. Führen Sie das Skript aus und speichern Sie die DOT-Ausgabe in `dependencies.dot`.
  3. Öffnen Sie Gephi, gehen Sie zu `Datei > Importieren > Graph-Datei` und wählen Sie `dependencies.dot` aus.
  4. Passen Sie das Layout an (z.B. ForceAtlas 2) und visualisieren Sie interaktiv.
- **Vorteile**: Ideal für große Graphen mit erweiterten Layout-Optionen.
- **Nachteile**: Erfordert manuellen Import und Einrichtung.

#### Online Graphviz Tools
Für eine schnelle Option ohne Installation:
- **Schritte**:
  1. Führen Sie das Skript aus und kopieren Sie die DOT-Ausgabe (von `digraph G {` bis `}`).
  2. Besuchen Sie ein Online-Tool wie [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/).
  3. Fügen Sie den DOT-Inhalt ein und klicken Sie, um den Graphen zu rendern.
- **Vorteile**: Keine Installation nötig.
- **Nachteile**: Erfordert Internetzugang; weniger Kontrolle über das Ausgabeformat.

#### yEd
yEd ist ein kostenloser Graph-Editor, unterstützt aber DOT nicht nativ:
- **Schritte**:
  1. Konvertieren Sie die DOT-Datei in GraphML oder ein anderes unterstütztes Format mit einem Tool wie `dot` (z.B. `dot -Tgraphml dependencies.dot -o dependencies.graphml`).
  2. Öffnen Sie yEd, importieren Sie die GraphML-Datei und passen Sie das Layout an.
- **Nachteile**: Zusätzlicher Konvertierungsschritt erforderlich.

---

### Warum Graphviz hier die beste Wahl ist

Die Ausgabe des Skripts ist auf DOT zugeschnitten, was Graphviz zur direktesten und effizientesten Wahl macht. Es ist leichtgewichtig, kommandozeilengesteuert und weitgehend unterstützt. Der generierte Graph wird in etwa so aussehen (konzeptionell):
- Knoten: `artifactId` jedes Moduls (z.B. `"module-a"`, `"module-b"`).
- Kanten: Pfeile wie `"module-a" -> "module-b"`, die zeigen, dass `module-a` von `module-b` abhängt.

Wenn Ihr Graph sehr groß ist, können Sie das Layout mit Graphviz-Optionen anpassen (z.B. `dot -Kneato` für eine andere Anordnung), aber die grundlegenden Schritte oben sollten ausreichen.

---

### Finale Empfehlung

Um den Maven-Abhängigkeitsgraphen aus Ihrem Skript zu visualisieren:
1. Führen Sie aus: `python script.py /pfad/zum/maven/projekt > dependencies.dot`
2. Installieren Sie Graphviz, falls nötig.
3. Konvertieren Sie in ein Bild: `dot -Tpng dependencies.dot -o dependencies.png`
4. Öffnen Sie `dependencies.png`, um Ihren Graphen zu betrachten.

Dieser Ansatz ist einfach, verwendet ein gängiges Tool (Graphviz) und passt perfekt zur Ausgabe Ihres Skripts. Wenn Sie Interaktivität oder alternative Formate benötigen, versuchen Sie es stattdessen mit Gephi oder einem Online-Tool.