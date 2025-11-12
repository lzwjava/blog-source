---
audio: false
generated: true
lang: fr
layout: post
title: Remappage des touches dans Ubuntu 24.04
translated: true
type: note
---

### Points Clés
- Il semble probable que vous puissiez échanger les touches Ctrl gauche et Verr Maj dans Ubuntu 24.04 en utilisant GNOME Tweaks, un outil graphique, ou via la ligne de commande avec `gsettings`.
- Les recherches suggèrent que les deux méthodes sont persistantes entre les sessions, ce qui les rend fiables pour un usage quotidien.
- Les preuves penchent en faveur de GNOME Tweaks pour sa facilité d'utilisation, tandis que la méthode en ligne de commande offre plus de contrôle pour les utilisateurs avancés.

#### Utilisation de GNOME Tweaks
GNOME Tweaks fournit une interface simple pour l'échange de touches :
- Installez-le si nécessaire avec `sudo apt install gnome-tweak-tool`.
- Ouvrez Tweaks, allez dans "Clavier et Souris", cliquez sur "Options de disposition supplémentaires" et sélectionnez "Échanger Ctrl et Verr Maj" sous "Position de Ctrl".

#### Utilisation de la Ligne de Commande
Pour une approche technique, utilisez le terminal :
- Exécutez `gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swapcaps']"` pour échanger les touches de manière persistante.

#### Détail Inattendu
Contrairement à Windows PowerToys, qui permet un remappage précis des touches, les méthodes d'Ubuntu échangent principalement le Ctrl gauche avec Verr Maj, ce qui peut affecter d'autres raccourcis clavier que vous utilisez.

---

### Note d'Enquête : Analyse Détaillée de l'Échange de Touches dans Ubuntu 24.04

Cette section propose une exploration complète de l'échange des touches Ctrl gauche et Verr Maj dans Ubuntu 24.04, similaire à la fonctionnalité offerte par PowerToys dans Windows. L'analyse s'appuie sur diverses sources pour garantir exactitude et profondeur, répondant aux utilisateurs recherchant des solutions adaptées aux débutants comme aux utilisateurs avancés.

#### Contexte
Ubuntu 24.04, nom de code "Noble Numbat", est une version LTS (Long Term Support) qui continue d'utiliser l'environnement de bureau GNOME, spécifiquement la version 46. Les utilisateurs familiers de Windows peuvent s'attendre à des options de personnalisation similaires, comme celles fournies par PowerToys, qui permettent d'échanger des touches spécifiques comme Ctrl gauche et Verr Maj. Sous Linux, la personnalisation du clavier est généralement gérée par des outils comme GNOME Tweaks ou des utilitaires en ligne de commande, offrant une flexibilité mais nécessitant des approches différentes comparé à Windows.

La demande de l'utilisateur d'échanger les touches Ctrl gauche et Verr Maj est courante parmi les développeurs et les utilisateurs avancés, en particulier ceux habitués aux workflows Emacs ou Vim, où Ctrl est fréquemment utilisé. Cette analyse explore à la fois les méthodes graphiques et en ligne de commande, en garantissant la persistance entre les sessions et la compatibilité avec Ubuntu 24.04.

#### Méthodes pour Échanger les Touches

##### Méthode 1 : Utilisation de GNOME Tweaks
GNOME Tweaks est un outil graphique qui simplifie la personnalisation du bureau, y compris les paramètres du clavier. Sur la base de la documentation disponible, il prend en charge l'échange de touches via son interface. Les étapes sont les suivantes :

1. **Installation :** Si ce n'est pas déjà fait, les utilisateurs peuvent installer GNOME Tweaks via le Logithèque Ubuntu ou en exécutant la commande :
   ```bash
   sudo apt install gnome-tweak-tool
   ```
   Cela garantit que l'outil est disponible, et il fait partie des dépôts standard pour Ubuntu 24.04.

2. **Accès aux Paramètres du Clavier :** Ouvrez GNOME Tweaks depuis le menu des applications ou en recherchant "Tweaks" dans l'aperçu des Activités. Naviguez vers la section "Clavier et Souris" dans le menu de gauche.

3. **Options de Disposition Supplémentaires :** Cliquez sur "Options de disposition supplémentaires" pour accéder aux paramètres avancés du clavier. Dans ce menu, localisez la section "Position de Ctrl", qui devrait inclure une option intitulée "Échanger Ctrl et Verr Maj". Sélectionnez cette option pour échanger la touche Ctrl gauche avec Verr Maj.

4. **Persistance :** Les modifications apportées via GNOME Tweaks sont généralement persistantes après les redémarrages, car elles modifient les paramètres GNOME stockés dans la base de données `dconf`, qui est spécifique à l'utilisateur et appliquée à la connexion.

Cette méthode est conviviale, en particulier pour ceux qui ne sont pas familiers avec les outils en ligne de commande, et correspond aux attentes d'interface graphique des utilisateurs Windows. Cependant, elle repose sur l'hypothèse que l'option "Échanger Ctrl et Verr Maj" est disponible dans GNOME Tweaks d'Ubuntu 24.04, basée sur la documentation historique de sources comme [Ask Ubuntu: How do I remap the Caps Lock and Ctrl keys?](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys) et [Opensource.com: How to swap Ctrl and Caps Lock keys in Linux](https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard), qui suggèrent une continuité dans la fonctionnalité.

##### Méthode 2 : Utilisation de la Commande `gsettings`
Pour les utilisateurs préférant le contrôle en ligne de commande ou rencontrant des problèmes avec GNOME Tweaks, la commande `gsettings` offre un moyen direct de modifier les options du clavier. Cette méthode utilise le système de paramètres GNOME, garantissant la persistance. Le processus est le suivant :

1. **Ouvrir le Terminal :** Accédez au terminal via Ctrl + Alt + T ou depuis l'aperçu des Activités.

2. **Définir l'Option Clavier :** Exécutez la commande suivante pour échanger les touches Ctrl gauche et Verr Maj :
   ```bash
   gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swapcaps']"
   ```
   Cette commande modifie la clé `xkb-options` sous `org.gnome.desktop.input-sources`, en ajoutant l'option "ctrl:swapcaps", qui est une option XKB standard pour échanger Ctrl et Verr Maj.

3. **Vérification et Persistance :** Après avoir exécuté la commande, testez le comportement des touches en appuyant sur Ctrl gauche et Verr Maj. Les changements sont persistants entre les sessions, car ils sont stockés dans la base de données `dconf` de l'utilisateur, appliquée à la connexion.

Cette méthode est particulièrement utile pour les utilisateurs avancés ou dans les configurations automatisées, comme les scripts pour plusieurs configurations utilisateur. Elle est soutenue par des sources comme [EmacsWiki: Moving The Ctrl Key](https://www.emacswiki.org/emacs/MovingTheCtrlKey), qui détaillent les options XKB et leurs effets.

#### Comparaison des Méthodes
Pour aider les utilisateurs à choisir la méthode appropriée, le tableau suivant compare GNOME Tweaks et `gsettings` sur la base de la facilité d'utilisation, de l'expertise technique requise et de la persistance :

| **Aspect**              | **GNOME Tweaks**                     | **Commande gsettings**               |
|-------------------------|--------------------------------------|--------------------------------------|
| **Facilité d'Utilisation** | Élevée (interface graphique)         | Moyenne (nécessite la connaissance du terminal) |
| **Expertise Technique** | Faible (adapté aux débutants)        | Moyenne (adapté aux utilisateurs avancés) |
| **Persistance**         | Automatique (stocké dans dconf)      | Automatique (stocké dans dconf)      |
| **Installation Nécessaire** | Peut nécessiter une installation     | Aucune installation supplémentaire nécessaire |
| **Flexibilité**         | Limitée aux options de l'interface graphique | Élevée (peut combiner plusieurs options) |

Ce tableau met en évidence que GNOME Tweaks est idéal pour les utilisateurs recherchant la simplicité, tandis que `gsettings` offre une flexibilité pour ceux à l'aise avec la ligne de commande.

#### Considérations et Mises en Garde
- **Spécificité au Ctrl Gauche :** Les deux méthodes devraient échanger la touche Ctrl gauche avec Verr Maj, car "ctrl:swapcaps" affecte généralement le Ctrl gauche dans les configurations XKB standard. Cependant, les utilisateurs doivent vérifier le comportement, car certaines configurations pourraient affecter les deux touches Ctrl selon la disposition du clavier.
- **Impact sur les Raccourcis :** L'échange de touches peut affecter les raccourcis clavier existants, tels que Ctrl+C pour copier ou Ctrl+V pour coller. Les utilisateurs doivent tester les raccourcis critiques après la configuration pour garantir la compatibilité, en particulier dans les applications comme les terminaux ou les EDI.
- **Problèmes Potentiels :** Bien qu'aucun rapport spécifique indiquant que l'option "Échanger Ctrl et Verr Maj" ne fonctionne pas dans Ubuntu 24.04 n'ait été trouvé, les utilisateurs doivent être conscients des bogues potentiels, comme noté dans des problèmes généraux de clavier tels que [Keyboard Issue with Ubuntu 24.04: Caps Lock Reversed After Login](https://ubuntuforums.org/showthread.php?t=2497465). Si des problèmes surviennent, la méthode en ligne de commande fournit une solution de secours.

#### Détail Inattendu : Comparaison avec Windows PowerToys
Contrairement à Windows PowerToys, qui offre un remappage précis des touches et peut cibler des touches spécifiques comme Ctrl gauche sans en affecter d'autres, les méthodes d'Ubuntu sont plus standardisées. L'option "Échanger Ctrl et Verr Maj" dans GNOME Tweaks ou "ctrl:swapcaps" dans `gsettings` échange principalement le Ctrl gauche avec Verr Maj, ce qui peut impacter d'autres comportements du clavier. Cette différence peut surprendre les utilisateurs s'attendant à une fonctionnalité identique, soulignant la nécessité de tester après la configuration.

#### Conclusion
GNOME Tweaks et `gsettings` fournissent tous deux des méthodes viables pour échanger les touches Ctrl gauche et Verr Maj dans Ubuntu 24.04, garantissant persistance et compatibilité avec le workflow de l'utilisateur. GNOME Tweaks offre une approche graphique et conviviale pour les débutants, tandis que `gsettings` s'adresse aux utilisateurs avancés recherchant un contrôle en ligne de commande. Les utilisateurs doivent vérifier le comportement après la configuration et considérer les impacts potentiels sur les raccourcis clavier, surtout compte tenu des différences avec Windows PowerToys.

### Citations Clés
- [How do I remap the Caps Lock and Ctrl keys Ask Ubuntu](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys)
- [How to swap Ctrl and Caps Lock keys in Linux Opensource.com](https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard)
- [Moving The Ctrl Key EmacsWiki](https://www.emacswiki.org/emacs/MovingTheCtrlKey)
- [Keyboard Issue with Ubuntu 24.04: Caps Lock Reversed After Login Ubuntu Forums](https://ubuntuforums.org/showthread.php?t=2497465)