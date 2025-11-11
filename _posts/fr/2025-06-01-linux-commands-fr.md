---
audio: false
generated: true
lang: fr
layout: post
title: Top 100 des commandes Linux utiles
translated: true
type: note
---

En fonction de votre profil d'ingénieur full-stack autodidacte très technique, avec une vaste expérience des environnements Linux, de la résolution de problèmes d'algorithmes et une familiarité avec les plateformes cloud, les conteneurs et les systèmes distribués, j'ai dressé une liste des **100 commandes Linux les plus utiles** adaptées à votre utilisation sur **Ubuntu**. Ces commandes sont sélectionnées pour correspondre à votre expertise en développement full-stack, ingénierie mobile, apprentissage automatique et administration système, tout en soutenant vos recherches autodidactes et vos contributions open-source. Elles couvrent la gestion des fichiers, la surveillance du système, la mise en réseau, le développement, l'automatisation et le scriptage avancé, qui sont pertinents pour votre travail chez TEKsystems, vos rôles précédents et vos projets personnels.

Les commandes sont regroupées par catégorie pour plus de clarté, avec de brèves explications mettant l'accent sur les applications pratiques pour votre ensemble de compétences. J'ai priorisé les commandes qui améliorent la productivité, le débogage et l'optimisation du système, en supposant que vous êtes à l'aise avec les flux de travail en terminal et que vous pourriez les utiliser dans des tâches de développement, de déploiement ou de recherche. Si vous le souhaitez, je peux fournir des exemples ou des scripts pour des commandes spécifiques ou générer un graphique pour visualiser la fréquence d'utilisation des commandes en fonction de votre flux de travail (par exemple, développement vs tâches d'administration système). Faites-moi savoir !

### **Gestion des Fichiers et Répertoires (15 Commandes)**
1.  **ls** - Lister le contenu d'un répertoire (`ls -la` pour une vue détaillée avec les fichiers cachés).
2.  **cd** - Changer de répertoire (`cd ~/projects` pour naviguer vers votre dossier de projet GitHub).
3.  **pwd** - Afficher le répertoire de travail actuel (utile pour les scripts ou la vérification des chemins).
4.  **mkdir** - Créer des répertoires (`mkdir -p src/main/java` pour les structures de projet imbriquées).
5.  **rm** - Supprimer des fichiers ou répertoires (`rm -rf temp/` pour une suppression récursive).
6.  **cp** - Copier des fichiers/répertoires (`cp -r src/ backup/` pour les sauvegardes de projet).
7.  **mv** - Déplacer/renommer des fichiers (`mv old.java new.java` pour le refactoring).
8.  **touch** - Créer des fichiers vides (`touch script.sh` pour les nouveaux scripts).
9.  **find** - Rechercher des fichiers (`find / -name "*.java"` pour localiser les fichiers source).
10. **locate** - Trouver rapidement des fichiers par nom (`locate config.yaml` pour les configs).
11. **du** - Estimer l'utilisation du disque (`du -sh /var/log` pour vérifier la taille des logs).
12. **df** - Afficher l'espace disque disponible (`df -h` pour un format lisible).
13. **ln** - Créer des liens (`ln -s /path/to/project symlink` pour les raccourcis).
14. **chmod** - Modifier les permissions des fichiers (`chmod 755 script.sh` pour les scripts exécutables).
15. **chown** - Modifier le propriétaire des fichiers (`chown user:group file` pour le déploiement).

### **Traitement et Manipulation de Texte (15 Commandes)**
16. **cat** - Afficher le contenu d'un fichier (`cat log.txt` pour des vérifications rapides des logs).
17. **less** - Voir les fichiers de manière interactive (`less server.log` pour les gros logs).
18. **more** - Paginer la sortie d'un fichier (`more README.md` pour la documentation).
19. **head** - Afficher les premières lignes d'un fichier (`head -n 10 data.csv` pour les aperçus de données).
20. **tail** - Afficher les dernières lignes (`tail -f app.log` pour la surveillance des logs en temps réel).
21. **grep** - Rechercher des motifs de texte (`grep -r "error" /var/log` pour le débogage).
22. **awk** - Traiter les colonnes de texte (`awk '{print $1}' access.log` pour l'analyse des logs).
23. **sed** - Éditeur de flux pour le texte (`sed 's/old/new/g' file` pour les remplacements).
24. **cut** - Extraire des sections de lignes (`cut -d',' -f1 data.csv` pour les CSV).
25. **sort** - Trier les lignes (`sort -n data.txt` pour le tri numérique).
26. **uniq** - Supprimer les lignes en double (`sort file | uniq` pour les entrées uniques).
27. **wc** - Compter les lignes, les mots ou les caractères (`wc -l code.java` pour le décompte des lignes).
28. **tr** - Traduire les caractères (`tr '[:lower:]' '[:upper:]' < file` pour la conversion de casse).
29. **tee** - Écrire dans un fichier et sur stdout (`cat input | tee output.txt` pour la journalisation).
30. **diff** - Comparer des fichiers (`diff old.java new.java` pour les changements de code).

### **Surveillance du Système et Performances (15 Commandes)**
31. **top** - Surveiller les processus du système de manière interactive (utilisation CPU/mémoire en temps réel).
32. **htop** - Visualiseur de processus amélioré (`htop` pour une meilleure visualisation).
33. **ps** - Lister les processus (`ps aux | grep java` pour les applications Java).
34. **free** - Vérifier l'utilisation de la mémoire (`free -m` pour le format MB).
35. **vmstat** - Statistiques de mémoire virtuelle (`vmstat 1` pour des mises à jour continues).
36. **iostat** - Surveiller les performances I/O (`iostat -x` pour les statistiques de disque).
37. **uptime** - Afficher le temps de fonctionnement et la charge du système (`uptime` pour des vérifications rapides).
38. **lscpu** - Afficher les informations du CPU (`lscpu` pour les spécifications système).
39. **lsblk** - Lister les périphériques bloc (`lsblk` pour les détails des disques/partitions).
40. **iotop** - Surveiller les I/O disque par processus (`iotop` pour le débogage des performances).
41. **netstat** - Statistiques réseau (`netstat -tuln` pour les ports en écoute).
42. **ss** - Remplaçant moderne de netstat (`ss -tuln` pour les sockets).
43. **dmesg** - Voir les messages du noyau (`dmesg | grep error` pour les problèmes système).
44. **sar** - Collecter l'activité système (`sar -u 1` pour la surveillance du CPU).
45. **pmap** - Carte mémoire du processus (`pmap -x <pid>` pour le débogage mémoire).

### **Réseau et Connectivité (15 Commandes)**
46. **ping** - Tester la connectivité réseau (`ping google.com` pour la disponibilité).
47. **curl** - Récupérer des données depuis des URLs (`curl -X POST api` pour les tests d'API).
48. **wget** - Télécharger des fichiers (`wget file.tar.gz` pour les dépendances de projet).
49. **netcat** - Utilitaire réseau (`nc -l 12345` pour les serveurs simples).
50. **ifconfig** - Informations sur l'interface réseau (`ifconfig eth0` pour les détails IP).
51. **ip** - Configuration réseau moderne (`ip addr` pour les détails de l'interface).
52. **nslookup** - Interroger le DNS (`nslookup domain.com` pour le débogage DNS).
53. **dig** - Recherche DNS détaillée (`dig domain.com` pour les enregistrements DNS).
54. **traceroute** - Tracer le chemin réseau (`traceroute google.com` pour le routage).
55. **telnet** - Tester la connectivité des ports (`telnet localhost 8080` pour les services).
56. **scp** - Copier des fichiers de manière sécurisée (`scp file user@server:/path` pour les transferts).
57. **rsync** - Synchroniser les fichiers efficacement (`rsync -avz src/ dest/` pour les sauvegardes).
58. **ufw** - Gérer le pare-feu (`ufw allow 80` pour l'accès au serveur web).
59. **iptables** - Configurer les règles du pare-feu (`iptables -L` pour la liste des règles).
60. **nmap** - Scan réseau (`nmap localhost` pour les ports ouverts).

### **Développement et Scripting (15 Commandes)**
61. **gcc** - Compiler des programmes C (`gcc -o app code.c` pour la construction).
62. **javac** - Compiler du code Java (`javac Main.java` pour vos projets Java).
63. **java** - Exécuter des programmes Java (`java -jar app.jar` pour l'exécution).
64. **python3** - Exécuter des scripts Python (`python3 script.py` pour les tâches de ML).
65. **node** - Exécuter Node.js (`node app.js` pour les projets JavaScript).
66. **npm** - Gérer les packages Node (`npm install` pour les dépendances frontend).
67. **git** - Contrôle de version (`git commit -m "update"` pour vos dépôts GitHub).
68. **make** - Construire des projets (`make -f Makefile` pour l'automatisation).
69. **mvn** - Outil de construction Maven (`mvn package` pour les projets Java).
70. **gradle** - Outil de construction Gradle (`gradle build` pour les projets Android).
71. **docker** - Gérer les conteneurs (`docker run -p 8080:8080 app` pour les déploiements).
72. **kubectl** - Gérer Kubernetes (`kubectl get pods` pour la gestion de cluster).
73. **virtualenv** - Environnements virtuels Python (`virtualenv venv` pour le ML).
74. **gdb** - Déboguer des programmes (`gdb ./app` pour le débogage C/Java).
75. **strace** - Tracer les appels système (`strace -p <pid>` pour le débogage).

### **Gestion des Paquets (10 Commandes)**
76. **apt** - Gestionnaire de paquets (`apt install vim` pour l'installation de logiciels).
77. **apt-get** - Outil de paquet avancé (`apt-get upgrade` pour les mises à jour système).
78. **dpkg** - Gérer les paquets .deb (`dpkg -i package.deb` pour les installations manuelles).
79. **apt-cache** - Interroger les informations des paquets (`apt-cache search java` pour les paquets).
80. **snap** - Gérer les paquets snap (`snap install code` pour VS Code).
81. **update-alternatives** - Gérer les applications par défaut (`update-alternatives --config java`).
82. **add-apt-repository** - Ajouter des PPAs (`add-apt-repository ppa:repo` pour les sources).
83. **apt-file** - Trouver les fichiers des paquets (`apt-file search /bin/bash` pour le débogage).
84. **dpkg-query** - Interroger les paquets installés (`dpkg-query -l` pour la liste).
85. **apt-mark** - Marquer les paquets (`apt-mark hold package` pour empêcher les mises à niveau).

### **Administration Système et Sécurité (15 Commandes)**
86. **sudo** - Exécuter des commandes en tant que root (`sudo apt update` pour les tâches d'administration).
87. **su** - Changer d'utilisateur (`su - user` pour différents comptes).
88. **passwd** - Changer les mots de passe (`passwd user` pour la sécurité).
89. **useradd** - Ajouter un utilisateur (`useradd -m dev` pour les nouveaux comptes).
90. **usermod** - Modifier un utilisateur (`usermod -aG sudo dev` pour les permissions).
91. **groupadd** - Créer des groupes (`groupadd developers` pour le contrôle d'accès).
92. **chgrp** - Changer le groupe propriétaire (`chgrp -R dev /project` pour les équipes).
93. **crontab** - Planifier des tâches (`crontab -e` pour les scripts automatisés).
94. **systemctl** - Gérer les services (`systemctl start nginx` pour les serveurs web).
95. **journalctl** - Voir les journaux système (`journalctl -u docker` pour les journaux de service).
96. **who** - Lister les utilisateurs connectés (`who` pour la surveillance du serveur).
97. **last** - Afficher l'historique de connexion (`last` pour les audits de sécurité).
98. **shutdown** - Éteindre le système (`shutdown -h now` pour l'arrêt du système).
99. **reboot** - Redémarrer le système (`reboot` pour les mises à jour).
100. **env** - Afficher les variables d'environnement (`env | grep PATH` pour le débogage).

### **Notes pour Votre Contexte**
-   **Focus Développement** : Les commandes comme `git`, `mvn`, `docker` et `kubectl` correspondent à vos flux de travail full-stack et conteneurisés, en particulier pour vos 10 projets GitHub et votre expérience cloud (AWS, Azure, Alibaba Cloud).
-   **Débogage et Performance** : Des outils comme `strace`, `gdb`, `htop` et `dmesg` sont inclus pour vos besoins de débogage backend et système, compte tenu de vos 8 ans d'expérience en backend.
-   **Réseau** : Les commandes comme `curl`, `netcat` et `nmap` soutiennent votre expertise en API et en réseau, utiles pour tester les microservices ou les déploiements cloud.
-   **Automatisation** : `crontab` et `rsync` sont pratiques pour automatiser les sauvegardes ou les déploiements, pertinents pour vos rôles en freelance et en entreprise.
-   **Recherche et Apprentissage** : Les outils de traitement de texte (`grep`, `awk`, `sed`) sont utiles pour analyser les journaux ou les ensembles de données, ce qui pourrait soutenir vos recherches autodidactes sur la restauration de la vision.

Si vous souhaitez une exploration plus approfondie de toute catégorie (par exemple, des exemples de scripts pour `awk` ou `sed`, des flux de travail Docker ou des commandes spécifiques au cloud), ou si vous souhaitez un graphique visualisant l'utilisation des commandes (par exemple, la fréquence par type de tâche), faites-le-moi savoir ! Vous pouvez également vérifier votre portfolio GitHub pour des commandes spécifiques à un projet ou partager plus de détails sur vos tâches actuelles chez TEKsystems pour des recommandations sur mesure.