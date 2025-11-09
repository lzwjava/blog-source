---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Karate Test Framework Architekturvisualisierung
translated: true
type: note
---

```python
import networkx as nx
import matplotlib.pyplot as plt

# Versuche Graphviz für ein saubereres Layout zu verwenden, falls verfügbar; andernfalls Fallback auf spring_layout.
def get_layout(G):
    try:
        # Versuche PyGraphviz
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # Versuche pydot
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # Fallback: Spring-Layout
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# Definiere Knoten, gruppiert nach Kategorie
nodes = {
    # Authoring
    "Feature-Dateien (.feature)": "Authoring",
    "Wiederverwendbare Features (call/read)": "Authoring",
    "karate-config.js / properties": "Authoring",
    "Testdaten (JSON/CSV)": "Authoring",

    # Execution
    "Runner (CLI/JUnit5/Maven/Gradle)": "Execution",
    "Parallel Runner": "Execution",

    # Runtime
    "Karate Engine (DSL Interpreter)": "Runtime",
    "JS Engine": "Runtime",
    "Variablen/Kontext": "Runtime",
    "Assertions & Matchers": "Runtime",

    # Protocols / IO
    "HTTP/REST/SOAP/GraphQL": "Protocols",
    "WebSocket": "Protocols",
    "UI-Treiber (web)": "Protocols",
    "Mock Server": "Protocols",

    # External
    "Externe Systeme/Services": "External",

    # Reporting
    "Reports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# Füge Knoten mit Kategorie-Attribut hinzu
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# Definiere Kanten (u -> v) mit optionalen Beschriftungen
edges = [
    # Authoring zu Execution
    ("Feature-Dateien (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "execute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Testdaten (JSON/CSV)", "Feature-Dateien (.feature)", "data-driven"),
    ("Wiederverwendbare Features (call/read)", "Feature-Dateien (.feature)", "reuse"),

    # Execution zu Runtime
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Parallel Runner", "optional"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Karate Engine (DSL Interpreter)", "invoke"),
    ("Parallel Runner", "Karate Engine (DSL Interpreter)", "parallelize"),

    # Runtime internals
    ("Karate Engine (DSL Interpreter)", "JS Engine", "script expressions"),
    ("Karate Engine (DSL Interpreter)", "Variablen/Kontext", "manage state"),

    # Engine zu Protocols
    ("Karate Engine (DSL Interpreter)", "HTTP/REST/SOAP/GraphQL", "call APIs"),
    ("Karate Engine (DSL Interpreter)", "WebSocket", "send/receive"),
    ("Karate Engine (DSL Interpreter)", "UI-Treiber (web)", "drive UI"),
    ("Karate Engine (DSL Interpreter)", "Mock Server", "start/stub"),

    # Protocols zu External Systems
    ("HTTP/REST/SOAP/GraphQL", "Externe Systeme/Services", "requests"),
    ("WebSocket", "Externe Systeme/Services", "messages"),
    ("UI-Treiber (web)", "Externe Systeme/Services", "browser/app"),
    ("Mock Server", "Externe Systeme/Services", "simulate"),

    # Responses fließen zurück zur Engine
    ("Externe Systeme/Services", "Karate Engine (DSL Interpreter)", "responses"),

    # Assertions und Reporting
    ("Karate Engine (DSL Interpreter)", "Assertions & Matchers", "verify"),
    ("Assertions & Matchers", "Reports (HTML, JUnit, JSON)", "results"),
    ("Karate Engine (DSL Interpreter)", "Reports (HTML, JUnit, JSON)", "runtime logs"),
    ("Reports (HTML, JUnit, JSON)", "CI/CD", "publish"),
]

# Füge Kanten zum Graphen hinzu
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Farben pro Kategorie
category_colors = {
    "Authoring": "#4C78A8",
    "Execution": "#F58518",
    "Runtime": "#B279A2",
    "Protocols": "#54A24B",
    "External": "#9A9A9A",
    "Reporting": "#E45756",
}

# Erstelle Farbliste für Knoten
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# Berechne Layout
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# Zeichne Knoten
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# Zeichne Kanten
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# Zeichne Beschriftungen
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# Zeichne eine Teilmenge der Kantenbeschriftungen, um Unübersichtlichkeit zu vermeiden
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"execute", "invoke", "parallelize", "call APIs", "start/stub", "verify", "results", "publish"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# Legende
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("Wie das Karate Test Framework funktioniert (High-Level Flow)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

Was dieses Diagramm vermittelt:
- **Authoring**: Sie schreiben .feature-Dateien, können andere Features wiederverwenden, konfigurieren via karate-config und füttern Daten ein.
- **Execution**: Sie führen Tests via CLI/JUnit5/Maven/Gradle aus, optional parallel.
- **Runtime**: Die Karate Engine interpretiert die DSL, verwendet eine JS Engine für Ausdrücke und verwaltet den Szenario-Zustand.
- **Protocols/IO**: Die Engine steuert HTTP (REST/SOAP/GraphQL), WebSocket und UI (via Karate's Treiber). Sie kann auch einen Mock Server starten, um Abhängigkeiten zu simulieren.
- **Externe Systeme**: Echte Services oder gemockte Services antworten.
- **Reporting**: Assertions produzieren Reports (HTML, JUnit XML, JSON), die Ihr CI/CD veröffentlichen kann.

Wenn Sie das Diagramm auf einen bestimmten Ausschnitt zugeschnitten haben möchten (z.B. nur API-Tests oder Betonung von Mocks oder UI), teilen Sie mir dies mit und ich passe die Knoten/Kanten an.