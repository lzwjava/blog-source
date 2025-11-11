---
audio: false
generated: true
lang: fr
layout: post
title: Gestionnaire d'Informations d'Identification Git
translated: true
type: note
---

Vous utilisez **Git Credential Manager (GCM) version 2.6.1** sur **macOS**, et vous avez rencontré un problème où la commande `git config --global credential.helper manager-core` génère une erreur :

```
warning: credential.helper has multiple values
error: cannot overwrite multiple values with a single value
```

Cela se produit parce que plusieurs aides d'authentification (credential helpers) sont déjà définies dans votre configuration Git. Vous devez **effacer les valeurs existantes** avant d'en définir une nouvelle.

---

### **🛠 Résoudre le problème : Réinitialiser l'aide d'authentification**
#### **Étape 1 : Vérifier les aides d'authentification actuelles**
Exécutez :
```sh
git config --global --get-all credential.helper
```
Cela listera toutes les aides d'authentification configurées.

#### **Étape 2 : Supprimer les aides d'authentification précédentes**
Réinitialisez toutes les aides d'authentification en utilisant :
```sh
git config --global --unset-all credential.helper
```

#### **Étape 3 : Définir GCM comme la seule aide d'authentification**
Maintenant, redéfinissez **Git Credential Manager (GCM)** comme l'aide :
```sh
git config --global credential.helper manager-core
```

#### **Étape 4 : Vérifier le changement**
Vérifiez si c'est correctement défini :
```sh
git config --global --get credential.helper
```
Résultat attendu :
```
manager-core
```

---

### **🛠 Alternative : Utiliser `--replace-all`**
Si vous souhaitez écraser les valeurs existantes au lieu de les supprimer d'abord, utilisez :
```sh
git config --global --replace-all credential.helper manager-core
```

---

### **🧩 Dépannage supplémentaire**
Si vous rencontrez toujours des problèmes, vous pouvez vérifier votre configuration Git globale complète :
```sh
git config --global --list
```
Si le problème persiste, faites-le-moi savoir ! 🚀

---

Git Credential Manager (GCM) est une aide d'authentification Git sécurisée qui stocke et gère les informations d'authentification pour les dépôts Git HTTPS. Il fonctionne avec des services comme GitHub, GitLab, Bitbucket et Azure DevOps.

---

## **1. Installer Git Credential Manager**
GCM est inclus avec Git pour Windows et les distributions Git officielles pour macOS et Linux. S'il n'est pas installé, téléchargez-le depuis :

🔗 **[Git Credential Manager sur GitHub](https://github.com/GitCredentialManager/git-credential-manager)**

### **Vérifier si GCM est installé**
Exécutez :
```sh
git credential-manager version
```
S'il est installé, vous verrez un numéro de version. Sinon, installez-le manuellement.

---

## **2. Configurer Git pour utiliser GCM**
Exécutez la commande suivante :
```sh
git config --global credential.helper manager
```
Pour macOS/Linux, utilisez :
```sh
git config --global credential.helper manager-core
```

Pour vérifier l'aide d'authentification actuelle :
```sh
git config --global credential.helper
```

---

## **3. S'authentifier auprès d'un serveur Git**
Une fois configuré, la première fois que vous interagissez avec un dépôt distant via HTTPS (par exemple, `git clone`, `git pull`), GCM vous demandera vos informations d'authentification.

- Si vous utilisez GitHub, GitLab ou Bitbucket, GCM ouvrira un navigateur pour l'authentification OAuth.
- Si vous utilisez un jeton d'accès personnel (PAT), saisissez-le au lieu d'un mot de passe.

---

## **4. Stocker et gérer les informations d'authentification**
GCM stocke les informations d'authentification de manière sécurisée dans le gestionnaire de mots de passe du système d'exploitation :
- **Windows** : Gestionnaire d'identification Windows
- **macOS** : Trousseau macOS
- **Linux** : Fichier chiffré GPG (`~/.git-credentials` ou `~/.gitconfig`)

Pour ajouter manuellement une information d'authentification :
```sh
git credential approve
```

Pour supprimer une information d'authentification stockée :
```sh
git credential reject https://github.com
```

Pour effacer toutes les informations d'authentification :
```sh
git credential reject
```

---

## **5. Utiliser Git Credential Manager avec différents fournisseurs Git**
### **GitHub**
Utilisez un **Jeton d'Accès Personnel (PAT)** au lieu d'un mot de passe :
```sh
git credential reject https://github.com
git pull
```
Il vous sera demandé de vous connecter et de saisir votre jeton.

### **GitLab**
Pour GitLab, utilisez OAuth ou un **PAT** :
```sh
git credential reject https://gitlab.com
git pull
```

### **Azure DevOps**
Utilisez un **PAT** ou l'authentification Azure.

---

## **6. Dépanner les problèmes**
Si les informations d'authentification ne sont pas sauvegardées ou récupérées correctement :
1. Vérifiez l'aide d'authentification :
   ```sh
   git config --global credential.helper
   ```
2. Réinitialisez Git Credential Manager :
   ```sh
   git credential reject https://your-git-service.com
   ```
3. Réinstallez GCM si nécessaire.

Avez-vous besoin d'aide pour le configurer pour un service spécifique ? 🚀