---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Limites des LLM dans les flux de travail complexes
translated: true
type: note
---

Vous avez absolument raison ! Les LLM (moi y compris) excellent dans les **petites tâches ciblées**—comme expliquer un concept unique, générer un court extrait de code ou déboguer une erreur spécifique—mais peinent avec les **flux de travail complexes et multi-étapes** qui impliquent :

1.  **De multiples configurations interconnectées** (par exemple, les fichiers Maven `pom.xml`, les arguments de l'agent Jacoco, l'intégration avec des tests Python).
2.  **Des dépendances avec état** (par exemple, "D'abord, mettez à jour `module-A/pom.xml`, puis exécutez `mvn test` avec ces drapeaux, puis fusionnez les rapports").
3.  **Des interactions entre systèmes** (par exemple, Java + Python + outils CI comme Jenkins/GitHub Actions).
4.  **Des changements de contexte** (par exemple, "Maintenant, oubliez la partie Java—comment analyser le XML Jacoco en Python ?").

---

### **Pourquoi les LLM échouent sur les flux de travail complexes**
1.  **Aucune Mémoire Persistante** : Nous ne nous "souvenons" pas des étapes précédentes à moins que vous ne nous le rappeliez explicitement (et même dans ce cas, les fenêtres de contexte sont limitées).
2.  **Pensée Linéaire** : Nous générons des réponses étape par étape mais ne pouvons pas suivre dynamiquement les dépendances (par exemple, "Avez-vous exécuté `mvn clean` avant l'agent ?").
3.  **Sur-Optimisation pour des Réponses Uniques** : Nous sommes entraînés à donner *une* réponse complète, pas un guidage itératif.
4.  **Aucun Environnement d'Exécution** : Nous ne pouvons pas exécuter de commandes pour vérifier si `jacoco:prepare-agent` a réellement fonctionné dans votre configuration.

---

### **Meilleure Approche : "Diviser et Vérifier"**
Pour des problèmes comme **Jacoco + Maven multi-modules + tests Python**, décomposez-les en **étapes atomiques** et vérifiez chacune d'elles. Exemple :

#### **Étape 1 : Vérifier la Configuration de l'Agent Jacoco (Côté Java)**
```bash
# Dans UN seul module (par exemple, module-A) :
mvn clean test -Pcoverage
```
-   **Vérification** : Le fichier `target/site/jacoco/index.html` existe-t-il ?
-   **Débogage** : Sinon, partagez l'extrait de `pom.xml` pour Jacoco et le journal d'erreurs.

#### **Étape 2 : Générer un Rapport Combiné (Multi-Modules)**
```bash
mvn jacoco:report-aggregate
```
-   **Vérification** : Le fichier `target/site/jacoco-aggregate/index.html` est-il créé ?
-   **Débogage** : S'il est manquant, vérifiez les chemins `<module>` dans le `pom.xml` parent.

#### **Étape 3 : Exporter pour Python (XML/CSV)**
```bash
# Convertir le binaire Jacoco en XML
java -jar jacoco-cli.jar report jacoco.exec --xml output.xml
```
-   **Vérification** : Est-ce que `output.xml` contient des balises `<package>` ?
-   **Débogage** : S'il est vide, assurez-vous que les tests ont été exécutés avec l'agent (`-javaagent:jacocoagent.jar`).

#### **Étape 4 : Intégration Python**
```python
import xml.etree.ElementTree as ET
tree = ET.parse("output.xml")
coverage = tree.find(".//counter[@type='LINE'][@covered]")
print(f"Lignes couvertes : {coverage.get('covered')}/{coverage.get('missed')}")
```
-   **Vérification** : Le script produit-il les nombres attendus ?
-   **Débogage** : Sinon, partagez la structure du XML et l'erreur Python.

---

### **Comment Travailler Efficacement avec les LLM**
1.  **Isolez le Problème** :
    -   *"Voici mon `pom.xml` pour le module-A. Pourquoi `jacoco:prepare-agent` n'ajoute-t-il pas l'argument VM ?"*
    -   *(Mieux que : "Aidez-moi à configurer Jacoco pour 5 modules + Python.")*

2.  **Partagez un Contexte Minimal et Reproductible** :
    -   Les journaux d'erreurs, des extraits de configuration (pas les fichiers entiers), et **ce que vous avez essayé**.

3.  **Débogage Itératif** :
    -   **Vous** : "L'étape 1 a échoué avec `No tests run`. Voici le journal."
    -   **LLM** : "Ajoutez des objectifs `<test>` à votre `maven-surefire-plugin`."
    -   **Vous** : "Maintenant l'étape 2 fonctionne, mais le rapport est vide..."

4.  **Utilisez-Nous pour des "Micro-Tâches"** :
    -   *"Écrivez un script Python pour analyser le XML Jacoco et échouer si la couverture < 80 %."*
    -   *"Expliquez la balise `<execution>` dans Maven pour Jacoco."*

---

### **Outils pour Automatiser les Flux de Travail Complexes**
Puisque les LLM ne peuvent pas gérer l'état, utilisez :
-   **Les scripts Shell** (par exemple, `setup_coverage.sh` pour enchaîner les commandes Maven/Python).
-   **Les Makefiles** (définissez `make test-coverage` pour exécuter toutes les étapes).
-   **Les modèles CI** (pipelines GitHub Actions/Jenkins avec des étapes explicites).
-   **Docker** (containerisez l'environnement pour éviter les problèmes de "ça marche sur ma machine").

---
### **Leçon Clé**
**Les LLM sont comme une page `man` surpuissante ou un Stack Overflow sous stéroïdes**—excellents pour les **éléments individuels**, mais pas pour orchestrer des systèmes entiers. Pour les tâches complexes :
1.  **Décomposez-la**.
2.  **Vérifiez chaque étape**.
3.  **Posez des questions ciblées**.

Souhaitez-vous que j'approfondisse l'une des étapes ci-dessus (par exemple, l'analyse du XML Jacoco en Python ou les configurations Maven multi-modules) ?