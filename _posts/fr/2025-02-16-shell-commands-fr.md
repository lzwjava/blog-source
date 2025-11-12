---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Commandes shell macOS
translated: true
type: note
---

Voici 200 commandes shell macOS couramment utilisées, classées par catégorie pour une référence plus facile. Ces commandes sont utiles pour naviguer dans le système de fichiers, gérer les fichiers, surveiller le système, et plus encore.

### Navigation dans le système de fichiers
- `ls` - Lister le contenu d'un répertoire.
- `cd` - Changer le répertoire courant.
- `pwd` - Afficher le répertoire de travail courant.
- `tree` - Afficher les répertoires sous forme d'arbres (s'il est installé).

### Opérations sur les fichiers
- `cp` - Copier des fichiers ou des répertoires.
- `mv` - Déplacer ou renommer des fichiers ou des répertoires.
- `rm` - Supprimer des fichiers ou des répertoires.
- `touch` - Créer un fichier vide ou mettre à jour son horodatage.
- `mkdir` - Créer un nouveau répertoire.
- `rmdir` - Supprimer un répertoire vide.
- `ln` - Créer des liens physiques et symboliques.
- `chmod` - Modifier les permissions d'un fichier.
- `chown` - Modifier le propriétaire et le groupe d'un fichier.
- `cat` - Concaténer et afficher le contenu d'un fichier.
- `less` - Voir le contenu d'un fichier page par page.
- `more` - Voir le contenu d'un fichier page par page.
- `head` - Afficher les premières lignes d'un fichier.
- `tail` - Afficher les dernières lignes d'un fichier.
- `nano` - Éditer des fichiers texte.
- `vi` - Éditer des fichiers texte.
- `vim` - Éditer des fichiers texte (version améliorée de `vi`).
- `find` - Rechercher des fichiers dans une hiérarchie de répertoires.
- `locate` - Trouver rapidement des fichiers par nom.
- `grep` - Rechercher du texte à l'aide de motifs.
- `diff` - Comparer des fichiers ligne par ligne.
- `file` - Déterminer le type d'un fichier.
- `stat` - Afficher l'état d'un fichier ou d'un système de fichiers.
- `du` - Estimer l'utilisation de l'espace disque des fichiers.
- `df` - Afficher l'utilisation de l'espace disque du système de fichiers.
- `dd` - Convertir et copier un fichier.
- `tar` - Stocker, lister ou extraire des fichiers dans une archive.
- `gzip` - Compresser ou décompresser des fichiers.
- `gunzip` - Décompresser des fichiers compressés avec gzip.
- `zip` - Empaqueter et compresser des fichiers.
- `unzip` - Extraire des fichiers compressés dans une archive ZIP.
- `rsync` - Synchronisation à distance de fichiers et de répertoires.
- `scp` - Copie sécurisée de fichiers entre hôtes.
- `curl` - Transférer des données depuis ou vers un serveur.
- `wget` - Télécharger des fichiers depuis le web.

### Informations système
- `uname` - Afficher des informations sur le système.
- `top` - Afficher les processus système.
- `htop` - Visualiseur de processus interactif (s'il est installé).
- `ps` - Afficher un instantané des processus courants.
- `kill` - Envoyer un signal à un processus.
- `killall` - Tuer des processus par nom.
- `bg` - Exécuter des tâches en arrière-plan.
- `fg` - Exécuter des tâches au premier plan.
- `jobs` - Lister les tâches actives.
- `nice` - Exécuter un programme avec une priorité d'ordonnancement modifiée.
- `renice` - Modifier la priorité des processus en cours d'exécution.
- `time` - Chronométrer l'exécution d'une commande.
- `uptime` - Afficher depuis combien de temps le système est en fonctionnement.
- `who` - Afficher qui est connecté.
- `w` - Afficher qui est connecté et ce qu'il fait.
- `whoami` - Afficher le nom de l'utilisateur courant.
- `id` - Afficher les informations sur l'utilisateur et le groupe.
- `groups` - Afficher les groupes auxquels appartient un utilisateur.
- `passwd` - Modifier le mot de passe utilisateur.
- `sudo` - Exécuter une commande en tant qu'un autre utilisateur.
- `su` - Changer d'utilisateur.
- `chroot` - Exécuter une commande avec un répertoire racine différent.
- `hostname` - Afficher ou définir le nom d'hôte du système.
- `ifconfig` - Configurer une interface réseau.
- `ping` - Envoyer une requête ICMP ECHO_REQUEST à des hôtes du réseau.
- `traceroute` - Tracer la route vers un hôte réseau.
- `netstat` - Statistiques réseau.
- `route` - Afficher ou manipuler la table de routage IP.
- `dig` - Utilitaire de recherche DNS.
- `nslookup` - Interroger interactivement les serveurs de noms Internet.
- `host` - Utilitaire de recherche DNS.
- `ftp` - Programme de transfert de fichiers Internet.
- `ssh` - Client SSH OpenSSH.
- `telnet` - Interface utilisateur pour le protocole TELNET.
- `nc` - Netcat, connexions et écoutes TCP et UDP arbitraires.
- `iftop` - Afficher l'utilisation de la bande passante sur une interface (s'il est installé).
- `nmap` - Outil d'exploration réseau et scanneur de sécurité/ports (s'il est installé).

### Gestion des disques
- `mount` - Monter un système de fichiers.
- `umount` - Démontrer un système de fichiers.
- `fdisk` - Manipulateur de table de partition pour Linux.
- `mkfs` - Construire un système de fichiers Linux.
- `fsck` - Vérifier et réparer un système de fichiers Linux.
- `df` - Afficher l'utilisation de l'espace disque du système de fichiers.
- `du` - Estimer l'utilisation de l'espace disque des fichiers.
- `sync` - Synchroniser les écritures en cache vers le stockage persistant.
- `dd` - Convertir et copier un fichier.
- `hdparm` - Obtenir/définir les paramètres du disque dur.
- `smartctl` - Contrôler et surveiller les disques ATA/SCSI-3 compatibles SMART (s'il est installé).

### Gestion des paquets
- `brew` - Gestionnaire de paquets Homebrew (s'il est installé).
- `port` - Gestionnaire de paquets MacPorts (s'il est installé).
- `gem` - Gestionnaire de paquets RubyGems.
- `pip` - Installateur de paquets Python.
- `npm` - Gestionnaire de paquets Node.js.
- `cpan` - Gestionnaire de paquets Perl.

### Traitement de texte
- `awk` - Langage d'analyse et de traitement de motifs.
- `sed` - Éditeur de flux pour filtrer et transformer le texte.
- `sort` - Trier les lignes des fichiers texte.
- `uniq` - Signaler ou omettre les lignes répétées.
- `cut` - Supprimer des sections de chaque ligne de fichiers.
- `paste` - Fusionner les lignes de fichiers.
- `join` - Joindre les lignes de deux fichiers sur un champ commun.
- `tr` - Traduire ou supprimer des caractères.
- `iconv` - Convertir le texte d'un encodage à un autre.
- `strings` - Trouver les chaînes de caractères imprimables dans les fichiers.
- `wc` - Afficher le nombre de lignes, de mots et d'octets pour chaque fichier.
- `nl` - Numéroter les lignes des fichiers.
- `od` - Dumper des fichiers dans divers formats.
- `xxd` - Créer un hexdump ou faire l'opération inverse.

### Scripting shell
- `echo` - Afficher une ligne de texte.
- `printf` - Formater et afficher des données.
- `test` - Évaluer une expression.
- `expr` - Évaluer des expressions.
- `read` - Lire une ligne depuis l'entrée standard.
- `export` - Définir une variable d'environnement.
- `unset` - Supprimer les valeurs et attributs des variables et fonctions du shell.
- `alias` - Créer un alias pour une commande.
- `unalias` - Supprimer un alias.
- `source` - Exécuter les commandes d'un fichier dans le shell courant.
- `exec` - Exécuter une commande.
- `trap` - Intercepter des signaux et autres événements.
- `set` - Définir ou supprimer les options du shell et les paramètres positionnels.
- `shift` - Décaler les paramètres positionnels.
- `getopts` - Analyser les paramètres positionnels.
- `type` - Décrire une commande.
- `which` - Localiser une commande.
- `whereis` - Localiser les fichiers binaires, source et de manuel pour une commande.

### Outils de développement
- `gcc` - Compilateur C et C++ du projet GNU.
- `make` - Processeur de makefile orienté répertoire.
- `cmake` - Générateur de makefile multiplateforme.
- `autoconf` - Générer des scripts de configuration.
- `automake` - Générer des fichiers Makefile.in.
- `ld` - L'éditeur de liens GNU.
- `ar` - Créer, modifier et extraire des archives.
- `nm` - Lister les symboles des fichiers objets.
- `objdump` - Afficher les informations des fichiers objets.
- `strip` - Supprimer les symboles des fichiers objets.
- `ranlib` - Générer un index pour une archive.
- `gdb` - Le débogueur GNU.
- `lldb` - Le débogueur LLVM.
- `valgrind` - Cadre d'instrumentation pour construire des outils d'analyse dynamique (s'il est installé).
- `strace` - Tracer les appels système et les signaux (s'il est installé).
- `ltrace` - Tracer les appels de bibliothèque (s'il est installé).
- `perf` - Outils d'analyse de performance pour Linux.
- `time` - Chronométrer l'exécution d'une commande.
- `xargs` - Construire et exécuter des lignes de commande à partir de l'entrée standard.
- `m4` - Processeur de macros.
- `cpp` - Le préprocesseur C.
- `flex` - Générateur d'analyseur lexical rapide.
- `bison` - Générateur d'analyseur syntaxique compatible Yacc.
- `bc` - Un langage de calculatrice à précision arbitraire.
- `dc` - Une calculatrice à précision arbitraire.

### Contrôle de version
- `git` - Système de contrôle de version distribué.
- `svn` - Système de contrôle de version Subversion.
- `hg` - Système de contrôle de version distribué Mercurial.
- `cvs` - Système de versions concurrentes.

### Divers
- `man` - Formater et afficher les pages de manuel en ligne.
- `info` - Lire les documents Info.
- `apropos` - Rechercher dans les noms et descriptions des pages de manuel.
- `whatis` - Afficher les descriptions en une ligne des pages de manuel.
- `history` - Afficher ou manipuler la liste d'historique.
- `yes` - Afficher une chaîne de caractères répétitivement jusqu'à l'arrêt.
- `cal` - Afficher un calendrier.
- `date` - Afficher ou définir la date et l'heure.
- `sleep` - Mettre en pause pendant une durée spécifiée.
- `watch` - Exécuter un programme périodiquement, en affichant le résultat en plein écran.
- `xargs` - Construire et exécuter des lignes de commande à partir de l'entrée standard.
- `seq` - Afficher une séquence de nombres.
- `shuf` - Générer des permutations aléatoires.
- `tee` - Lire depuis l'entrée standard et écrire vers la sortie standard et les fichiers.
- `tput` - Initialiser un terminal ou interroger la base de données terminfo.
- `stty` - Changer et afficher les paramètres de ligne du terminal.
- `clear` - Effacer l'écran du terminal.
- `reset` - Réinitialiser le terminal à un état sain.
- `script` - Créer un enregistrement de la session terminal.
- `wall` - Écrire un message à tous les utilisateurs.
- `write` - Envoyer un message à un autre utilisateur.
- `mesg` - Contrôler l'accès en écriture à votre terminal.
- `talk` - Parler à un autre utilisateur.
- `ytalk` - Encore un autre programme de discussion (s'il est installé).
- `crontab` - Maintenir les fichiers crontab pour les utilisateurs individuels.
- `at` - Planifier l'exécution de commandes à une heure ultérieure.
- `batch` - Planifier l'exécution de commandes dans une file d'attente par lots.
- `nice` - Exécuter un programme avec une priorité d'ordonnancement modifiée.
- `renice` - Modifier la priorité des processus en cours d'exécution.
- `time` - Chronométrer l'exécution d'une commande.
- `ulimit` - Définir ou afficher les limites de ressources utilisateur.
- `pr` - Convertir les fichiers texte pour l'impression.
- `lp` - Envoyer des fichiers à une imprimante.
- `lpr` - Imprimer des fichiers.
- `lpq` - Afficher le statut de la file d'attente d'impression.
- `lprm` - Supprimer les travaux de la file d'attente d'impression.
- `enscript` - Convertir le texte en PostScript, HTML ou RTF, avec coloration syntaxique (s'il est installé).
- `a2ps` - Filtre Any to PostScript.
- `ps2pdf` - Convertir PostScript en PDF.
- `pdf2ps` - Convertir PDF en PostScript.
- `gs` - Interpréteur Ghostscript.
- `convert` - Convertir entre les formats d'image (s'il est installé).
- `mogrify` - Redimensionner, faire pivoter et transformer des images (s'il est installé).
- `exiftool` - Lire, écrire et modifier les métadonnées dans les fichiers (s'il est installé).
- `jpegoptim` - Optimiser les fichiers JPEG (s'il est installé).
- `optipng` - Optimiser les fichiers PNG (s'il est installé).

Ces commandes couvrent un large éventail de fonctionnalités et sont essentielles pour les utilisateurs qui souhaitent gérer et interagir efficacement avec leur système macOS via le terminal.