---
audio: false
generated: true
lang: fr
layout: post
title: Corriger l'Erreur TCMalloc
translated: true
type: note
---

L'erreur "Cannot locate TCMalloc. Do you have tcmalloc or google-perftool installed on your system? (improves CPU memory usage)" indique que la bibliothèque TCMalloc, faisant partie des gperftools de Google, n'est pas installée ou n'est pas correctement configurée sur votre système Linux. TCMalloc est un allocateur de mémoire qui peut améliorer les performances et réduire l'utilisation de la mémoire, en particulier dans des applications comme Stable Diffusion. Voici comment résoudre ce problème :

### Étapes pour corriger l'erreur TCMalloc

1. **Installer TCMalloc et Google Perftools**
   En fonction de votre distribution Linux, utilisez le gestionnaire de paquets approprié pour installer les bibliothèques requises.

   - **Pour les systèmes basés sur Ubuntu/Debian** :
     ```bash
     sudo apt-get update
     sudo apt-get install libgoogle-perftools-dev libtcmalloc-minimal4 -y
     ```
     Cela installe à la fois `libgoogle-perftools-dev` (complet, inclut TCMalloc) et `libtcmalloc-minimal4` (une version légère).

   - **Pour les systèmes basés sur Fedora** :
     ```bash
     sudo dnf install gperftools-libs -y
     ```
     Cela installe les bibliothèques TCMalloc nécessaires.

   - **Pour les systèmes basés sur CentOS/RHEL** :
     ```bash
     sudo yum install gperftools-libs -y
     ```
     Si le paquet n'est pas disponible dans les dépôts par défaut, vous devrez peut-être d'abord activer le dépôt EPEL :
     ```bash
     sudo yum install epel-release
     sudo yum install gperftools-libs -y
     ```

2. **Vérifier l'installation**
   Après l'installation, vérifiez si TCMalloc est installé :
   ```bash
   dpkg -l | grep tcmalloc
   ```
   Vous devriez voir `libtcmalloc-minimal4` ou des paquets similaires listés. Alternativement, vérifiez le chemin de la bibliothèque :
   ```bash
   dpkg -L libgoogle-perftools-dev | grep libtcmalloc.so
   ```
   Cela affichera le chemin vers la bibliothèque TCMalloc (par exemple, `/usr/lib/libtcmalloc.so.4`).

3. **Définir la variable d'environnement LD_PRELOAD**
   Pour garantir que votre application utilise TCMalloc, définissez la variable d'environnement `LD_PRELOAD` pour pointer vers la bibliothèque TCMalloc. Cela peut être fait temporairement ou définitivement.

   - **Temporairement (pour la session en cours)** :
     Exécutez votre application avec `LD_PRELOAD` défini :
     ```bash
     export LD_PRELOAD=/usr/lib/libtcmalloc.so.4
     ./launch.py
     ```
     Remplacez `/usr/lib/libtcmalloc.so.4` par le chemin réel trouvé à l'étape 2 s'il est différent.

   - **Définitivement (pour Stable Diffusion ou similaire)** :
     Si vous utilisez un script comme `webui.sh` (commun avec Stable Diffusion), modifiez le script (par exemple, `webui-user.sh`) pour inclure :
     ```bash
     export LD_PRELOAD=libtcmalloc.so.4
     ```
     Enregistrez le fichier et relancez le script :
     ```bash
     ./webui.sh
     ```
     Alternativement, ajoutez-le à votre configuration shell (par exemple, `~/.bashrc` ou `~/.zshrc`) :
     ```bash
     echo 'export LD_PRELOAD=/usr/lib/libtcmalloc.so.4' >> ~/.bashrc
     source ~/.bashrc
     ```

4. **Relancer l'application**
   Après avoir installé TCMalloc et défini `LD_PRELOAD`, redémarrez votre application :
   ```bash
   ./launch.py
   ```
   L'erreur ne devrait plus apparaître, et vous pourriez constater une amélioration de l'utilisation de la mémoire ou des performances.

5. **Dépannage**
   - **Si le chemin de la bibliothèque est incorrect** : Si `LD_PRELOAD` échoue (par exemple, "cannot open shared object file"), vérifiez le nom exact et le chemin de la bibliothèque :
     ```bash
     find /usr/lib -name "libtcmalloc*.so*"
     ```
     Mettez à jour `LD_PRELOAD` avec le chemin correct (par exemple, `libtcmalloc_minimal.so.4` si vous utilisez la version minimale).
   - **Si l'erreur persiste** : Assurez-vous que la version installée de TCMalloc est compatible avec votre système (glibc 2.35 et GCC 11.4.0 dans votre cas). Si les problèmes continuent, essayez d'installer à partir des sources :
     ```bash
     git clone https://github.com/google/tcmalloc.git
     cd tcmalloc
     bazel build //tcmalloc:hello_main
     bazel run //tcmalloc:hello_main
     ```
     Suivez le guide de démarrage rapide de TCMalloc pour des instructions détaillées.
   - **Problèmes de mémoire** : Si vous rencontrez des échecs d'allocation ou des plantages, assurez-vous que votre système dispose de suffisamment de mémoire et que TCMalloc n'est pas en conflit avec d'autres allocateurs.

6. **Optionnel : Vérifier l'utilisation de TCMalloc**
   Pour confirmer que TCMalloc fonctionne, vous pouvez exécuter un programme de test simple ou vérifier l'utilisation de la mémoire avec des outils comme `top` ou `htop` pendant l'exécution de votre application. TCMalloc réduit généralement la fragmentation de la mémoire et peut fournir un léger gain de performances.

### Notes supplémentaires
- **Pourquoi TCMalloc ?** TCMalloc est un allocateur de mémoire haute performance qui réduit l'utilisation de la mémoire CPU et la fragmentation, en particulier dans les applications threadées comme Stable Diffusion. Il n'est pas strictement requis mais peut améliorer les performances.
- **Compatibilité** : Votre système (glibc 2.35, Python 3.10.12, GCC 11.4.0) est compatible avec les dernières versions de TCMalloc, donc les étapes ci-dessus devraient fonctionner. Si vous utilisez une application compilée sur mesure, assurez-vous qu'elle est compilée avec la prise en charge de TCMalloc.
- **Contexte Stable Diffusion** : Cette erreur apparaît souvent avec l'interface WebUI Stable Diffusion d'AUTOMATIC1111. Les étapes ci-dessus, en particulier l'installation de `libgoogle-perftools-dev` et la définition de `LD_PRELOAD`, sont connues pour la résoudre.

Si vous rencontrez des erreurs spécifiques ou avez besoin d'aide pour une distribution Linux particulière, faites-le-moi savoir et je pourrai adapter les instructions !