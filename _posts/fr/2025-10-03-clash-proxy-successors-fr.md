---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Successeurs de Proxy Clash et Support Linux
translated: true
type: note
---

Clash, un outil proxy basé sur des règles similaire à Shadowsocks, a vu son dépôt original supprimé par son auteur en 2023 en raison de pressions réglementaires en Chine. La communauté a poursuivi le développement via des forks et des successeurs comme Clash.Meta (maintenant officiellement appelé Mihomo), qui est largement considéré comme le remplacement le plus fiable et le plus activement maintenu. Il prend en charge les binaires Linux, y compris pour Ubuntu, et inclut des fonctionnalités comme le DNS over HTTPS (DoH), le tunneling et le routage basé sur des règles.

Pour un dépôt GitHub fiable sur Linux/Ubuntu, je recommande le projet de continuation principal. Voici un résumé des meilleures options basées sur l'adoption par la communauté, les mises à jour et le support Linux :

### Dépôts Recommandés
- **MetaCubeX/mihomo (Clash.Meta Core)** : Il s'agit du principal successeur de Clash, forké et maintenu par la communauté après la suppression de l'original. Il offre une fonctionnalité de proxy complète, des mises à jour fréquentes et des binaires pré-construits pour Linux (x86_64 et arm64). La compatibilité Ubuntu est excellente, avec des binaires testés sur les versions 18.04+. Il est open-source, sans publicité et hautement personnalisable via des fichiers de configuration YAML.
  - GitHub : https://github.com/MetaCubeX/mihomo
  - Pourquoi fiable : Plus de 14k étoiles, communauté active, et les binaires incluent des bases de données GeoIP pour le routage. Liens de téléchargement directs pour les binaires CLI Linux dans la section des releases.
  - Installation pour Ubuntu : Téléchargez le dernier binaire "mihomo-linux-amd64" depuis les releases, rendez-le exécutable (`chmod +x mihomo`), et exécutez-le. Requiert un fichier config.yaml avec les règles de proxy. [1][2]
  - Alternatives si le core ne convient pas :
    - **CarlDegio/verge** : Un wrapper GUI basé sur Tauri pour Clash.Meta, fournissant un tableau de bord intuitif pour Linux (Ubuntu inclus). Repose sur Mihomo pour la stabilité.
      - GitHub : https://github.com/CarlDegio/verge
      - Pourquoi fiable : Support GUI pour le bureau, plus de 2k étoiles, changement de profil facile et icône dans la barre système. Téléchargez l'AppImage pour Ubuntu. [3]
    - **chen08209/FlClash** : Client multi-plateforme (incluant les binaires Linux) basé sur Clash.Meta. Se concentre sur la simplicité et un design sans publicité, avec une interface simple pour la configuration.
      - GitHub : https://github.com/chen08209/FlClash
      - Pourquoi fiable : Léger, supporte Ubuntu via des builds deb/AppImage, et intègre les bindings Mihomo. [4]
  - Pour les sauvegardes historiques : Kuingsmile/clash-core propose des builds archivés du core d'avant suppression, avec des releases pour téléchargement Linux si vous préférez une version non maintenue mais historique. [5]

### Notes Additionnelles
- **Conseils d'Installation** : Assurez-vous d'avoir libc (glibc 2.17+) pour Ubuntu. Utilisez des outils comme `systemd` ou `screen` pour l'exécuter comme un service en arrière-plan. Vérifiez les téléchargements avec les hashs SHA256 pour la sécurité.
- **Critères de Fiabilité** : Ces dépôts ont des contributeurs actifs, de grandes bases d'utilisateurs (nombre élevé d'étoiles/forks) et évitent les risques liés aux projets abandonnés post-2023. Clash.Premin (probablement une faute de frappe pour Premium) est un fork payant mais moins axé sur l'open-source.
- **Rappel Légal/Usage** : Clash est destiné à contourner la censure ; assurez-vous de vous conformer aux lois locales, car son utilisation peut attirer l'attention dans les régions restrictives.
- Si vous avez besoin d'une interface utilisateur ou de fonctionnalités spécifiques (par exemple, multi-plateforme), verge ou FlClash sont plus conviviaux que le CLI Mihomo core. Pour les détails, consultez le README de chaque dépôt. Si des problèmes surviennent, le dépôt Mihomo a une documentation extensive. [6][7][1][8]

Si aucun ne convient ou si vous avez besoin d'un guide étape par étape pour Ubuntu, fournissez plus de détails !

Citations :
[1] https://github.com/djoeni/Clash.Meta
[2] https://discussion.fedoraproject.org/t/rhbz-2305079-review-request-clash-meta-a-rule-based-network-proxy-tool-aka-mihomo/146312
[3] https://github.com/CarlDegio/verge
[4] https://github.com/chen08209/FlClash
[5] https://github.com/Kuingsmile/clash-core/releases
[6] https://github.com/fengwz17/Clash-For-Ubuntu
[7] https://news.ycombinator.com/item?id=38126160
[8] https://github.com/hiddify/Clash.Meta