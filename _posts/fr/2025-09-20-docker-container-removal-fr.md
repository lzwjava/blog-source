---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Résoudre les problèmes de suppression de conteneurs Docker
translated: true
type: note
---

Parfait — merci, cette sortie confirme que le conteneur est bloqué en **Removal In Progress** et `docker rm -f` échoue avec la même erreur overlay2. Ci-dessous, je vais détailler un plan de récupération méthodique et ordonné, spécifiquement pour **macOS avec Docker Desktop** (votre invite montre les messages du proxy Docker Desktop). Je marquerai clairement les étapes destructrices et je fournirai des commandes exactes que vous pourrez copier/coller. Suivez-les dans l'ordre jusqu'à ce que le problème soit résolu.

---

## 1) Vérifications rapides non destructrices (one-liners)

Exécutez celles-ci en premier — elles sont sûres et aident à recueillir des informations.

```bash
# Versions et informations Docker (utiles pour le débogage)
docker version
docker info

# Inspecter le conteneur bloqué (peut ou non retourner des informations complètes)
docker inspect ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18 || true

# Essayer de lire les logs (peut échouer si l'état du conteneur est corrompu)
docker logs ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18 || true
```

Si `docker inspect` ou `docker logs` produisent une sortie utile, collez-la ici et je l'interpréterai. (Si elles échouent avec des messages overlay, vous pouvez quand même continuer.)

---

## 2) Redémarrer Docker Desktop (sûr, résout souvent le problème)

Quittez Docker Desktop complètement, puis redémarrez-le.

```bash
osascript -e 'quit app "Docker"'
open -a Docker
```

Après le redémarrage de Docker, essayez :

```bash
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

Si cela échoue toujours, continuez.

---

## 3) Si le redémarrage n'a pas aidé — tuer le processus VM bas niveau puis redémarrer Docker (relativement sûr)

Parfois, la VM intégrée (hyperkit) est bloquée. La tuer force un redémarrage propre. C'est normalement sûr mais cela arrêtera tous les conteneurs en cours d'exécution.

```bash
# trouver le processus hyperkit utilisé par Docker Desktop
ps aux | grep -i hyperkit | grep -v grep

# le tuer (remplacez PID par le nombre de la commande précédente)
sudo kill -9 <PID>

# puis redémarrez Docker
open -a Docker
```

Réessayez `docker rm -f <id>`.

---

## 4) Tentatives de nettoyage non destructrices

Si le conteneur ne veut toujours pas se supprimer, essayez de nettoyer les objets Docker inutilisés. Ces commandes sont sûres pour les éléments inutilisés :

```bash
docker system prune -f
docker volume prune -f
docker container prune -f
```

Puis réessayez la commande `docker rm -f`.

---

## 5) Exporter ce dont vous avez besoin avant une réinitialisation destructive (important)

Si rien ne corrige le conteneur bloqué, l'option pratique suivante sur Docker Desktop est **Reset / Clean / Purge** via l'interface utilisateur de Docker Desktop — mais cela **peut supprimer les images/volumes/conteneurs**. Si vous avez des images ou des volumes que vous souhaitez conserver, sauvegardez-les maintenant.

Sauvegardez les images :

```bash
# lister les images qui vous intéressent
docker images

# sauvegarder une image (exemple)
docker save -o ~/myimage.tar my-image:tag
```

Exportez les volumes (exemple — remplacez `myvolume` et `./backup` selon vos besoins) :

```bash
mkdir -p ~/docker-vol-backups
docker run --rm -v myvolume:/data -v ~/docker-vol-backups:/backup alpine \
  sh -c "cd /data && tar czf /backup/myvolume.tgz ."
```

Si le conteneur bloqué empêche l'accès normal `docker run` aux volumes, les sauvegardes pourraient ne pas fonctionner ; dans ce cas, passez à l'option Reset ci-dessous.

---

## 6) Utiliser l'interface de dépannage de Docker Desktop — prochaine étape recommandée

Ouvrez Docker Desktop → cliquez sur l'icône **Troubleshoot** (ou Préférences → Dépannage). Essayez ces actions dans l'ordre :

1. **Restart Docker** (si vous ne l'avez pas fait après avoir tué hyperkit).
2. **Clean / Purge data** — cela supprime les images/conteneurs/volumes. **Destructeur**.
3. **Reset to factory defaults** — **destructeur**, réinitialise l'état de Docker Desktop.

Si vous voulez que je vous aide à conserver des images/volumes importantes avant la réinitialisation, donnez-moi la sortie de `docker images` et `docker volume ls` (de l'étape 1) et je fournirai les commandes exactes de sauvegarde/export.

---

## 7) Supprimer forcément les fichiers de la VM Docker (avancé / destructeur) — seulement si vous acceptez la perte de données

Si vous êtes à l'aise avec la perte des données Docker locales et que la réinitialisation via l'interface utilisateur n'a pas fonctionné, vous pouvez supprimer les fichiers de la VM de Docker Desktop. C'est le dernier recours.

**Avertissement — cela supprime tous les conteneurs, images et volumes de Docker Desktop.**

1. Quittez Docker Desktop.
2. Dans le Finder ou le terminal, supprimez le dossier de données de Docker :

```bash
# quittez d'abord docker
osascript -e 'quit app "Docker"'

# supprimer les données de la VM Docker Desktop (destructeur)
rm -rf ~/Library/Containers/com.docker.docker
rm -rf ~/.docker
```

3. Redémarrez Docker Desktop (il recréera l'état). Puis exécutez `docker system prune -a --volumes` pour nettoyer ce qui reste.

---

## 8) Collecter des diagnostics pour une aide plus approfondie

Si vous souhaitez que j'approfondisse avant les étapes destructrices, générez les diagnostics de Docker Desktop et collez l'ID de diagnostic ici :

* Docker Desktop → Dépannage → **Get Support** ou **Generate Diagnostics** — cela donnera un ID de diagnostic. Partagez cet ID (ou l'archive de diagnostic complète) et je pourrai interpréter les logs et recommander des corrections ciblées.

Vous pouvez aussi coller les sorties de ces commandes (non destructrices) :

```bash
docker info
docker ps -a
docker inspect ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18 || true
```

---

## Chemin recommandé court (résumé)

1. Quittez et redémarrez Docker Desktop. Réessayez `docker rm -f`.
2. Si toujours bloqué : tuez hyperkit (sudo kill -9 PID), redémarrez Docker Desktop. Réessayez.
3. Exécutez `docker system prune` / `volume prune`. Réessayez.
4. Exportez/sauvegardez toutes les images/volumes dont vous avez besoin.
5. Utilisez Docker Desktop → Dépannage → **Clean / Purge data** (ou Reset) si vous pouvez vous permettre la perte de données.
6. Si vous voulez que j'aide à interpréter les logs avant les étapes destructrices, collez les sorties de `docker info` et `docker ps -a` ou l'ID de diagnostic.

---

Dites-moi quelle étape vous venez d'essayer et collez les sorties de :

```bash
docker info
docker ps -a
docker images
docker volume ls
```

— Je les analyserai et je donnerai la prochaine commande exacte adaptée à votre état.