---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre l'Erreur 403 Forbidden de Nginx
translated: true
type: note
---

Pour corriger l'erreur "403 Forbidden" que vous rencontrez avec votre configuration Nginx, vous devez résoudre deux problèmes principaux : une utilisation incorrecte de la directive `root` dans votre bloc `location` et des problèmes potentiels de permissions du système de fichiers. Voici un guide étape par étape pour résoudre le problème en fonction de votre configuration fournie :

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies {
        root /path/to/your/movie/folder;
        autoindex on; # Active le listing des répertoires
    }
}
```

Lorsque vous visitez `http://localhost/movies`, vous obtenez une erreur 403 Forbidden, ce qui indique généralement que Nginx ne peut pas accéder au répertoire cible ou le servir. Voici comment le corriger :

---

### 1. Corriger la Configuration Nginx
Le bloc `location /movies` actuel utilise `root /path/to/your/movie/folder;`. Dans Nginx, la directive `root` ajoute l'URI de la requête (par exemple, `/movies`) au chemin spécifié, ce qui signifie que Nginx tente de servir les fichiers depuis `/path/to/your/movie/folder/movies`. Si ce répertoire n'existe pas, Nginx renvoie une erreur 403.

Pour corriger cela, vous devez utiliser la directive `alias` au lieu de `root`. La directive `alias` mappe l'URI `/movies/` directement vers `/path/to/your/movie/folder/` sans ajouter l'URI, ce qui correspond probablement au comportement souhaité.

Mettez à jour votre configuration comme suit :

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # Active le listing des répertoires
    }
}
```

- **Changements Clés :**
  - Remplacement de `root` par `alias`.
  - Ajout de barres obliques finales à `location /movies/` et `alias /path/to/your/movie/folder/` pour assurer une gestion correcte des répertoires avec `autoindex`.

- **Appliquer les Changements :**
  Après avoir mis à jour le fichier de configuration (par exemple, `/etc/nginx/nginx.conf` ou un fichier dans `/etc/nginx/sites-enabled/`), redémarrez Nginx pour appliquer les changements :
  - Sur Linux : `sudo systemctl restart nginx`
  - Sur Windows : Arrêtez et redémarrez le service Nginx manuellement.

- **Tester l'URL :**
  Visitez `http://localhost/movies/` (notez la barre oblique finale) pour voir si le listing du répertoire apparaît.

---

### 2. Vérifier les Permissions du Système de Fichiers
Si le changement de configuration seul ne résout pas l'erreur 403, le problème pourrait être lié aux permissions du système de fichiers. Nginx a besoin d'un accès en lecture à `/path/to/your/movie/folder/` et à son contenu, et cet accès dépend de l'utilisateur sous lequel Nginx s'exécute (généralement `nginx` ou `www-data`).

- **Identifier l'Utilisateur Nginx :**
  Vérifiez votre fichier de configuration principal Nginx (par exemple, `/etc/nginx/nginx.conf`) pour la directive `user`. Cela pourrait ressembler à :
  ```nginx
  user nginx;
  ```
  Si ce n'est pas spécifié, cela pourrait être par défaut `www-data` ou un autre utilisateur selon votre système.

- **Vérifier les Permissions :**
  Exécutez la commande suivante pour inspecter les permissions de votre dossier de films :
  ```bash
  ls -l /path/to/your/movie/folder
  ```
  Cela affichera le propriétaire, le groupe et les permissions (par exemple, `drwxr-xr-x`).

- **Ajuster les Permissions si Nécessaire :**
  Assurez-vous que l'utilisateur Nginx a un accès en lecture (et en exécution pour les répertoires). Voici deux options :
  - **Option 1 : Changer le Propriétaire (Recommandé) :**
    Définissez le propriétaire du dossier comme étant l'utilisateur Nginx (par exemple, `nginx`) :
    ```bash
    sudo chown -R nginx:nginx /path/to/your/movie/folder
    ```
    Remplacez `nginx` par l'utilisateur réel si différent (par exemple, `www-data`).

  - **Option 2 : Rendre Lisible par Tous (Moins Sécurisé) :**
    Si vous ne voulez pas changer le propriétaire, rendez le dossier lisible par les autres :
    ```bash
    sudo chmod -R o+r /path/to/your/movie/folder
    ```

- **Assurer l'Accès au Répertoire :**
  Le répertoire lui-même a besoin des permissions d'exécution (`x`) pour que Nginx puisse accéder à son contenu :
  ```bash
  sudo chmod o+x /path/to/your/movie/folder
  ```

- **Vérifier les Répertoires Parents :**
  Si `/path/to/your/movie/folder` se trouve dans un répertoire parent restreint (par exemple, `/home/user/`), assurez-vous que tous les répertoires parents jusqu'à la racine ont les permissions d'exécution pour l'utilisateur Nginx :
  ```bash
  sudo chmod o+x /path /path/to /path/to/your /path/to/your/movie
  ```

---

### 3. Vérifier et Déboguer
Après avoir effectué ces changements, testez à nouveau en visitant `http://localhost/movies/`. Si l'erreur 403 persiste :

- **Vérifier le Journal d'Erreurs Nginx :**
  Consultez le journal d'erreurs pour obtenir des détails spécifiques (généralement situé à `/var/log/nginx/error.log`) :
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```
  Recherchez des messages comme "permission denied" ou "directory index is forbidden" pour identifier le problème.

- **Considérations Supplémentaires :**
  - **SELinux (le cas échéant) :** Sur des systèmes comme CentOS avec SELinux activé, cela pourrait bloquer l'accès. Définissez temporairement SELinux en mode permissif pour tester :
    ```bash
    sudo setenforce 0
    ```
    Si cela résout le problème, vous devrez ajuster les politiques SELinux (par exemple, en utilisant `chcon` ou `audit2allow`).
  - **Pare-feu :** Assurez-vous que le port 80 est ouvert si vous y accédez depuis une autre machine (bien que cela soit peu probable lors de tests locaux via `localhost`).

---

### Configuration Finale
Voici la configuration corrigée et complète :

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # Active le listing des répertoires
    }
}
```

- Remplacez `/path/to/your/movie/folder/` par le chemin absolu réel vers votre répertoire de films.
- Redémarrez Nginx : `sudo systemctl restart nginx`.
- Visitez `http://localhost/movies/` pour confirmer que le listing du répertoire fonctionne.

En corrigeant la directive `alias` et en assurant des permissions de fichiers appropriées, l'erreur 403 Forbidden devrait être résolue, vous permettant d'accéder à votre dossier de films via Nginx avec succès.

---

Pour corriger votre erreur Nginx 403 Forbidden et vous assurer que votre fichier `.mkv` unique est accessible, affinons la configuration en fonction de votre situation. Vous avez un fichier `.mkv` et vous voulez savoir où l'enregistrer pour que l'utilisateur Nginx puisse y accéder. Ci-dessous, je vous guide à travers le processus étape par étape, y compris le choix d'un répertoire approprié et la configuration de Nginx.

### Étape 1 : Choisir un Répertoire pour Votre Fichier `.mkv`
Lorsque vous décidez où stocker votre fichier `.mkv` pour que Nginx puisse le servir, considérez ces facteurs :
- **Accessibilité** : L'utilisateur Nginx (par exemple, `nginx` ou `www-data`) a besoin d'un accès en lecture.
- **Conventions** : Les serveurs web servent généralement les fichiers depuis des répertoires standard comme `/var/www/` ou `/srv/www/`.
- **Sécurité** : Évitez de placer les fichiers dans des emplacements trop permissifs ou sensibles (par exemple, `/home/user/` sauf si nécessaire).

Pour votre cas, comme il s'agit d'un seul fichier `.mkv` et que vous testez localement (`localhost`), je recommande d'utiliser `/var/www/html/movies/` comme emplacement simple et standard. Voici pourquoi :
- `/var/www/html/` est une racine web par défaut courante pour Nginx et Apache.
- Elle est généralement détenue par l'utilisateur ou le groupe du serveur web, ce qui facilite la gestion des permissions.
- Ajouter un sous-répertoire `/movies/` permet de garder les choses organisées.

Si `/var/www/html/` n'existe pas ou n'est pas adapté à votre système, les alternatives incluent :
- `/srv/www/movies/` (un autre répertoire web standard).
- `/usr/share/nginx/html/movies/` (parfois la racine des documents par défaut de Nginx).

Pour cet exemple, utilisons `/var/www/html/movies/`.

### Étape 2 : Configurer le Répertoire et le Fichier
En supposant que vous êtes sur un système Linux, suivez ces étapes :

1. **Créer le Répertoire** :
   ```bash
   sudo mkdir -p /var/www/html/movies
   ```

2. **Déplacer Votre Fichier `.mkv`** :
   Remplacez `yourfile.mkv` par le nom réel de votre fichier et déplacez-le vers le répertoire :
   ```bash
   sudo mv /path/to/yourfile.mkv /var/www/html/movies/yourfile.mkv
   ```

3. **Définir les Permissions** :
   L'utilisateur Nginx (généralement `nginx` ou `www-data`) a besoin d'un accès en lecture au fichier et d'un accès en exécution au répertoire. Tout d'abord, identifiez l'utilisateur Nginx en vérifiant `/etc/nginx/nginx.conf` :
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   Recherchez une ligne comme `user nginx;` ou `user www-data;`. Si ce n'est pas spécifié, cela pourrait être par défaut `www-data` (Ubuntu/Debian) ou `nginx` (CentOS/RHEL).

   Ensuite, ajustez la propriété :
   ```bash
   sudo chown -R nginx:nginx /var/www/html/movies
   ```
   Remplacez `nginx` par `www-data` ou l'utilisateur réel si différent.

   Assurez des permissions appropriées :
   ```bash
   sudo chmod -R 755 /var/www/html/movies
   ```
   - `755` signifie que le propriétaire (Nginx) a un accès complet, et les autres (y compris le processus du serveur web) peuvent lire et exécuter (naviguer) le répertoire.

### Étape 3 : Configurer Nginx
Mettez à jour votre configuration Nginx pour servir le fichier `.mkv` depuis `/var/www/html/movies/`. Voici une configuration minimale fonctionnelle :

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/html/movies/;
        autoindex on; # Active le listing des répertoires si vous voulez parcourir les fichiers
    }
}
```

- **Notes :**
  - Utilisez `alias` au lieu de `root` pour mapper `/movies/` directement vers `/var/www/html/movies/`.
  - `autoindex on;` est optionnel. Si vous le désactivez (`autoindex off;`), vous devrez spécifier l'URL exacte du fichier (par exemple, `http://localhost/movies/yourfile.mkv`) pour y accéder.

Sauvegardez cette configuration (par exemple, dans `/etc/nginx/sites-enabled/default` ou un fichier personnalisé comme `/etc/nginx/conf.d/movies.conf`), puis testez et redémarrez Nginx :
```bash
sudo nginx -t  # Tester la configuration pour les erreurs de syntaxe
sudo systemctl restart nginx  # Appliquer les changements
```

### Étape 4 : Tester l'Accès
- Ouvrez votre navigateur et visitez :
  - `http://localhost/movies/` (si `autoindex` est activé, vous verrez un listing du répertoire avec `yourfile.mkv`).
  - `http://localhost/movies/yourfile.mkv` (pour accéder directement au fichier).
- Si cela fonctionne, le fichier devrait soit s'afficher dans le navigateur (s'il est pris en charge), soit proposer un téléchargement.

### Étape 5 : Déboguer si Nécessaire
Si vous obtenez toujours une erreur 403 :
1. **Vérifier les Permissions** :
   ```bash
   ls -l /var/www/html/movies/
   ```
   Assurez-vous que `yourfile.mkv` est lisible (par exemple, `-rwxr-xr-x` ou au moins `-rw-r--r--`).

2. **Vérifier les Journaux Nginx** :
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```
   Recherchez des indices comme "permission denied."

3. **SELinux (le cas échéant)** :
   Si vous êtes sur un système avec SELinux (par exemple, CentOS), exécutez :
   ```bash
   sudo setenforce 0  # Désactiver temporairement
   ```
   Testez à nouveau. Si cela fonctionne, vous devrez ajuster les contextes SELinux :
   ```bash
   sudo chcon -R -t httpd_sys_content_t /var/www/html/movies/
   sudo setenforce 1  # Réactiver SELinux
   ```

### Réflexions Finales
En enregistrant votre fichier `.mkv` dans `/var/www/html/movies/`, en définissant les permissions correctes et en utilisant la directive `alias` dans Nginx, vous devriez résoudre l'erreur 403. Cette configuration est simple et suit les conventions des serveurs web, la rendant facile pour l'utilisateur Nginx d'accéder au fichier. Faites-moi savoir si vous rencontrez des problèmes !

---

Si vous obtenez une erreur "invalid user" avec `sudo chown -R nginx:nginx /var/www/movies`, cela signifie que l'utilisateur `nginx` n'existe pas sur votre système. Cela se produit parce que le processus Nginx pourrait s'exécuter sous un utilisateur différent, comme `www-data` (commun sur Debian/Ubuntu) ou un autre par défaut selon votre OS.

### Correction : Identifier et Utiliser le Bon Utilisateur
1. **Vérifier l'Utilisateur Nginx** :
   Regardez dans votre fichier de configuration Nginx (généralement `/etc/nginx/nginx.conf`) :
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   - S'il dit `user www-data;`, utilisez `www-data`.
   - S'il dit `user nginx;`, l'utilisateur `nginx` devrait exister (pourrait indiquer une mauvaise configuration).
   - Si aucune directive `user` n'est trouvée, l'utilisateur par défaut dépend de votre système :
     - Ubuntu/Debian : `www-data`
     - CentOS/RHEL : `nginx`
     - Autre : Pourrait être `http`, `apache`, ou similaire.

2. **Alternative : Vérifier le Processus en Cours d'Exécution** :
   Si la configuration n'est pas claire, voyez sous quel utilisateur Nginx s'exécute :
   ```bash
   ps aux | grep nginx
   ```
   Recherchez dans la première colonne (par exemple, `www-data` ou `nginx`) pour les processus worker.

3. **Appliquer le Bon Utilisateur** :
   En supposant que c'est `www-data` (commun sur Ubuntu/Debian), mettez à jour la commande :
   ```bash
   sudo chown -R www-data:www-data /var/www/movies
   ```
   S'il s'agit d'un utilisateur différent (par exemple, `http`), utilisez :
   ```bash
   sudo chown -R http:http /var/www/movies
   ```

4. **Définir les Permissions** :
   Après avoir corrigé la propriété, assurez des permissions appropriées :
   ```bash
   sudo chmod -R 755 /var/www/movies
   ```

5. **Redémarrer et Tester** :
   ```bash
   sudo systemctl restart nginx
   ```
   Visitez `http://localhost/movies/yourfile.mkv`.

### Si Toujours Bloqué
Si ni `nginx` ni `www-data` ne fonctionnent et que la vérification du processus n'aide pas, faites-moi savoir votre OS (par exemple, Ubuntu, CentOS) ou la sortie de `ps aux | grep nginx`, et je identifierai l'utilisateur exact pour vous !

---

Si `autoindex on;` est défini mais que `http://localhost/movies/` ne liste toujours pas les fichiers, déboguons et corrigeons cela étape par étape. Comme vous ne voyez pas le listing du répertoire, cela pourrait être un problème de configuration, un problème de permissions ou autre chose qui le bloque. Voici comment le résoudre :

### 1. Vérifier Votre Configuration
Assurez-vous que votre configuration Nginx est correcte et appliquée. Elle devrait ressembler à ceci :

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

- **Erreurs Courantes :**
  - Faute de frappe dans le chemin `alias` (par exemple, `/var/www/movie/` au lieu de `/var/www/movies/`).
  - `autoindex on;` est dans le mauvais bloc ou commenté.
  - Le fichier de configuration n'est pas chargé (par exemple, enregistré au mauvais emplacement).

Vérifiez où se trouve votre configuration :
- Si elle est dans `/etc/nginx/sites-enabled/`, assurez-vous qu'elle est correctement liée (par exemple, `ls -l /etc/nginx/sites-enabled/`).
- Si elle est dans `/etc/nginx/conf.d/`, assurez-vous qu'elle se termine par `.conf` (par exemple, `movies.conf`).

Testez et rechargez :
```bash
sudo nginx -t
sudo systemctl reload nginx  # Recharger au lieu de redémarrer pour éviter les interruptions
```

### 2. Confirmer l'Existence des Fichiers
Vérifiez que `/var/www/movies/` contient votre fichier `.mkv` :
```bash
ls -l /var/www/movies/
```
- S'il est vide, déplacez votre fichier là :
  ```bash
  sudo mv /path/to/yourfile.mkv /var/www/movies/
  ```
- S'il n'est pas vide, notez les noms de fichiers pour les tests.

### 3. Vérifier les Permissions
Nginx a besoin d'un accès en lecture (`r`) et en exécution (`x`) au répertoire et aux fichiers. Vérifiez :
```bash
ls -ld /var/www/movies/
ls -l /var/www/movies/
```
- La sortie devrait ressembler à :
  ```
  drwxr-xr-x 2 www-data www-data 4096 Mar 15 14:00 /var/www/movies/
  -rw-r--r-- 1 www-data www-data 123456 Mar 15 14:00 yourfile.mkv
  ```
- Corrigez si nécessaire (remplacez `www-data` par votre utilisateur Nginx) :
  ```bash
  sudo chown -R www-data:www-data /var/www/movies/
  sudo chmod -R 755 /var/www/movies/
  ```

### 4. Vérifier les Journaux
Consultez le journal d'erreurs Nginx pour obtenir des indices :
```bash
sudo tail -n 20 /var/log/nginx/error.log
```
- **"permission denied"** : Indique un problème de permissions—revérifiez l'étape 3.
- **"directory index forbidden"** : Suggère que `autoindex` ne fonctionne pas—vérifiez à nouveau la configuration.
- Aucune erreur pertinente : Pourrait signifier que Nginx n'atteint pas le bon bloc de localisation.

### 5. Tester l'Accès Direct
Essayez d'accéder à un fichier spécifique :
- Visitez `http://localhost/movies/yourfile.mkv`.
- Si cela fonctionne mais que `/movies/` ne fonctionne pas, `autoindex` ou la configuration du répertoire est le problème.

### 6. Corrections Courantes
- **Barre Oblique Finale** : Assurez-vous que `alias` se termine par `/` (`/var/www/movies/`), et testez à la fois `http://localhost/movies` et `http://localhost/movies/`.
- **SELinux (si sur CentOS/RHEL)** :
  ```bash
  sudo setenforce 0  # Désactiver temporairement
  ```
  Testez à nouveau. Si cela fonctionne, appliquez :
  ```bash
  sudo chcon -R -t httpd_sys_content_t /var/www/movies/
  sudo setenforce 1  # Réactiver SELinux
  ```
- **Blocs de Localisation Conflictuels** : Si un autre bloc `location` (par exemple, `location /`) écrase `/movies/`, déplacez ce bloc plus haut dans la configuration ou rendez-le plus spécifique.

### 7. Configuration de Test Minimale
Si cela ne fonctionne toujours pas, simplifiez pour isoler le problème. Remplacez votre configuration par :

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

Sauvegardez, testez et rechargez :
```bash
sudo nginx -t
sudo systemctl reload nginx
```

### Que Se Passe-t-il ?
Dites-moi :
- Que voyez-vous à `http://localhost/movies/` (par exemple, 403, 404, page blanche) ?
- Des erreurs dans `sudo tail -n 20 /var/log/nginx/error.log` ?
- La sortie de `ls -l /var/www/movies/` ?

Avec cela, je peux identifier le problème exact et faire fonctionner votre listing de répertoire !