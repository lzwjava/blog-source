---
audio: false
generated: true
lang: fr
layout: post
title: Commandes Git avancées
translated: true
type: note
---

Git est comme un couteau suisse pour les développeurs — polyvalent, puissant et parfois déroutant si vous ne savez pas quel outil utiliser. Aujourd'hui, nous allons explorer certaines des fonctionnalités et workflows les plus astucieux de Git : le cherry-picking de changements, les fusions avec style, le rebasage pour un historique plus propre, la suppression de ces gros fichiers gênants que vous avez accidentellement commités, et l'annulation d'un commit lorsque vous réalisez que vous êtes parti dans la mauvaise direction. Décomposons tout cela.

#### Cherry-Picking : Prendre Juste Ce Dont Vous Avez Besoin
Imaginez que vous ayez une branche de fonctionnalité avec une douzaine de commits, mais qu'il y ait un commit brillant que vous souhaitez extraire et appliquer à votre branche principale — sans apporter le reste. C'est là qu'intervient `git cherry-pick`.

C'est super simple : trouvez le hash du commit (vous pouvez le récupérer via `git log`), basculez sur la branche de destination, et exécutez :
```
git cherry-pick <commit-hash>
```
Boom, ce commit fait maintenant partie de votre branche actuelle. S'il y a un conflit, Git fera une pause et vous laissera le résoudre, comme pour une fusion. Une fois satisfait, committez les changements, et c'est bon.

J'utilise cela tout le temps quand une correction de bug se glisse dans une branche de fonctionnalité désordonnée et que j'en ai besoin sur `main` ASAP. Mais attention — le cherry-picking duplique le commit, il obtient donc un nouveau hash. Ne vous attendez pas à ce que cela se passe bien si vous fusionnez la branche originale plus tard sans un peu de nettoyage.

#### Options de Fusion : Plus Qu'un Simple "Merge"
La fusion est la base de Git, mais saviez-vous qu'elle existe en plusieurs versions ? Le `git merge` par défaut effectue un "fast-forward" si possible (pour rectifier l'historique) ou crée un commit de fusion si les branches ont divergé. Mais vous avez des options :

- **`--no-ff` (No Fast-Forward)** : Force un commit de fusion même si un fast-forward est possible. J'adore cela pour garder une trace claire de quand une branche de fonctionnalité a été intégrée à `main`. Exécutez-le ainsi :
  ```
  git merge --no-ff feature-branch
  ```
- **`--squash`** : Rassemble tous les changements de la branche en un seul commit sur votre branche actuelle. Pas de commit de fusion, juste un paquet unique et bien rangé. Parfait pour compacter une branche désordonnée en quelque chose de présentable :
  ```
  git merge --squash feature-branch
  ```
  Après cela, vous devrez committer manuellement pour finaliser.

Chacune a sa place. Je penche vers `--no-ff` pour les branches de longue durée et `--squash` quand j'ai une branche pleine de commits "WIP" que je préférerais oublier.

#### Rebasage : Réécrire l'Histoire Comme un Pro
Si les fusions vous semblent trop désordonnées, `git rebase` pourrait être votre style. Il prend vos commits et les rejoue sur une autre branche, vous donnant un historique linéaire qui donne l'impression que vous avez tout planifié parfaitement dès le départ.

Basculez sur votre branche de fonctionnalité et exécutez :
```
git rebase main
```
Git va décoller vos commits, mettre à jour la branche pour qu'elle corresponde à `main`, et recoller vos changements par-dessus. Si des conflits surviennent, résolvez-les, puis `git rebase --continue` jusqu'à ce que ce soit terminé.

L'avantage ? Une timeline impeccable. L'inconvénient ? Si vous avez déjà poussé cette branche et que d'autres y travaillent, le rebasage réécrit l'histoire — préparez-vous aux emails énervés de vos coéquipiers. Je me limite au rebasage pour les branches locales ou les projets en solo. Pour le travail partagé, la fusion est plus sûre.

#### Supprimer les Gros Fichiers de l'Historique : Oups, Cette Vidéo de 2 Go
On est tous passé par là : vous committez accidentellement un fichier énorme, vous le poussez, et maintenant votre repo est gonflé. Git n'oublie pas facilement, mais vous pouvez effacer ce fichier de l'historique avec un peu d'effort.

L'outil recommandé ici est `git filter-branch` ou le plus récent `git filter-repo` (je recommande ce dernier — il est plus rapide et moins sujet aux erreurs). Disons que vous avez commité `bigfile.zip` et devez vous en débarrasser :
1. Installez `git-filter-repo` (consultez sa documentation pour l'installation).
2. Exécutez :
   ```
   git filter-repo --path bigfile.zip --invert-paths
   ```
   Cela supprime `bigfile.zip` de chaque commit dans l'historique.
3. Force-push de l'historique réécrit :
   ```
   git push --force
   ```

Attention : cela réécrit l'histoire, alors coordonnez-vous avec votre équipe. Et si c'est dans une pull request quelque part, vous devrez peut-être aussi nettoyer les refs. Une fois supprimé, votre repo maigrira après un garbage collection (`git gc`).

#### Dé-committer : Remonter le Temps
Vous avez fait un commit et l'avez instantanément regretté ? Git vous couvre. Il y a plusieurs façons de l'annuler, selon où vous en êtes :

- **Si vous n'avez pas encore poussé** : Utilisez `git reset`. Pour annuler le dernier commit mais garder les changements dans votre répertoire de travail :
  ```
  git reset HEAD^ --soft
  ```
  Vous voulez supprimer complètement les changements ?
  ```
  git reset HEAD^ --hard
  ```
- **Si vous avez déjà poussé** : Vous devrez réécrire l'histoire. Faites un reset local avec `git reset HEAD^`, puis force-push :
  ```
  git push --force
  ```
  Encore une fois, cela modifie l'histoire partagée, alors agissez avec prudence.

`git reset --soft` m'a sauvé la mise plus de fois que je ne peux compter — parfait quand je committe trop tôt et que j'ai besoin de modifier quelque chose.

#### Pour Conclure

La flexibilité de Git est ce qui le rend si puissant, mais il est facile de s'emmêler les pinceaux si vous ne connaissez pas vos options. Utilisez le cherry-picking pour une précision chirurgicale, ajustez les fusions pour qu'elles correspondent à votre workflow, rebasez pour un historique poli, et ne paniquez pas quand vous devez effacer une erreur — que ce soit un énorme fichier ou un commit précipité. Entraînez-vous sur un repo test si vous êtes nerveux, et bientôt, cela vous semblera naturel.

Quelle est votre astuce Git préférée ? Faites-le moi savoir — je suis toujours partant pour apprendre quelque chose de nouveau !