---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre le Fichier de Configuration de Ghostty
translated: true
type: note
---

### Fonctionnement du fichier de configuration Ghostty

Le fichier de configuration de Ghostty utilise un format texte simple avec des paires clé-valeur de type `clé = valeur`. Il est conçu pour être simple, vous permettant de ne remplacer que les paramètres par défaut qui vous intéressent—Ghostty inclut des valeurs par défaut raisonnables pour tout le reste, donc un fichier de configuration minimal, voire vide, fonctionne parfaitement.

#### Aperçu rapide de la syntaxe
- **Clés et valeurs** : Les clés sont toujours en minuscules et sensibles à la casse (par exemple, `font-family = JetBrains Mono`). Les valeurs peuvent être sans guillemets sauf si elles contiennent des espaces ou des caractères spéciaux (par exemple, `font-family = "JetBrains Mono Nerd Font"`). Les espaces autour du `=` n'ont pas d'importance.
- **Commentaires** : Commencez une ligne par `#` pour des notes (par exemple, `# Mon thème personnalisé`). Pas de commentaires en ligne après les valeurs, sinon ils seront analysés comme faisant partie de la valeur.
- **Rétablir la valeur par défaut** : Utilisez une valeur vide comme `clé =` pour remettre un paramètre à la valeur par défaut intégrée de Ghostty.
- **Valeurs spéciales** : Certaines options ont des formats uniques, comme les durées (par exemple, `resize-overlay-duration = 4s 200ms`)—consultez la documentation pour les détails.
- **Chargement du fichier** : Ghostty recherche le fichier de configuration à `~/.config/ghostty/config` (Linux/Windows) ou `~/Library/Application Support/com.mitchellh.ghostty/config` (macOS). Vous pouvez inclure d'autres fichiers avec `config-file = chemin/vers/autre.conf` pour des configurations modulaires.
- **Surcharges en ligne de commande** : Tout paramètre peut également être défini via des drapeaux de ligne de commande (par exemple, `ghostty --font-family="Fira Code"`), qui ont priorité sur le fichier.

Les changements prennent effet immédiatement si vous rechargez avec le raccourci par défaut (Cmd+Shift+, sur macOS ou Ctrl+Shift+, sur Linux/Windows) ou en exécutant `ghostty +reload-config`.

Pour voir toutes les options et valeurs par défaut, exécutez `ghostty +show-config --default --docs` dans votre terminal.

### À quoi ressemble une configuration normale ?
Une configuration "normale" est souvent minimale—elle modifie juste quelques éléments comme la police, les couleurs ou les marges intérieures pour plus de confort. Les valeurs par défaut de Ghostty incluent JetBrains Mono comme famille de police (avec prise en charge intégrée de Nerd Font), un jeu de couleurs d'arrière-plan/premier plan épuré et pas de marge intérieure supplémentaire.

Voici un exemple simple et typique pour une configuration à thème sombre avec une police populaire, quelques marges intérieures et des raccourcis clavier de base. Enregistrez ceci dans votre fichier `config` :

```
# Thème sombre basique avec des marges et une police personnalisée
background = 1e1e1e
foreground = f8f8f2
font-family = "JetBrains Mono Nerd Font"
font-size = 14

# Ajouter un peu d'espace autour du texte
window-padding-x = 8
window-padding-y = 8

# Raccourcis clavier personnalisés (remplace les valeurs par défaut si nécessaire)
keybind = cmd+t=new_tab
keybind = cmd+w=close_tab
keybind = cmd+d=new_split:right
```

Cela garde les choses légères tout en personnalisant l'essentiel. Vous pouvez l'étendre avec plus de couleurs (par exemple, des entrées de palette comme `color0 = 282a36`) ou des thèmes provenant de la documentation.

[Documentation de configuration Ghostty](https://ghostty.org/docs/config)