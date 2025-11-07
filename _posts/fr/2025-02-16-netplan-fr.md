---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Netplan, Systemd, SSH, Nettoyage de Conda
translated: true
type: post
---

### Table des matières

1. [Essais de Netplan](#trying-netplan)
   - La configuration IP statique a causé la perte de la connexion SSH
   - Accès physique requis pour annuler les modifications
   - Modification du fichier de résolution DNS du système

2. [Service Systemd](#systemd-service)
   - Configuration du service pour l'inférence LLM locale
   - Configuration de l'interface web pour les modèles LLM
   - Établissement du service d'outil proxy basé sur des règles
   - Utilisation des commandes systemctl pour la gestion des services

3. [Configuration SSH](#ssh-configuration)
   - Proxy des connexions externes via corkscrew
   - Exclusion du réseau local du proxy
   - Gestion des clés SSH via keychain et agent
   - Spécification de l'emplacement par défaut de la clé privée

4. [Supprimer Conda sous Linux](#delete-conda-in-linux)
   - Suppression de l'intégralité du répertoire d'installation de conda
   - Suppression du code d'initialisation de conda de bashrc
   - Mise à jour de la variable d'environnement PATH
   - Élimination des binaires conda du chemin système


## Essais de Netplan

J'ai essayé la configuration ci-dessous pour attribuer une adresse IP statique à une machine Ubuntu. Je fais tourner OpenWebUI et llama.cpp sur ce serveur.

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

Après avoir exécuté `sudo netplan apply`, la machine n'était plus accessible via `ssh lzw@192.168.1.128`.

Le clavier et la souris ont été utilisés pour se connecter à la machine, supprimer les fichiers et restaurer les paramètres.

`/etc/resolv.conf` a été modifié.

---

## Service Systemd

*13.02.2025*

## Configuration du service LLaMA Server

Cette section explique comment configurer un service systemd pour exécuter le serveur LLaMA, qui fournit des capacités d'inférence LLM locales.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Configuration du service Open WebUI

Cette section explique comment configurer un service systemd pour exécuter Open WebUI, qui fournit une interface web permettant d'interagir avec les modèles LLM.

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## Configuration du service Clash

Cette section explique comment configurer un service systemd pour exécuter Clash, un outil proxy basé sur des règles.

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# Créer le fichier de service
sudo emacs /etc/systemd/system/clash.service 

# Recharger le daemon systemd
sudo systemctl daemon-reload

# Activer et démarrer le service
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# Vérifier le statut
sudo systemctl status clash.service
```

---

## Configuration SSH

*09.02.2025*

Ce fichier `ssh-config` configure le comportement du client SSH. Décomposons chaque partie :

-   `Host * !192.*.*.*`: Cette section s'applique à tous les hôtes *sauf* ceux correspondant au motif `192.*.*.*` (généralement, les adresses de réseau local).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: C'est la partie clé. Elle indique à SSH d'utiliser le programme `corkscrew` pour se connecter à l'hôte cible.
        -   `corkscrew`: Un outil qui vous permet de tunneler les connexions SSH via des proxys HTTP ou HTTPS.
        -   `localhost 7890`: Spécifie l'adresse (`localhost`) et le port (`7890`) du serveur proxy. Cela suppose que vous avez un serveur proxy en cours d'exécution sur votre machine locale, écoutant sur le port 7890 (par exemple, Shadowsocks, un proxy SOCKS, ou une autre solution de tunneling).
        -   `%h`: Une variable SSH spéciale qui se développe en le nom d'hôte cible auquel vous essayez de vous connecter.
        -   `%p`: Une autre variable SSH qui se développe en le port cible (généralement 22 pour SSH).
    - En résumé, ce bloc `Host` configure SSH pour utiliser le proxy `corkscrew` pour toutes les connexions *sauf* celles vers le réseau local.

-   `Host *`: Cette section s'applique à *tous* les hôtes.
    -   `UseKeychain yes`: Sur macOS, cela indique à SSH de stocker et de récupérer les clés SSH de votre Trousseau, afin que vous n'ayez pas à saisir votre mot de passe à chaque fois.
    -   `AddKeysToAgent yes`: Cela ajoute automatiquement vos clés SSH à l'agent SSH, afin que vous n'ayez pas à les ajouter manuellement après chaque redémarrage.
    -   `IdentityFile ~/.ssh/id_rsa`: Spécifie le chemin d'accès à votre fichier de clé SSH privée. `~/.ssh/id_rsa` est l'emplacement par défaut de la clé privée RSA.

**En substance, cette configuration met en place un proxy pour toutes les connexions SSH sauf celles sur le réseau local, et elle configure la gestion des clés pour plus de commodité.**


```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa 
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa    
```

---

## Supprimer Conda sous Linux

*07.02.2025*

```bash
rm -rf ~/anaconda3
```

Supprimer le code ci-dessous dans `.bashrc`:

```bash
# >>> conda initialize >>>
# !! Le contenu de ce bloc est géré par 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Mettre à jour le chemin de :

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

Pour :

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```