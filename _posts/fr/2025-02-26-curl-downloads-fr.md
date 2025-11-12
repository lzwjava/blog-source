---
audio: false
generated: true
lang: fr
layout: post
title: Dépannage des Téléchargements curl
translated: true
type: note
---

Lorsque vous essayez de télécharger un fichier ZIP d'Eclipse depuis eclipse.org en utilisant `curl -O`, vous pourriez rencontrer un problème où il télécharge un fichier HTML au lieu du fichier ZIP souhaité, accompagné d'une erreur "301 Moved Permanently". Cela se produit parce que l'URL que vous utilisez redirige vers un autre emplacement, et `curl` ne suit pas automatiquement cette redirection vers le fichier réel. Voici comment résoudre ce problème :

### Comprendre le problème

- **301 Moved Permanently** : Ce code de statut HTTP signifie que la ressource (le fichier ZIP) a été déplacée de façon permanente vers une nouvelle URL. Les serveurs utilisent souvent des redirections pour les liens de téléchargement afin de pointer vers des sites miroirs ou des emplacements mis à jour.
- **Comportement de `curl -O`** : L'option `-O` indique à `curl` de sauvegarder le contenu téléchargé dans un fichier portant le nom du fichier distant. Cependant, sans gestion explicite des redirections, `curl` peut sauvegarder le contenu de la réponse de redirection intermédiaire (souvent une page HTML) au lieu de la suivre vers le fichier ZIP.

### Solution

Pour garantir que `curl` suit la redirection et télécharge le fichier ZIP d'Eclipse, utilisez l'option `-L` conjointement avec `-O`. Le drapeau `-L` indique à `curl` de suivre toutes les redirections jusqu'à ce qu'il atteigne la destination finale.

#### Commande

```bash
curl -L -O <URL>
```

- **`-L`** : Suit les redirections, comme la redirection 301, vers le nouvel emplacement.
- **`-O`** : Sauvegarde le fichier avec le nom d'origine de l'URL finale.
- **`<URL>`** : Remplacez ceci par l'URL de téléchargement spécifique d'Eclipse, par exemple `https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip`.

### Instructions étape par étape

1.  **Trouver la bonne URL** :
    - Visitez le site web d'Eclipse (par exemple, `https://www.eclipse.org/downloads/`).
    - Sélectionnez le package souhaité (par exemple, Eclipse IDE for Java Developers).
    - Faites un clic droit sur le lien ou le bouton de téléchargement et copiez l'URL. Alternativement, utilisez les outils de développement de votre navigateur (F12, onglet Réseau) pour capturer l'URL exacte lorsque vous cliquez sur télécharger.

2.  **Exécuter la commande** :
    - Ouvrez votre terminal.
    - Exécutez la commande `curl` avec les options `-L` et `-O`, en utilisant l'URL que vous avez copiée :
      ```bash
      curl -L -O https://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
      ```
    - Cela devrait télécharger le fichier ZIP (par exemple, `eclipse-java-2023-03-R-win32-x86_64.zip`) dans votre répertoire actuel.

### Dépannage

Si vous rencontrez toujours des problèmes, essayez ces étapes supplémentaires :

- **Vérifier les redirections avec une sortie verbeuse** :
  - Utilisez l'option `-v` pour voir des informations détaillées sur la requête et les redirections :
    ```bash
    curl -v -L -O <URL>
    ```
  - Cherchez l'en-tête `Location` dans la réponse 301 pour voir où elle redirige. Si elle pointe vers une page HTML au lieu d'un fichier ZIP, l'URL n'est peut-être pas le lien de téléchargement direct.

- **Vérifier l'URL** :
  - Eclipse utilise souvent un script `download.php` qui peut rediriger vers un miroir. Assurez-vous que votre URL est soit le lien direct vers le fichier ZIP, soit un lien de redirection qui aboutit au fichier. Par exemple, un lien miroir direct pourrait ressembler à :
    ```bash
    curl -L -O https://mirror.its.dal.ca/eclipse/technology/epp/downloads/release/2023-03/R/eclipse-java-2023-03-R-win32-x86_64.zip
    ```

- **Définir un en-tête User-Agent** :
  - Certains serveurs se comportent différemment selon le client. Si le serveur renvoie du HTML parce qu'il détecte `curl`, imitez un navigateur en ajoutant un User-Agent :
    ```bash
    curl -L -O -A "Mozilla/5.0" <URL>
    ```

### Pourquoi cela fonctionne

Le site web d'Eclipse peut rediriger les requêtes de téléchargement vers un miroir ou une URL mise à jour. Sans `-L`, `curl -O` sauvegarde la réponse de redirection (une page HTML) au lieu de la suivre. Ajouter `-L` garantit que `curl` suit la redirection 301 jusqu'au fichier ZIP réel, résolvant ainsi le problème.

En suivant ces étapes, vous devriez réussir à télécharger le fichier ZIP d'Eclipse depuis eclipse.org en utilisant `curl`.