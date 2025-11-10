---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Journalisation Git détaillée
translated: true
type: note
---

Pour activer la journalisation verbeuse dans Git, vous pouvez utiliser des indicateurs spécifiques ou des variables d'environnement selon la commande et le niveau de détail nécessaire. Voici les principales approches :

1. **Utiliser l'indicateur `--verbose` ou `-v`** :
   De nombreuses commandes Git prennent en charge l'indicateur `--verbose` (ou `-v`) pour fournir une sortie plus détaillée. Par exemple :
   ```bash
   git commit --verbose
   ```
   Cela affiche le diff des modifications en cours de validation en plus de la sortie habituelle.

2. **Activer le mode verbeux pour des commandes spécifiques** :
   - Pour `git push` :
     ```bash
     git push --verbose
     ```
     Cela fournit des détails sur le processus de push, incluant les références envoyées et la communication avec le serveur.
   - Pour `git fetch` :
     ```bash
     git fetch --verbose
     ```
     Cela affiche des informations détaillées sur ce qui est récupéré.
   - Pour `git clone` :
     ```bash
     git clone --verbose <repository>
     ```
     Cela affiche la progression et des détails supplémentaires pendant le clonage.

3. **Définir la variable d'environnement `GIT_TRACE`** :
   Pour un débogage approfondi, vous pouvez activer la sortie de trace de Git pour voir les détails de bas niveau des opérations Git :
   ```bash
   GIT_TRACE=1 git <commande>
   ```
   Cela génère des journaux détaillés sur les processus internes de Git, tels que l'exécution des commandes et les appels système.

4. **Activer des niveaux de trace spécifiques** :
   Vous pouvez utiliser des variables d'environnement plus granulaires pour des aspects spécifiques de Git :
   - `GIT_TRACE_CURL` : Active la journalisation verbeuse pour les opérations HTTP (utile pour les interactions distantes) :
     ```bash
     GIT_TRACE_CURL=1 git <commande>
     ```
   - `GIT_TRACE_PACKET` : Affiche les détails au niveau des paquets pour le protocole Git :
     ```bash
     GIT_TRACE_PACKET=1 git <commande>
     ```
   - `GIT_TRACE_PERFORMANCE` : Journalise les données de performance :
     ```bash
     GIT_TRACE_PERFORMANCE=1 git <commande>
     ```

5. **Augmenter la verbosité pour les commandes liées aux diff** :
   Pour des commandes comme `git diff` ou `git log`, vous pouvez utiliser des options pour obtenir plus de détails :
   - `git diff --stat` affiche un résumé des modifications.
   - `git log --verbose` ou `git log -p` inclut le diff complet pour chaque commit.

6. **Configuration globale pour la sortie verbeuse** :
   Vous pouvez configurer Git pour qu'il soit toujours verbeux pour certaines commandes en définissant des alias ou en utilisant des options de configuration. Par exemple :
   ```bash
   git config --global alias.logv "log --verbose"
   ```
   Ensuite, exécuter `git logv` inclura toujours la sortie verbeuse.

**Exemple** :
Pour voir la sortie détaillée d'une opération de push avec traçage complet :
```bash
GIT_TRACE=1 git push --verbose
```

**Notes** :
- La sortie verbeuse peut être écrasante, surtout avec `GIT_TRACE`, utilisez-la donc pour déboguer des problèmes spécifiques.
- Consultez les pages de manuel pour des commandes spécifiques (par exemple, `man git-push`) pour voir si elles prennent en charge `--verbose` ou d'autres indicateurs de débogage.
- Sous Windows, utilisez la même syntaxe de variable d'environnement dans l'invite de commandes (`set GIT_TRACE=1`) ou PowerShell (`$env:GIT_TRACE=1`).

Si vous avez besoin d'une journalisation verbeuse pour une commande ou un scénario Git spécifique, faites-le-moi savoir et je pourrai fournir un exemple adapté !