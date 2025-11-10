---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration Nginx sur macOS Homebrew
translated: true
type: note
---

Pour Nginx installé via Homebrew sur macOS (comme indiqué par le chemin du binaire `/opt/homebrew/bin/nginx`), le fichier de configuration principal se trouve généralement à l'emplacement :

```
/opt/homebrew/etc/nginx/nginx.conf
```

Ce répertoire contient également d'autres fichiers associés, tels que les blocs serveur dans un sous-répertoire `servers/` (par exemple, `/opt/homebrew/etc/nginx/servers/`).

Pour confirmer le chemin exact du fichier de configuration utilisé par votre instance Nginx, exécutez la commande suivante dans votre terminal :

```
nginx -t
```

Cela testera la configuration et affichera le chemin vers le fichier `nginx.conf` qu'il utilise. Alternativement, utilisez `nginx -V` pour voir les détails de compilation, y compris le préfixe du chemin de configuration.

Si vous êtes sur un Mac Intel plus ancien où Homebrew s'installe dans `/usr/local` à la place, le chemin serait `/usr/local/etc/nginx/nginx.conf`, mais votre chemin de binaire fourni confirme l'emplacement `/opt/homebrew`.

**Références**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)