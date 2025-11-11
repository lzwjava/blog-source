---
audio: false
generated: true
lang: fr
layout: post
title: Outils de visualisation de branches Git
translated: true
type: note
---

Pour visualiser plusieurs branches dans un dépôt Git sous Windows, vous pouvez utiliser TortoiseGit ou d'autres outils pour afficher un graphe des branches sélectionnées. Le graphe de révisions de TortoiseGit est puissant mais peut devenir complexe lorsqu'il affiche toutes les branches. Voici les étapes pour visualiser un graphe de plusieurs branches spécifiques à l'aide de TortoiseGit, ainsi que des outils alternatifs offrant plus de flexibilité.

### Utilisation de TortoiseGit pour visualiser plusieurs branches
Le graphe de révisions de TortoiseGit peut afficher plusieurs branches, mais il ne permet pas de sélectionner des branches spécifiques directement dans l'interface. Cependant, vous pouvez filtrer la vue pour vous concentrer sur les branches pertinentes.

1.  **Ouvrir le graphe de révisions** :
    *   Accédez au dossier de votre dépôt dans l'Explorateur Windows.
    *   Faites un clic droit sur le dossier, sélectionnez **TortoiseGit** > **Revision Graph**.
    *   Cela affiche par défaut un graphe de toutes les références (branches, tags, etc.), ce qui peut être encombré si vous avez de nombreuses branches.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

2.  **Filtrer des branches spécifiques** :
    *   Dans la fenêtre du graphe de révisions, utilisez les **options de filtre** pour réduire l'encombrement :
        *   Allez dans le menu **View** et sélectionnez **Show branchings and mergings** pour mettre en avant les relations entre les branches.[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
        *   Pour vous concentrer sur des branches spécifiques, faites un clic droit sur un commit et sélectionnez **Show Log** pour afficher la boîte de dialogue du journal, où vous pouvez activer/désactiver **View > Labels > Local branches** ou **Remote branches** pour afficher uniquement les références pertinentes.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)
    *   Alternativement, utilisez l'option **Walk Behavior > Compressed Graph** dans la boîte de dialogue du journal pour simplifier le graphe, en n'affichant que les points de fusion et les commits avec des références (comme les pointes de branches).[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-showlog.html)[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)

3.  **Naviguer dans le graphe** :
    *   Utilisez la **fenêtre de vue d'ensemble** pour naviguer dans les grands graphes en faisant glisser la zone mise en surbrillance.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
    *   Survolez un nœud de révision pour voir les détails comme la date, l'auteur et les commentaires.[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)
    *   Utilisez Ctrl+clic sur deux révisions pour les comparer via le menu contextuel (par exemple, **Compare Revisions**).[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-revgraph.html)

4.  **Limitations** :
    *   Le graphe de révisions de TortoiseGit affiche toutes les branches sauf si elles sont filtrées, et il n'y a pas d'option directe pour sélectionner uniquement des branches spécifiques dans la vue du graphe.[](https://stackoverflow.com/questions/60244772/how-to-interpret-tortoise-git-revision-graph)
    *   Pour une vue plus claire, envisagez les outils alternatifs ci-dessous.

### Outils alternatifs pour visualiser plusieurs branches
Si l'interface de TortoiseGit est trop limitée pour sélectionner des branches spécifiques, essayez ces outils, qui offrent plus de contrôle sur la visualisation des branches :

#### 1. **Visual Studio Code avec l'extension Git Graph**
*   **Installation** : Téléchargez Visual Studio Code et installez l'extension **Git Graph**.[](https://x.com/midudev/status/1797990974917927150)
*   **Utilisation** :
    *   Ouvrez votre dépôt dans VS Code.
    *   Accédez à la vue Git Graph depuis l'onglet Source Control ou la palette de commandes (`Ctrl+Shift+P`, tapez "Git Graph").
    *   Sélectionnez les branches spécifiques à afficher dans le graphe en cliquant sur les noms des branches dans l'interface.
    *   Le graphe affiche les commits, les branches et les fusions avec des lignes codées par couleur pour plus de clarté.[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)
*   **Avantages** : Léger, gratuit et permet de sélectionner interactivement plusieurs branches. Prend en charge la comparaison de commits et les opérations Git de base.[](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)

#### 2. **SourceTree**
*   **Installation** : Téléchargez SourceTree (gratuit) pour Windows.[](https://stackoverflow.com/questions/12324050/how-can-i-visualize-github-branch-history-on-windows)[](https://stackoverflow.com/questions/12912985/git-visual-diff-between-branches)
*   **Utilisation** :
    *   Ouvrez votre dépôt dans SourceTree.
    *   La vue **History** montre une représentation graphique des branches et des commits.
    *   Utilisez la liste des branches sur la gauche pour activer/désactiver la visibilité de branches spécifiques, en vous concentrant uniquement sur celles que vous souhaitez voir.
    *   Faites un clic droit sur les branches ou les commits pour des actions comme la fusion ou la comparaison.[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
*   **Avantages** : Visualisation claire des branches avec un code couleur cohérent et des fonctionnalités interactives comme la fusion par glisser-déposer.[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 3. **GitKraken**
*   **Installation** : Téléchargez GitKraken (gratuit pour les projets open source, payant pour les dépôts privés).[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)[](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git)
*   **Utilisation** :
    *   Ouvrez votre dépôt dans GitKraken.
    *   Le graphe central affiche toutes les branches, avec des options pour masquer/afficher des branches spécifiques via la liste des branches.
    *   Cliquez sur les étiquettes de branches pour vous concentrer sur des branches spécifiques ou utilisez la recherche pour filtrer les commits.[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
*   **Avantages** : Intuitif et visuellement attrayant, avec un code couleur cohérent pour les branches et des fonctionnalités avancées comme la résolution de conflits.[](https://superuser.com/questions/699094/how-can-i-visualize-git-flow-branches)[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)

#### 4. **Ligne de commande avec `git log`**
*   Si vous préférez une solution en terminal, utilisez la vue graphique intégrée à Git :
    ```bash
    git log --graph --oneline --decorate --branches=<branch1> --branches=<branch2>
    ```
    Remplacez `<branch1>` et `<branch2>` par les noms des branches que vous souhaitez visualiser (par exemple, `feature1`, `feature2`). Utilisez `--branches=*` pour toutes les branches ou spécifiez explicitement plusieurs branches.[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
*   **Alias pour plus de commodité** :
    Créez un alias Git pour un accès plus facile :
    ```bash
    git config --global alias.tree "log --graph --oneline --decorate --branches="
    ```
    Puis exécutez `git tree feature1 feature2` pour voir un graphe de seulement ces branches.[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)
*   **Avantages** : Aucun logiciel supplémentaire nécessaire, et vous pouvez spécifier les branches exactes. La sortie est textuelle mais claire pour les petits dépôts.[](https://x.com/GWierzowiecki/status/1927657575048179899)

### Recommandations
*   **Pour la simplicité et l'intégration** : Utilisez **VS Code avec Git Graph** pour une solution légère et gratuite qui vous permet de sélectionner des branches spécifiques.[](https://x.com/midudev/status/1797990974917927150)
*   **Pour une visualisation avancée** : Utilisez **GitKraken** ou **SourceTree** pour une interface graphique plus aboutie avec une sélection interactive des branches et un code couleur cohérent.[](https://www.geeksforgeeks.org/how-to-visualizing-branch-topology-in-git/)
*   **Pour les utilisateurs de TortoiseGit** : Restez sur le graphe de révisions et utilisez des filtres comme **Compressed Graph** ou **Show branchings and mergings** pour vous concentrer sur les branches clés, mais soyez conscient de ses limitations pour sélectionner des branches spécifiques.[](https://stackoverflow.com/questions/67642974/tortoisegit-log-can-i-view-only-branch-and-merge-commits)
*   **Pour les utilisateurs du terminal** : Utilisez la commande `git log` avec des filtres de branches spécifiques pour une visualisation rapide et précise sans outils supplémentaires.[](https://how-to.dev/how-to-display-git-branches-as-a-tree-in-cli)

Si vous avez un grand nombre de branches, GitKraken ou SourceTree sont probablement les meilleures options pour visualiser sélectivement uniquement les branches qui vous intéressent, car ils offrent une activation/désactivation intuitive des branches. Faites-moi savoir si vous avez besoin d'aide pour configurer l'un de ces outils ou pour des clarifications supplémentaires !