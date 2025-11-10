---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Modification du port de l'interface Web ouverte
translated: true
type: note
---

Pour changer le port lors de l'exécution d'Open WebUI en utilisant la commande `open-webui serve` (généralement après une installation via pip), utilisez le flag `--port` suivi du numéro de port de votre choix. Le port par défaut est 8080.

### Étapes :
1. Assurez-vous qu'Open WebUI est installé :  
   ```
   pip install open-webui
   ```

2. Exécutez le serveur sur un port différent (par exemple, 3000) :  
   ```
   open-webui serve --port 3000
   ```

   - Cela rendra l'interface Web accessible à l'adresse `http://localhost:3000` (ou l'adresse IP de votre serveur avec le nouveau port).
   - Remarque : La variable d'environnement `PORT` est ignorée lors de l'utilisation de la commande `serve` ; vous devez utiliser le flag `--port` à la place.

Si vous utilisez Docker au lieu d'une installation directe :
- Définissez la variable d'environnement `PORT`, par exemple `docker run -e PORT=3000 ...`.
- Mappez le port externe avec `-p <port_hôte>:3000` (ajustez si nécessaire).

Pour tous les détails d'installation et de configuration, reportez-vous à la documentation officielle.

[Configuration des variables d'environnement | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[Démarrage rapide | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)