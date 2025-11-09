---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Guide d'Automatisation en Ligne de Commande avec xdotool
translated: true
type: note
---

## Qu'est-ce que xdotool ?

xdotool est un outil d'automatisation en ligne de commande pour X11 (environnements de bureau Linux) qui vous permet de :
- Contrôler les mouvements et les clics de la souris
- Envoyer des frappes au clavier aux applications
- Manipuler les fenêtres (déplacer, redimensionner, focaliser)
- Rechercher des fenêtres selon divers critères
- Automatiser les interactions avec le bureau de manière programmatique

## Installation

```bash
# Ubuntu/Debian
sudo apt install xdotool

# Fedora/RHEL/CentOS
sudo dnf install xdotool

# Arch Linux
sudo pacman -S xdotool

# À partir des sources
git clone https://github.com/jordansissel/xdotool
cd xdotool
make
sudo make install
```

## Commandes principales

### Commandes d'information sur les fenêtres

#### `getactivewindow`
Obtient l'ID de la fenêtre actuellement active/focalisée.
```bash
xdotool getactivewindow
# Sortie : 52428807 (ID de fenêtre)

# Obtenir le titre de la fenêtre active
xdotool getactivewindow getwindowname
```

#### `getwindowfocus`
Similaire à getactivewindow mais peut se comporter différemment selon le gestionnaire de fenêtres.
```bash
xdotool getwindowfocus
```

#### `getwindowname`
Obtient le titre/nom d'une fenêtre.
```bash
# Obtenir le nom de la fenêtre active
xdotool getactivewindow getwindowname

# Obtenir le nom d'un ID de fenêtre spécifique
xdotool getwindowname 52428807
```

#### `getwindowpid`
Obtient l'ID de processus (PID) associé à une fenêtre.
```bash
xdotool getactivewindow getwindowpid
```

#### `getwindowgeometry`
Obtient la position et les informations de taille d'une fenêtre.
```bash
xdotool getactivewindow getwindowgeometry
# Sortie : Window 52428807
#   Position: 100,50 (screen: 0)
#   Geometry: 800x600
```

#### `getdisplaygeometry`
Obtient les dimensions de l'écran/affichage.
```bash
xdotool getdisplaygeometry
# Sortie : 1920x1080
```

### Recherche et sélection de fenêtres

#### `search`
Recherche des fenêtres selon divers critères.
```bash
# Recherche par nom/titre de fenêtre
xdotool search --name "Firefox"
xdotool search --name "Terminal"

# Recherche par nom de classe
xdotool search --class "firefox"

# Recherche insensible à la casse
xdotool search --name --onlyvisible --maxdepth 1 "terminal"

# Options de recherche courantes :
# --name : recherche les titres de fenêtres
# --class : recherche les noms de classe des fenêtres
# --classname : recherche les noms d'instance de classe des fenêtres
# --onlyvisible : uniquement les fenêtres visibles
# --maxdepth N : limite la profondeur de recherche
# --limit N : limite le nombre de résultats
# --desktop N : recherche un bureau/espace de travail spécifique
```

#### `selectwindow`
Sélection interactive de fenêtre (cliquer pour sélectionner).
```bash
xdotool selectwindow
# Cliquez sur n'importe quelle fenêtre pour obtenir son ID
```

### Contrôle de la souris

#### `click`
Simule les clics de souris.
```bash
# Clic gauche à la position actuelle
xdotool click 1

# Clic droit
xdotool click 3

# Clic molette
xdotool click 2

# Double clic
xdotool click --repeat 2 1

# Clic à des coordonnées spécifiques
xdotool mousemove 500 300 click 1

# Clic avec délai
xdotool click --delay 500 1
```

#### `getmouselocation`
Obtient la position actuelle du curseur de la souris.
```bash
xdotool getmouselocation
# Sortie : x:500 y:300 screen:0 window:52428807

# Obtenir uniquement les coordonnées
xdotool getmouselocation --shell
# Sortie : X=500 Y=300 SCREEN=0 WINDOW=52428807
```

#### Mouvement de la souris
```bash
# Déplacer la souris vers une position absolue
xdotool mousemove 500 300

# Déplacer la souris relativement à la position actuelle
xdotool mousemove_relative 10 -20

# Déplacer et cliquer en une seule commande
xdotool mousemove 500 300 click 1
```

### Saisie au clavier

#### `key`
Envoie des frappes au clavier à la fenêtre active.
```bash
# Envoyer une seule touche
xdotool key Return
xdotool key Escape
xdotool key Tab

# Envoyer des combinaisons de touches
xdotool key ctrl+c
xdotool key ctrl+alt+t
xdotool key shift+F10

# Envoyer plusieurs touches en séquence
xdotool key ctrl+l type "https://google.com" key Return

# Noms de touches courants :
# - Lettres : a, b, c, ... (minuscules)
# - Chiffres : 1, 2, 3, ...
# - Spéciales : Return, Escape, Tab, space, BackSpace, Delete
# - Fonction : F1, F2, ... F12
# - Modificateurs : ctrl, alt, shift, super (touche Windows)
# - Flèches : Up, Down, Left, Right
```

#### Saisie de texte
```bash
# Taper du texte (simule la frappe de chaque caractère)
xdotool type "Hello World"

# Taper avec un délai entre les caractères
xdotool type --delay 100 "Slow typing"

# Effacer le délai pour une frappe rapide
xdotool type --clearmodifiers --delay 0 "Fast text"
```

### Manipulation de fenêtres

```bash
# Focaliser/activer une fenêtre
xdotool windowactivate WINDOW_ID

# Réduire la fenêtre
xdotool windowminimize WINDOW_ID

# Agrandir la fenêtre
xdotool windowmaximize WINDOW_ID

# Fermer la fenêtre
xdotool windowclose WINDOW_ID

# Déplacer la fenêtre à une position
xdotool windowmove WINDOW_ID 100 50

# Redimensionner la fenêtre
xdotool windowsize WINDOW_ID 800 600

# Déplacer la fenêtre vers un bureau spécifique
xdotool set_desktop_for_window WINDOW_ID 2

# Amener la fenêtre au premier plan
xdotool windowraise WINDOW_ID

# Afficher la fenêtre
xdotool windowmap WINDOW_ID

# Masquer la fenêtre
xdotool windowunmap WINDOW_ID
```

### Fonctionnalités avancées

#### `behave`
Configurer les comportements (déclencheurs) d'événements de fenêtre.
```bash
# Exécuter une commande quand la fenêtre gagne le focus
xdotool behave WINDOW_ID focus exec echo "Window focused"

# Exécuter quand une fenêtre est créée
xdotool behave WINDOW_ID create exec "notify-send 'New window'"

# Événements disponibles : focus, unfocus, mouse-enter, mouse-leave, create, destroy
```

#### `behave_screen_edge`
Déclencher des actions quand la souris atteint les bords de l'écran.
```bash
# Exécuter une commande quand la souris atteint le bord gauche
xdotool behave_screen_edge left exec "echo 'Left edge hit'"

# Bords disponibles : left, right, top, bottom
```

## Exemples pratiques

### Scripts d'automatisation de base

#### Ouvrir un terminal et exécuter une commande
```bash
#!/bin/bash
# Ouvrir un terminal et exécuter la commande ls
xdotool key ctrl+alt+t
sleep 1
xdotool type "ls -la"
xdotool key Return
```

#### Capturer la fenêtre active
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
NAME=$(xdotool getwindowname $WINDOW | sed 's/[^a-zA-Z0-9]/_/g')
import -window $WINDOW "screenshot_${NAME}.png"
```

#### Focaliser une application spécifique
```bash
#!/bin/bash
# Focaliser Firefox ou l'ouvrir s'il n'est pas en cours d'exécution
WINDOW=$(xdotool search --onlyvisible --class "firefox" | head -1)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    firefox &
fi
```

### Scripts de gestion de fenêtres

#### Disposer les fenêtres côte à côte
```bash
#!/bin/bash
# Obtenir la géométrie de l'écran
eval $(xdotool getdisplaygeometry --shell)
HALF_WIDTH=$((WIDTH / 2))

# Obtenir les deux fenêtres les plus récentes
WINDOWS=($(xdotool search --onlyvisible --maxdepth 1 "" | tail -2))

# Positionner la première fenêtre à gauche
xdotool windowsize ${WINDOWS[0]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[0]} 0 0

# Positionner la deuxième fenêtre à droite
xdotool windowsize ${WINDOWS[1]} $HALF_WIDTH $HEIGHT
xdotool windowmove ${WINDOWS[1]} $HALF_WIDTH 0
```

#### Centrer la fenêtre active
```bash
#!/bin/bash
WINDOW=$(xdotool getactivewindow)
eval $(xdotool getdisplaygeometry --shell)
eval $(xdotool getwindowgeometry --shell $WINDOW)

NEW_X=$(((WIDTH - WINDOW_WIDTH) / 2))
NEW_Y=$(((HEIGHT - WINDOW_HEIGHT) / 2))

xdotool windowmove $WINDOW $NEW_X $NEW_Y
```

### Automatisation spécifique aux applications

#### Automatisation du navigateur
```bash
#!/bin/bash
# Ouvrir un nouvel onglet et naviguer
xdotool key ctrl+t
sleep 0.5
xdotool type "github.com"
xdotool key Return
```

#### Automatisation de l'éditeur de texte
```bash
#!/bin/bash
# Tout sélectionner et copier dans le presse-papiers
xdotool key ctrl+a
sleep 0.1
xdotool key ctrl+c
```

## Conseils et bonnes pratiques

### Timing et délais
```bash
# Ajouter des délais pour les applications lentes
xdotool key ctrl+alt+t
sleep 2  # Attendre que le terminal s'ouvre
xdotool type "echo hello"

# Utiliser les délais intégrés de xdotool
xdotool key --delay 100 ctrl+alt+t
```

### Gestion des erreurs
```bash
#!/bin/bash
# Vérifier si la fenêtre existe avant d'agir dessus
WINDOW=$(xdotool search --name "MyApp" 2>/dev/null)
if [ -n "$WINDOW" ]; then
    xdotool windowactivate $WINDOW
else
    echo "Window not found"
    exit 1
fi
```

### Travailler avec plusieurs fenêtres
```bash
#!/bin/bash
# Agir sur toutes les fenêtres d'une application spécifique
xdotool search --name "Firefox" | while read WINDOW; do
    xdotool windowactivate $WINDOW
    xdotool key F5  # Actualiser
    sleep 0.5
done
```

### Débogage
```bash
# Activer la sortie verbeuse
xdotool --verbose key Return

# Obtenir des informations détaillées sur la fenêtre
xdotool search --name "Terminal" getwindowgeometry getwindowname getwindowpid
```

## Cas d'utilisation courants

1. **Gestion de fenêtres** : Focaliser, déplacer, redimensionner les fenêtres de manière programmatique
2. **Test d'applications** : Automatiser les scénarios de test d'interface graphique
3. **Outils de présentation** : Automatiser la navigation des diapositives et le changement de fenêtres
4. **Macros de jeu** : Automatiser les tâches répétitives dans les jeux
5. **Accessibilité** : Créer des méthodes de saisie personnalisées pour les utilisateurs en situation de handicap
6. **Administration système** : Automatiser les tâches d'administration basées sur l'interface graphique
7. **Outils de développement** : Intégrer avec les IDE et les flux de travail de développement

## Dépannage

### Problèmes courants

- **Les commandes ne fonctionnent pas** : Assurez-vous que X11 est en cours d'exécution (pas Wayland)
- **Problèmes de permissions** : Certaines opérations peuvent nécessiter des permissions utilisateur appropriées
- **Fenêtre non trouvée** : Utilisez `xdotool search` pour vérifier que la fenêtre existe et est visible
- **Problèmes de timing** : Ajoutez des délais appropriés entre les commandes
- **Caractères spéciaux** : Utilisez un échappement approprié pour les caractères spéciaux dans la saisie de texte

### Considérations de sécurité

- xdotool peut contrôler n'importe quelle application, à utiliser avec prudence
- Évitez d'exécuter des scripts xdotool non fiables
- Soyez prudent avec l'automatisation qui traite des données sensibles
- Envisagez d'utiliser `xdotool` uniquement dans des environnements contrôlés

Ce guide couvre les fonctionnalités essentielles et avancées de xdotool. Expérimentez avec ces commandes pour créer des scripts d'automatisation de bureau puissants adaptés à vos besoins spécifiques.