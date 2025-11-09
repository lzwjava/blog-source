---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Architecture de Visualisation du Framework de Test Karate
translated: true
type: note
---

Voici un script Python autonome qui utilise NetworkX et Matplotlib pour dessiner une architecture/flux de haut niveau illustrant le fonctionnement du framework de test Karate. Il regroupe les composants par rôle (rédaction, exécution, runtime, protocoles/ES, systèmes externes et reporting), et montre le flux typique depuis les fichiers feature à travers le moteur vers les protocoles et le reporting.

Instructions :
- pip install networkx matplotlib
- Optionnellement, installez pygraphviz ou pydot + graphviz si vous voulez une disposition plus propre ; le script détecte automatiquement et utilise un layout spring en repli.

Code :

```python
import networkx as nx
import matplotlib.pyplot as plt

# Essaye d'utiliser Graphviz pour une disposition plus propre si disponible ; sinon, utilise spring_layout.
def get_layout(G):
    try:
        # Essaye PyGraphviz
        from networkx.drawing.nx_agraph import graphviz_layout
        return graphviz_layout(G, prog="dot")
    except Exception:
        try:
            # Essaye pydot
            from networkx.drawing.nx_pydot import graphviz_layout
            return graphviz_layout(G, prog="dot")
        except Exception:
            # Repli : layout spring
            return nx.spring_layout(G, k=1.2, seed=42)

G = nx.DiGraph()

# Définit les nœuds groupés par catégorie
nodes = {
    # Rédaction
    "Fichiers feature (.feature)": "Rédaction",
    "Fonctionnalités réutilisables (call/read)": "Rédaction",
    "karate-config.js / properties": "Rédaction",
    "Données de test (JSON/CSV)": "Rédaction",

    # Exécution
    "Runner (CLI/JUnit5/Maven/Gradle)": "Exécution",
    "Runner parallèle": "Exécution",

    # Runtime
    "Moteur Karate (interpréteur DSL)": "Runtime",
    "Moteur JS": "Runtime",
    "Variable/contexte": "Runtime",
    "Assertions & matchers": "Runtime",

    # Protocoles / ES
    "HTTP/REST/SOAP/GraphQL": "Protocoles",
    "WebSocket": "Protocoles",
    "Pilote UI (web)": "Protocoles",
    "Serveur mock": "Protocoles",

    # Externe
    "Systèmes/services externes": "Externe",

    # Reporting
    "Rapports (HTML, JUnit, JSON)": "Reporting",
    "CI/CD": "Reporting",
}

# Ajoute les nœuds avec l'attribut catégorie
for n, cat in nodes.items():
    G.add_node(n, category=cat)

# Définit les arêtes (u -> v) avec libellés optionnels
edges = [
    # Rédaction vers Exécution
    ("Fichiers feature (.feature)", "Runner (CLI/JUnit5/Maven/Gradle)", "exécute"),
    ("karate-config.js / properties", "Runner (CLI/JUnit5/Maven/Gradle)", "configure"),
    ("Données de test (JSON/CSV)", "Fichiers feature (.feature)", "piloté par les données"),
    ("Fonctionnalités réutilisables (call/read)", "Fichiers feature (.feature)", "réutilise"),

    # Exécution vers Runtime
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Runner parallèle", "optionnel"),
    ("Runner (CLI/JUnit5/Maven/Gradle)", "Moteur Karate (interpréteur DSL)", "invoque"),
    ("Runner parallèle", "Moteur Karate (interpréteur DSL)", "parallélise"),

    # Interne au Runtime
    ("Moteur Karate (interpréteur DSL)", "Moteur JS", "expressions script"),
    ("Moteur Karate (interpréteur DSL)", "Variable/contexte", "gère l'état"),

    # Moteur vers protocoles
    ("Moteur Karate (interpréteur DSL)", "HTTP/REST/SOAP/GraphQL", "appelle les APIs"),
    ("Moteur Karate (interpréteur DSL)", "WebSocket", "envoie/reçoit"),
    ("Moteur Karate (interpréteur DSL)", "Pilote UI (web)", "pilote l'UI"),
    ("Moteur Karate (interpréteur DSL)", "Serveur mock", "démarre/simule"),

    # Protocoles vers systèmes externes
    ("HTTP/REST/SOAP/GraphQL", "Systèmes/services externes", "requêtes"),
    ("WebSocket", "Systèmes/services externes", "messages"),
    ("Pilote UI (web)", "Systèmes/services externes", "navigateur/app"),
    ("Serveur mock", "Systèmes/services externes", "simule"),

    # Réponses remontant vers le moteur
    ("Systèmes/services externes", "Moteur Karate (interpréteur DSL)", "réponses"),

    # Assertions et reporting
    ("Moteur Karate (interpréteur DSL)", "Assertions & matchers", "vérifie"),
    ("Assertions & matchers", "Rapports (HTML, JUnit, JSON)", "résultats"),
    ("Moteur Karate (interpréteur DSL)", "Rapports (HTML, JUnit, JSON)", "logs runtime"),
    ("Rapports (HTML, JUnit, JSON)", "CI/CD", "publie"),
]

# Ajoute les arêtes au graphe
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Couleurs par catégorie
category_colors = {
    "Rédaction": "#4C78A8",
    "Exécution": "#F58518",
    "Runtime": "#B279A2",
    "Protocoles": "#54A24B",
    "Externe": "#9A9A9A",
    "Reporting": "#E45756",
}

# Construit la liste de couleurs pour les nœuds
node_colors = [category_colors[G.nodes[n]["category"]] for n in G.nodes()]

# Calcule la disposition
pos = get_layout(G)

plt.figure(figsize=(14, 10))
# Dessine les nœuds
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1600, alpha=0.9, linewidths=1.2, edgecolors="black")
# Dessine les arêtes
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>", arrowsize=16, width=1.2, connectionstyle="arc3,rad=0.06")
# Dessine les libellés
nx.draw_networkx_labels(G, pos, font_size=9, font_color="white")

# Dessine un sous-ensemble de libellés d'arêtes pour réduire l'encombrement
important_edge_labels = {
    (u, v): d["label"]
    for u, v, d in G.edges(data=True)
    if d["label"] in {"exécute", "invoque", "parallélise", "appelle les APIs", "démarre/simule", "vérifie", "résultats", "publie"}
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=important_edge_labels, font_size=8, label_pos=0.5, rotate=False)

# Légende
import matplotlib.patches as mpatches
legend_patches = [mpatches.Patch(color=col, label=cat) for cat, col in category_colors.items()]
plt.legend(handles=legend_patches, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.05), frameon=False)

plt.title("Fonctionnement du Framework de Test Karate (Flux de Haut Niveau)", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
```

Ce que ce diagramme communique :
- Rédaction : Vous écrivez des fichiers .feature, pouvez réutiliser d'autres fonctionnalités, configurer via karate-config, et alimenter avec des données.
- Exécution : Vous exécutez via CLI/JUnit5/Maven/Gradle, optionnellement en parallèle.
- Runtime : Le moteur Karate interprète le DSL, utilise un moteur JS pour les expressions et gère l'état du scénario.
- Protocoles/ES : Le moteur pilote HTTP (REST/SOAP/GraphQL), WebSocket et l'UI (via le pilote de Karate). Il peut également démarrer un serveur mock pour simuler les dépendances.
- Systèmes externes : Les services réels ou simulés répondent.
- Reporting : Les assertions produisent des rapports (HTML, JUnit XML, JSON), que votre CI/CD peut publier.

Si vous voulez que le diagramme soit adapté à une partie spécifique (par exemple, seulement les tests API, ou en mettant l'accent sur les mocks ou l'UI), dites-le-moi et j'ajusterai les nœuds/arêtes.