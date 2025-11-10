---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide Complet d'Enterprise Linux RHEL
translated: true
type: note
---

Voici un **guide complet de Red Hat Enterprise Linux (RHEL)**. Je le structurerai étape par étape pour que vous puissiez l'utiliser à la fois comme un parcours d'apprentissage et une référence.

---

## 1. Introduction à Red Hat Linux

Red Hat Enterprise Linux (RHEL) est une distribution Linux commerciale développée par **Red Hat, Inc.**, conçue pour **la stabilité, la sécurité et le support entreprise**. Elle est largement utilisée dans les secteurs bancaire, de la santé, gouvernemental et l'informatique d'entreprise en raison de son cycle de support à long terme et de son écosystème de logiciels certifiés.

Points clés :

* Support de qualité entreprise (cycle de vie de 10+ ans par version majeure).
* Certifié sur les principaux matériels (Dell, HP, IBM, etc.).
* Largement utilisé dans le cloud (AWS, Azure, GCP), les conteneurs (OpenShift, Kubernetes) et la virtualisation.

---

## 2. Installation et Configuration

* **Téléchargement** : Les images ISO officielles sont disponibles via le Portail Client Red Hat (nécessite un abonnement).
* **Installateurs** : Utilise l'**installateur Anaconda** avec des modes graphique et texte.
* **Partitionnement** : Options pour LVM, XFS (système de fichiers par défaut) et les disques chiffrés.
* **Outils post-installation** : `subscription-manager` pour enregistrer le système.

---

## 3. Gestion des paquets

* **RPM (Red Hat Package Manager)** – le format sous-jacent pour les logiciels.
* **DNF (Dandified Yum)** – le gestionnaire de paquets par défaut dans RHEL 8 et versions ultérieures.

  * Installer un paquet :

    ```bash
    sudo dnf install httpd
    ```
  * Mettre à jour le système :

    ```bash
    sudo dnf update
    ```
  * Rechercher des paquets :

    ```bash
    sudo dnf search nginx
    ```

RHEL prend également en charge les **AppStreams** pour les versions multiples des logiciels (par exemple, Python 3.6 vs 3.9).

---

## 4. Bases de l'administration système

* **Gestion des utilisateurs** :
  `useradd`, `passwd`, `usermod`, `/etc/passwd`, `/etc/shadow`
* **Gestion des processus** :
  `ps`, `top`, `htop`, `kill`, `systemctl`
* **Gestion des disques** :
  `lsblk`, `df -h`, `mount`, `umount`, `fdisk`, `parted`
* **Services système** (systemd) :

  ```bash
  systemctl start nginx
  systemctl enable nginx
  systemctl status nginx
  ```

---

## 5. Mise en réseau

* Configuration stockée dans `/etc/sysconfig/network-scripts/`.
* Commandes :

  * `nmcli` (NetworkManager CLI)
  * `ip addr`, `ip route`, `ping`, `traceroute`
* Pare-feu :

  * Géré par **firewalld** (`firewall-cmd`).
  * Exemple :

    ```bash
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```

---

## 6. Sécurité

* **SELinux** : Système de contrôle d'accès obligatoire.

  * Vérifier le statut : `sestatus`
  * Modes : enforcing, permissive, disabled
* **FirewallD** : Gère la sécurité du réseau.
* **Mises à jour système** : Correctifs de sécurité via `dnf update`.
* **Auditd** : Journalisation et conformité.

---

## 7. Journalisation et surveillance

* **Journaux système** :
  Stockés sous `/var/log/`.
* **Journald** :
  `journalctl -xe`
* **Outils de performance** :

  * `sar` (paquet sysstat)
  * `vmstat`, `iostat`, `dstat`
* **Red Hat Insights** : Analyse système basée sur le cloud.

---

## 8. Virtualisation et conteneurs

* **KVM** (Kernel-based Virtual Machine) pour la virtualisation.
* **Podman** (au lieu de Docker) :

  ```bash
  podman run -it centos /bin/bash
  ```
* **OpenShift** (plateforme Kubernetes) pour l'orchestration.

---

## 9. Gestion du stockage

* **LVM (Logical Volume Manager)** pour une gestion flexible des disques.
* **XFS** : Système de fichiers par défaut.
* **Stratis** : Gestion du stockage avec provisionnement fin et instantanés.

---

## 10. Automatisation et gestion de la configuration

* **Ansible** : Plateforme d'automatisation de Red Hat.
* **Kickstart** : Automatise les installations du système d'exploitation.
* **Rôles système** : Rôles Ansible prédéfinis pour RHEL.

---

## 11. Abonnements et support

* Red Hat utilise un **modèle d'abonnement**.
* `subscription-manager` pour enregistrer, attacher des abonnements et activer les dépôts.
* L'abonnement développeur RHEL est **gratuit pour les particuliers**.

---

## 12. Bonnes pratiques

* Maintenez toujours les systèmes à jour avec les correctifs de sécurité.
* Utilisez SELinux en mode enforcing sauf pour le débogage.
* Centralisez la journalisation avec `rsyslog` ou la stack ELK.
* Automatisez les tâches répétitives avec Ansible.
* Surveillez l'état du système avec Red Hat Insights.

---

## 13. Ressources d'apprentissage

* [Documentation Red Hat](https://access.redhat.com/documentation)
* [Red Hat Academy](https://www.redhat.com/en/services/training-and-certification/red-hat-academy)
* Certifications :

  * **RHCSA** (Red Hat Certified System Administrator)
  * **RHCE** (Red Hat Certified Engineer)
  * **RHCA** (Red Hat Certified Architect)

---

✅ C'est la base.
Souhaitez-vous que je **développe ceci en un "guide pratique"** avec des commandes et des flux de travail concrets (comme la configuration d'un serveur web, d'une base de données, d'un pare-feu, etc.), ou préférez-vous le garder plus **théorique et conceptuel** ?