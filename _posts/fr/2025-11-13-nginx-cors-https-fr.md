---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration CORS et HTTPS de Nginx
translated: true
type: note
---

```nginx
# Définit une map pour gérer les origines autorisées
map $http_origin $cors_origin {
    default "https://example.com";
    "http://localhost:3000" "http://localhost:3000";
    "https://example.com" "https://example.com";
    "https://www.example.com" "https://www.example.com";
}
```

### Fonctionnement
- Crée une variable `$cors_origin` basée sur la valeur de l'en-tête `Origin` entrant (`$http_origin`).
- Si la requête provient de `http://localhost:3000`, `https://example.com` ou `https://www.example.com`, elle renvoie exactement cette origine.
- Pour toute autre origine (ou aucune origine), elle utilise par défaut `https://example.com`.
- Ceci est utilisé plus tard pour définir dynamiquement l'en-tête `Access-Control-Allow-Origin`, activant CORS uniquement pour les domaines frontaux de confiance.

---

```nginx
# Redirection HTTP vers HTTPS
server {
    listen 80;
    server_name example.com api.example.com;
    return 301 https://$host$request_uri;
}
```

### Fonctionnement
- Écoute sur le port 80 (HTTP).
- Correspond aux requêtes pour `example.com` ou `api.example.com`.
- Redirige définitivement (301) tout le trafic vers la version HTTPS de la même URL.
- Impose des connexions sécurisées ; aucun accès HTTP simple n'est autorisé.

---

```nginx
# Configuration principale du site pour example.com
server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    root /home/project/project-web;
    index index.html index.htm index.php default.html default.htm default.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires 30d;
    }

    location ~ .*\.(js|css)?$ {
        expires 12h;
    }

    error_page 404 /index.html;
}
```

### Fonctionnement
- **Serveur HTTPS** pour `example.com` sur le port 443 avec SSL activé.
- Utilise des certificats **Let's Encrypt** (renouvelables automatiquement, gratuits).
- Impose des versions TLS modernes (`TLSv1.2`, `TLSv1.3`) et des chiffrements robustes pour la sécurité.
- Sert les fichiers statiques depuis `/home/project/project-web`.
- Tente de servir le fichier demandé → le répertoire → 404.
- Définit les **en-têtes de cache** :
  - Images : cache de 30 jours.
  - JS/CSS : cache de 12 heures.
- Toutes les erreurs 404 sont redirigées vers `index.html` → permet le **routage SPA (Single Page App)** (ex: React, Vue).

---

```nginx
# Configuration API pour api.example.com
server {
    listen 443 ssl;
    server_name api.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com-0001/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com-0001/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";

    location / {
        # Efface tout en-tête Access-Control préexistant
        more_clear_headers 'Access-Control-Allow-Origin';

        # Gère les requêtes préliminaires CORS (preflight)
        if ($request_method = 'OPTIONS') {
            add_header 'Access-Control-Allow-Origin' $cors_origin;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE';
            add_header 'Access-Control-Allow-Headers' 'Origin, Content-Type, Accept, Authorization, X-Client-Info, X-Trace-Id, X-Requested-With, X-HTTP-Method-Override, DNT, Keep-Alive, User-Agent, If-Modified-Since, Cache-Control, Content-Range, Range';
            add_header 'Access-Control-Max-Age' 3600;
            return 204;
        }

        add_header 'Access-Control-Allow-Origin' $cors_origin always;
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
        add_header 'Access-Control-Allow-Headers' '...' always;

        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 600s;
        proxy_send_timeout 600s;
        proxy_read_timeout 600s;
        send_timeout 600s;
    }
}
```

### Fonctionnement
- **Proxy inverse HTTPS** pour `api.example.com`.
- Utilise un **certificat Let's Encrypt distinct** (probablement dû à de multiples domaines/SAN).
- Tout le trafic est proxyfié vers un **backend local** fonctionnant sur `localhost:5000` (ex: Flask, Node.js, etc.).

#### Gestion de CORS
- Utilise la map `$cors_origin` pour **autoriser dynamiquement** uniquement les origines approuvées.
- **Efface toute valeur existante** de `Access-Control-Allow-Origin` pour éviter les conflits.
- Gère les **requêtes préliminaires OPTIONS** :
  - Renvoie immédiatement `204 No Content`.
  - Autorise les méthodes et en-têtes courants.
  - Met en cache la requête préliminaire pendant 1 heure (`Max-Age: 3600`).
- Pour les requêtes réelles, ajoute les en-têtes CORS avec `always` pour qu'ils apparaissent même sur les réponses d'erreur.

#### Paramètres du Proxy
- Transmet l'IP réelle du client et les informations de protocole au backend.
- Délais d'attente élevés (10 minutes) → adapté pour les opérations API longues (ex: téléchargements de fichiers, calculs lourds).

---

### Résumé de l'Architecture

| Composant           | Objectif |
|---------------------|----------|
| `example.com`       | Sert le SPA statique (React/Vue/etc.) |
| `api.example.com`   | Passerelle API sécurisée → backend sur le port 5000 |
| HTTP → HTTPS        | Tout le trafic forcé en TLS |
| CORS                | Restreint à `example.com`, `www`, et `localhost:3000` |
| Cache               | Optimisé pour les performances |
| SSL                 | Let's Encrypt, chiffrements modernes |

### Notes de Sécurité
- Configuration TLS robuste (note A+ sur SSL Labs probable).
- CORS **n'est pas en wildcard** → empêche les sites non autorisés d'appeler l'API.
- Gestion efficace des requêtes préliminaires.
- IP réelle transférée → utile pour la journalisation/la limitation de débit dans le backend.

Faites-moi savoir si vous voulez un diagramme ou une version Dockerisée !