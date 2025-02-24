---
audio: false
lang: de
layout: post
title: Visualisieren Abhängigkeiten
translated: true
---

Um die Maven-Abhängigkeitsgrafik zu visualisieren, die durch das bereitgestellte Python-Skript generiert wird, können Sie **Graphviz** verwenden, ein weit verbreitetes und einfaches grafisches Tool, das Graphen rendert, die in der DOT-Sprache beschrieben sind. Das Skript gibt einen Abhängigkeitsgraphen im DOT-Format aus, der Abhängigkeiten zwischen Modulen innerhalb Ihres Maven-Projekts als gerichteten Graphen darstellt, wobei die Knoten durch `artifactId`s und die Kanten Abhängigkeitsbeziehungen gekennzeichnet sind. Im Folgenden sind die Schritte zur Zeichnung und Visualisierung dieses Graphen mit Graphviz aufgeführt, zusammen mit Hinweisen auf alternative Tools wie Polyglot oder andere, falls Sie unterschiedliche Optionen bevorzugen.

---

### Verwendung von Graphviz (Empfohlene Vorgehensweise)

Graphviz ist hier ideal, weil das Skript direkt DOT-Format-Ausgabe generiert, die Graphviz nativ unterstützt. Folgen Sie diesen Schritten:

1. **Skript ausführen**
   Führen Sie das Python-Skript aus und geben Sie das Stammverzeichnis Ihres Maven-Projekts als Argument an. Dies generiert die DOT-Ausgabe für den Abhängigkeitsgraphen.
   ```bash
   python script.py /pfad/zu/maven/projekt
   ```

2. **DOT-Ausgabe in eine Datei speichern**
   Leiten Sie die Ausgabe des Skripts in eine Datei um, z.B. `dependencies.dot`. Diese Datei wird die Graphbeschreibung im DOT-Format enthalten.
   ```bash
   python script.py /pfad/zu/maven/projekt > dependencies.dot
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
   Verwenden Sie den `dot`-Befehl von Graphviz, um die DOT-Datei in ein Bild umzuwandeln. Zum Beispiel, um eine PNG-Datei zu erstellen:
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   - Sie können `-Tpng` durch andere Formate wie `-Tsvg` für SVG oder `-Tpdf` für PDF ersetzen, je nach Ihren Vorlieben.

5. **Graph anzeigen**
   Öffnen Sie die generierte `dependencies.png`-Datei mit einem beliebigen Bildbetrachter, um den Abhängigkeitsgraphen zu sehen. Jeder Knoten wird ein Modul-`artifactId` darstellen und Pfeile werden Abhängigkeiten zwischen Modulen anzeigen.

---

### Alternative Tools

Wenn Sie Graphviz nicht verwenden möchten oder andere gängige grafische Tools ausprobieren möchten, hier sind einige Optionen:

#### Polyglot Notebooks (z.B. mit Jupyter)
Polyglot Notebooks visualisieren DOT-Dateien nicht direkt, aber Sie können Graphviz in einer Jupyter-Notebook-Umgebung integrieren:
- **Schritte**:
  1. Installieren Sie Graphviz und das `graphviz`-Python-Paket:
     ```bash
     pip install graphviz
     sudo apt-get install graphviz  # Für Ubuntu, anpassen für Ihr OS
     ```
  2. Ändern Sie das Skript, um die Python-Bibliothek `graphviz` anstelle von rohem DOT zu verwenden. Fügen Sie dies am Ende Ihres Skripts hinzu:
     ```python
     from graphviz import Digraph

     dot = Digraph()
     for from_module, to_module in sorted(dependencies):
         dot.edge(from_module, to_module)
     dot.render('dependencies', format='png', view=True)
     ```
  3. Führen Sie das geänderte Skript aus, um `dependencies.png` direkt zu generieren und anzuzeigen.
- **Hinweis**: Dies setzt weiterhin Graphviz unter der Haube ein, sodass es kein vollständig separates Tool ist.

#### Gephi
Gephi ist ein Open-Source-Netzwerkvisualisierungstool, das DOT-Dateien importieren kann:
- **Schritte**:
  1. Laden Sie Gephi von [gephi.org](https://gephi.org/) herunter und installieren Sie es.
  2. Führen Sie das Skript aus und speichern Sie die DOT-Ausgabe in `dependencies.dot`.
  3. Öffnen Sie Gephi, gehen Sie zu `Datei > Importieren > Graph-Datei` und wählen Sie `dependencies.dot` aus.
  4. Passen Sie das Layout (z.B. ForceAtlas 2) an und visualisieren Sie es interaktiv.
- **Vorteile**: Großartig für große Graphen mit fortschrittlichen Layout-Optionen.
- **Nachteile**: Erfordert manuelles Importieren und Einrichten.

#### Online Graphviz Tools
Für eine schnelle, installationsfreie Option:
- **Schritte**:
  1. Führen Sie das Skript aus und kopieren Sie die DOT-Ausgabe (von `digraph G {` bis `}`).
  2. Besuchen Sie ein Online-Tool wie [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/).
  3. Fügen Sie den DOT-Inhalt ein und klicken Sie zum Rendern des Graphen.
- **Vorteile**: Keine Installation erforderlich.
- **Nachteile**: Erfordert Internetzugang; weniger Kontrolle über das Ausgabeformat.

#### yEd
yEd ist ein kostenloser Graph-Editor, unterstützt DOT jedoch nicht nativ:
- **Schritte**:
  1. Konvertieren Sie die DOT-Datei in GraphML oder ein anderes unterstütztes Format mit einem Tool wie `dot` (z.B. `dot -Tgraphml dependencies.dot -o dependencies.graphml`).
  2. Öffnen Sie yEd, importieren Sie die GraphML-Datei und passen Sie das Layout an.
- **Nachteile**: Zusätzlicher Konvertierungsschritt erforderlich.

---

### Warum Graphviz hier am besten ist
Die Ausgabe des Skripts ist für DOT optimiert, was Graphviz zur direktesten und effizientesten Wahl macht. Es ist leichtgewichtig, command-line-gesteuert und weit unterstützt. Der generierte Graph wird in etwa so aussehen (konzeptuell):
- Knoten: `artifactId` jedes Moduls (z.B. `"modul-a"`, `"modul-b"`).
- Kanten: Pfeile wie `"modul-a" -> "modul-b"`, die zeigen, dass `modul-a` von `modul-b` abhängt.

Wenn Ihr Graph groß ist, können Sie das Layout mit Graphviz-Optionen anpassen (z.B. `dot -Kneato` für eine andere Anordnung), aber die grundlegenden Schritte oben sollten ausreichen.

---

### Endgültige Empfehlung
Um den Maven-Abhängigkeitsgraphen aus Ihrem Skript zu visualisieren:
1. Ausführen: `python script.py /pfad/zu/maven/projekt > dependencies.dot`
2. Installieren Sie Graphviz, falls erforderlich.
3. Konvertieren Sie in ein Bild: `dot -Tpng dependencies.dot -o dependencies.png`
4. Öffnen Sie `dependencies.png`, um Ihren Graphen zu betrachten.

Dieser Ansatz ist einfach, verwendet ein gängiges Tool (Graphviz) und passt perfekt zur Ausgabe Ihres Skripts. Wenn Sie Interaktivität oder alternative Formate benötigen, probieren Sie Gephi oder ein Online-Tool aus.