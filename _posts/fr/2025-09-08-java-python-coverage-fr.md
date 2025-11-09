---
audio: false
date: 2025-09-08
generated: true
image: false
lang: fr
layout: post
title: Couverture Java Multi-module avec Python
translated: true
type: note
---

En examinant votre configuration, vous faites face à un défi complexe mais intéressant : utiliser des tests d'intégration Python pour générer la couverture d'un projet Java multi-module. Laissez-moi analyser la situation et suggérer une stratégie complète.

## Défis actuels

1. **Tests cross-language** : Des tests Python exerçant du code Java
2. **Couverture multi-module** : Nécessité de capturer la couverture sur tous les modules depuis les tests d'intégration
3. **Interdépendances des modules** : `PlaygroundUtils` n'a pas de endpoints directs mais est exercé via `PlaygroundWeb`
4. **Problème d'évolutivité** : Comment gérer cela pour 10+ modules

## Stratégie recommandée

### Option 1 : Agent JaCoCo unique, rapport fusionné (Recommandé)

C'est l'approche la plus évolutive pour votre cas d'utilisation :## Améliorations et stratégie clés

### 1. **Approche par agent JaCoCo unique**
- Utiliser UN seul fichier `jacoco-it.exec` au niveau parent
- Configurer l'agent avec `append=true` et `includes=org.lzw.*`
- Cela capture la couverture de TOUS les modules en une seule passe

### 2. **Agrégation des rapports**
- Utiliser `jacoco:report-aggregate` pour créer un rapport unifié
- Cela trouve automatiquement toutes les classes des modules et génère la couverture pour elles

### 3. **Exécution basée sur les profils**
- Séparer les préoccupations : profil `run-integration-tests` pour exécuter les tests
- Profil `integration-test-coverage` pour générer les rapports
- Rend le build plus modulaire et maintenable

### 4. **Évolutivité pour 10+ modules**

Pour les projets plus importants, considérez cette approche améliorée :## Résumé et bonnes pratiques

### Pour votre configuration actuelle à 2 modules :
1. **Utiliser un seul fichier exec JaCoCo** au niveau parent avec `append=true`
2. **Lancer Jetty une seule fois** avec l'agent configuré pour capturer tous les modules
3. **Utiliser `report-aggregate`** pour générer un rapport unifié

### Pour passer à 10+ modules :
1. **Regroupement des modules** : Créer des groupes logiques (core, service, web) et générer des rapports séparés
2. **Suivi de couverture** : Implémenter un helper Python pour suivre quels modules sont couverts
3. **Tests parallèles** : Exécuter différentes suites de tests en parallèle pour un retour plus rapide
4. **Couverture incrémentale** : Utiliser les profils Maven pour exécuter la couverture pour des groupes de modules spécifiques

### Points de configuration clés :
- **`append=true`** : Garantit que les multiples exécutions de tests accumulent la couverture
- **`includes=org.lzw.*`** : Capture tous vos modules dans un seul agent
- **Séparation des profils** : Garder les tests d'intégration séparés des builds réguliers
- **Fichier exec unique** : Élimine le besoin de lancer Jetty plusieurs fois

### Utilisation en ligne de commande :
```bash
# Couverture complète avec tests d'intégration
mvn clean verify -Prun-integration-tests,integration-test-coverage

# Couverture uniquement des tests unitaires
mvn clean test

# Couverture pour un groupe de modules spécifique
mvn clean verify -Pcoverage-by-layer
```

Cette approche est évolutive car :
1. Vous ne démarrez/arrêtez Jetty qu'une seule fois, quel que soit le nombre de modules
2. JaCoCo gère automatiquement les fichiers de classes multi-modules
3. Les tests Python n'ont pas besoin de connaître la structure des modules Java
4. Les rapports peuvent être agrégés ou séparés selon les besoins pour différents publics

L'idée clé est que l'agent JaCoCo peut capturer la couverture pour TOUTES les classes dans la JVM, pas seulement le module testé. En utilisant un fichier exec partagé et le goal aggregate, vous obtenez des données de couverture complètes en une seule exécution de test.