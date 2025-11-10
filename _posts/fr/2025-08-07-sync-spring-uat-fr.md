---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Synchroniser les branches et le code UAT du printemps
translated: true
type: note
---

Voici une collection de bonnes pratiques et de modèles que vous pouvez combiner pour maintenir vos trois branches UAT synchronisées, garder votre historique propre et gérer le code spécifique à chaque pays dans une application Spring—ainsi qu'un aperçu de l'endroit où l'IA peut aider.

---

## 1. Gestion des branches & synchronisation

1.  **Développement en Trunk-Based avec des branches de fonctionnalités à courte durée de vie**

    *   Maintenez une seule branche **main** (ou **develop**).
    *   Pour chaque ticket Jira (ex: FT-103) et pays, créez des branches de fonctionnalités nommées :

        ```
        feature/FT-103-cn
        feature/FT-103-sg
        feature/FT-103-tw
        ```
    *   Lorsque le travail est prêt, fusionnez-le dans **main**, puis effectuez un cherry-pick ou fusionnez dans chaque branche `uat_cn`, `uat_sg`, `uat_tw`.
    *   Avantage : les fusions dans main se font une seule fois ; les branches pays ne récupèrent que ce dont elles ont besoin.

2.  **Synchronisation régulière des branches UAT**

    *   Planifiez une tâche quotidienne (ou à chaque build) pour rebaser chaque branche `uat_*` sur `main` afin qu'elles ne divergent pas trop.
    *   Automatisez cela dans l'intégration continue (ex: une GitHub Action qui rebase `uat_cn` chaque nuit).

3.  **Utilisez des pull-requests + application de la revue**

    *   Exigez une PR pour chaque fusion de branche de fonctionnalité → main.
    *   Assurez-vous que le ticket "FT-xxx" est dans le nom de la branche et dans le titre/la description de la PR.

---

## 2. Conventions de message de commit & squashing

1.  **Style conventionnel avec la clé JIRA**

    ```
    FT-103: fix null-pointer in customer lookup
    ```

2.  **Micro-commit → squash au moment de la fusion**

    *   Pendant le développement de la fonctionnalité, les développeurs committent au fur et à mesure :

        ```
        FT-103 #1: initial wiring of service beans
        FT-103 #2: add validation logic
        FT-103 #3: update error handling
        ```
    *   Lors de la fusion de la PR, utilisez "Squash and merge" pour regrouper tous les commits FT-103 en un seul commit concis :

        ```
        FT-103: customer-service validation and error handling
        ```

3.  **Numérotation dans un ticket**

    *   Si vous devez suivre plusieurs étapes distinctes dans le même ticket, la numérotation (`#1`, `#2`) est acceptable pendant le développement.
    *   Une fois fusionné, squash everything en un *seul* commit FT-103 ; l'historique reste propre et chaque ticket représente un changement logique unique.

4.  **Automatisez le linting des commits**

    *   Utilisez un hook Git ou un plugin d'intégration continue (ex: [commitlint](https://commitlint.js.org)) pour imposer `FT-\d+` au début de chaque message.
    *   Imposez éventuellement un scope : `FT-103(sg): …`.

---

## 3. Gestion du code spécifique à un pays dans Spring

1.  **Profils & beans conditionnels**

    *   Définissez un profil Spring par pays : `@Profile("cn")`, `@Profile("sg")`, `@Profile("tw")`.
    *   Dans `application-cn.yml`, `application-sg.yml`, etc., définissez les propriétés spécifiques à chaque pays.
    *   Au démarrage, passez `--spring.profiles.active=cn` (ou sg, tw) pour sélectionner les bons beans.

2.  **Pattern Strategy / modules plugin**

    *   Créez une interface `PaymentProcessor` avec trois implémentations (`CnPaymentProcessor`, etc.).
    *   Utilisez `@Component` + `@Profile` ou une factory qui sélectionne le bean en fonction d'un flag d'exécution.

3.  **Fichiers de ressources / feature flags**

    *   Si les différences sont minimes (ex: formats de date, URLs de endpoints), gardez un seul chemin de code et externalisez les différences dans des fichiers de propriétés ou un service de feature flags.

4.  **Modules séparés (si la logique est très différente)**

    *   Pour une logique très divergente, séparez en sous-modules :

        ```
        /core
        /country-cn
        /country-sg
        /country-tw
        ```
    *   L'application principale n'importe que le module du pays actif au moment du build/déploiement.

---

## 4. Séparation des tâches par auteur vs par ticket

*   **Par ticket, pas par auteur.** Les tâches doivent être unitarisées autour des *fonctionnalités* (IDs Jira), et non de la personne.
*   Si plusieurs développeurs travaillent sur FT-103, ils collaborent sur la même branche ou utilisent des branches thématiques basées dessus—mais finissent par fusionner dans la branche FT-103 unique.
*   Les métadonnées de l'auteur restent dans le champ "author" du commit ; vous n'avez pas besoin de squasher par auteur.

---

## 5. Mettre l'IA à contribution

1.  **Génération de messages de commit**

    *   Des outils comme GitHub Copilot ou OpenAI peuvent suggérer des messages de commit propres et conventionnels à partir de votre diff.
    *   Intégrez un pre-commit hook qui exécute `ai-commit --preview` pour rédiger un brouillon du message à revoir.

2.  **Description de PR & changelog**

    *   Utilisez un assistant IA pour résumer tous les commits d'un ticket en une description de PR cohérente ou une note de release :

        > “Summarize the changes in feature/FT-103 into bullet points.”

3.  **Assistance à la revue de code**

    *   Les linters alimentés par l'IA (SonarQube avec des plugins IA, DeepCode) peuvent signaler des problèmes dans les chemins de code spécifiques à un pays.

4.  **Automatisation des cherry-picks/rebases**

    *   Écrivez un petit script (ou utilisez une plateforme low-code) qui, lorsque FT-103 est fusionné dans `main`, effectue automatiquement un cherry-pick dans chaque branche `uat_*` et ouvre des PRs pour tout conflit de fusion.

---

### Pour résumer

1.  **Développez sur** `feature/FT-XXX-<cn/sg/tw>`.
2.  **Committtez librement** (les étapes numérotées sont OK), en référençant la clé JIRA.
3.  **Ouvrez une PR** → main ; choisissez **Squash-and-merge** pour que chaque FT-XXX soit un commit propre.
4.  **La tâche d'intégration continue** rebase/fusionne automatiquement ce commit dans chaque branche `uat_cn`, `uat_sg`, `uat_tw`.
5.  **Les profils Spring** au runtime sélectionnent la logique du pays correcte—pas de duplication de code dans trois branches.
6.  **Les outils d'IA** aident à faire respecter le style des commits, à résumer les PRs et à gérer les fusions.

Ce workflow maintient la propreté de votre historique, assure que chaque ticket est traçable jusqu'à un seul commit dans tous les environnements, sépare la logique métier par pays au runtime au lieu de l'avoir dans l'historique Git, et tire parti de l'IA là où elle apporte le plus de valeur.