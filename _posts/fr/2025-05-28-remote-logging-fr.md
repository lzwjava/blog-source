---
audio: false
generated: true
lang: fr
layout: post
title: Journalisation à distance dans IntelliJ IDEA
translated: true
type: note
---

Il semble que vous soyez en train de passer d'Eclipse avec le plugin Liberty Tools à IntelliJ IDEA pour le débogage distant, et que vous souhaitiez reproduire la capacité de visualiser, effacer et filtrer les nouveaux journaux déclenchés par des actions frontend dans un serveur WebSphere Liberty, similairement à votre utilisation de la console dans Eclipse ou à la surveillance des journaux dans VS Code. Vous demandez spécifiquement si IntelliJ IDEA prend en charge la journalisation distante et comment visualiser et gérer efficacement les nouveaux journaux générés par des clics frontend, comme vous le faisiez en plaçant le curseur à la fin d'un fichier journal dans VS Code.

Ci-dessous, je vais expliquer comment configurer IntelliJ IDEA pour visualiser et gérer les journaux distants d'un serveur WebSphere Liberty pendant une session de débogage distant, y compris l'effacement des journaux et la concentration sur les nouveaux journaux déclenchés par des actions frontend. J'aborderai également comment reproduire un workflow similaire à votre configuration VS Code pour sélectionner les nouveaux journaux.

---

### Comprendre vos besoins
1.  **Comportement d'Eclipse Liberty Tools** : Dans Eclipse avec le plugin Liberty Tools, vous utilisiez une vue console pour voir les journaux du serveur WebSphere Liberty, les effacer et observer les nouveaux journaux déclenchés par les interactions frontend.
2.  **Workflow VS Code** : Vous ouvriez le répertoire WebSphere Liberty (`wlp`) dans VS Code, placiez le curseur à la fin d'un fichier journal (par exemple, `messages.log`) et pouviez facilement sélectionner ou visualiser les nouveaux journaux ajoutés lors de l'interaction avec le frontend.
3.  **Objectif IntelliJ IDEA** : Vous avez configuré le débogage distant dans IntelliJ IDEA et vous voulez :
    - Visualiser les journaux du serveur WebSphere Liberty distant en temps réel.
    - Effacer les journaux ou vous concentrer sur les nouveaux journaux déclenchés par des actions frontend.
    - Reproduire la facilité de sélection des nouveaux journaux comme dans VS Code.

### Est-ce qu'IntelliJ IDEA prend en charge la journalisation distante ?
Oui, IntelliJ IDEA prend en charge la visualisation des journaux d'un serveur distant, y compris WebSphere Liberty, pendant une session de débogage distant. Cependant, contrairement au plugin Liberty Tools d'Eclipse qui fournit une console dédiée pour les journaux du serveur Liberty, IntelliJ IDEA nécessite une configuration manuelle pour afficher les journaux distants dans la fenêtre d'outil **Run** ou **Debug**. Vous pouvez y parvenir en configurant l'onglet **Logs** dans la Run/Debug Configuration ou en intégrant des outils externes pour suivre (`tail`) les fichiers journaux distants. IntelliJ IDEA vous permet également d'effacer les journaux et de filtrer les nouvelles entrées, bien que l'expérience diffère de celle d'Eclipse ou de VS Code.

---

### Configuration de la journalisation distante dans IntelliJ IDEA
Pour reproduire vos workflows Eclipse et VS Code, vous devez configurer IntelliJ IDEA pour accéder et afficher les journaux des fichiers journaux du serveur WebSphere Liberty distant (par exemple, `messages.log` ou `console.log` dans le répertoire `wlp/usr/servers/<nomDuServeur>/logs`). Voici comment procéder :

#### Étape 1 : Configurer le débogage distant
Étant donné que vous avez déjà configuré le débogage distant dans IntelliJ IDEA, je suppose que vous avez une configuration **Remote JVM Debug**. Sinon, voici un rapide rappel :
1.  Allez dans **Run > Edit Configurations**.
2.  Cliquez sur l'icône **+** et sélectionnez **Remote JVM Debug**.
3.  Définissez les éléments suivants :
    - **Name** : Par exemple, "Liberty Remote Debug".
    - **Host** : L'adresse du serveur distant (par exemple, `localhost` ou une IP comme `192.168.1.100`).
    - **Port** : Le port de débogage (par défaut pour Liberty est souvent `7777` sauf personnalisation).
    - **Command-line arguments for remote JVM** : Copiez les arguments générés (par exemple, `-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:7777`) et assurez-vous qu'ils sont appliqués à la JVM du serveur Liberty.
4.  Appliquez et sauvegardez la configuration.
5.  Démarrez le serveur Liberty avec les arguments de débogage (par exemple, modifiez `jvm.options` ou utilisez la commande `server debug`).

#### Étape 2 : Configurer l'affichage du fichier journal dans IntelliJ IDEA
Pour visualiser les journaux distants dans la fenêtre d'outil Debug d'IntelliJ IDEA, vous devez spécifier l'emplacement du fichier journal dans la Run/Debug Configuration. Étant donné que les journaux sont sur un serveur distant, vous devrez y accéder via un dossier monté, SSH ou un plugin.

**Option 1 : Accéder aux journaux via un dossier monté ou une copie locale**
Si le répertoire de journaux du serveur distant est accessible (par exemple, via un partage réseau, SFTP ou copié localement), vous pouvez configurer IntelliJ pour afficher les journaux :
1.  **Monter ou copier les journaux** :
    - Montez le répertoire de journaux du serveur distant (par exemple, `wlp/usr/servers/<nomDuServeur>/logs`) sur votre machine locale en utilisant SSHFS, NFS ou une autre méthode.
    - Alternativement, utilisez un outil comme `rsync` ou `scp` pour copier périodiquement `messages.log` ou `console.log` sur votre machine locale.
2.  **Ajouter le fichier journal à la Run/Debug Configuration** :
    - Allez dans **Run > Edit Configurations** et sélectionnez votre configuration Remote JVM Debug.
    - Ouvrez l'onglet **Logs**.
    - Cliquez sur l'icône **+** pour ajouter un fichier journal.
    - Spécifiez :
        - **Log file location** : Le chemin d'accès au fichier journal (par exemple, `/chemin/vers/mounted/wlp/usr/servers/defaultServer/logs/messages.log`).
        - **Alias** : Un nom pour l'onglet de journal (par exemple, "Liberty Logs").
        - **Show all files coverable by pattern** : Décochez cette option pour n'afficher que le dernier fichier journal (utile pour les journaux rotatifs comme `messages.log`).
        - **Skip Content** : Cochez cette option pour n'afficher que les nouvelles entrées de journal à partir de l'exécution en cours, similairement à l'effacement des journaux dans Eclipse.
    - Cliquez sur **Apply** et **OK**.
3.  **Exécuter le débogueur** :
    - Démarrez la session de débogage distante en sélectionnant la configuration et en cliquant sur le bouton **Debug**.
    - Un nouvel onglet (par exemple, "Liberty Logs") apparaîtra dans la fenêtre d'outil **Debug**, affichant le contenu du fichier journal.
    - Les nouvelles entrées de journal déclenchées par des clics frontend s'ajouteront à cet onglet en temps réel si le fichier est accessible.

**Option 2 : Utiliser SSH pour suivre (`tail`) les journaux distants**
Si le montage ou la copie des journaux n'est pas réalisable, vous pouvez utiliser le terminal SSH intégré d'IntelliJ ou un plugin pour suivre directement le fichier journal distant :
1.  **Activer l'accès SSH** :
    - Assurez-vous d'avoir un accès SSH au serveur distant hébergeant Liberty.
    - Configurez SSH dans IntelliJ IDEA via **File > Settings > Tools > SSH Configurations**.
2.  **Utiliser le terminal intégré** :
    - Ouvrez la fenêtre d'outil **Terminal** dans IntelliJ IDEA (Alt+F12).
    - Exécutez une commande pour suivre le fichier journal :
        ```bash
        ssh user@serveur-distant tail -f /chemin/vers/wlp/usr/servers/<nomDuServeur>/logs/messages.log
        ```
    - Cela diffuse le fichier journal en temps réel vers le terminal, similairement à votre workflow de curseur à la fin dans VS Code.
3.  **Effacer les journaux** :
    - Le terminal d'IntelliJ n'a pas de bouton "effacer les journaux" direct comme la console d'Eclipse. À la place, vous pouvez :
        - Arrêter la commande `tail` (Ctrl+C) et la redémarrer pour simuler un effacement.
        - Effacer la sortie du terminal en utilisant le bouton **Clear All** dans la barre d'outils du terminal.
4.  **Filtrer les nouveaux journaux** :
    - Utilisez `grep` pour filtrer les journaux pour des événements spécifiques déclenchés par le frontend :
        ```bash
        ssh user@serveur-distant tail -f /chemin/vers/wlp/usr/servers/<nomDuServeur>/logs/messages.log | grep "motif-spécifique"
        ```
    - Par exemple, si les clics frontend déclenchent des journaux avec un mot-clé spécifique (par exemple, "INFO"), filtrez pour ceux-ci.

**Option 3 : Utiliser un plugin pour une visualisation améliorée des journaux**
Les plugins **Log4JPlugin** ou **Grep Console** peuvent améliorer la visualisation des journaux dans IntelliJ IDEA :
1.  **Installer un plugin** :
    - Allez dans **File > Settings > Plugins**, recherchez "Log4JPlugin" ou "Grep Console" et installez.
    - Redémarrez IntelliJ IDEA.
2.  **Configurer Log4JPlugin** :
    - Après avoir configuré la configuration de débogage distant, utilisez Log4JPlugin pour pointer vers le fichier journal distant (nécessite SSH ou un dossier monté).
    - Ce plugin vous permet de visualiser et de filtrer les journaux dans un onglet dédié, similairement à la console Liberty Tools d'Eclipse.
3.  **Configurer Grep Console** :
    - Grep Console vous permet de mettre en évidence et de filtrer les messages de journal en fonction de motifs, facilitant la concentration sur les nouveaux journaux déclenchés par des actions frontend.
    - Configurez-le dans l'onglet **Run/Debug Configurations > Logs** en spécifiant le fichier journal et en activant le plugin.

#### Étape 3 : Reproduire le workflow "Curseur à la fin" de VS Code
Pour imiter le comportement de VS Code qui consiste à placer le curseur à la fin du fichier journal et à sélectionner les nouveaux journaux :
1.  **Défilement automatique vers la fin** :
    - Dans l'onglet de journal de la fenêtre d'outil **Debug** (de l'Option 1), IntelliJ IDEA défile automatiquement vers la fin du fichier journal à mesure que de nouvelles entrées sont ajoutées, similairement à `tail -f`.
    - Assurez-vous que **Scroll to the end** est activé dans la barre d'outils de l'onglet de journal (une petite icône de flèche pointant vers le bas).
2.  **Sélectionner les nouveaux journaux** :
    - Cliquez à la fin de l'onglet de journal pour y placer le curseur.
    - Lorsque vous interagissez avec le frontend, de nouvelles entrées de journal apparaîtront, et vous pouvez les sélectionner en glissant la souris ou en utilisant des raccourcis clavier (par exemple, Maj+Flèches).
    - Alternativement, utilisez la fonctionnalité **Search** dans l'onglet de journal (icône de loupe) pour filtrer les nouvelles entrées en fonction de mots-clés ou d'horodatages.
3.  **Effacer les journaux pour les nouvelles entrées** :
    - Cochez l'option **Skip Content** dans l'onglet Logs de la Run/Debug Configuration pour n'afficher que les nouvelles entrées de journal de la session en cours, "effaçant" efficacement les anciens journaux.
    - Si vous utilisez le terminal SSH, arrêtez et redémarrez la commande `tail -f` pour réinitialiser la vue vers les nouveaux journaux.

#### Étape 4 : Déboguer et surveiller les journaux déclenchés par le frontend
1.  **Définir des points d'arrêt** :
    - Dans IntelliJ IDEA, ouvrez les fichiers source Java concernés (par exemple, les contrôleurs backend gérant les requêtes frontend).
    - Définissez des points d'arrêt en cliquant dans la gouttière à côté de la ligne de code (ou appuyez sur Ctrl+F8 / Cmd+F8).
2.  **Démarrer le débogage** :
    - Exécutez la configuration de débogage distant.
    - La fenêtre d'outil Debug affichera l'onglet de journal (si configuré) et s'arrêtera aux points d'arrêt déclenchés par des clics frontend.
3.  **Corréler les journaux avec les points d'arrêt** :
    - Lorsqu'un point d'arrêt est atteint, vérifiez l'onglet de journal ou le terminal pour les entrées de journal correspondantes.
    - IntelliJ IDEA reconnaît les frameworks de journalisation comme SLF4J ou Log4J (courants dans les applications Liberty) et fournit des liens cliquables dans l'onglet de journal pour sauter vers le code source où le journal a été généré.
4.  **Filtrer pour les actions frontend** :
    - Utilisez la barre de recherche dans l'onglet de journal pour filtrer les messages de journal spécifiques (par exemple, "INFO [frontend]" ou "POST /endpoint").
    - Si vous utilisez Grep Console, configurez des motifs pour mettre en évidence les journaux liés au frontend.

---

### Différences avec Eclipse et VS Code
-   **Eclipse Liberty Tools** : Fournit une console dédiée pour les journaux Liberty avec des options intégrées d'effacement et de filtrage. IntelliJ IDEA nécessite une configuration manuelle ou des plugins pour obtenir une fonctionnalité similaire.
-   **VS Code** : Suivre un fichier journal dans VS Code est léger et manuel, l'approche du curseur à la fin étant simple pour une inspection rapide des journaux. Les onglets de journal ou le terminal d'IntelliJ IDEA sont plus intégrés mais moins flexibles pour le placement manuel du curseur.
-   **Effacement des journaux** :
    - Eclipse : Bouton d'effacement en un clic dans la console.
    - IntelliJ IDEA : Utilisez **Skip Content** ou redémarrez la commande `tail` du terminal.
    - VS Code : Effacez manuellement le terminal ou redémarrez `tail -f`.
-   **Visualisation des journaux en temps réel** :
    - Les trois IDE prennent en charge la visualisation des journaux en temps réel, mais l'onglet de journal d'IntelliJ IDEA nécessite un fichier monté ou un plugin, tandis que VS Code repose sur des commandes terminal.

---

### Recommandations
1.  **Approche préférée** : Utilisez **l'Option 1 (Dossier monté)** pour l'expérience la plus proche de la console d'Eclipse. Elle intègre les journaux dans la fenêtre d'outil Debug, prend en charge le défilement automatique et permet le filtrage. L'option **Skip Content** imite l'effacement des journaux.
2.  **Pour une simplicité de type VS Code** : Utilisez **l'Option 2 (Terminal SSH)** avec `tail -f` pour une expérience légère de type curseur à la fin. Combinez avec `grep` pour filtrer les journaux déclenchés par le frontend.
3.  **Améliorez avec des plugins** : Installez **Grep Console** pour un meilleur filtrage et une meilleure mise en évidence des journaux, en particulier pour les journaux spécifiques au frontend.
4.  **Note sur les performances** : Si le serveur distant a un volume de journaux élevé, le montage ou la copie des journaux peut être plus lent que le suivi via SSH. Testez les deux approches pour trouver la meilleure adaptée.

---

### Dépannage
-   **Onglet de journal vide** : Assurez-vous que le chemin du fichier journal est correct et accessible. Si vous utilisez un dossier monté, vérifiez que le montage est actif. Si vous utilisez SSH, vérifiez la syntaxe de la commande `tail -f`.
-   **Les journaux ne se mettent pas à jour** : Confirmez que le serveur Liberty écrit dans le fichier journal spécifié (par exemple, `messages.log`). Vérifiez les permissions de fichier ou les problèmes de journaux rotatifs.
-   **Aucun journal frontend** : Vérifiez que les actions frontend atteignent le backend (utilisez des points d'arrêt) et que le framework de journalisation (par exemple, SLF4J) est configuré pour sortir les messages pertinents.
-   **Problèmes de plugin** : Si Log4JPlugin ou Grep Console ne fonctionne pas, assurez-vous qu'ils sont compatibles avec votre version d'IntelliJ IDEA (par exemple, 2024.1 ou ultérieure).

---

### Exemple de workflow
1.  Configurez la Remote JVM Debug avec le fichier journal `/path/to/mounted/wlp/usr/servers/defaultServer/logs/messages.log`.
2.  Démarrez la session de débogage.
3.  Ouvrez la fenêtre d'outil **Debug**, basculez vers l'onglet "Liberty Logs" et activez **Scroll to the end**.
4.  Cliquez sur un bouton frontend pour déclencher une requête backend.
5.  Surveillez l'onglet de journal pour les nouvelles entrées (par exemple, "INFO [frontend] Button clicked").
6.  Utilisez la barre de recherche pour filtrer les mots-clés spécifiques ou sélectionnez les nouvelles lignes de journal pour inspection.
7.  Si nécessaire, arrêtez et redémarrez la session de débogage avec **Skip Content** activé pour effacer les anciens journaux.

---

### Notes supplémentaires
-   **Journaux spécifiques à Liberty** : WebSphere Liberty écrit généralement dans `messages.log` ou `console.log` dans `wlp/usr/servers/<nomDuServeur>/logs`. Assurez-vous que votre Run/Debug Configuration pointe vers le bon fichier.
-   **Corrélation Frontend-Backend** : Si les clics frontend ne produisent pas les journaux attendus, vérifiez la configuration de journalisation du point de terminaison backend (par exemple, assurez-vous que les instructions `logger.info()` existent).
-   **Outils alternatifs** : Si la visualisation des journaux d'IntelliJ n'est pas satisfaisante, envisagez d'exécuter `tail -f` dans un terminal ou VS Code séparé à côté d'IntelliJ pour la surveillance des journaux, tout en utilisant IntelliJ pour le débogage.

Si vous avez besoin d'aide pour des étapes de configuration spécifiques, la configuration de plugins ou le filtrage des journaux pour une action frontend particulière, veuillez fournir plus de détails (par exemple, version de Liberty, chemin du fichier journal ou technologie frontend), et je pourrai adapter les instructions davantage !