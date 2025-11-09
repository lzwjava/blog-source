---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Réparation des Liaisons Python GI Défectueuses
translated: true
type: note
---

### Diagnostic mis à jour
D'après les nouveaux détails, votre installation de Python 3.13.7 (probablement manuelle ou via PPA/source) a corrompu les liaisons GObject Introspection (GI) du système. L'extension C `_gi` du module `gi` est compilée pour la version de Python par défaut de votre distribution (probablement 3.10 ou 3.11, étant donné les répertoires dans `/usr/lib/python`), et non pour la 3.13. Cela provoque l'erreur d'importation circulaire lorsque `gnome-terminal` (un script Python) tente de la charger. La configuration multi-versions dans `/usr/lib/python` confirme cette incompatibilité — les paquets système comme `python3-gi` ne sont pas encore construits pour la 3.13 (elle est trop récente pour la plupart des distributions en 2025).

Les journaux UFW restent du bruit non pertinent.

### Correction recommandée : Revenir à la version Python système par défaut
La solution la plus propre est de ramener `/usr/bin/python3` à la valeur par défaut de votre distribution (par exemple, 3.10), puis de réinstaller les liaisons GI. Cela évite les solutions de contournement comme copier des fichiers .so, qui peuvent entraîner des incohérences.

1.  **Identifier et revenir à la version Python par défaut** (utilisez `update-alternatives` si configuré ; sinon, créez un lien symbolique manuellement) :
    ```
    # Vérifier si les alternatives sont configurées
    sudo update-alternatives --config python3
    ```
    - Si des options sont listées, sélectionnez celle avec la priorité la plus basse (généralement la valeur par défaut de la distribution, comme 3.10).
    - Si aucune alternative n'est configurée (courant sur Ubuntu standard), revenez-en manuellement :
      ```
      # En supposant que la valeur par défaut est 3.10 (courant pour Ubuntu 22.04 ; remplacez par 3.11 si c'est votre version de base)
      sudo rm /usr/bin/python3
      sudo ln -s /usr/bin/python3.10 /usr/bin/python3
      ```
    - Vérifiez : `python3 --version` devrait maintenant afficher 3.10.x (ou votre version par défaut).

2.  **Réinstaller les paquets GI et GNOME Terminal** :
    ```
    sudo apt update
    sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
    ```

3.  **Tester** :
    ```
    python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
    gnome-terminal
    ```
    - Si le test Python réussit mais que le terminal échoue toujours, réinitialisez sa configuration : `dconf reset -f /org/gnome/terminal/`.

### Si vous souhaitez conserver Python 3.13
- C'est plus délicat, car `python3-gi` officiel n'existera pas encore pour la 3.13. Vous devrez compiler PyGObject à partir des sources :
  1. Installez les dépendances de compilation : `sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`.
  2. Téléchargez et compilez PyGObject : Suivez le [guide officiel](https://pygobject.gnome.org/install.html) avec `--prefix=/usr/local`.
  3. Mais cela risque de casser d'autres outils système — revenez en arrière en cas de problème.
- Ou, copiez de manière peu recommandable l'extension `_gi` (déconseillé à long terme) :
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # Ajustez '3[01]' à votre version par défaut (3.10 ou 3.11)
  ```
  Puis réinstallez `python3-gi` comme indiqué ci-dessus.

### Prévention
- Ne remplacez pas manuellement `/usr/bin/python3` — utilisez des virtualenvs (`python3 -m venv myenv`) pour les projets nécessitant la 3.13.
- Si vous avez installé la 3.13 via le PPA deadsnakes, supprimez-le et utilisez la version Python de la distribution.

Si cela ne résout pas le problème, exécutez `ls -l /usr/bin/python*` et `dpkg -l | grep python3 | grep -E 'gi|default'` et partagez le résultat.

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)