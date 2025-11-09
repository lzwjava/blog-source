---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre le conflit de version GLIBC de Ghostty
translated: true
type: note
---

Le problème que vous rencontrez ne vient pas seulement de conflits d'installation — il est principalement dû au fait que le Snap et le `.deb` que vous avez téléchargé ont été compilés pour GLIBC 2.38 (d'Ubuntu 24.04), mais votre système utilise Ubuntu 22.04 (comme l'indique la version 2.35 de GLIBC dans votre paquet `libc-bin`). Cela provoque l'erreur « version `GLIBC_2.38' not found » lors de l'exécution du binaire. Avoir les deux installations actives peut également entraîner des conflits de chemin (par exemple, déterminer quel binaire `ghostty` est exécuté), donc oui, vous devriez d'abord les supprimer pour nettoyer la situation.

### Étape 1 : Supprimer les installations existantes
Exécutez ces commandes pour désinstaller les deux versions :
```
sudo snap remove ghostty
sudo apt remove ghostty
```
- Cela supprimera la version Snap et la version `.deb` sans autre effet sur votre système.
- Vérifiez la suppression avec `which ghostty` (ne devrait rien retourner) et `snap list | grep ghostty` (devrait être vide).

### Étape 2 : Installer une version compatible
Ghostty n'a pas encore de paquets `.deb` officiels pour Ubuntu 22.04, mais il existe un dépôt non officiel fiable qui compile des fichiers `.deb` compatibles pour cette version (et d'autres). Il gère automatiquement la compatibilité GLIBC.

La méthode la plus simple est d'utiliser leur script d'installation automatique, qui détecte votre version d'Ubuntu et récupère le bon paquet :
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/mkasberg/ghostty-ubuntu/HEAD/install.sh)"
```
- Ceci télécharge et installe le dernier `.deb` compatible (actuellement autour de la v1.2.x pour les versions récentes).
- Une fois terminé, lancez `ghostty` pour tester — l'application devrait démarrer sans l'erreur GLIBC.
- Si vous voyez des invites de dépendances manquantes pendant l'installation (par exemple pour `libonig5`), approuvez-les simplement avec `Y`.

Si vous préférez une installation manuelle :
1. Allez sur la [page des releases](https://github.com/mkasberg/ghostty-ubuntu/releases).
2. Téléchargez le fichier `.deb` étiqueté pour Ubuntu 22.04 (par exemple, un nom comme `ghostty_1.2.1-0.ppa1_amd64_22.04.deb` — le nom exact varie selon la version).
3. Installez-le avec `sudo dpkg -i ghostty_*.deb` (à exécuter depuis le dossier de téléchargement).
4. S'il se plaint de dépendances manquantes, corrigez avec `sudo apt install -f`.

### Notes supplémentaires
- **Pourquoi une compilation depuis les sources n'est pas nécessaire ici** : Le dépôt non officiel fait le travail difficile pour vous, mais si vous souhaitez compiler Ghostty vous-même (par exemple, pour une version personnalisée), suivez le [guide de compilation officiel](https://ghostty.org/docs/install/build). Cela nécessite Zig 0.13 et certaines dépendances comme `libgtk-4-dev`, mais la méthode par `.deb` est plus simple.
- **Envisagez-vous de mettre à niveau Ubuntu ?** Si vous êtes ouvert à l'idée, passer à la version 24.04 vous permettrait d'utiliser le Snap officiel ou le `.deb` pour 24.04 que vous avez essayé précédemment, sans problème.
- Après l'installation, vous pouvez configurer Ghostty via `~/.config/ghostty/config` (voir la [documentation](https://ghostty.org/docs/config) pour les options).

Si vous rencontrez des erreurs pendant ces étapes, collez la sortie ici pour obtenir de l'aide supplémentaire !