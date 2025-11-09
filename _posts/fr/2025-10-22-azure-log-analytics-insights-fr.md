---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Azure Log Analytics contre Azure Insights
translated: true
type: note
---

Bonne question — ils sont **étroitement liés**, mais **pas identiques**. Détaillons cela clairement.

---

### **1. Azure Log Analytics**

**Azure Log Analytics** est un **outil/service** au sein d'**Azure Monitor** qui vous permet de **collecter, interroger et analyser les journaux** de vos ressources cloud et locales.

* Il stocke les journaux dans un **espace de travail Log Analytics**.
* Vous pouvez exécuter des requêtes en utilisant le **Langage de Requête Kusto (KQL)** pour analyser les données.
* Il est utilisé pour :

  * Résoudre des problèmes
  * Investiguer les performances
  * Surveiller la sécurité
  * Créer des tableaux de bord et des alertes personnalisés

Considérez Log Analytics comme le **data lake et le moteur de requête** pour toutes vos données de journaux dans Azure.

---

### **2. Azure Insights**

**Azure Insights** (souvent vu sous forme d'**Application Insights** ou **Azure Monitor Insights**) fait partie du même écosystème de surveillance, mais se concentre davantage sur la **surveillance au niveau de l'application** plutôt que sur les journaux bruts.

Il existe différents types d'"Insights" :

* **Application Insights** — surveille les applications (APM) : performances, exceptions, dépendances, comportement des utilisateurs, etc.
* **VM Insights**, **Container Insights**, **Network Insights** — fournissent des vues de surveillance préconfigurées pour des types de ressources spécifiques.

Tous ces Insights **stockent leur télémétrie et leurs métriques dans des espaces de travail Log Analytics**, ils **reposent donc sur Log Analytics en arrière-plan**.

---

### **3. Relation**

* **Azure Insights = couche de visualisation et de surveillance intelligente**
* **Log Analytics = stockage des journaux et moteur de requête sous-jacent**

En bref :

> Log Analytics est l'*endroit* où les données résident et sont analysées.
> Insights sont la *façon* dont vous visualisez et interprétez ces données pour des types de ressources spécifiques.

---

### **Exemple**

Si vous activez **Application Insights** sur une application web :

* Il collecte la télémétrie (requêtes, dépendances, traces, exceptions).
* Ces données sont stockées dans **un espace de travail Log Analytics**.
* Vous pouvez utiliser **Log Analytics** pour exécuter des requêtes KQL sur ces mêmes données pour une analyse personnalisée plus poussée.

---

Souhaitez-vous que je montre un simple **exemple KQL** de la façon dont Log Analytics interroge les données d'Application Insights ?