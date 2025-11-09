---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Surveillance de l'activité réseau avec des droits administrateur
translated: true
type: note
---

### Surveillance des requêtes HTTP et des connexions TCP avec des droits administrateur

En supposant que vous travaillez sur un système de type Linux/Unix (par exemple, Ubuntu, CentOS) avec des privilèges root/administrateur, vous pouvez surveiller l'activité réseau de manière éthique pour le dépannage, l'audit de sécurité ou le pentesting. **Important : Ne faites cela que sur des systèmes vous appartenant ou pour lesquels vous avez une autorisation explicite — la surveillance non autorisée est illégale.** Je me concentrerai sur les outils en ligne de commande, qui sont légers et ne nécessitent pas d'interface graphique.

#### 1. **Surveiller toutes les connexions TCP**
   Utilisez des outils intégrés comme `ss` (remplacement moderne de `netstat`) ou `tcpdump` pour une capture en temps réel. Ceux-ci affichent les connexions actives, les ports et les processus.

   - **Lister toutes les connexions TCP actuelles (vue statique) :**
     ```
     sudo ss -tunap
     ```
     - `-t` : TCP uniquement.
     - `-u` : UDP si nécessaire (mais vous avez demandé TCP).
     - `-n` : Ports numériques (pas de résolution DNS).
     - `-a` : Tous les états (établies, en écoute, etc.).
     - `-p` : Afficher les processus propriétaires.
     Exemple de sortie :
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     Pour les sockets en écoute uniquement : `sudo ss -tlnp`.

   - **Surveillance en temps réel avec watch :**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     Actualise toutes les secondes.

   - **Capturer le trafic TCP en direct (au niveau des paquets) :**
     Installez `tcpdump` s'il n'est pas présent : `sudo apt update && sudo apt install tcpdump` (Debian/Ubuntu) ou `sudo yum install tcpdump` (RHEL/CentOS).
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any` : Toutes les interfaces.
     - `-n` : Pas de résolution de noms.
     - `-v` : Mode verbeux.
     Ajoutez `port 80 or port 443` pour filtrer HTTP/HTTPS : `sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A` (`-A` pour le contenu ASCII, pour voir les en-têtes HTTP).

     Sauvegardez dans un fichier pour une analyse ultérieure : `sudo tcpdump -i any tcp -w capture.pcap`.

#### 2. **Surveiller les journaux de requêtes HTTP**
   Les journaux HTTP dépendent de votre serveur web (Apache, Nginx, etc.). Si aucun serveur web n'est en cours d'exécution, utilisez la capture réseau (ci-dessus) pour inspecter le trafic HTTP. Pour les journaux spécifiques au serveur :

   - **Apache (httpd) :**
     Les journaux se trouvent généralement dans `/var/log/apache2/access.log` (Ubuntu) ou `/var/log/httpd/access_log` (CentOS).
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - Affiche les requêtes en temps réel : IP, horodatage, méthode (GET/POST), URL, code de statut.
     Exemple de ligne : `192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`.

     Pour tous les journaux : `sudo grep "GET\|POST" /var/log/apache2/access.log | less`.

   - **Nginx :**
     Journaux dans `/var/log/nginx/access.log`.
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     Format similaire à Apache.

   - **Si aucun serveur web (reniflage HTTP général) :**
     Utilisez `tcpdump` comme ci-dessus avec `-A` pour vider les charges utiles HTTP, ou installez `ngrep` pour une correspondance par regex :
     ```
     sudo apt install ngrep  # Installer si nécessaire
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     Cela filtre et enregistre les méthodes HTTP.

   - **Avancé : Configurer un proxy transparent pour une journalisation complète.**
     Installez le proxy Squid : `sudo apt install squid`.
     Configurez `/etc/squid/squid.conf` pour journaliser tout le HTTP (ajoutez `access_log /var/log/squid/access.log squid`).
     Redirigez le trafic via iptables : `sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`.
     Puis taillez le journal Squid : `sudo tail -f /var/log/squid/access.log`.

#### Conseils pour le "Hacking" (Pentesting Éthique)
- **Combinez les outils :** Redirigez `tcpdump` vers `grep` pour des motifs spécifiques, par exemple, `sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`.
- **Visualisez avec Wireshark :** Pour une analyse graphique, installez Wireshark (`sudo apt install wireshark`), exécutez en tant que root, et ouvrez votre fichier `.pcap`.
- **Renforcement de la sécurité :** Après la surveillance, effacez les journaux s'ils sont sensibles : `sudo truncate -s 0 /var/log/access.log`.
- **Remarque multiplateforme :** Sur Windows (avec les droits admin), utilisez `netstat -anob` pour TCP et l'Observateur d'événements pour les journaux. Sur macOS, `netstat -an` et `tcpdump`.

Cette configuration vous donne une visibilité complète sans outils externes. Testez d'abord dans une VM.

[Page de manuel de la commande Linux ss](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tutoriel Tcpdump](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Format du journal d'accès Apache](https://httpd.apache.org/docs/2.4/logs.html)