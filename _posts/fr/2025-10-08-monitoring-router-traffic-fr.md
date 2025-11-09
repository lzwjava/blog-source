---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Surveillance du trafic réseau du routeur
translated: true
type: note
---

### Surveillance des requêtes HTTP et des connexions TCP sur le routeur 360 Wi-Fi 6 T7

Le 360 T7 exécute un firmware personnalisé basé sur Linux (pas entièrement OpenWrt d'origine), donc les capacités de surveillance sont limitées dans la configuration d'origine par rapport à un shell Linux complet. Avec les droits administrateur (via l'interface web), vous pouvez accéder aux journaux de base. Pour un "hacking" plus approfondi, comme la journalisation des requêtes HTTP en temps réel ou le suivi des connexions TCP, l'approche éthique la plus efficace est de flasher OpenWrt (qui est officiellement supporté), d'activer SSH et d'utiliser les outils Linux standard. **Avertissement : Flasher un firmware personnalisé annule la garantie et risque de bricker l'appareil—sauvegardez d'abord et suivez les guides attentivement. Ne faites cela que sur votre propre appareil.**

#### 1. **Accéder aux droits administrateur sur le firmware d'origine**
   - Connectez-vous au Wi-Fi du routeur ou via Ethernet.
   - Ouvrez un navigateur et allez sur `http://ihome.360.cn` ou `http://192.168.0.1` (IP par défaut).
   - Connexion : Nom d'utilisateur par défaut `admin`, mot de passe imprimé sur l'étiquette du routeur (souvent `admin` ou une chaîne unique comme `360XXXXXX`—vérifiez l'étiquette au dos).
   - Une fois connecté, naviguez vers **Système > Journal** ou **Sécurité > Journal** pour les journaux système et de trafic de base. Cela affiche les blocages du pare-feu, les connexions et certaines activités HTTP (par ex., sites bloqués ou intrusions), mais pas les détails complets des requêtes HTTP.

   **Surveillance de base via l'interface web :**
   - **Journaux système** : Affichez les événements récents, y compris les tentatives de connexion TCP et les erreurs. Exportez les journaux (peut nécessiter le mot de passe de l'étiquette pour le décryptage).
   - **Statistiques de trafic** : Sous **Statut > Réseau** ou **Avancé > Moniteur de trafic**, consultez l'utilisation de la bande passante par appareil/IP, mais pas de manière granulaire HTTP/TCP.
   - Limitations : Aucune inspection de payload HTTP en temps réel ; les journaux sont de haut niveau et non exportables sans authentification.

#### 2. **Surveillance avancée : Flasher OpenWrt pour un accès shell**
   Le 360 T7 (puce MT7981B) est supporté dans les snapshots OpenWrt 23.05+. Le flashing donne un accès root complet via SSH, où vous pouvez exécuter des outils comme `tcpdump` pour les captures de paquets et `logread` pour les journaux.

   **Étapes pour flasher OpenWrt (Niveau élevé ; Utilisez le guide officiel) :**
   1. Téléchargez l'image factory depuis les téléchargements OpenWrt (recherchez "Qihoo 360T7 sysupgrade.bin" ou l'image factory).
   2. Sauvegardez le firmware d'origine : Dans l'interface web, allez dans **Système > Sauvegarde** et téléchargez la configuration/le firmware.
   3. Téléversez via l'interface web : **Système > Mise à niveau du firmware**, sélectionnez le fichier .bin et appliquez (le routeur redémarre sous OpenWrt).
   4. Post-flash : Accédez à l'interface web sur `http://192.168.1.1` (interface LuCI), nom d'utilisateur `root`, pas de mot de passe initialement—définissez-en un immédiatement via SSH ou l'interface.
   5. Activez SSH : Il est activé par défaut sur le port 22. Connectez-vous depuis votre PC : `ssh root@192.168.1.1` (utilisez PuTTY sur Windows).

   **Atténuation des risques** : Si bloqué, utilisez la récupération TFTP (maintenez reset pendant le démarrage) ou la console série (nécessite un adaptateur UART).

#### 3. **Surveillance sur OpenWrt (via le shell SSH)**
   Une fois connecté en SSH en tant que root, le routeur agit comme un système Linux minimal. Installez les paquets si nécessaire via `opkg update && opkg install tcpdump` (le stockage intégré est de 128 Mo, donc gardez-le léger).

   - **Lister toutes les connexions TCP actuelles (Vue statique) :**
     ```
     ss -tunap
     ```
     - Affiche les sockets TCP établies/en écoute, les ports, les processus (par ex., `tcp ESTAB 0 0 192.168.1.1:80 192.168.1.100:54321 users:(("uhttpd",pid=1234,fd=3))`).
     - Pour le temps réel : `watch -n 1 'ss -tunap'`.

   - **Capture du trafic TCP en temps réel :**
     Installez si nécessaire : `opkg update && opkg install tcpdump`.
     ```
     tcpdump -i any tcp -n -v
     ```
     - `-i any` : Toutes les interfaces (br-lan pour le LAN, eth0.2 pour le WAN).
     - Filtrer HTTP : `tcpdump -i any tcp port 80 -n -v -A` (`-A` affiche le payload ASCII pour les en-têtes/requêtes HTTP).
     - Sauvegarder dans un fichier : `tcpdump -i any tcp -w /tmp/capture.pcap` (téléchargez via SCP : `scp root@192.168.1.1:/tmp/capture.pcap .`).
     - Pour HTTPS (port 443), notez que les payloads sont chiffrés—utilisez Wireshark hors ligne pour l'analyse.

   - **Surveiller les journaux de requêtes HTTP :**
     - Journaux système (inclut le serveur web si vous utilisez uhttpd) : `logread | grep uhttpd` ou `logread -f` pour le temps réel.
     - Activez la journalisation HTTP détaillée : Éditez `/etc/config/uhttpd` (configuration du serveur web), ajoutez `option log_file '/var/log/uhttpd.log'`, puis `/etc/init.d/uhttpd restart`. Suivez en temps réel : `tail -f /var/log/uhttpd.log` (affiche les requêtes GET/POST, IPs, URLs).
     - Pour le trafic HTTP complet du réseau : Utilisez `tcpdump` comme ci-dessus, ou installez `ngrep` (`opkg install ngrep`) : `ngrep -d any 'GET|POST|HTTP' -O /tmp/http.pcap`.

   - **Journaux du Pare-feu/Connexions :**
     - Activez la journalisation sur les règles : `uci set firewall.@rule[0].log='1'; uci commit; /etc/init.d/firewall restart`.
     - Affichez : `logread | grep fw` (affiche les connexions TCP rejetées/acceptées).

#### Conseils pour un "Hacking" Éthique
- **Sécurité** : Après la configuration, changez le mot de passe root (`passwd`), désactivez l'authentification par mot de passe dans `/etc/ssh/sshd_config` pour n'autoriser que les clés, et restreignez l'accès SSH au LAN uniquement via le pare-feu.
- **Performance** : Le T7 a 256 Mo de RAM—évitez les captures lourdes à long terme pour empêcher l'épuisement de la mémoire (OOM).
- **Revenir au firmware d'origine** : Téléchargez le firmware officiel depuis le site de 360, téléversez-le via la fonction sysupgrade d'OpenWrt (avec `--force` si nécessaire).
- Testez dans un environnement sécurisé ; pour l'analyse via interface graphique, transférez le fichier .pcap vers votre PC via SCP et ouvrez-le dans Wireshark.

Cela donne une visibilité complète. Si l'interface d'origine suffit pour les besoins de base, restez-y pour éviter le flashing.

[OpenWrt Techdata: Qihoo 360T7](https://openwrt.org/toh/hwdata/qihoohardware/qihoohardware_360t7)  
[Manuel 360 T7U (Section Journaux)](https://ipc-pr-cdn.jia.360.cn/ipc-pr/luyouqiT7U.pdf)  
[Guide de journalisation OpenWrt](https://openwrt.org/docs/guide-user/base-system/log.essentials)  
[Forum 360 : Export des journaux](https://bbs.360.cn/forum-7007-1.html)