---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Corriger l'erreur d'authentification de Copilot Chat
translated: true
type: note
---

Cette erreur signifie généralement que **GitHub Copilot Chat** n'a pas pu trouver un jeton d'authentification valide, il ne peut donc pas communiquer avec le service Copilot.
Ce n'est pas un bug de code — c'est un problème **d'authentification/de configuration**.

Voici comment le résoudre étape par étape selon l'endroit où vous utilisez Copilot Chat :

---

### 1. Vérifiez que vous êtes connecté avec un compte compatible Copilot

* Dans **VS Code** ou un IDE **JetBrains** :

  1. Ouvrez la Palette de commandes (**Ctrl+Shift+P** / **Cmd+Shift+P**).
  2. Recherchez **“GitHub: Sign in”**.
  3. Suivez le processus de connexion (cela ouvrira un navigateur pour autoriser).
  4. Assurez-vous que le compte avec lequel vous vous êtes connecté a **un abonnement GitHub Copilot actif**.
* Dans **Neovim CLI** (`copilot.vim` ou `copilot.lua`) :

  * Exécutez `:Copilot sign in` et suivez le lien dans votre navigateur.

---

### 2. Vérifiez que GitHub Copilot Chat est activé

* Dans VS Code :

  * Allez dans **Extensions** → recherchez “GitHub Copilot Chat” → assurez-vous qu'il est installé et activé.
  * Paramètres → recherchez “Copilot Chat: Enabled” → activez-le.

---

### 3. Actualisez le jeton d'authentification

Parfois, les jetons expirent ou sont perdus (surtout si vous avez changé de réseau, mis à jour l'IDE ou changé de compte).

* VS Code :

  1. Palette de commandes → **“GitHub Copilot: Sign out”**.
  2. Puis **“GitHub Copilot: Sign in”** à nouveau.
* CLI :

  * Supprimez le fichier de jeton (par exemple, `~/.config/github-copilot/hosts.json`) et reconnectez-vous.

---

### 4. Vérifiez les restrictions réseau / pare-feu

* Si vous êtes sur un VPN d'entreprise ou derrière un pare-feu, GitHub Copilot peut être empêché d'atteindre son API.
* Autorisez l'accès à `github.com`, `api.githubcopilot.com` et `copilot-proxy.githubusercontent.com`.

---

### 5. Mettez à jour votre IDE et les extensions Copilot

* Les versions obsolètes de VS Code ou des extensions Copilot provoquent parfois ce problème.
* Mettez les deux à jour, puis redémarrez votre IDE.

---

💡 Si vous corrigez l'authentification mais que vous voyez toujours des erreurs, GitHub Copilot Chat nécessite également **l'accès à la fonctionnalité Chat** — certains comptes ont Copilot pour le codage mais **pas Chat** à moins qu'il ne soit explicitement activé dans les paramètres.

---

Si vous le souhaitez, je peux vous donner **la séquence de commandes VS Code exacte** pour réinitialiser complètement l'authentification de Copilot Chat afin qu'il vous redemande d'accéder. Souhaitez-vous que je prépare cela ?