---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Compression des validations Git par auteur
translated: true
type: note
---

### Comprendre l'objectif
Git n'a pas de commande intégrée "squash par auteur", mais vous pouvez y parvenir en utilisant un rebase interactif pour regrouper et fusionner manuellement les commits. L'idée est de prendre les 10 derniers commits (en supposant qu'ils impliquent 3 auteurs distincts) et de fusionner les commits de chaque auteur en un seul commit par auteur, ce qui donne un total de 3 commits.

Ceci suppose :
- Vous êtes sur la branche contenant ces commits (par exemple, main ou une branche de fonctionnalité).
- Les commits sont linéaires (pas de fusions).
- Vous connaissez les auteurs à l'avance.

Si les commits sont non linéaires ou complexes, cela peut nécessiter une manipulation minutieuse pour éviter les conflits.

### Étapes pour fusionner les commits par auteur
1. **Vérifier les 10 derniers commits**  
   Exécutez `git log --oneline -10` pour voir les 10 derniers commits, y compris leurs hash, auteurs et messages. Identifiez les auteurs (par exemple, via `git log --format="%an" -10 | sort | uniq` pour lister les auteurs uniques).

2. **Démarrer un rebase interactif**  
   Identifiez le commit précédant le 10ème. Si votre dernier commit est à HEAD, et qu'il y a 10 commits, la base est `HEAD~10`. Exécutez :  
   ```
   git rebase -i HEAD~10
   ```  
   Ceci ouvre un éditeur (vim par défaut) avec une liste des 10 derniers commits. Cela ressemble à ceci :  
   ```
   pick abc123 Premier commit par Auteur A  
   pick def456 Deuxième commit par Auteur A  
   pick ghi789 Commit par Auteur B  
   pick jkl012 Commit par Auteur C  
   ... (plus de commits)
   ```  
   - Chaque ligne commence par `pick`.

3. **Marquer les commits à fusionner par auteur**  
   Pour chaque auteur, changez `pick` en `s` (squash) sur tous leurs commits sauf le premier que vous souhaitez conserver pour cet auteur. Décidez :
   - Un commit "à conserver" par auteur (choisissez le plus ancien ou le plus pertinent comme base).
   - Changez les autres de cet auteur en `s` pour les fusionner dedans.  
   Exemple (pour 3 auteurs) :  
   ```
   pick abc123 Premier commit par Auteur A (conserver celui-ci)  
   s    def456 Deuxième commit par Auteur A (fusionner dans le précédent)  
   pick ghi789 Commit par Auteur B (conserver celui-ci)  
   pick jkl012 Premier commit par Auteur C (conserver celui-ci)  
   s    mno345 Deuxième commit par Auteur C (fusionner dans le précédent)  
   ```  
   Sauvegardez et quittez l'éditeur. Ceci démarre le rebase.

4. **Modifier les messages de commit pendant le rebase**  
   Pour chaque opération de fusion, Git fera une pause et vous laissera modifier le message du commit (en combinant ceux fusionnés). Mettez-le à jour avec quelque chose comme "Commits fusionnés par Auteur A : description". Sauvegardez et continuez.  
   S'il y a plus de fusions, répétez pour chaque auteur. Exécutez `git rebase --continue` après chaque modification.  
   Si des conflits surviennent (rares dans une fusion simple), résolvez-les avec `git add <fichier>` puis `git rebase --continue`.

5. **Vérifier et pousser**  
   Après la fin du rebase, vérifiez le log : `git log --oneline -10`. Vous devriez voir 3 commits, chacun d'un auteur.  
   Effectuez un push forcé si vous poussez vers une branche partagée (rebase destructif) : `git push --force-with-lease origin nom-de-la-branche`.  
   **Avertissement :** Ne forcez le push que si vous êtes sûr que les anciens commits ne sont pas nécessaires ailleurs, car cela réécrit l'historique.

### Conseils et mises en garde
- Si les auteurs ont de nombreux commits, regroupez-les efficacement dans la liste du rebase (tous ceux de l'Auteur A ensemble, etc.).
- Pour l'automatisation, des outils comme `git-interactive-rebase-tool` ou des scripts peuvent aider, mais le rebase manuel est simple.
- Si vous devez filtrer par auteur exact, utilisez `git log --author="Nom de l'Auteur"` au préalable pour confirmer.
- Testez d'abord sur une branche de sauvegarde pour éviter la perte de données.

Pour en savoir plus sur le rebase : `git help rebase`. Si cela ne correspond pas exactement à votre scénario, fournissez plus de détails sur la structure des commits.