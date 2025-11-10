---
audio: false
generated: true
lang: fr
layout: post
title: Problèmes de point d'accès et d'état de l'écran iOS
translated: true
type: note
---

### Impact de l'écran allumé/éteint sur le Point d'accès personnel iOS

La fonction Point d'accès personnel iOS (en supposant que c'est ce que vous vouliez dire par "personal hubspot", car c'est une fonction iPhone courante pour partager votre connexion Internet cellulaire) est conçue pour rester active même lorsque l'écran de l'iPhone est éteint ou verrouillé. Selon la documentation officielle et les tutoriels d'Apple, le point d'accès devrait continuer à fonctionner en arrière-plan sans interruption liée à l'état de l'écran, tant que des appareils sont connectés et l'utilisent.

Cependant, sur la base de rapports d'utilisateurs et de discussions sur les forums, il peut y avoir des problèmes de stabilité de connexion lorsque l'écran s'éteint :
- Dans certains cas, le point d'accès peut se déconnecter ou devenir indisponible après le verrouillage de l'écran, surtout s'il y a une inactivité perçue (par exemple, aucun transfert de données pendant une courte période) ou en raison de comportements d'économie de batterie. Cela semble plus courant dans les anciennes versions d'iOS (comme iOS 15 ou antérieur) ou des configurations spécifiques, comme l'utilisation de la 5G. Cela n'arrive pas toujours, mais c'est une plainte fréquente.
- Pour atténuer ce problème, les solutions de contournement courantes incluent :
  - Régler le Verrouillage automatique sur "Jamais" dans Réglages > Affichage & Luminosité (cela maintient l'écran allumé indéfiniment, évitant les problèmes liés au verrouillage, mais draine la batterie plus rapidement).
  - Garder la page des paramètres du Point d'accès personnel ouverte sur votre iPhone avant de verrouiller l'écran.
  - Utiliser Siri pour activer le point d'accès alors que l'écran est déjà éteint (par exemple, dire "Active le Point d'accès personnel"), ce que certains utilisateurs rapportent comme permettant de le maintenir actif plus longtemps sans arrêt automatique.
- Si aucun appareil n'est connecté, le point d'accès peut s'éteindre automatiquement après environ 90 secondes d'inactivité lorsque l'écran est éteint, comme mesure d'économie d'énergie. Mais s'il est activement utilisé, il devrait rester allumé.

Concernant la vitesse : Il n'y a aucune preuve ou rapport indiquant que l'écran soit allumé ou éteint affecte directement la vitesse Internet du point d'accès. La vitesse est davantage influencée par des facteurs tels que la force du signal cellulaire, la congestion du réseau, l'utilisation de la 5G par rapport à la LTE, le nombre d'appareils connectés, ou l'activation du Mode faible consommation (qui peut réduire les performances pour économiser la batterie). L'état de l'écran ne semble pas impacter la bande passante ou la latence lorsque la connexion est stable.

Si vous rencontrez des déconnexions ou des lenteurs, essayez de redémarrer votre iPhone, de mettre à jour vers la dernière version d'iOS, de désactiver le Mode faible consommation ou de réinitialiser les paramètres réseau (Réglages > Général > Transferer ou Réinitialiser l'iPhone > Réinitialiser > Réinitialiser les paramètres réseau). Pour les problèmes persistants, vérifiez les limites de votre forfait de données ou contactez le Support Apple.

[Support Apple : Configurer le Point d'accès personnel](https://support.apple.com/en-us/HT204023)
[Ask Different : Le Point d'accès personnel ne reste pas connecté](https://apple.stackexchange.com/questions/332984/personal-hotspot-not-staying-connected)
[Reddit : Le point d'accès de l'iPhone ne cesse de se déconnecter](https://www.reddit.com/r/iphone/comments/170i24n/your_iphones_hotspot_keep_disconnecting_i_think_i/)
[MacRumors : Le point d'accès en 5G s'arrête sauf si l'écran est allumé](https://forums.macrumors.com/threads/ios-15-3-1-hotspot-on-5g-stops-unless-i-keep-screen-on.2336283/)
[wikiHow : Rendre le point d'accès de votre iPhone plus rapide](https://www.wikihow.com/Make-Hotspot-Faster-iPhone)
[BroadbandNow : Pourquoi mon point d'accès est-il si lent ?](https://broadbandnow.com/guides/why-is-my-hotspot-so-slow)