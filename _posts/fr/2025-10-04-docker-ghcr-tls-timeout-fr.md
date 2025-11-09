---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre l'Erreur de Délai de Connexion TLS de Docker GHCR
translated: true
type: note
---

L'erreur que vous rencontrez, `Get "https://ghcr.io/v2/": net/http: TLS handshake timeout`, indique généralement un problème de réseau lorsque Docker tente de récupérer des images depuis GitHub Container Registry (GHCR). Voici quelques étapes pour résoudre le problème :

---

### 1. **Vérifiez votre connexion Internet**
- Assurez-vous que votre machine a une connexion Internet stable.
- Essayez d'accéder à `https://ghcr.io` dans votre navigateur pour confirmer que vous pouvez atteindre le site.

---

### 2. **Vérifiez le statut du démon Docker**
- Redémarrez le démon Docker :
  ```bash
  sudo systemctl restart docker
  ```
- Vérifiez que Docker est en cours d'exécution :
  ```bash
  sudo systemctl status docker
  ```

---

### 3. **Configurez le DNS de Docker**
- Si vous êtes derrière un réseau d'entreprise ou un proxy, Docker peut avoir besoin de paramètres DNS personnalisés.
- Modifiez ou créez le fichier `/etc/docker/daemon.json` :
  ```json
  {
    "dns": ["8.8.8.8", "1.1.1.1"]
  }
  ```
- Redémarrez Docker :
  ```bash
  sudo systemctl restart docker
  ```

---

### 4. **Vérifiez les paramètres de proxy**
- Si vous êtes derrière un proxy, configurez Docker pour l'utiliser :
  ```bash
  mkdir -p ~/.docker
  echo '{
    "proxies": {
      "default": {
        "httpProxy": "http://your-proxy-address:port",
        "httpsProxy": "http://your-proxy-address:port",
        "noProxy": "localhost,127.0.0.1"
      }
    }
  }' > ~/.docker/config.json
  ```
- Remplacez `your-proxy-address:port` par les détails réels de votre proxy.

---

### 5. **Réessayez de récupérer l'image manuellement**
- Essayez de récupérer l'image manuellement pour voir si le problème persiste :
  ```bash
  docker pull ghcr.io/librechat/librechat:latest
  ```
- Si cela fonctionne, réessayez `docker-compose up -d`.

---

### 6. **Vérifiez les restrictions du pare-feu/réseau**
- Assurez-vous que votre pare-feu ou votre réseau ne bloque pas l'accès à `ghcr.io`.
- Désactivez temporairement le pare-feu pour tester :
  ```bash
  sudo ufw disable
  ```
  (Réactivez-le après les tests si nécessaire.)

---

### 7. **Mettez à jour Docker et Docker-Compose**
- Assurez-vous d'utiliser les dernières versions :
  ```bash
  sudo apt update && sudo apt upgrade docker-ce docker-compose-plugin
  ```

---

### 8. **Définissez les variables d'environnement UID/GID**
- Les avertissements concernant `UID` et `GID` ne sont pas critiques, mais vous pouvez les définir dans votre fichier `.env` ou `docker-compose.yml` pour les supprimer :
  ```bash
  echo "UID=$(id -u)" >> .env
  echo "GID=$(id -g)" >> .env
  ```

---

### 9. **Utilisez un miroir de registre différent (Optionnel)**
- Si GHCR est constamment inaccessible, vous pouvez essayer d'utiliser un miroir (bien que cela ne soit pas recommandé pour la production) :
  ```json
  {
    "registry-mirrors": ["https://mirror.example.com"]
  }
  ```
  Ajoutez ceci dans `/etc/docker/daemon.json` et redémarrez Docker.

---

### 10. **Vérifiez la synchronisation de l'heure**
- Assurez-vous que l'heure de votre système est synchronisée :
  ```bash
  sudo apt install ntp
  sudo systemctl restart ntp
  ```

---

### Tableau récapitulatif des commandes

| Étape | Commande/Action |
|------|----------------|
| Redémarrer Docker | `sudo systemctl restart docker` |
| Vérifier le statut Docker | `sudo systemctl status docker` |
| Configurer le DNS | Modifier `/etc/docker/daemon.json` |
| Récupérer l'image manuellement | `docker pull ghcr.io/librechat/librechat:latest` |
| Définir UID/GID | `echo "UID=$(id -u)" >> .env` |

---

Si le problème persiste après avoir essayé ces étapes, faites-moi savoir le résultat de :
```bash
docker info
```
et tous les messages d'erreur que vous voyez en exécutant les commandes ci-dessus. Cela aidera à approfondir le diagnostic !