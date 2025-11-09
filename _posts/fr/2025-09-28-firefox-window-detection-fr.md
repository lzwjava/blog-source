---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Outils de détection de fenêtre Firefox pour Linux
translated: true
type: note
---

En plus de `xdotool`, il existe plusieurs outils et méthodes alternatifs pour obtenir des informations sur la fenêtre active de Firefox sous Linux :

## Outils alternatifs

### 1. **wmctrl**
Une alternative plus robuste à xdotool :
```bash
# Obtenir la fenêtre active
wmctrl -a

# Lister toutes les fenêtres avec détails
wmctrl -l -x

# Obtenir spécifiquement les fenêtres Firefox
wmctrl -l | grep -i firefox
```

### 2. **qdbus** (pour les applications KDE/Qt)
```bash
# Obtenir les informations de la fenêtre active
qdbus org.kde.KWin /KWin activeWindow

# Obtenir la liste des fenêtres
qdbus org.kde.KWin /KWin windows
```

### 3. **xwininfo**
Utilitaire X11 intégré :
```bash
# Sélection interactive de fenêtre
xwininfo

# Obtenir les informations de la fenêtre racine
xwininfo -root -tree | grep -i firefox

# Obtenir la fenêtre active (nécessite de connaître l'ID de fenêtre)
xwininfo -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d' ' -f5)
```

### 4. **xprop**
Un autre utilitaire X11 :
```bash
# Obtenir les propriétés de la fenêtre active
xprop -root _NET_ACTIVE_WINDOW

# Obtenir la classe et le titre de la fenêtre
xprop -root | grep "_NET_ACTIVE_WINDOW(WINDOW)"
```

## Pour les systèmes Wayland

Si vous utilisez Wayland, les outils X11 ne fonctionneront pas. Essayez plutôt :

### 5. **swaymsg** (pour Sway)
```bash
swaymsg -t get_tree | jq -r '.. | select(.focused? == true)'
```

### 6. **hyprctl** (pour Hyprland)
```bash
hyprctl activewindow
```

### 7. **gdbus** (GNOME/GTK)
```bash
gdbus call --session --dest org.gnome.Shell --object-path /org/gnome/Shell --method org.gnome.Shell.Eval "global.get_window_actors()"
```

## Solutions Python

### 8. **Python avec Xlib**
```python
from Xlib import X, display
from Xlib.error import XError

def get_active_window():
    try:
        d = display.Display()
        root = d.screen().root
        
        # Obtenir la fenêtre active
        active_window = root.get_full_property(
            d.intern_atom('_NET_ACTIVE_WINDOW'), X.AnyPropertyType
        )
        
        if active_window:
            window_id = active_window.value[0]
            window = d.create_resource_object('window', window_id)
            window_name = window.get_wm_name()
            return window_name
    except XError:
        return None

print(get_active_window())
```

### 9. **Python avec subprocess**
```python
import subprocess

def get_firefox_windows():
    try:
        # Utilisation de wmctrl
        result = subprocess.run(['wmctrl', '-l'], 
                              capture_output=True, text=True)
        firefox_windows = [line for line in result.stdout.split('\n') 
                          if 'firefox' in line.lower()]
        return firefox_windows
    except FileNotFoundError:
        return "wmctrl not installed"

print(get_firefox_windows())
```

## Dépannage de votre problème xdotool

L'erreur "BadWindow" signifie généralement :

1. **Problèmes de permissions** : Essayez d'exécuter avec différentes permissions
2. **Problèmes d'affichage** : Vérifiez si `$DISPLAY` est correctement défini
3. **Conflit Wayland** : Vous utilisez peut-être Wayland au lieu de X11

Pour vérifier votre serveur d'affichage :
```bash
echo $XDG_SESSION_TYPE
loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type
```

## Approche recommandée

Pour une compatibilité maximale, je recommande cet ordre :

1. **wmctrl** - Le plus fiable sur différents gestionnaires de fenêtres
2. **Combinaison xwininfo + xprop** - Intégrés dans la plupart des installations X11
3. **Solution Python** - La plus flexible et programmable
4. **Outils spécifiques à l'environnement de bureau** (swaymsg, hyprctl, etc.)

Essayez d'abord `wmctrl -l | grep -i firefox` - c'est généralement le remplacement le plus direct pour la fonctionnalité de détection de fenêtre de xdotool.