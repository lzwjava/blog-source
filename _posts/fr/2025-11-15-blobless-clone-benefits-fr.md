---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Avantages du clonage Git sans objets blob
translated: true
type: note
---

La commande Git :

```bash
git clone --filter=blob:none <url-du-dépôt>
```

est un **clone partiel** qui ne télécharge **presque aucun contenu de fichier** (blobs) au moment du checkout. Voici exactement ce qu'elle fait et pourquoi elle est utile :

### Ce que signifie `--filter=blob:none`
- `--filter=blob:none` indique à Git d'utiliser le **clonage sans blobs**.
- Git télécharge toujours :
  - Tous les commits (l'historique)
  - Tous les objets d'arbre (la structure des répertoires)
  - Toutes les références/branches/tags
- Mais il télécharge **zéro contenu de fichier** (blobs) lors du clone initial.
- Lorsque vous utilisez plus tard `git checkout` ou changez de branche, Git télécharge uniquement les blobs (contenus des fichiers) pour les fichiers dont vous avez réellement besoin dans votre arbre de travail à ce moment-là.

### Principaux avantages
- Clone initial extrêmement rapide et minuscule (souvent seulement quelques Mo, même pour d'énormes dépôts comme le noyau Linux, Android ou le code source de Windows).
- Utilise beaucoup moins de bande passante réseau et d'espace disque au départ.
- Parfait pour l'intégration continue/déploiement continu (CI/CD), les consultations rapides, ou lorsque vous n'avez besoin que de l'historique (par ex. `git log`, blame, diff entre les commits) sans avoir à extraire les fichiers.

### Exemple de comparaison de taille (monde réel)

| Dépôt           | Clone normal | Clone `blob:none` | Gain de vitesse |
|-----------------|--------------|-------------------|-----------------|
| torvalds/linux  | ~5+ Go       | ~300–400 Mo       | 10–20× plus rapide |
| microsoft/vscode| ~2–3 Go      | ~200 Mo           | beaucoup plus rapide |

### Commandes de suivi courantes après un clone blob:none
```bash
# La première fois que vous avez besoin d'un arbre de travail :
git checkout <branche>        # télécharge uniquement les blobs nécessaires

# Ou si vous voulez tout récupérer plus tard :
git fetch --unshallow        # pas nécessaire pour le blobless
# Pour récupérer définitivement les blobs manquants :
git repack -a -d             # optionnel, force le téléchargement de tous les blobs
```

### Filtres associés que vous pourriez voir
- `--filter=blob:none` → aucun blob initialement (le plus agressif)
- `--filter=tree:0`    → télécharge les arbres mais pas les blobs (effet similaire)
- `--filter=sparse:oid=<oid>` → pour le checkout partiel (sparse-checkout) avec des blobs partiels

### Résumé
```bash
git clone --filter=blob:none https://github.com/example/repo.git
```
= “Donnez-moi l'historique et la structure complets immédiatement, mais téléchargez le contenu des fichiers plus tard, à la demande.”  
Excellent pour les énormes monorepos ou lorsque vous voulez simplement parcourir l'historique sans attendre des heures.