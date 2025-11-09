---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide de Configuration du Pare-feu Linux
translated: true
type: note
---

Bonne question — configurer un pare-feu sous Linux (comme **Red Hat** ou **Ubuntu**) implique principalement d'utiliser soit **`firewalld`** soit **`ufw`**, selon votre système. Voici un guide clair pour les deux familles, afin que vous puissiez choisir celle qui vous convient.

---

### 🔹 Sur **Red Hat / CentOS / Fedora** (firewalld)

#### 1. Vérifier si `firewalld` est installé et en cours d'exécution

```bash
sudo systemctl status firewalld
```

S'il ne fonctionne pas :

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

#### 2. Utilisation de base

Vérifier les zones actives (les zones regroupent les interfaces et les règles) :

```bash
sudo firewall-cmd --get-active-zones
```

Lister toutes les règles pour la zone actuelle :

```bash
sudo firewall-cmd --list-all
```

#### 3. Autoriser ou bloquer les ports/services

Autoriser un port (par exemple SSH sur le port 22) :

```bash
sudo firewall-cmd --permanent --add-port=22/tcp
```

Autoriser un service connu (par exemple HTTP) :

```bash
sudo firewall-cmd --permanent --add-service=http
```

Bloquer/supprimer un service :

```bash
sudo firewall-cmd --permanent --remove-service=http
```

Recharger pour appliquer :

```bash
sudo firewall-cmd --reload
```

#### 4. Vérifier les règles

```bash
sudo firewall-cmd --list-all
```

---

### 🔹 Sur **Ubuntu / Debian** (ufw)

Ubuntu est livré avec **UFW** (Uncomplicated Firewall), plus simple à gérer.

#### 1. Activer UFW

```bash
sudo ufw enable
```

#### 2. Autoriser/interdire les ports ou services

Autoriser SSH :

```bash
sudo ufw allow ssh
```

Autoriser HTTP (port 80) :

```bash
sudo ufw allow 80/tcp
```

Autoriser une plage de ports spécifique :

```bash
sudo ufw allow 1000:2000/tcp
```

Interdire un service :

```bash
sudo ufw deny 23/tcp
```

#### 3. Vérifier le statut

```bash
sudo ufw status verbose
```

#### 4. Réinitialiser les règles si nécessaire

```bash
sudo ufw reset
```

---

### 🔹 Pour les deux systèmes

Pour **bloquer tout le trafic entrant sauf quelques exceptions**, vous pouvez :

1. Refuser tout le trafic entrant par défaut

   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```

   *(pour `firewalld`, utilisez les zones ou les zones de rejet pour un comportement similaire)*

2. Ensuite, autorisez sélectivement les ports (par exemple, 22, 80, 443).

---

### 🔹 Conseil de sécurité

Toujours **autoriser SSH en premier** avant d'activer ou de modifier les règles du pare-feu à distance — sinon vous vous serez verrouillé dehors.

---

Souhaitez-vous que je vous montre **un exemple de configuration minimale d'un pare-feu** (par exemple pour un serveur web typique autorisant uniquement SSH + HTTP + HTTPS) ?