---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Diagrammwerkzeuge jenseits von Graphviz und NetworkX
translated: true
type: note
---

Große Auswahl jenseits von Graphviz und NetworkX, gruppiert nach bevorzugter Arbeitsweise.

Text/DSL – „Diagrams as Code“
- PlantUML: Vollständiges UML (Sequenz, Klasse, Komponente, Deployment), C4-Modell, Aktivität; riesiges Ökosystem.
- Mermaid: Leichte, Markdown-ähnliche Syntax; ideal für Flussdiagramme, Sequenz, Klasse, ER, Zustand; native Darstellung auf GitHub/GitLab.
- D2 (von Terrastruct): Saubere, allgemeine Diagramm-DSL mit gutem Auto-Layout; unterstützt Ebenen und große Diagramme.
- Structurizr (C4): Modell-zuerst (C4) mit einer DSL; Export nach PlantUML/Mermaid; gut für Architekturdokumente.
- C4-PlantUML: C4-Modell-Vorlagen auf Basis von PlantUML.
- nomnoml: Minimale Syntax, schnelle Skizzen für Klassen/Beziehungen.
- Kroki: Server, der viele DSLs (PlantUML, Mermaid, Graphviz) für Dokumentations-Pipelines rendert.

Code-First (Diagramme aus Code/IaC generieren)
- diagrams (mingrammer, Python): Programmatische Cloud-Architekturdiagramme (AWS/Azure/GCP/K8s).
- Terraform-Helfer: Inframap (Zeichnen aus State), Blast Radius (interaktive Graphen aus Terraform).
- AWS CDK: cdk-dia für Architekturdiagramme aus CDK-Apps.
- Go/TS-Bibliotheken: GoDiagrams (Go), ts-graphviz (TypeScript) für code-basierte Generierung.

Web-Visualisierungsbibliotheken (interaktive Graphen)
- Cytoscape.js: Visualisierung großer Graphen, Layout-Algorithmen, gute Performance.
- D3.js: Leistungsstark, aber Low-Level für benutzerdefinierte Graph-/Diagrammvisualisierungen.
- vis-network (vis.js): Einfache Netzwerkgraphen mit Physik-Engine.
- Sigma.js: Schnelles Rendering für große Graphen.
- ECharts: Allgemeine Diagramme mit Graph-Modul; schnelle Ergebnisse.
- pyvis (Python): Einfache, interaktive Netzwerkgraphen über Vis.js.

GUI-Diagrammtools (Drag-and-Drop)
- diagrams.net (draw.io): Kostenlos, einfach, große Schablonen (UML, Cloud-Icons).
- yEd/yFiles: Großartiges Auto-Layout; yFiles ist kommerzielles SDK, yEd ist kostenlose Desktop-App.
- Lucidchart/Miro: Kollaborative Web-Tools; gut für Teams.
- OmniGraffle (macOS), Visual Paradigm, StarUML, Enterprise Architect: UML-/Architektur-Tooling.

Architektur-spezifische und Domänen-Tools
- C4-Modell: Structurizr, C4-PlantUML, Mermaid C4-Erweiterungen.
- Cloud-Architektur SaaS: Cloudcraft (AWS), Hava, Lucidscale, CloudSkew; Import aus Cloud/IaC.
- BPMN/Prozess: Camunda Modeler, bpmn.io.
- Sequenz/Timing: WebSequenceDiagrams, WaveDrom (Timing-Diagramme).
- ER/Datenbankdiagramme: dbdiagram.io, SchemaSpy.

Schnellauswahl nach Szenario
- Docs-as-Code in Markdown/READMEs: Mermaid.
- Vollständiges UML + C4 mit Vorlagen: PlantUML oder Structurizr.
- Cloud-Architektur aus Code/IaC: diagrams (Python), Inframap/Blast Radius (Terraform), cdk-dia (AWS CDK).
- Interaktive Web-App-Graphen: Cytoscape.js oder vis-network; für benutzerdefinierte Visuals, D3.js.
- Schnelles GUI-Zeichnen: diagrams.net (draw.io); für Auto-Layout, yEd.

Wenn Sie Ihre Präferenzen mitteilen (Text vs. GUI, statische Bilder vs. interaktiv, verwendete Sprachen und Diagrammtypen wie Sequenz/C4/Cloud/ER), kann ich eine kurze Liste und Starter-Vorlagen empfehlen.