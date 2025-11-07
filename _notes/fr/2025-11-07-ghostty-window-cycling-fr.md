---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Raccourcis de navigation entre les fenêtres de Ghostty
translated: true
---

Oui, je comprends totalement — Cmd + ` (tilde/backtick) pour parcourir les fenêtres dans Ghostty est rapide et intuitif, surtout si vous les traitez comme des sessions légères et indépendantes au lieu de tout entasser dans des onglets. Ça a ce flux cyclique agréable sans la surcharge mentale d'une barre d'onglets encombrée. La navigation par défaut avec Cmd + Shift + [ / ] pour les onglets (ou le focus des panneaux avec Cmd + [ / ]) semble effectivement maladroite sur Mac, car vous devez gérer Shift en plus de Cmd, et ces crochets ne sont pas les plus accessibles sans devoir étirer les doigts.

Vous avez tout à fait raison : une simple combinaison Cmd + touche est bien plus élégante pour la plupart des gens — ergonomique, rapide à exécuter et moins sujette aux erreurs que les enchaînements de modificateurs. Les paramètres par défaut de Ghostty vont déjà dans ce sens pour la sélection des onglets (Cmd + 1–8 saute directement vers des onglets spécifiques), mais si vous privilégiez les fenêtres aux onglets, vous pourriez remapper le parcours vers quelque chose d'encore plus simple comme Cmd + J/K (style Vim) ou Cmd + ←/→ pour la fenêtre précédente/suivante. C'est super facile à personnaliser dans le fichier de configuration — il suffit d'ajouter des lignes comme :

```
keybind = "cmd-j", "window:previous"
keybind = "cmd-k", "window:next"
```

Cela limite la combinaison à un modificateur + une touche, sans complication. Quelle configuration utilisez-vous principalement — plusieurs fenêtres Ghostty réparties sur plusieurs espaces, ou toutes épinglées sur un seul bureau ? Si vous avez une action spécifique que vous souhaitez assigner (comme des échanges rapides de panneaux), je peux réfléchir à d'autres ajustements.