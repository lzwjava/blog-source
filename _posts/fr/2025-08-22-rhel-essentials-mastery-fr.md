---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Maîtriser les bases de Red Hat Enterprise Linux
translated: true
type: note
---

## Introduction à Red Hat Linux
Red Hat Enterprise Linux (RHEL) est un système d'exploitation open-source de premier plan développé par Red Hat, Inc. Il est conçu pour les environnements d'entreprise, offrant stabilité, sécurité et une prise en charge robuste pour les applications critiques. RHEL est largement utilisé dans les serveurs, les environnements cloud et l'infrastructure informatique des entreprises.

### Historique
- **1994** : Red Hat Linux a été publié pour la première fois en tant que distribution Linux commerciale.
- **2002** : Red Hat a introduit Red Hat Enterprise Linux, en se concentrant sur la fiabilité de niveau entreprise.
- **2025** : RHEL 9 est la dernière version majeure, avec RHEL 10 en développement, offrant des fonctionnalités avancées comme une sécurité renforcée et la prise en charge des conteneurs.

### Fonctionnalités Clés
- **Stabilité** : RHEL priorise le support à long terme (LTS) avec un cycle de vie de 10 ans par version majeure.
- **Sécurité** : Fonctionnalités comme SELinux (Security-Enhanced Linux), firewalld et des correctifs de sécurité réguliers.
- **Performance** : Optimisé pour le calcul haute performance, la virtualisation et les déploiements cloud.
- **Modèle d'Abonnement** : Donne accès aux mises à jour, au support et aux logiciels certifiés via les abonnements Red Hat.
- **Écosystème** : S'intègre avec Red Hat OpenShift, Ansible et d'autres outils pour le DevOps et l'automatisation.

## Installation
### Configuration Système Requise
- **Minimum** :
  - 1,5 Go de RAM
  - 20 Go d'espace disque
  - Processeur 1 GHz
- **Recommandé** :
  - 4 Go de RAM ou plus
  - 40 Go+ d'espace disque
  - Processeur multi-cœur

### Étapes d'Installation
1. **Télécharger RHEL** :
   - Obtenez l'ISO RHEL depuis le [Portail Client Red Hat](https://access.redhat.com) (nécessite un abonnement ou un compte développeur).
   - Alternativement, utilisez un abonnement développeur gratuit pour un usage non productif.
2. **Créer un Support Amovible de Démarrage** :
   - Utilisez des outils comme `dd` ou Rufus pour créer une clé USB bootable.
   - Commande exemple : `sudo dd if=rhel-9.3-x86_64.iso of=/dev/sdX bs=4M status=progress`
3. **Démarrer et Installer** :
   - Démarrez depuis la clé USB ou le DVD.
   - Suivez l'installateur Anaconda :
     - Sélectionnez la langue et la région.
     - Configurez le partitionnement des disques (manuel ou automatique).
     - Configurez les paramètres réseau.
     - Créez un mot de passe root et des comptes utilisateur.
4. **Enregistrer le Système** :
   - Après l'installation, enregistrez-vous avec Red Hat Subscription Manager : `subscription-manager register --username <nom_utilisateur> --password <mot_de_passe>`.
   - Attachez un abonnement : `subscription-manager attach --auto`.

## Administration Système
### Gestion des Paquets
RHEL utilise **DNF** (Dandified YUM) pour la gestion des paquets.
- Installer un paquet : `sudo dnf install <nom-du-paquet>`
- Mettre à jour le système : `sudo dnf update`
- Rechercher des paquets : `sudo dnf search <mot-clé>`
- Activer des dépôts : `sudo subscription-manager repos --enable <id-du-dépôt>`

### Gestion des Utilisateurs
- Ajouter un utilisateur : `sudo useradd -m <nom_utilisateur>`
- Définir un mot de passe : `sudo passwd <nom_utilisateur>`
- Modifier un utilisateur : `sudo usermod -aG <groupe> <nom_utilisateur>`
- Supprimer un utilisateur : `sudo userdel -r <nom_utilisateur>`

### Gestion du Système de Fichiers
- Vérifier l'utilisation du disque : `df -h`
- Lister les systèmes de fichiers montés : `lsblk`
- Gérer les partitions : Utilisez `fdisk` ou `parted` pour le partitionnement des disques.
- Configurer LVM (Logical Volume Manager) :
  - Créer un volume physique : `pvcreate /dev/sdX`
  - Créer un groupe de volumes : `vgcreate <nom-groupe-volumes> /dev/sdX`
  - Créer un volume logique : `lvcreate -L <taille> -n <nom-volume-logique> <nom-groupe-volumes>`

### Mise en Réseau
- Configurer le réseau avec `nmcli` :
  - Lister les connexions : `nmcli connection show`
  - Ajouter une IP statique : `nmcli con mod <nom-connexion> ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual`
  - Activer la connexion : `nmcli con up <nom-connexion>`
- Gérer le pare-feu avec `firewalld` :
  - Ouvrir un port : `sudo firewall-cmd --add-port=80/tcp --permanent`
  - Recharger le pare-feu : `sudo firewall-cmd --reload`

### Sécurité
- **SELinux** :
  - Vérifier le statut : `sestatus`
  - Définir le mode (enforcing/permissive) : `sudo setenforce 0` (permissif) ou `sudo setenforce 1` (enforcing)
  - Modifier les politiques : Utilisez `semanage` et `audit2allow` pour les politiques personnalisées.
- **Mises à jour** :
  - Appliquer les correctifs de sécurité : `sudo dnf update --security`
- **SSH** :
  - Sécuriser SSH : Modifiez `/etc/ssh/sshd_config` pour désactiver la connexion root (`PermitRootLogin no`) et changer le port par défaut.
  - Redémarrer SSH : `sudo systemctl restart sshd`

## Fonctionnalités Avancées
### Conteneurs et Virtualisation
- **Podman** : L'outil de conteneurs sans privilèges root de RHEL.
  - Exécuter un conteneur : `podman run -it docker.io/library/centos bash`
  - Construire une image : `podman build -t <nom-image> .`
- **Virtualisation** : Utilisez `libvirt` et `virt-manager` pour gérer les machines virtuelles.
  - Installer : `sudo dnf install libvirt virt-manager`
  - Démarrer libvirt : `sudo systemctl start libvirtd`

### Automatisation avec Ansible
- Installer Ansible : `sudo dnf install ansible`
- Créer un playbook :
  ```yaml
  - name: Installer Apache
    hosts: all
    tasks:
      - name: Installer httpd
        dnf:
          name: httpd
          state: present
  ```
- Exécuter le playbook : `ansible-playbook playbook.yml`

### Intégration Cloud
- RHEL s'intègre avec AWS, Azure et Google Cloud.
- Utilisez Red Hat OpenShift pour l'orchestration de conteneurs.
- Déployez des images RHEL dans des environnements cloud via Red Hat Cloud Access.

## Dépannage
- **Journaux** : Vérifiez `/var/log` pour les journaux système (par ex., `/var/log/messages` ou `/var/log/secure`).
- **Systemd** : Gérez les services avec `systemctl` :
  - Vérifier le statut d'un service : `systemctl status <service>`
  - Redémarrer un service : `systemctl restart <service>`
- **Performance** : Utilisez `top`, `htop` ou `vmstat` pour surveiller les performances du système.
- **Problèmes Réseau** : Utilisez `ping`, `traceroute` ou `nslookup` pour les diagnostics.

## Bonnes Pratiques
- Mettez régulièrement à jour le système pour corriger les vulnérabilités.
- Utilisez des mots de passe forts et appliquez les politiques SELinux.
- Sauvegardez les données critiques avec des outils comme `rsync` ou `rear` de Red Hat.
- Surveillez l'état du système avec des outils comme Cockpit (`sudo dnf install cockpit`).

## Ressources
- [Portail Client Red Hat](https://access.redhat.com)
- [Documentation RHEL](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux)
- [Programme Développeur Red Hat](https://developers.redhat.com)
- Forums communautaires comme [Red Hat Discuss](https://discuss.redhat.com)