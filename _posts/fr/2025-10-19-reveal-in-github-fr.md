---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Révéler dans GitHub Plugin Xcode
translated: true
type: note
---

### Qu'est-ce que Reveal-In-GitHub ?

Reveal-In-GitHub est un plugin Xcode qui vous permet de naviguer rapidement depuis votre espace de travail Xcode vers les fonctionnalités clés de GitHub pour votre dépôt actuel. Il est conçu pour les développeurs travaillant sur des projets Git hébergés sur GitHub, permettant un accès en un clic (ou via un raccourci clavier) à des éléments tels que l'historique des commits, les vues blame, les pull requests, les issues et les notifications—sans quitter Xcode ni avoir à taper manuellement des URL.

### Prérequis
- Xcode installé (testé sur les versions récentes ; aucune version minimale spécifique mentionnée).
- Votre projet doit être un dépôt Git hébergé sur GitHub (le plugin détecte automatiquement l'URL du dépôt et les chemins des fichiers).
- Si votre projet a plusieurs dépôts Git distants (remotes), vous serez invité à en sélectionner un par défaut lors de la première utilisation.

### Installation
Il existe deux principales méthodes d'installation :

#### Option 1 : Utilisation d'Alcatraz (Recommandée)
1. Installez Alcatraz si vous ne l'avez pas déjà fait (un gestionnaire de paquets pour les plugins Xcode). Vous pouvez trouver des guides de configuration en ligne, comme [celui-ci](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/) si vous préférez des instructions en chinois.
2. Ouvrez Alcatraz dans Xcode (via le menu : `Window > Package Manager`).
3. Recherchez "Reveal In GitHub".
4. Cliquez sur **Install**.
5. Redémarrez Xcode.

#### Option 2 : Installation manuelle
1. Clonez le dépôt :  
   ```
   git clone https://github.com/lzwjava/Reveal-In-GitHub.git
   ```
2. Ouvrez le fichier `Reveal-In-GitHub.xcodeproj` dans Xcode.
3. Compilez le projet (Product > Build ou ⌘B). Cela génère le fichier `Reveal-In-GitHub.xcplugin`.
4. Déplacez le plugin vers :  
   `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/`
5. Redémarrez Xcode.

Après l'installation, le plugin devrait apparaître dans la barre de menus de Xcode sous **Editor > Reveal In GitHub**.

### Comment l'utiliser
Une fois installé et Xcode redémarré :
1. Ouvrez un projet hébergé sur GitHub dans Xcode et éditez un fichier source (par exemple, naviguez jusqu'à une ligne spécifique).
2. Utilisez l'un des raccourcis clavier ou éléments de menu sous **Editor > Reveal In GitHub** pour accéder à GitHub. Le plugin détecte automatiquement votre dépôt, le fichier actuel, le numéro de ligne et le hash du dernier commit.

Voici un aide-mémoire pour les éléments de menu et raccourcis intégrés (les raccourcis suivent le modèle ⌃⇧⌘ + première lettre du titre) :

| Élément de menu | Raccourci   | Fonctionnalité | Exemple d'URL GitHub (pour le fichier LZAlbumManager.m à la ligne 40 dans le dépôt lzwjava/LZAlbum au commit fd7224) |
|-----------------|-------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| **Setting**     | ⌃⇧⌘S      | Ouvre le panneau de personnalisation | N/A |
| **Repo**        | ⌃⇧⌘R      | Ouvre la page principale du dépôt | https://github.com/lzwjava/LZAlbum |
| **Issues**      | ⌃⇧⌘I      | Ouvre la liste des issues | https://github.com/lzwjava/LZAlbum/issues |
| **PRs**         | ⌃⇧⌘P      | Ouvre la liste des pull requests | https://github.com/lzwjava/LZAlbum/pulls |
| **Quick File**  | ⌃⇧⌘Q      | Ouvre la vue du fichier à la ligne actuelle | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **List History**| ⌃⇧⌘L     | Ouvre l'historique des commits pour le fichier | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| **Blame**       | ⌃⇧⌘B      | Ouvre la vue blame pour la ligne actuelle | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **Notifications**| ⌃⇧⌘N   | Ouvre les notifications du dépôt | https://github.com/lzwjava/LZAlbum/notifications?all=1 |

- **Conseils** :
  - Les raccourcis n'entrent pas en conflit avec ceux par défaut de Xcode.
  - Si vous avez une sélection de texte, certaines actions (comme Blame) s'ancreront sur cette plage (par exemple, #L40-L43).
  - Testez-le : Ouvrez un projet, allez à une ligne, et appuyez sur ⌃⇧⌘B—cela devrait ouvrir la page blame dans votre navigateur.

### Personnalisation
Pour modifier ou ajouter des éléments de menu :
1. Appuyez sur ⌃⇧⌘S ou allez dans **Editor > Reveal In GitHub > Setting**.
2. Dans le panneau :
   - Ajoutez de nouveaux éléments en cliquant sur le bouton "+" : Entrez un titre (par exemple, "Wiki"), un raccourci et un modèle d'URL.
   - Les modèles d'URL utilisent des espaces réservés comme :
     - `{git_remote_url}` : URL complète du dépôt (par exemple, https://github.com/user/repo).
     - `{commit}` : Hash du dernier commit de la branche actuelle.
     - `{file_path}` : Chemin relatif vers le fichier.
     - `#{selection}` : Ligne ou sélection actuelle (par exemple, #L40).
   - Exemple : Pour un lien vers le wiki, définissez le modèle sur `{git_remote_url}/wiki`.
3. Si vous avez plusieurs dépôts distants, utilisez le bouton "Clear Default Repos" pour réinitialiser les sélections.

Le plugin est inspiré de [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) et est sous licence MIT.

[Reveal-In-GitHub GitHub Repository](https://github.com/lzwjava/Reveal-In-GitHub)