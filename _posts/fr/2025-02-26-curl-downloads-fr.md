---
audio: false
generated: false
lang: fr
layout: post
title: Résoudre les problèmes de téléchargements curl
translated: true
---

Lorsque vous essayez de télécharger un fichier ZIP Eclipse depuis eclipse.org en utilisant `curl -O`, vous pourriez rencontrer un problème où il télécharge un fichier HTML au lieu du fichier ZIP souhaité, accompagné d'une erreur "301 Moved Permanently". Cela se produit parce que l'URL que vous utilisez redirige vers un autre emplacement, et `curl` ne suit pas automatiquement cette redirection vers le fichier réel. Voici comment résoudre ce problème :

### Comprendre le Problème

- **301 Moved Permanently** : Ce code de statut HTTP signifie que la ressource (le fichier ZIP) a été déplacée de manière permanente vers une nouvelle URL. Les serveurs utilisent souvent des redirections pour les liens de téléchargement afin de pointer vers des sites miroirs ou des emplacements mis à jour.
- **Comportement de `curl -O`** : L'option `-O` indique à `curl` d'enregistrer le contenu téléchargé dans un fichier nommé d'après le fichier distant. Cependant, sans gérer explicitement les redirections, `curl` pourrait enregistrer le contenu de la réponse de redirection intermédiaire (souvent une page HTML) au lieu de suivre la redirection vers le fichier ZIP.

### Solution

Pour vous assurer que `curl` suit la redirection et télécharge le fichier ZIP Eclipse, utilisez l'option `-L` en même temps que `-O`. Le drapeau `-L` indique à `curl` de suivre toutes les redirections jusqu'à ce qu'il atteigne la destination finale.

#### Commande

```bash
curl -L -O <URL>
```

- **`-L`** : Suit les redirections, comme la redirection 301, vers le nouvel emplacement.
- **`-O`** : Enregistre le fichier avec le nom d'origine à partir de l'URL finale.
- **`<URL>`** : Remplacez ceci par l'URL de téléchargement Eclipse spécifique, comme `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`.

### Instructions Étape par Étape

1. **Trouver l'URL Correcte** :
   - Visitez le site web Eclipse (par exemple, `https://www.eclipse.org/downloads/`).
   - Sélectionnez le package souhaité (par exemple, Eclipse IDE pour les développeurs Java).
   - Faites un clic droit sur le lien ou le bouton de téléchargement et copiez l'URL. Alternativement, utilisez les outils de développement de votre navigateur (F12, onglet Réseau) pour capturer l'URL exacte lorsque vous cliquez sur télécharger.

2. **Exécuter la Commande** :
   - Ouvrez votre terminal.
   - Exécutez la commande `curl` avec les options `-L` et `-O`, en utilisant l'URL que vous avez copiée :
     ```bash
     curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
     ```
   - Cela devrait télécharger le fichier ZIP (par exemple, `eclipse-java-2023-03-R-win32-x86_64.zip`) dans votre répertoire actuel.

### Dépannage

Si vous rencontrez toujours des problèmes, essayez ces étapes supplémentaires :

- **Vérifier les Redirections avec une Sortie Verbose** :
  - Utilisez l'option `-v` pour voir des informations détaillées sur la requête et les redirections :
    ```bash
    curl -v -L -O <URL>
    ```
  - Regardez l'en-tête `Location` dans la réponse 301 pour voir où elle redirige. Si elle pointe vers une page HTML au lieu d'un fichier ZIP, l'URL pourrait ne pas être le lien de téléchargement direct.

- **Vérifier l'URL** :
  - Eclipse utilise souvent un script `download.php` qui peut rediriger vers un miroir. Assurez-vous que votre URL est soit le lien direct vers le fichier ZIP, soit un lien de redirection qui se résout en fichier. Par exemple, un lien miroir direct pourrait ressembler à :
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **Définir un En-tête User-Agent** :
  - Certains serveurs se comportent différemment en fonction du client. Si le serveur renvoie HTML parce qu'il détecte `curl`, imitez un navigateur en ajoutant un User-Agent :
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### Pourquoi Cela Fonctionne

Le site web Eclipse peut rediriger les demandes de téléchargement vers un miroir ou une URL mise à jour. Sans `-L`, `curl -O` enregistre la réponse de redirection (une page HTML) au lieu de la suivre. L'ajout de `-L` assure que `curl` suit la redirection 301 vers le fichier ZIP réel, résolvant ainsi le problème.

En suivant ces étapes, vous devriez pouvoir télécharger avec succès le fichier ZIP Eclipse depuis eclipse.org en utilisant `curl`.