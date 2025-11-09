---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Outils de diagrammes au-delà de Graphviz et NetworkX
translated: true
type: note
---

Excellentes alternatives à Graphviz et NetworkX, classées selon votre méthode de travail préférée.

**Textuel/DSL « les diagrammes comme du code »**
- **PlantUML** : UML complet (séquence, classe, composant, déploiement), modèle C4, activité ; écosystème énorme.
- **Mermaid** : Syntaxe légère de type Markdown ; excellent pour les organigrammes, séquences, classes, MER, états ; rendu natif sur GitHub/GitLab.
- **D2 (par Terrastruct)** : DSL de diagramme généraliste et épuré avec un bon auto-agencement ; prend en charge les calques et les grands diagrammes.
- **Structurizr (C4)** : Approche « model-first » (C4) avec un DSL ; exporte vers PlantUML/Mermaid ; idéal pour la documentation d'architecture.
- **C4-PlantUML** : Modèles C4 basés sur PlantUML.
- **nomnoml** : Syntaxe minimale, pour des esquisses rapides de classes et de relations.
- **Kroki** : Serveur qui rend de nombreux DSL (PlantUML, Mermaid, Graphviz) pour les pipelines de documentation.

**Code-first (générer des diagrammes à partir du code/IaC)**
- **diagrams (mingrammer, Python)** : Diagrammes d'architecture cloud programmatiques (AWS/Azure/GCP/K8s).
- **Aides Terraform** : Inframap (dessine à partir de l'état), Blast Radius (graphes interactifs à partir de Terraform).
- **AWS CDK** : cdk-dia pour les diagrammes d'architecture à partir des applications CDK.
- **Librairies Go/TS** : GoDiagrams (Go), ts-graphviz (TypeScript) pour la génération basée sur le code.

**Librairies de visualisation web (graphes interactifs)**
- **Cytoscape.js** : Visualisation de grands graphes, algorithmes de mise en page, bonnes performances.
- **D3.js** : Puissant mais de plus bas niveau pour des visuels de graphes/diagrammes personnalisés.
- **vis-network (vis.js)** : Création facile de graphes de réseau avec simulation physique.
- **Sigma.js** : Rendu rapide pour les grands graphes.
- **ECharts** : Bibliothèque de graphiques généraux avec un module graphe ; résultats rapides.
- **pyvis (Python)** : Création simple de graphes de réseau interactifs via Vis.js.

**Outils de diagramme GUI (glisser-déposer)**
- **diagrams.net (draw.io)** : Gratuit, facile, grandes bibliothèques de formes (UML, icônes cloud).
- **yEd/yFiles** : Excellent auto-agencement ; yFiles est un SDK commercial, yEd est un logiciel gratuit.
- **Lucidchart/Miro** : Outils web collaboratifs ; adaptés aux équipes.
- **OmniGraffle (macOS), Visual Paradigm, StarUML, Enterprise Architect** : Outils pour UML/architecture.

**Outils spécifiques à l'architecture et au domaine**
- **Modèle C4** : Structurizr, C4-PlantUML, extensions Mermaid C4.
- **SaaS d'architecture cloud** : Cloudcraft (AWS), Hava, Lucidscale, CloudSkew ; importation depuis le cloud/l'IaC.
- **BPMN/Processus** : Camunda Modeler, bpmn.io.
- **Séquence/chronogrammes** : WebSequenceDiagrams, WaveDrom (diagrammes de timing).
- **Diagrammes MER/BDD** : dbdiagram.io, SchemaSpy.

**Choix rapides par scénario**
- **Docs-as-code en Markdown/README** : Mermaid.
- **UML complet + C4 avec templates** : PlantUML ou Structurizr.
- **Architecture cloud à partir du code/IaC** : diagrams (Python), Inframap/Blast Radius (Terraform), cdk-dia (AWS CDK).
- **Graphes interactifs pour application web** : Cytoscape.js ou vis-network ; pour de la visualisation personnalisée, D3.js.
- **Dessin GUI rapide** : diagrams.net (draw.io) ; pour l'auto-agencement, yEd.

Si vous partagez vos préférences (texte vs GUI, images statiques vs interactives, langages utilisés et types de diagrammes comme séquence/C4/cloud/MER), je peux vous recommander une liste restreinte et des modèles de démarrage.