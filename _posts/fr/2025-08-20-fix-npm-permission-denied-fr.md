---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Corriger l'Erreur d'Autorisation Refusée de npm
translated: true
type: note
---

L'erreur que vous rencontrez, `EACCES: permission denied`, signifie que votre utilisateur actuel **n'a pas les permissions d'écriture** sur le répertoire `/usr/local/lib/node_modules`. C'est un problème courant lors de l'installation de packages npm globaux sur Linux ou macOS.

### **Comment Résoudre Ce Problème**

#### **Option 1 : Utiliser `sudo` (Non Recommandé pour un Usage Régulier)**
Vous pouvez utiliser `sudo` pour exécuter la commande en tant qu'utilisateur root, mais ceci **n'est pas recommandé** pour un usage régulier, car cela peut entraîner des problèmes de permissions avec les packages npm par la suite.

```bash
sudo npm install -g @anthropic-ai/claude-code
```

#### **Option 2 : Changer le Répertoire par Défaut de npm (Recommandé)**
La meilleure pratique consiste à configurer npm pour utiliser un répertoire dans votre dossier personnel où vous avez les permissions d'écriture.

1. **Créer un répertoire global npm dans votre dossier personnel :**
   ```bash
   mkdir ~/.npm-global
   ```
2. **Configurer npm pour utiliser ce répertoire :**
   ```bash
   npm config set prefix '~/.npm-global'
   ```
3. **Ajouter le nouveau répertoire à votre `PATH` :**
   Ouvrez votre fichier de configuration de shell (par exemple, `~/.bashrc`, `~/.zshrc`, ou `~/.profile`) et ajoutez cette ligne :
   ```bash
   export PATH=~/.npm-global/bin:$PATH
   ```
   Puis, rechargez votre shell :
   ```bash
   source ~/.bashrc  # ou ~/.zshrc, ~/.profile
   ```
4. **Réessayer l'installation :**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

#### **Option 3 : Corriger les Permissions de `/usr/local` (Avancé)**
Si vous souhaitez continuer à utiliser `/usr/local`, vous pouvez changer sa propriété pour votre utilisateur :
```bash
sudo chown -R $(whoami) /usr/local/lib/node_modules
```
Puis réessayez l'installation.

---

**Recommandation :** Utilisez l'**Option 2** pour éviter les problèmes de permissions à l'avenir.