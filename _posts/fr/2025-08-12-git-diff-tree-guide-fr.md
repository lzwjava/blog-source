---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide Git Diff-Tree
translated: true
type: note
---

Voici un guide pratique et complet sur `git diff-tree` : ce que c'est, quand l'utiliser, et les options que vous utiliserez réellement dans votre travail. J'éviterai les grands tableaux et me concentrerai sur des explications ciblées avec des exemples prêts à copier-coller.

# Ce que fait réellement `git diff-tree`

* Il compare des **objets arbre**. Dans un usage quotidien, cela signifie généralement : « montrez-moi ce qui a changé dans un **commit** par rapport à son/ses parent(s). »
* C'est une commande de **plomberie** (adaptée aux scripts), contrairement à `git show`/`git log` qui sont des commandes de porcelaine (orientées humain).
* Il ne regarde jamais votre répertoire de travail ; il compare uniquement les arbres stockés dans le dépôt (commits, tags pointant vers des commits, ou identifiants d'arbre bruts).

# Formes de base que vous utiliserez

1. Différencier un commit par rapport à son parent

```bash
git diff-tree -p <commit>
```

Si `<commit>` a un parent, vous voyez un patch normal. S'il s'agit d'un commit de fusion, vous ne verrez rien à moins de le demander (voir ci-dessous).

2. Différencier explicitement deux arbres/commits

```bash
git diff-tree -p <old-tree-or-commit> <new-tree-or-commit>
```

Idéal lorsque vous voulez comparer deux points quelconques, pas seulement « commit vs parent ».

3. Afficher uniquement les noms de fichiers (pas de patch)

```bash
git diff-tree --name-only -r <commit>
```

Ajoutez `-r` pour récursion dans les sous-répertoires afin d'obtenir une liste plate.

4. Afficher les noms avec le type de changement

```bash
git diff-tree --name-status -r <commit>
# Affiche des lignes comme :
# A chemin/vers/nouveau_fichier
# M chemin/vers/modifié
# D chemin/vers/supprimé
```

5. Afficher un patch (diff complet)

```bash
git diff-tree -p <commit>            # diff unifié comme `git show`
git diff-tree -U1 -p <commit>        # moins de contexte (1 ligne)
```

# Options à connaître absolument (avec le pourquoi/le quand)

* `-r` — Récursion dans les sous-arbres pour voir tous les chemins imbriqués. Sans cela, un répertoire modifié peut apparaître comme une seule ligne.
* `--no-commit-id` — Supprime l'en-tête « commit <sha> » lors de la génération de sortie par commit pour un script.
* `--root` — Lorsqu'un commit n'a **aucun parent** (commit initial), affiche tout de même ses changements par rapport à l'arbre vide.
* `-m` — Pour les commits de fusion, affiche les diffs **par rapport à chaque parent** (produit plusieurs diffs).
* `-c` / `--cc` — Diff de fusion combiné. `--cc` est une vue raffinée (celle qu'utilise `git show` pour les fusions).
* `--name-only` / `--name-status` / `--stat` / `--numstat` — Différents styles de résumé. `--numstat` est adapté aux scripts (nombre de lignes ajoutées/supprimées).
* `--diff-filter=<set>` — Filtre par type de changement, p. ex. `--diff-filter=AM` (uniquement Ajouté ou Modifié) ; lettres courantes : `A`jouté, `M`odifié, `S`upprimé, `R`enommé, `C`opié, `T`ype changé.
* `-M` / `-C` — Détecte les renommages et copies. Ajoute un seuil de similarité optionnel, p. ex. `-M90%`.
* `--relative[=<path>]` — Restreint la sortie à un sous-répertoire ; sans argument, utilise le répertoire de travail actuel.
* `-z` — Terminaison des chemins par **NUL** pour une analyse machine non ambiguë (gère les sauts de ligne ou les tabulations dans les noms de fichiers).
* `--stdin` — Lit une liste de commits (ou de paires) depuis l'entrée standard. C'est la sauce secrète pour les opérations rapides par lots.

# Modèles canoniques pour les scripts

### 1) Lister les fichiers modifiés pour un seul commit

```bash
git diff-tree --no-commit-id --name-status -r <commit>
```

### 2) Traitement par lots sur de nombreux commits (rapide !)

```bash
git rev-list main --since="2025-08-01" |
  git diff-tree --stdin -r --no-commit-id --name-status
```

`--stdin` évite de lancer `git` par commit et est beaucoup plus rapide pour de grandes plages.

### 3) Uniquement les ajouts et modifications dans un répertoire

```bash
git diff-tree -r --no-commit-id --name-status \
  --diff-filter=AM <commit> -- src/backend/
```

### 4) Compter les lignes ajoutées/supprimées par fichier (adapté aux scripts)

```bash
git diff-tree -r --no-commit-id --numstat <commit>
# Sortie : "<ajoutées>\t<supprimées>\t<chemin>"
```

### 5) Détecter et afficher les renommages dans un commit

```bash
git diff-tree -r --no-commit-id -M --name-status <commit>
# Lignes comme : "R100 ancien/nom.txt\tnouveau/nom.txt"
```

### 6) Patch pour un commit de fusion

```bash
git diff-tree -m -p <merge-commit>     # patches par parent
git diff-tree --cc <merge-commit>      # vue combinée (patch unique)
```

### 7) Commit initial (aucun parent)

```bash
git diff-tree --root -p <initial-commit>
```

# Comprendre le format d'enregistrement brut (si vous analysez manuellement)

Utilisez `--raw` (implicitement utilisé par certains modes) pour obtenir des enregistrements minimaux et stables :

```
:100644 100644 <oldsha> <newsha> M<TAB>chemin
```

* Les nombres sont les modes de fichier : `100644` fichier régulier, `100755` exécutable, `120000` lien symbolique, `160000` gitlink (sous-module).
* Le statut est une seule lettre (`A`, `M`, `D`, etc.), possiblement avec un score (p. ex., `R100`).
* Pour les renommages/copies, vous verrez deux chemins. Avec `-z`, les champs sont séparés par NUL ; sans `-z`, ils sont séparés par des tabulations.

**Astuce :** Si vous créez des outils fiables, utilisez toujours `-z` et séparez sur NUL. Les noms de fichiers avec des sauts de ligne existent.

# Comparaison de `git diff-tree` avec les commandes associées (pour choisir la bonne)

* `git diff` : compare **l'index/le répertoire de travail** vs HEAD ou deux commits/arbres quelconques ; développement interactif.
* `git show <commit>` : un wrapper convivial pour « diff vs parent + métadonnées ». Idéal pour les humains.
* `git log -p` : historique plus patches. Pour les plages, c'est souvent plus pratique que de boucler manuellement avec `diff-tree`.
* `git diff-tree` : plomberie pour les **diffs par commit précis et scriptables**, pouvant être traités par lots avec `--stdin`.

# Exemples concrets

### « Qu'est-ce qui a changé dans ce commit de fusion de PR ? »

```bash
git diff-tree --cc <merge-commit> | less
```

Si vous avez besoin de détails par parent :

```bash
git diff-tree -m -p <merge-commit> | less
```

### « Fournir à une étape de CI une liste propre des fichiers modifiés par le dernier commit »

```bash
git diff-tree --no-commit-id --name-only -r HEAD > changed.txt
```

### « Uniquement les fichiers Java ajoutés ou modifiés dans les 20 derniers commits »

```bash
git rev-list -n 20 HEAD |
  git diff-tree --stdin -r --no-commit-id --name-only --diff-filter=AM |
  grep -E '\.java$'
```

### « Résumer l'activité (lignes ajoutées/supprimées) pour un tag de release »

```bash
git diff-tree -r --no-commit-id --numstat v1.2.0..v1.3.0
```

### « Gérer les noms de fichiers bizarres en toute sécurité »

```bash
git diff-tree -z -r --no-commit-id --name-status <commit> |
  awk -v RS='\0' 'NR%2{status=$0; next}{printf "%s %s\n", status, $0}'
```

# Notes sur les performances

* Préférez `--stdin` avec `git rev-list` pour les grandes plages ; cela évite la surcharge des processus.
* Ignorez les patches (`--name-only`/`--name-status`) lorsque vous n'avez pas besoin des changements de ligne.
* Évitez la détection des renommages (`-M`, `-C`) si la vitesse est plus importante que la précision.

# Pièges & cas particuliers

* **Aucune sortie pour les fusions par défaut.** Vous devez passer `-m` (par parent) ou `--cc`/`-c` (combiné).
* **Le commit initial est “arbre vide vs arbre”.** Utilisez `--root` pour forcer un diff.
* **Les sous-modules** affichent le mode `160000` et un SHA (gitlink). Vous ne verrez pas les diffs internes sauf si vous effectuez un diff dans le dépôt du sous-module.
* **Les pathspecs sont après `--`.** Si vous filtrez par chemins, placez-les après `--` pour éviter toute ambiguïté.
* **Noms de fichiers avec espaces/sauts de ligne.** Ajoutez toujours `-z` si vous analysez.

# « Snippets » aide-mémoire rapides que vous réutiliserez

```bash
# Fichiers modifiés (liste plate)
git diff-tree --no-commit-id --name-only -r <commit>
```