---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de mise à niveau de Node.js pour Ubuntu
translated: true
type: note
---

La mise à niveau de Node.js sur Ubuntu peut se faire de plusieurs manières. Les méthodes les plus fiables et recommandées sont l'utilisation de **`nvm` (Node Version Manager)** ou du **dépôt NodeSource**. Vous trouverez ci-dessous des instructions détaillées pour les deux méthodes.

---

## **Méthode 1 : Utilisation de NVM (Recommandée)**
NVM vous permet d'installer et de gérer facilement plusieurs versions de Node.js.

### 1. Installer NVM
Ouvrez un terminal et exécutez :
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
Ensuite, rechargez votre shell :
```bash
source ~/.bashrc
```
ou
```bash
source ~/.zshrc
```
(cela dépend de votre shell)

### 2. Installer la Dernière Version de Node.js
Listez les versions disponibles :
```bash
nvm ls-remote
```
Installez la dernière version LTS (recommandée pour la plupart des utilisateurs) :
```bash
nvm install --lts
```
Ou installez une version spécifique (par exemple, 20.x) :
```bash
nvm install 20
```

### 3. Définir la Version par Défaut
```bash
nvm alias default 20
```

### 4. Vérifier
```bash
node -v
npm -v
```

---

## **Méthode 2 : Utilisation du Dépôt NodeSource**
Cette méthode installe Node.js de manière globale sur le système.

### 1. Supprimer l'Ancienne Version de Node.js (si installée via apt)
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. Ajouter le Dépôt NodeSource**
Pour **Node.js 20.x** (LTS en août 2025) :
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
Pour **Node.js 22.x** (si disponible) :
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. Installer Node.js
```bash
sudo apt install -y nodejs
```

### 4. Vérifier
```bash
node -v
npm -v
```

---

## **Méthode 3 : Utilisation du Dépôt par Défaut d'Ubuntu (Non Recommandée)**
Le dépôt par défaut d'Ubuntu contient souvent des versions obsolètes de Node.js. Si vous souhaitez toujours l'utiliser :
```bash
sudo apt update
sudo apt install nodejs npm
```
Mais cette méthode n'est **pas recommandée** pour le développement, car la version est généralement ancienne.

---

## **Quelle Méthode Devriez-Vous Utiliser ?**
- **Utilisez NVM** si vous souhaitez basculer facilement entre différentes versions de Node.js ou si vous avez besoin des dernières fonctionnalités.
- **Utilisez NodeSource** si vous voulez une installation stable et globale sur le système.