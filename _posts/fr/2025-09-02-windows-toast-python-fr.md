---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Notifications toast Windows avec Python
translated: true
type: note
---

### Qu'est-ce que win10toast ?
win10toast est une bibliothèque Python légère qui vous permet d'envoyer des notifications toast (alertes pop-up) sur Windows 10 à partir de vos scripts Python. Elle est utile pour les notifications utilisateur dans les applications de bureau ou les scripts, de manière similaire aux toasts natifs de Windows.

### Prérequis
- Python 3.x installé.
- Windows 10 (elle repose sur des API spécifiques à Windows).
- Aucune dépendance supplémentaire au-delà de Python.

### Installation
Installez la bibliothèque via pip (l'outil d'installation de paquets Python) :

```
pip install win10toast
```

Si vous utilisez un environnement virtuel, activez-le d'abord.

### Utilisation de base
1. Importez le module :
   ```python
   from win10toast import ToastNotifier
   ```

2. Créez une instance de `ToastNotifier` et appelez sa méthode `show_toast` pour afficher une notification :
   ```python
   toaster = ToastNotifier()
   toaster.show_toast("Titre", "Message", icon_path=None, duration=5)
   ```
   - **Titre** : Une chaîne de caractères pour l'en-tête de la notification.
   - **Message** : Une chaîne de caractères pour le corps de la notification.
   - **icon_path** : Chemin facultatif vers un fichier .ico ou .png pour l'icône de la notification (par exemple, `"chemin/vers/icone.ico"`). Omettre pour ne pas avoir d'icône.
   - **duration** : Durée en secondes pendant laquelle le toast apparaît (5 par défaut ; Windows peut écraser cette valeur).

La notification apparaîtra dans le Centre d'action et sous forme de pop-up.

### Utilisation avancée
- **Personnalisation de l'icône** : Utilisez un fichier image (128x128 pixels recommandé pour une meilleure qualité).
- **Gestion des clics** : Passez une fonction de rappel (support limité ; le comportement lors d'un clic est basique).
- **Notifications multiples** : Instanciez `ToastNotifier` une fois et réutilisez-le pour envoyer plusieurs toasts.
- **Gestion des erreurs** : Encapsulez dans un bloc try-except pour gérer les problèmes potentiels de l'API Windows, par exemple si les notifications sont désactivées.

Exemple avec icône et gestion des erreurs :
```python
from win10toast import ToastNotifier
import os

try:
    toaster = ToastNotifier()
    icon = "C:\\chemin\\vers\\icone.ico"  # Remplacez par le chemin réel
    toaster.show_toast("Alerte !", "Votre script s'est terminé.", icon_path=icon, duration=10)
except Exception as e:
    print(f"Échec de la notification : {e}")
```

### Limitations et conseils
- Les notifications nécessitent que le Centre d'action de Windows 10 soit activé (Paramètres > Système > Notifications et actions).
- Pour des fonctionnalités plus complexes (par exemple, des actions ou des images), envisagez des alternatives comme plyer ou winrt (faisant partie du SDK Windows moderne).
- Si les notifications n'apparaissent pas, vérifiez les paramètres du mode Assisté de Windows ou essayez d'exécuter le script en tant qu'administrateur.

Pour la documentation complète, consultez le [dépôt GitHub win10toast](https://github.com/Charnelx/win10toast). Si vous rencontrez des problèmes, fournissez les détails de l'erreur pour une aide adaptée.