---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre l'Erreur de Configuration de libcurl
translated: true
type: note
---

Cette erreur signifie que le script `configure` essaie de trouver **libcurl** (une bibliothèque pour les requêtes HTTP/HTTPS), mais il ne peut pas localiser `curl-config` — un binaire utilitaire qui indique où libcurl est installé.

Voici comment résoudre le problème en fonction de votre système :

---

### 🧩 Pour Ubuntu / Debian

Exécutez :

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

Puis réessayez :

```bash
./configure
```

---

### 🧩 Pour Fedora / CentOS / RHEL

Exécutez :

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 Pour Arch / Manjaro

Exécutez :

```bash
sudo pacman -S curl
```

---

### 🔍 Pour vérifier l'installation

Après l'installation, assurez-vous que `curl-config` est disponible :

```bash
which curl-config
```

Si cela retourne un chemin comme `/usr/bin/curl-config`, c'est bon.

Puis relancez :

```bash
./configure
make
sudo make install
```

---

Souhaitez-vous que j'explique ce que `curl-config` fait réellement et pourquoi `configure` en a besoin ?