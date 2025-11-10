---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Mettre à niveau Open WebUI en toute sécurité
translated: true
type: note
---

Je vous comprends. Voici les méthodes sûres et directes pour mettre à niveau Open WebUI.

## Si vous avez installé avec `pip` (votre cas)

```bash
# 1) (Recommandé) activez l'environnement que vous utilisez pour Open WebUI
#    ex. avec conda :
conda activate open-webui
#    ou avec venv :
# source ~/open-webui-venv/bin/activate

# 2) Mettez à niveau vers la dernière version
python3.11 -m pip install -U open-webui

# 3) (Optionnel) si le cache de pip pose problème
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) Vérifiez ce que vous avez obtenu
python3.11 -m pip show open-webui
```

La documentation officielle indique que simplement `pip install -U open-webui` effectue la mise à niveau vers la dernière version. ([Open WebUI][1])

### Gardez vos données/paramètres persistants

Lorsque vous exécutez le serveur, vous pouvez spécifier un répertoire de données pour que les mises à niveau ne l'affectent pas :

```bash
# macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

Cela reprend les conseils de la documentation pour définir `DATA_DIR` (ou utiliser `uvx … @latest serve` avec la même variable) afin que vos conversations et configurations existent en dehors de l'installation du package. ([Open WebUI][2])

> Astuce : Si vous avez précédemment exécuté Open WebUI sans `DATA_DIR`, commencez à l'utiliser maintenant ; Open WebUI utilisera ce dossier à l'avenir.

## Si vous avez utilisé Docker (pour être exhaustif)

```bash
# arrêtez et supprimez l'ancien conteneur (les données sont dans le volume nommé)
docker rm -f open-webui

# récupérez la dernière image
docker pull ghcr.io/open-webui/open-webui:main

# redémarrez avec votre volume existant
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

Ceci est le processus de mise à jour manuelle recommandé par le projet ; vos données persistent dans le volume Docker `open-webui`. ([Open WebUI][3])

## Vérifiez quelle est la version "latest"

Vous pouvez confirmer la dernière version sur GitHub Releases avant/après votre mise à niveau. ([GitHub][4])

Si des erreurs surviennent (par exemple, incompatibilité de version Python), assurez-vous d'utiliser Python 3.11 pour la méthode pip, ce que le projet recommande explicitement. ([GitHub][5])

Vous voulez que je vérifie votre environnement actuel ou interprète une erreur de mise à niveau ? Collez-la ici et je la diagnostiquerai.

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ Démarrage rapide"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI : Accueil"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "Mettre à jour Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "Versions · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui : Interface IA conviviale ..."