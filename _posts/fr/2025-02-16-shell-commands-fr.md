---
audio: false
generated: true
lang: fr
layout: post
title: Commandes Shell macOS
translated: true
---

Voici 200 commandes couramment utilisées pour le shell macOS, catégorisées pour une référence plus facile. Ces commandes sont utiles pour naviguer dans le système de fichiers, gérer les fichiers, surveiller le système, et bien plus encore.

### Navigation dans le système de fichiers
- `ls` - Lister le contenu d'un répertoire.
- `cd` - Changer de répertoire courant.
- `pwd` - Afficher le répertoire de travail courant.
- `tree` - Afficher les répertoires sous forme d'arbres (si installé).

### Opérations sur les fichiers
- `cp` - Copier des fichiers ou des répertoires.
- `mv` - Déplacer ou renommer des fichiers ou des répertoires.
- `rm` - Supprimer des fichiers ou des répertoires.
- `touch` - Créer un fichier vide ou mettre à jour l'horodatage.
- `mkdir` - Créer un nouveau répertoire.
- `rmdir` - Supprimer un répertoire vide.
- `ln` - Créer des liens durs et symboliques.
- `chmod` - Modifier les permissions des fichiers.
- `chown` - Modifier le propriétaire et le groupe des fichiers.
- `cat` - Concatener et afficher le contenu des fichiers.
- `less` - Afficher le contenu des fichiers page par page.
- `more` - Afficher le contenu des fichiers page par page.
- `head` - Afficher les premières lignes d'un fichier.
- `tail` - Afficher les dernières lignes d'un fichier.
- `nano` - Éditer des fichiers texte.
- `vi` - Éditer des fichiers texte.
- `vim` - Éditer des fichiers texte (version améliorée de `vi`).
- `find` - Rechercher des fichiers dans une hiérarchie de répertoires.
- `locate` - Trouver rapidement des fichiers par nom.
- `grep` - Rechercher du texte en utilisant des motifs.
- `diff` - Comparer des fichiers ligne par ligne.
- `file` - Déterminer le type de fichier.
- `stat` - Afficher le statut d'un fichier ou d'un système de fichiers.
- `du` - Estimer l'utilisation de l'espace disque par les fichiers.
- `df` - Afficher l'utilisation de l'espace disque des systèmes de fichiers.
- `dd` - Convertir et copier un fichier.
- `tar` - Stocker, lister ou extraire des fichiers dans une archive.
- `gzip` - Compresser ou décompresser des fichiers.
- `gunzip` - Décompresser des fichiers compressés avec gzip.
- `zip` - Emballer et compresser des fichiers.
- `unzip` - Extraire des fichiers compressés dans une archive ZIP.
- `rsync` - Synchronisation de fichiers et de répertoires à distance.
- `scp` - Copier des fichiers de manière sécurisée entre des hôtes.
- `curl` - Transférer des données vers ou depuis un serveur.
- `wget` - Télécharger des fichiers depuis le web.

### Informations système
- `uname` - Afficher les informations système.
- `top` - Afficher les processus système.
- `htop` - Visionneuse de processus interactive (si installé).
- `ps` - Fournir un instantané des processus en cours.
- `kill` - Envoyer un signal à un processus.
- `killall` - Tuer des processus par nom.
- `bg` - Exécuter des tâches en arrière-plan.
- `fg` - Exécuter des tâches en premier plan.
- `jobs` - Lister les tâches actives.
- `nice` - Exécuter un programme avec une priorité de planification modifiée.
- `renice` - Modifier la priorité des processus en cours d'exécution.
- `time` - Chronométrer l'exécution d'une commande.
- `uptime` - Afficher le temps d'exécution du système.
- `who` - Afficher qui est connecté.
- `w` - Afficher qui est connecté et ce qu'ils font.
- `whoami` - Afficher le nom de l'utilisateur actuel.
- `id` - Afficher les informations utilisateur et groupe.
- `groups` - Afficher les groupes auxquels appartient un utilisateur.
- `passwd` - Changer le mot de passe de l'utilisateur.
- `sudo` - Exécuter une commande en tant qu'un autre utilisateur.
- `su` - Basculer d'utilisateur.
- `chroot` - Exécuter une commande avec un répertoire racine différent.
- `hostname` - Afficher ou définir le nom d'hôte du système.
- `ifconfig` - Configurer une interface réseau.
- `ping` - Envoyer une requête ICMP ECHO_REQUEST aux hôtes réseau.
- `traceroute` - Tracer la route vers un hôte réseau.
- `netstat` - Statistiques réseau.
- `route` - Afficher ou manipuler la table de routage IP.
- `dig` - Utilitaire de recherche DNS.
- `nslookup` - Interroger les serveurs de noms Internet de manière interactive.
- `host` - Utilitaire de recherche DNS.
- `ftp` - Programme de transfert de fichiers Internet.
- `ssh` - Client SSH OpenSSH.
- `telnet` - Interface utilisateur du protocole TELNET.
- `nc` - Netcat, connexions et écoutes TCP et UDP arbitraires.
- `iftop` - Afficher l'utilisation de la bande passante sur une interface (si installé).
- `nmap` - Outil d'exploration réseau et scanner de ports de sécurité (si installé).

### Gestion des disques
- `mount` - Monter un système de fichiers.
- `umount` - Démonter un système de fichiers.
- `fdisk` - Manipulateur de table de partition pour Linux.
- `mkfs` - Construire un système de fichiers Linux.
- `fsck` - Vérifier et réparer un système de fichiers Linux.
- `df` - Afficher l'utilisation de l'espace disque des systèmes de fichiers.
- `du` - Estimer l'utilisation de l'espace disque par les fichiers.
- `sync` - Synchroniser les écritures en cache avec le stockage persistant.
- `dd` - Convertir et copier un fichier.
- `hdparm` - Obtenir/définir les paramètres du disque dur.
- `smartctl` - Contrôler et surveiller les disques ATA/SCSI-3 activés SMART (si installé).

### Gestion des paquets
- `brew` - Gestionnaire de paquets Homebrew (si installé).
- `port` - Gestionnaire de paquets MacPorts (si installé).
- `gem` - Gestionnaire de paquets RubyGems.
- `pip` - Installeur de paquets Python.
- `npm` - Gestionnaire de paquets Node.js.
- `cpan` - Gestionnaire de paquets Perl.

### Traitement de texte
- `awk` - Langage de balayage et de traitement de motifs.
- `sed` - Éditeur de flux pour filtrer et transformer le texte.
- `sort` - Trier les lignes de fichiers texte.
- `uniq` - Signaler ou omettre les lignes répétées.
- `cut` - Supprimer des sections de chaque ligne de fichiers.
- `paste` - Fusionner les lignes de fichiers.
- `join` - Joindre les lignes de deux fichiers sur un champ commun.
- `tr` - Traduire ou supprimer des caractères.
- `iconv` - Convertir du texte d'un encodage à un autre.
- `strings` - Trouver des chaînes imprimables dans des fichiers.
- `wc` - Afficher le nombre de nouvelles lignes, de mots et d'octets pour chaque fichier.
- `nl` - Numéroter les lignes de fichiers.
- `od` - Dump des fichiers dans divers formats.
- `xxd` - Faire un hexdump ou l'inverse.

### Scripting shell
- `echo` - Afficher une ligne de texte.
- `printf` - Formater et imprimer des données.
- `test` - Évaluer une expression.
- `expr` - Évaluer des expressions.
- `read` - Lire une ligne depuis l'entrée standard.
- `export` - Définir une variable d'environnement.
- `unset` - Annuler les valeurs et attributs des variables et fonctions de shell.
- `alias` - Créer un alias pour une commande.
- `unalias` - Supprimer un alias.
- `source` - Exécuter des commandes à partir d'un fichier dans le shell actuel.
- `exec` - Exécuter une commande.
- `trap` - Piéger les signaux et autres événements.
- `set` - Définir ou annuler les options et paramètres positionnels du shell.
- `shift` - Décaler les paramètres positionnels.
- `getopts` - Analyser les paramètres positionnels.
- `type` - Décrire une commande.
- `which` - Localiser une commande.
- `whereis` - Localiser les fichiers binaires, sources et pages de manuel d'une commande.

### Outils de développement
- `gcc` - Compilateur C et C++ du projet GNU.
- `make` - Processeur de makefile orienté répertoire.
- `cmake` - Générateur de makefile multiplateforme.
- `autoconf` - Générer des scripts de configuration.
- `automake` - Générer des fichiers Makefile.in.
- `ld` - Le linker GNU.
- `ar` - Créer, modifier et extraire des archives.
- `nm` - Lister les symboles des fichiers objets.
- `objdump` - Afficher des informations à partir des fichiers objets.
- `strip` - Supprimer les symboles des fichiers objets.
- `ranlib` - Générer un index pour une archive.
- `gdb` - Le débogueur GNU.
- `lldb` - Le débogueur LLVM.
- `valgrind` - Framework d'instrumentation pour construire des outils d'analyse dynamique (si installé).
- `strace` - Traquer les appels système et les signaux (si installé).
- `ltrace` - Traquer les appels de bibliothèque (si installé).
- `perf` - Outils d'analyse des performances pour Linux.
- `time` - Chronométrer l'exécution d'une commande.
- `xargs` - Construire et exécuter des lignes de commande à partir de l'entrée standard.
- `m4` - Processeur de macros.
- `cpp` - Le préprocesseur C.
- `flex` - Générateur rapide d'analyseur lexical.
- `bison` - Générateur de parseur compatible avec Yacc.
- `bc` - Langage de calcul à précision arbitraire.
- `dc` - Calculatrice à précision arbitraire.

### Contrôle de version
- `git` - Système de contrôle de version distribué.
- `svn` - Système de contrôle de version Subversion.
- `hg` - Système de contrôle de version distribué Mercurial.
- `cvs` - Système de versions concurrentes.

### Divers
- `man` - Formater et afficher les pages de manuel en ligne.
- `info` - Lire les documents Info.
- `apropos` - Rechercher les noms et descriptions des pages de manuel.
- `whatis` - Afficher les descriptions d'une ligne de page de manuel.
- `history` - Afficher ou manipuler la liste d'historique.
- `yes` - Sortir une chaîne de manière répétée jusqu'à ce qu'elle soit tuée.
- `cal` - Afficher un calendrier.
- `date` - Afficher ou définir la date et l'heure.
- `sleep` - Attendre un certain temps.
- `watch` - Exécuter un programme périodiquement, affichant la sortie en plein écran.
- `xargs` - Construire et exécuter des lignes de commande à partir de l'entrée standard.
- `seq` - Afficher une séquence de nombres.
- `shuf` - Générer des permutations aléatoires.
- `tee` - Lire à partir de l'entrée standard et écrire vers la sortie standard et les fichiers.
- `tput` - Initialiser un terminal ou interroger la base de données terminfo.
- `stty` - Changer et afficher les paramètres de la ligne terminal.
- `clear` - Effacer l'écran du terminal.
- `reset` - Réinitialiser le terminal à un état sain.
- `script` - Créer un typescript de la session terminal.
- `wall` - Écrire un message à tous les utilisateurs.
- `write` - Envoyer un message à un autre utilisateur.
- `mesg` - Contrôler l'accès à l'écriture de votre terminal.
- `talk` - Parler à un autre utilisateur.
- `ytalk` - Un autre programme de discussion (si installé).
- `crontab` - Maintenir les fichiers crontab pour les utilisateurs individuels.
- `at` - Planifier l'exécution de commandes une fois à un moment ultérieur.
- `batch` - Planifier l'exécution de commandes dans une file d'attente de traitement par lots.
- `nice` - Exécuter un programme avec une priorité de planification modifiée.
- `renice` - Modifier la priorité des processus en cours d'exécution.
- `time` - Chronométrer l'exécution d'une commande.
- `ulimit` - Définir ou signaler les limites de ressources utilisateur.
- `pr` - Convertir les fichiers texte pour l'impression.
- `lp` - Envoyer des fichiers à une imprimante.
- `lpr` - Imprimer des fichiers.
- `lpq` - Afficher le statut de la file d'attente d'impression.
- `lprm` - Supprimer des travaux de la file d'attente d'impression.
- `enscript` - Convertir du texte en PostScript, HTML ou RTF, avec mise en évidence de la syntaxe (si installé).
- `a2ps` - Filtre Any to PostScript.
- `ps2pdf` - Convertir PostScript en PDF.
- `pdf2ps` - Convertir PDF en PostScript.
- `gs` - Interpréteur Ghostscript.
- `convert` - Convertir entre différents formats d'image (si installé).
- `mogrify` - Redimensionner, faire pivoter et transformer des images (si installé).
- `exiftool` - Lire, écrire et éditer les métadonnées des fichiers (si installé).
- `jpegoptim` - Optimiser les fichiers JPEG (si installé).
- `optipng` - Optimiser les fichiers PNG (si installé).

Ces commandes couvrent une large gamme de fonctionnalités et sont essentielles pour les utilisateurs qui souhaitent gérer et interagir efficacement avec leur système macOS via le terminal.