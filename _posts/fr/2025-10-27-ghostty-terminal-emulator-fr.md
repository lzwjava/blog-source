---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Ghostty : Émulateur de Terminal Rapide et Multiplateforme'
translated: true
type: note
---

Ghostty est un émulateur de terminal multiplateforme conçu pour la vitesse, les fonctionnalités et l'intégration native sur macOS et Linux (avec la prise en charge de Windows en cours de développement). Il est principalement construit en **Zig**, un langage de programmation système moderne axé sur la sécurité, les performances et la simplicité — et non en Rust, comme vous l'avez demandé.

### Détails clés de l'implémentation
- **Architecture de base** : Le cœur partagé (gérant l'émulation de terminal, le rendu et une grande partie de la logique) est écrit en Zig. Cela permet un contrôle de bas niveau et des performances élevées, y compris l'accélération GPU via Metal (sur macOS) ou Vulkan/OpenGL (multiplateforme).
- **Couches spécifiques à la plateforme** : Pour obtenir une sensation native, il utilise des boîtes à outils de plateforme pour l'interface graphique :
  - macOS : Swift/AppKit pour la gestion des fenêtres et de l'interface utilisateur.
  - Linux : GTK pour la gestion des fenêtres.
  - Le pipeline de rendu partagé en Zig relie le tout.
- **Fonctionnalités notables de sa conception** :
  - Démarrage et rendu extrêmement rapides (par exemple, gère de grandes sorties sans lag).
  - Prend en charge les ligatures, les emojis et la typographie avancée.
  - Configurable via des scripts Lua pour l'extensibilité.
  - Pas de bloat — il est minimaliste mais comprend des fonctionnalités essentielles comme les onglets, la recherche et l'intégration du presse-papiers OSC 52.
- **Philosophie de développement** : Créé par Mitchell Hashimoto (de HashiCorp), il privilégie l'exactitude et l'efficacité par rapport aux astuces de compatibilité courantes dans les terminaux plus anciens comme xterm. Il est open-source sous licence MIT.

Si vous êtes intéressé par son développement ou son hacking, consultez le dépôt GitHub pour la base de code Zig et les instructions de compilation (nécessite Zig 0.13+).

### Références
- [Dépôt GitHub de Ghostty](https://github.com/ghostty-org/ghostty)
- [Présentation de Ghostty (Blog de Mitchell Hashimoto)](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Notes de version de Ghostty 1.0](https://dansasser.me/posts/ghostty-1-0-a-terminal-emulator-built-for-speed-features-and-native-integration/)