---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Synchronisation Automatisée Git via Cron
translated: true
type: note
---

Pour synchroniser automatiquement les mises à jour des `git push` d'un ordinateur portable vers un clone du même repo sur un autre ordinateur (sans `git pull` manuel), vous ne pouvez pas compter uniquement sur Git pour des mises àjour "automatiques" en temps réel entre les machines—Git est conçu pour être basé sur une opération de pull. Cependant, vous pouvez configurer une tâche planifiée sur le second ordinateur pour récupérer et fusionner périodiquement les changements depuis le dépôt distant (GitHub dans votre cas). C'est la méthode la plus simple et fiable pour une configuration personnelle comme la vôtre.

Voici comment procéder sur votre Mac (puisque vous utilisez un MacBook Air). Nous utiliserons `cron` pour la planification, car il est intégré au système et léger. Supposons que les deux ordinateurs portables ont des clones de `github.com:lzwjava/blog-source`, et que vous êtes sur la branche `main`.

### Étape 1 : Vérifier que le repo du second ordinateur est correctement configuré
Sur le second ordinateur :
1. Naviguez vers votre repo : `cd /chemin/vers/blog-source`
2. Assurez-vous qu'il suit le dépôt distant : `git remote -v` (devrait afficher `origin` comme votre repo GitHub).
3. Si ce n'est pas le cas, ajoutez-le : `git remote add origin git@github.com:lzwjava/blog-source.git`
4. Récupérez l'état actuel : `git fetch origin`
5. Passez sur main : `git checkout main`
6. Définissez la branche en amont : `git branch --set-upstream-to=origin/main main`

Testez un pull manuel : `git pull origin main`. Cela devrait fonctionner comme dans votre sortie.

### Étape 2 : Créer un script pour le pull automatisé
Créez un script shell simple pour gérer le pull en toute sécurité (il récupère, vérifie les conflits et pull si tout est propre).

1. À la racine de votre repo, créez `auto-pull.sh` :
   ```bash:disable-run
   #!/bin/bash
   cd "$(dirname "$0")"  # Se déplace dans le répertoire du repo
   git fetch origin
   if git diff HEAD origin/main --quiet; then
       git pull origin main
       echo "Auto-pull terminé : $(date)"
   else
       echo "Avertissement : Changements locaux détectés. Pull ignoré. Résolvez manuellement : $(date)"
       # Optionnel : Envoyer un email ou une notification (voir ci-dessous)
   fi
   ```

2. Rendez-le exécutable : `chmod +x auto-pull.sh`

Ce script :
- Récupère les mises à jour sans les fusionner.
- Vérifie si votre branche locale est propre (aucun changement non commité).
- Effectue le pull seulement si c'est sûr ; sinon, vous avertit.

### Étape 3 : Planifiez-le avec Cron
Cron exécute des tâches périodiquement. Nous l'exécuterons toutes les 5 minutes (ajustez si nécessaire, par exemple toutes les heures).

1. Ouvrez l'éditeur crontab : `crontab -e` (utilisez nano si demandé : `nano ~/.crontab`).

2. Ajoutez cette ligne à la fin (pour toutes les 5 minutes) :
   ```
   */5 * * * * /chemin/vers/blog-source/auto-pull.sh >> /chemin/vers/blog-source/pull-log.txt 2>&1
   ```
   - Remplacez `/chemin/vers/blog-source` par le chemin réel de votre repo (par exemple, `~/blog-source`).
   - Le `>> pull-log.txt` enregistre la sortie dans un fichier pour le débogage.

3. Sauvegardez et quittez (Ctrl+O, Entrée, Ctrl+X dans nano).
4. Vérifiez : `crontab -l` (devrait afficher votre ligne).
5. Testez : Attendez 5 minutes ou exécutez `crontab -e` à nouveau pour ajouter temporairement `* * * * *` (toutes les minutes), puis revenez en arrière.

Cron s'exécute en tant qu'utilisateur, donc il respecte votre clé SSH pour l'authentification GitHub (comme dans votre sortie de pull).

### Améliorations optionnelles
- **Gérer les Conflits/Notifications** : Si le script détecte des problèmes, ajoutez une notification. Modifiez `auto-pull.sh` pour ajouter :
  ```bash
  # En cas d'avertissement, envoyer une notification macOS
  osascript -e 'display notification "Git pull ignoré en raison de changements locaux" with title "Synchronisation du Repo Blog"'
  ```
- **Exécution lors d'un Push (depuis le premier ordinateur)** : Pour une synchronisation plus "instantanée", utilisez GitHub Actions sur le premier ordinateur. Créez `.github/workflows/sync.yml` :
  ```yaml
  name: Auto Sync
  on: [push]
  jobs:
    sync:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - name: Notify (e.g., via webhook to second laptop)
          run: curl -X POST https://your-second-laptop-webhook-endpoint  # Configurez un serveur simple sur le second ordinateur
  ```
  Mais cela nécessite un écouteur sur la seconde machine (par exemple, via ngrok + une petite app Flask), ce qui est excessif pour la plupart des cas.
- **Compromis sur la Fréquence** : Toutes les 5 minutes convient pour un repo de blog. Pour du temps réel, envisagez des outils comme `watch` dans un terminal (`watch -n 300 git pull`), mais cron est plus pratique.
- **Note sur le Proxy** : Votre sortie montre des proxys HTTP/HTTPS—cron les héritera, donc les pulls devraient fonctionner tels quels.

Maintenant, lorsque vous poussez depuis le premier ordinateur (`git push origin main`), le second se synchronisera automatiquement toutes les 5 minutes. Vérifiez `pull-log.txt` pour l'historique.

Si vous rencontrez des problèmes d'authentification/proxy dans cron, ajoutez `export HTTP_PROXY=http://127.0.0.1:7890` etc. au script. Pour Windows sur l'autre ordinateur, utilisez plutôt le Planificateur de tâches.