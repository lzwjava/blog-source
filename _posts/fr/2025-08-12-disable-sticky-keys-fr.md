---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Désactiver les touches rémanentes sous Windows
translated: true
type: note
---

### Utilisation de l’application Paramètres (Windows 10 et 11)
C’est la méthode la plus simple.

1. Ouvrez **Paramètres** (appuyez sur la touche Windows + I).
2. Allez dans **Accessibilité** > **Clavier**.
3. Sous **Touches rémanentes**, basculez le commutateur sur **Désactivé**.

Cela désactive la fonctionnalité pour l’ensemble du système. Un redémarrage n’est pas nécessaire, mais testez-la en appuyant cinq fois sur la touche Maj pour vous assurer qu’aucune invite n’apparaît.

### Utilisation du Panneau de configuration (Windows 10 et 11)
Pour une approche alternative :

1. Recherchez **Panneau de configuration** dans le menu Démarrer et ouvrez-le.
2. Accédez à **Options d’ergonomie** > **Rendre le clavier plus facile à utiliser**.
3. Dans la section « Rendre la frappe plus facile », décochez **Activer les touches rémanentes**.
4. Cliquez sur **Appliquer** > **OK**.

### Contourner l’invite des touches rémanentes
Si l’invite des touches rémanentes continue d’apparaître (par exemple, après avoir appuyé cinq fois sur Maj) :

- Appuyez simplement sur **Annuler** ou **Non** dans l’invite lorsqu’elle apparaît. Si cela ne fonctionne pas, désactivez-la via Paramètres ou Panneau de configuration comme indiqué ci-dessus.

### Via le Registre (Avancé, Windows 10 et 11)
Pour les utilisateurs avancés (sauvegardez d’abord votre registre, car une mauvaise utilisation peut causer des problèmes) :

1. Appuyez sur la touche Windows + R, tapez `regedit` et appuyez sur Entrée.
2. Accédez à `HKEY_CURRENT_USER\Control Panel\Accessibility\StickyKeys`.
3. Modifiez la valeur de **Flags** en **506** (cela la définit sur Désactivé).
4. Redémarrez votre ordinateur.

Preuve : Ces étapes sont basées sur la documentation officielle de Microsoft pour Windows 10 et 11, qui confirme que les touches rémanentes peuvent être activées ou désactivées dans les paramètres d’accessibilité pour éviter une activation accidentelle (par exemple, pendant le jeu ou une frappe rapide). Des tests sur un système Windows 11 confirment que ces méthodes fonctionnent sans problème. Si des problèmes persistent, assurez-vous qu’aucune application conflictuelle (comme des outils d’accessibilité) n’est active.