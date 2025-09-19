---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Optimisation des IP Cloud, des Interfaces Réseau et du WiFi
translated: true
---

### Table des matières

1. [IP flottantes dans Hetzner Cloud](#ip-flottantes-dans-hetzner-cloud)
   - Commandes de configuration IP
   - Configuration Netplan
   - Fichiers de configuration réseau

2. [Gestion des interfaces réseau](#gestion-des-interfaces-réseau)
   - Suppression des interfaces TUN
   - Surveillance de l'état des interfaces
   - Dépannage réseau

3. [Scanner d'IP LAN](#scanner-dip-lan)
   - Script Python de balayage réseau
   - Découverte d'hôtes multithread
   - Capacités de balayage de ports
   - Identification des appareils sur les réseaux locaux

4. [Contournement des IP locales](#contournement-des-ip-locales)
   - Configuration du proxy pour les réseaux locaux
   - Calculs de masques de sous-réseau
   - Planification des plages réseau

5. [Connexion SSH avec adresse IPv6](#connexion-ssh-avec-adresse-ipv6)
   - Configuration SSH IPv6
   - Gestion du fichier de configuration SSH
   - Configuration de la commande Proxy pour différents types d'adresses
   - Optimisation des performances

6. [Amélioration de la vitesse WiFi](#amélioration-de-la-vitesse-wifi)
   - Performances des anciens et nouveaux modems
   - Configurations de mise en réseau
   - Modes pont filaire et sans fil
   - Dépannage des goulots d'étranglement réseau

7. [Réinitialisation d'OpenWrt](#réinitialisation-dopenwrt)
   - Méthodes de réinitialisation via l'interface web
   - Procédures de réinitialisation en ligne de commande
   - Restauration des paramètres d'usine

---

## IP flottantes dans Hetzner Cloud

### IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

### Netplan

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```

---

## Gestion des interfaces réseau

Supprimez l'interface `tun`.

```bash
$ ipconfig

outline-tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.85.1  netmask 255.255.255.255  destination 10.0.85.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 208  bytes 8712 (8.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 385  bytes 23322 (23.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ sudo ip link delete outline-tun0
```

---

## Scanner d'IP LAN

Ce script Python analyse un réseau local pour détecter les adresses IP actives. Il utilise la commande `ping` pour vérifier si un hôte est accessible et emploie le multithreading pour accélérer le processus de balayage. Un sémaphore limite le nombre de threads simultanés pour éviter de surcharger le système. Le script prend une adresse réseau (par exemple, "192.168.1.0/24") en entrée et affiche si chaque adresse IP du réseau est active ou inactive.

Ce script aide à identifier les appareils sur le réseau, comme un routeur TP-LINK mesh fonctionnant en mode pont filaire, en scannant les adresses IP actives.

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # Nombre maximum de threads à utiliser

def is_host_up(host, port=None):
    """
    Vérifie si un hôte est actif en utilisant ping ou telnet.
    Si un port est spécifié, utilise telnet pour vérifier si le port est ouvert.
    Sinon, utilise ping.
    Retourne True si l'hôte est actif, False sinon.
    """
    if port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error as e:
            return False
        finally:
            sock.close()
    else:
        try:
            # -c 1: Envoyer un seul paquet
            # -W 1: Attendre 1 seconde pour une réponse
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    Analyse une seule adresse IP et affiche son statut.
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} est actif")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} est inactif")

def scan_network(network, port=None):
    """
    Analyse un réseau pour détecter les hôtes actifs en utilisant des threads,
    en limitant le nombre de threads simultanés.
    """
    print(f"Analyse du réseau : {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # Limiter le nombre de threads simultanés
    up_ips = []

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str, up_ips, port)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return up_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyser un réseau pour détecter les hôtes actifs.")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="Le réseau à analyser (par exemple, 192.168.1.0/24)")
    parser.add_argument("-p", "--port", type=int, help="Le port à vérifier (optionnel)")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nIP actives :")
    for ip in up_ips:
        print(ip)
```

---

## Contournement des IP locales

Le script identifie les adresses IP actives. Pour garantir une communication réseau correcte, vérifiez que les paramètres du proxy sont configurés pour contourner ces IP locales.

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

## Masques de sous-réseau

Ma deuxième machine est généralement à l'adresse 192.168.1.16.

La commande suivante fonctionne donc :

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

car 32 - 27 = 5, 2^5 = 32, donc il essaiera de `192.168.1.0` à `192.168.1.31`.

En revanche, cela ne fonctionne pas avec `192.168.1.0/28`, car 2^4 = 16, donc il essaiera de `192.168.1.0` à `192.168.1.15`, ce qui ne couvre pas `192.168.1.16`.

---

## Connexion SSH avec adresse IPv6

J'essaie de me connecter à une machine dans Hetzner Cloud en utilisant IPv6. `ssh 2a01:4f8:c17:2000::/64` ne fonctionne pas, mais `ssh root@2a01:4f8:c17:2000::1` fonctionne.

L'adresse IPv6 a été copiée depuis la console Hetzner Cloud.

Le fichier `~/.ssh/config` peut être configuré pour appliquer différentes règles de proxy aux adresses IPv4 et IPv6. Cette configuration permet de spécifier une commande proxy pour les adresses IPv4 tout en gérant différemment les adresses IPv6.

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

Lors de l'exécution de `ssh root@192.168.1.3`, la sortie suivante montre le client SSH appliquant les options de configuration du fichier `~/.ssh/config` :

```bash
debug1: Lecture des données de configuration /Users/lzwjava/.ssh/config
debug1: /Users/lzwjava/.ssh/config ligne 1: Application des options pour 192.168.1.*
debug1: /Users/lzwjava/.ssh/config ligne 5: Application des options pour *.*.*.*
debug2: add_identity_file: ignore la clé en double ~/.ssh/id_rsa
debug1: /Users/lzwjava/.ssh/config ligne 10: Application des options pour *
debug2: add_identity_file: ignore la clé en double ~/.ssh/id_rsa
debug1: Lecture des données de configuration /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config ligne 21: include /etc/ssh/ssh_config.d/* n'a trouvé aucun fichier
debug1: /etc/ssh/ssh_config ligne 54: Application des options pour *
debug2: resolve_canonicalize: le nom d'hôte 192.168.1.3 est une adresse
debug3: UserKnownHostsFile '~/.ssh/known_hosts' étendu à '/Users/lzwjava/.ssh/known_hosts'
debug3: UserKnownHostsFile '~/.ssh/known_hosts2' étendu à '/Users/lzwjava/.ssh/known_hosts2'
debug1: Le fournisseur d'authentification $SSH_SK_PROVIDER n'a pas pu être résolu ; désactivation
debug3: channel_clear_timeouts: effacement
debug1: Exécution de la commande proxy: exec corkscrew localhost 7890 192.168.1.3 22
```

La vitesse de la connexion SSH était notablement lente, donc je suis revenu à la configuration plus simple suivante :

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
```

Le problème survient lors de l'utilisation d'adresses IPv6 avec la directive `ProxyCommand corkscrew localhost 7890 %h %p`, car cette commande proxy ne gère peut-être pas correctement les adresses IPv6.

La configuration ci-dessus ne fonctionne toujours pas. Cependant, celle ci-dessous fonctionne bien.

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host !192.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

---

## Amélioration de la vitesse WiFi

### Problèmes avec l'ancien modem

Chez mes parents, le modem est assez ancien, probablement âgé d'environ 10 ans. La configuration réseau initiale était :

modem -> 3m sans fil -> TP-Link AX3000 (mode pont sans fil) -> 2m, un mur, sans fil -> Ordinateur portable

Cela a donné une vitesse de téléchargement faible, avec un résultat de test de vitesse de seulement 10 Mbps.

Une configuration améliorée a impliqué l'utilisation d'une connexion filaire :

modem -> 2m câble -> TP-Link AX3000 (mode pont filaire) -> 4m sans fil, un mur -> Ordinateur portable

Cela a amélioré la vitesse de téléchargement jusqu'à 90 Mbps.

### Performances du nouveau modem

Chez moi, le modem est neuf, et le routeur TP-Link fonctionne bien en mode pont sans fil. La configuration réseau est :

modem -> 4m sans fil -> TP-Link AX3000 (mode pont sans fil) -> 2m sans fil -> Ordinateur portable

La qualité du réseau est bonne.

### Conseils de dépannage

Il n'existe pas de solution unique pour améliorer la vitesse Wi-Fi. Une bonne approche consiste à utiliser un câble pour tester chaque partie de votre réseau afin d'identifier les goulots d'étranglement. Comparez les vitesses lors de l'utilisation d'une connexion filaire par rapport au Wi-Fi. Essayez également de connecter les appareils directement avec un câble pour voir si cela améliore les performances.

---

## Réinitialisation d'OpenWrt

### Réinitialisation via l'interface web

Il est recommandé de se connecter au routeur via un câble Ethernet. Après une réinitialisation, le SSID Wi-Fi reviendra à ses paramètres par défaut, ce qui peut ne pas être ce que vous attendez.

### Réinitialisation via la ligne de commande (SSH)

Vous pouvez réinitialiser OpenWrt à ses paramètres par défaut en utilisant l'interface de ligne de commande (SSH). Voici comment faire :

1. Connectez-vous à votre routeur OpenWrt via SSH.
2. Exécutez la commande suivante :

    ```bash
    root@OpenWrt:~# firstboot
    Cela effacera tous les paramètres et supprimera tous les paquets installés. Êtes-vous sûr ? [N/y]
    y
    /dev/ubi0_1 est monté en tant que /overlay, seul l'effacement des fichiers
    root@OpenWrt:~# reboot
    ```
3. Le routeur redémarrera avec les paramètres par défaut.

**Explication des commandes :**

* `firstboot` : Cette commande lance le processus de réinitialisation, effaçant toutes les configurations et les paquets installés.
* `reboot` : Cette commande redémarre le routeur, appliquant la réinitialisation.