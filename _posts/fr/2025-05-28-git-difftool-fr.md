---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de BeyondCompare avec Git Difftool
translated: true
type: note
---

Pour configurer Beyond Compare comme `git difftool`, suivez ces étapes. Ces instructions supposent que Beyond Compare est installé et que Git est configuré sur votre système.

### Étapes pour configurer Beyond Compare comme `git difftool`

1. **Vérifier l'installation de Beyond Compare**
   Assurez-vous que Beyond Compare est installé et accessible depuis la ligne de commande. Vous pouvez le vérifier en exécutant :
   ```
   bcomp
   ```
   S'il n'est pas reconnu, assurez-vous que l'exécutable Beyond Compare (par exemple, `BCompare.exe` sur Windows ou `bcomp` sur macOS/Linux) se trouve dans le PATH de votre système.

2. **Configurer Git pour utiliser Beyond Compare**
   Exécutez les commandes de configuration Git suivantes dans votre terminal ou invite de commande :

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "chemin/vers/bcomp"
   git config --global difftool.prompt false
   ```

   - Remplacez `"chemin/vers/bcomp"` par le chemin réel vers l'exécutable Beyond Compare :
     - **Windows** : Typiquement `"C:\Program Files\Beyond Compare 4\BCompare.exe"`. Utilisez des doubles barres obliques inverses (`\\`) ou des barres obliques (`/`) dans le chemin.
     - **macOS** : Généralement `/Applications/Beyond Compare.app/Contents/MacOS/bcomp`.
     - **Linux** : Souvent `/usr/bin/bcomp` ou l'emplacement où `bcomp` est installé.
   - Le paramètre `difftool.prompt false` empêche Git de vous demander de lancer le difftool pour chaque fichier.

3. **(Optionnel) Configurer comme outil de fusion (Merge Tool)**
   Si vous souhaitez également utiliser Beyond Compare comme `mergetool`, ajoutez ces commandes :

   ```bash
   git config --global merge.tool bc
   git config --global mergetool.bc.path "chemin/vers/bcomp"
   git config --global mergetool.prompt false
   ```

4. **Tester la configuration**
   Pour vérifier la configuration, créez ou naviguez vers un dépôt Git avec des modifications et exécutez :

   ```bash
   git difftool
   ```

   Cela devrait lancer Beyond Compare pour afficher les différences entre vos fichiers modifiés et le dernier commit. Si vous l'utilisez comme mergetool, testez avec :

   ```bash
   git mergetool
   ```

   (Cela s'applique uniquement si vous avez des conflits de fusion.)

5. **Notes spécifiques aux plateformes**
   - **Windows** : Assurez-vous d'utiliser le chemin correct vers `BCompare.exe`. Si le chemin contient des espaces, encadrez-le de guillemets.
   - **macOS/Linux** : La commande `bcomp` a souvent besoin d'attendre que Beyond Compare se ferme avant de rendre le contrôle au terminal. La documentation de Beyond Compare suggère que cela est géré automatiquement, mais si Git se termine prématurément, vous devrez peut-être ajuster les scripts ou utiliser un wrapper (voir le support de Beyond Compare pour plus de détails).
   - Si vous rencontrez des problèmes, vérifiez le chemin et assurez-vous que Beyond Compare est sous licence et fonctionnel.

6. **Exemple de configuration pour Windows**
   Pour Beyond Compare 4 sur Windows, les commandes pourraient ressembler à :

   ```bash
   git config --global diff.tool bc
   git config --global difftool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global difftool.prompt false
   git config --global merge.tool bc
   git config --global mergetool.bc.path "C:\\Program Files\\Beyond Compare 4\\BCompare.exe"
   git config --global mergetool.prompt false
   ```

7. **Vérifier la configuration**
   Vérifiez votre configuration Git pour vous assurer que les paramètres sont appliqués :

   ```bash
   git config --global --list
   ```

   Recherchez des entrées comme `diff.tool=bc` et `difftool.bc.path`.

### Conseils supplémentaires
- **Comparer des fichiers spécifiques** : Utilisez `git difftool <fichier>` pour comparer un fichier spécifique.
- **Comparer des branches** : Utilisez `git difftool branche1 branche2` pour comparer les différences entre deux branches.
- **Paramètres de Beyond Compare** : Dans Beyond Compare, vous pouvez personnaliser les règles de comparaison (par exemple, ignorer les espaces blancs) via son interface pour une meilleure visualisation des différences.
- **Dépannage** : Si Beyond Compare ne se lance pas, vérifiez le chemin dans le paramètre `difftool.bc.path`. Utilisez `which bcomp` (macOS/Linux) ou `where BCompare.exe` (Windows) pour localiser l'exécutable.

Cette configuration devrait vous permettre d'utiliser Beyond Compare de manière transparente avec `git difftool` et, optionnellement, `git mergetool`. Si vous rencontrez des problèmes spécifiques, indiquez-moi votre système d'exploitation et les messages d'erreur pour obtenir des conseils plus adaptés !