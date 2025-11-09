---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Alternativen zu Python Diagram-as-Code-Tools
translated: true
type: note
---

Hier sind Python-freundliche Optionen (neben Graphviz und NetworkX), die das Erstellen von Software-Design-/Architekturdiagrammen unkompliziert machen. Ich habe sie nach Anwendungsfall gruppiert und kurze Anmerkungen sowie kleine Beispiele hinzugefügt.

Diagram-as-Code (UML, C4, Flussdiagramme, Sequenzen)
- PlantUML (über python-plantuml oder lokale JAR)
  - Ideal für UML: Klasse, Sequenz, Komponente, Zustand, Aktivität, Deployment.
  - Funktioniert gut in CI und mit Dokumentation.
  - Beispiel:
    @startuml
    class User
    class Order
    User "1" --> "*" Order
    @enduml
- Mermaid (CLI oder Kroki-Server verwenden; Python kann den Renderer aufrufen)
  - Einfache Syntax für Sequenz, Klasse, Flussdiagramm, ER, Zustand usw.
  - Wird in vielen Dokumentationstools und Wikis gut dargestellt.
  - Beispiel:
    flowchart LR
      API --> DB
- BlockDiag-Familie (blockdiag, seqdiag, actdiag, nwdiag)
  - Reine Python-Tools zum Erstellen von Block-, Sequenz-, Aktivitäts- und Netzwerkdiagrammen aus einfachem Text.
  - Beispiel (seqdiag):
    seqdiag {
      Client -> API [label = "GET /users"];
      API -> DB [label = "query"];
    }
- Structurizr (C4-Modell; Community Python-Client)
  - Modelliert Softwarearchitektur (Kontext, Container, Komponente) und rendert über Structurizr/PlantUML.
  - Stärke bei Architekturdokumentation mit mehreren Ansichten und ADR-Workflows.
- Kroki (Diagram-as-a-Service; Python-Client verfügbar)
  - Rendert viele DSLs (PlantUML, Mermaid, Graphviz, BPMN usw.) über eine einzige HTTP-API aus Python.

Cloud- und Infrastrukturarchitektur
- Diagrams (von mingrammer)
  - Diagram-as-Code für Cloud-/Systemarchitektur mit offiziellen Provider-Icons (AWS, Azure, GCP, K8s, On-Premise).
  - Sehr beliebt für Architekturübersichten.
  - Beispiel:
    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    with Diagram("Web Service", show=False):
        EC2("api") >> RDS("db")

Interaktive Netzwerk-/Graph-Visualisierungen (praktisch für Systemkarten, Abhängigkeiten)
- PyVis (vis.js)
  - Minimaler Code, um interaktive HTML-Graphen zu erstellen.
  - Beispiel:
    from pyvis.network import Network
    net = Network(); net.add_nodes(["API","DB"]); net.add_edge("API","DB"); net.show("arch.html")
- Dash Cytoscape / ipycytoscape (Cytoscape.js)
  - Für interaktive, anpassbare Graphen in Dash-Apps oder Jupyter. Gut zum Erkunden von Abhängigkeiten und Flüssen.
- Plotly
  - Erstellt interaktive Node-Link-Diagramme mit benutzerdefiniertem Styling; einfach einzubetten/zu teilen.
- Bokeh / HoloViews
  - Interaktive Plotting mit Netzwerkunterstützung; gut für Python-zentrierte Dashboards.
- python-igraph
  - Schnelle Graph-Bibliothek mit integriertem Plotting; geeignet, wenn Layout-Algorithmen plus exportierbare Diagramme benötigt werden.

Dokumentationsintegrationen (Diagramme nah an der Dokumentation halten)
- Sphinx-Erweiterungen: sphinxcontrib-plantuml, sphinxcontrib-mermaid, sphinxcontrib-blockdiag
  - Schreibe Diagramme inline in reStructuredText/Markdown und baue sie in deinem Dokumentations-Pipeline.
- MkDocs-Plugins (für Mermaid/PlantUML)
  - Praktisch für moderne statische Seiten.

Code- und Architektur-Reverse-Engineering
- pylints pyreverse
  - Erzeugt UML-Klassen- und Paketdiagramme aus Python-Code (rendert oft über Graphviz, aber der Workflow ist einfach).
- pydeps
  - Erstellt Import-/Abhängigkeitsgraphen von Python-Paketen, praktisch für Architekturkarten in großen Codebasen.

Spezialisierte Diagramme
- SchemDraw
  - Programmatische Schaltkreis-/Logik-/Flussdiagramme in Python; saubere Vektorausgabe.
- railroad-diagrams
  - Erzeugt Syntax-/Grammatikdiagramme (nützlich für Protokoll-/Spezifikationsdokumentation).

Tipps zur Auswahl
- Schnelle UML/Sequenz-Dokumentation: PlantUML oder Mermaid.
- Cloud-/Systemarchitektur-Poster: Diagrams (mingrammer).
- Interaktive Erkundung und Sharing: PyVis oder Dash Cytoscape.
- C4-Modell und lebendige Architekturdokumentation: Structurizr (mit PlantUML/Mermaid via Export).
- Auto-Diagramme aus Code: pyreverse, pydeps.

Wenn du mir deine Ziel-Diagrammtypen (UML-Klasse, Sequenz, C4, Cloud, Datenfluss, Paketabhängigkeiten) und das Ausgabeformat (PNG/SVG/HTML/embedded in docs) nennst, kann ich ein minimales Setup und eine Startvorlage vorschlagen.