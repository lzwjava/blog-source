---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide pour changer le port de Nginx sur macOS
translated: true
type: note
---

Vous souhaitez que Nginx sur macOS écoute sur **un port différent** de celui par défaut (80 pour HTTP, 443 pour HTTPS). Voici un guide étape par étape clair :

---

### 1. Localisez votre fichier de configuration Nginx

* Si vous l'avez installé via **Homebrew**, la configuration par défaut se trouve généralement ici :

  ```
  /usr/local/etc/nginx/nginx.conf
  ```

  ou, sur Apple Silicon :

  ```
  /opt/homebrew/etc/nginx/nginx.conf
  ```
* Si vous l'avez installé manuellement, il peut s'agir de `/usr/local/nginx/conf/nginx.conf`.

---

### 2. Modifiez la directive `listen`

1. Ouvrez le fichier de configuration dans un éditeur de texte :

   ```bash
   nano /opt/homebrew/etc/nginx/nginx.conf
   ```
2. Trouvez le bloc `server` :

   ```nginx
   server {
       listen 80;
       server_name localhost;

       location / {
           root   html;
           index  index.html index.htm;
       }
   }
   ```
3. Changez `listen 80;` pour le port souhaité, par exemple 8080 :

   ```nginx
   listen 8080;
   ```

---

### 3. Testez la configuration

Exécutez :

```bash
nginx -t
```

* Si le message indique `syntax is ok` et `test is successful`, votre configuration est valide.
* S'il y a des erreurs, vérifiez les numéros de ligne indiqués.

---

### 4. Redémarrez Nginx

* Si installé via Homebrew :

```bash
brew services restart nginx
```

* Ou manuellement :

```bash
sudo nginx -s reload
```

---

### 5. Accédez via le nouveau port

* Dans votre navigateur ou avec curl :

```
http://localhost:8080
```

---

**Notes supplémentaires :**

* Les ports **<1024** nécessitent `sudo` sur macOS. Ainsi, utiliser des ports comme 80 nécessitera les privilèges root, mais pas 8080 ou 3000.
* Si vous souhaitez exécuter plusieurs serveurs Nginx simultanément, chacun **doit avoir un port unique**.

---

Je peux aussi vous donner une **astuce rapide pour exécuter temporairement Nginx sur n'importe quel port sans modifier nginx.conf** en utilisant un drapeau en ligne de commande. C'est pratique pour les tests. Voulez-vous que je vous la montre ?