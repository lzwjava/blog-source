---
audio: false
date: 2025-09-14
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Désactivation de l'authentification de connexion à LibreChat
translated: true
type: note
---

Pour que **LibreChat** fonctionne sans nécessiter de connexions fréquentes (ou pour désactiver complètement la connexion), vous pouvez ajuster les paramètres d'authentification. Voici les étapes pour résoudre le problème :

---

### **1. Désactiver l'authentification (Aucune connexion requise)**
Si vous souhaitez que **LibreChat soit complètement ouvert** (aucune connexion), modifiez la configuration :

#### **Option A : Variables d'environnement (Recommandé)**
Définissez les éléments suivants dans votre fichier `.env` (ou variables d'environnement) :
```env
# Désactiver complètement l'authentification
AUTHENTICATION=false
```
Puis redémarrez LibreChat :
```bash
docker compose down && docker compose up -d  # Si vous utilisez Docker
# OU
npm run build && npm run start  # Si vous l'exécutez localement
```

#### **Option B : Modifier `config.yaml`**
Si vous utilisez un fichier `config.yaml`, ajoutez :
```yaml
auth:
  enabled: false
```

---

### **2. Corriger les problèmes de déconnexion fréquente (Si vous souhaitez garder la connexion)**
Si vous **souhaitez conserver l'authentification** mais corriger le problème de déconnexion fréquente, essayez ces solutions :

#### **A. Augmenter l'expiration de la session/du cookie**
Modifiez les paramètres de session dans `.env` :
```env
# Prolonger le délai d'expiration de la session (en secondes, par exemple 7 jours = 604800)
SESSION_EXPIRY=604800

# S'assurer que les cookies sont sécurisés (si vous utilisez HTTPS)
COOKIE_SECURE=true  # Mettre à false pour tester en HTTP
COOKIE_SAME_SITE=lax
```

#### **B. Utiliser un stockage de session persistant**
Par défaut, LibreChat peut utiliser des sessions en mémoire (qui se réinitialisent au redémarrage). Passez à un **stockage de session basé sur une base de données** (par exemple, Redis ou PostgreSQL) :

1. **Installer Redis** (s'il n'est pas déjà installé) :
   ```bash
   docker run -d --name redis -p 6379:6379 redis
   ```
2. Mettez à jour `.env` :
   ```env
   SESSION_STORE=redis
   REDIS_URL=redis://localhost:6379
   ```

#### **C. Vérifier les paramètres du proxy inverse (Si vous utilisez Nginx/Apache)**
Si vous êtes derrière un proxy (par exemple, Nginx), assurez-vous que :
- Les cookies sont correctement transmis.
- `ProxyPass` inclut les directives `cookie`.

Exemple de configuration Nginx :
```nginx
location / {
    proxy_pass http://localhost:3080;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_cookie_path / /;  # S'assurer que les cookies ne sont pas mal délimités
}
```

#### **D. Vider le cache du navigateur et tester en navigation privée**
Parfois, le cache du navigateur ou des cookies corrompus causent des problèmes. Essayez :
- Effacer les cookies pour `librechat.example.com`.
- Tester en **Mode Navigation privée** ou avec un navigateur différent.

---

### **3. Déboguer les problèmes de cookies**
Si les cookies ne persistent toujours pas :
1. **Vérifiez les Outils de développement du navigateur** (`F12` > **Application** > **Cookies**) pour voir si `connect.sid` (ou similaire) est défini.
2. **Vérifiez l'attribut `SameSite`** (devrait être `Lax` ou `None` si cross-site).
3. **Assurez-vous que le `Domain` est correct** (par exemple, `.example.com` pour les sous-domaines).

---

### **4. Mettre à jour LibreChat**
Si vous utilisez une ancienne version, des bogues ont pu être corrigés dans les versions plus récentes :
```bash
git pull origin main
docker compose down && docker compose up -d --build
```

---

### **Notes finales**
- **Avertissement de sécurité** : Désactiver l'authentification (`AUTHENTICATION=false`) rend LibreChat **accessible publiquement**. Ne faites cela que pour des réseaux de confiance/internes.
- **HTTPS requis** : Si vous utilisez des cookies, assurez-vous que votre site est en **HTTPS** (ou définissez `COOKIE_SECURE=false` pour les tests).