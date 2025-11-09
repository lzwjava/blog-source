---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Limitations et solutions de suivi du DJI Mini 3
translated: true
type: note
---

Le DJI Mini 3 (le modèle de base) ne dispose pas de fonctions intégrées telles que ActiveTrack (suivi visuel d'objet) ou le mode Follow Me (suivi par GPS) pour poursuivre automatiquement ou survoler une voiture en mouvement pour des photos ou des vidéos. C'est une limitation importante par rapport aux drones DJI haut de gamme. Cependant, le DJI Mini 3 Pro prend en charge ActiveTrack, qui utilise la caméra du drone pour suivre visuellement des sujets comme des voitures, des personnes ou des véhicules depuis l'arrière, le dessus ou d'autres positions, vous permettant de capturer des plans dynamiques tandis que le drone maintient une distance et une hauteur définies.

Concernant les API pour le développement personnalisé :
- Le SDK Mobile de DJI (pour les applications Android/iOS) prend en charge la série Mini 3, y compris le contrôle de vol basique comme les commandes de manche virtuel (par exemple, pour ajuster manuellement la position/la vitesse) et les missions par waypoints. Vous pourriez créer une application personnalisée pour faire suivre au drone la trajectoire d'une voiture si vous intégrez des données GPS en temps réel de la voiture (via Bluetooth, une application compagnon ou un émetteur externe). Ce ne serait pas un suivi visuel "prêt à l'emploi", mais cela pourrait approximer une poursuite depuis le dessus ou l'arrière en calculant des décalages (par exemple, 10-20 mètres en arrière et 50 mètres au-dessus).
- Cependant, les API de mission ActiveTrack du SDK (pour le suivi visuel automatisé) **ne sont pas prises en charge** sur le Mini 3 ou le Mini 3 Pro—elles sont limitées aux modèles plus anciens comme le Mavic Air 2 ou l'Air 2S.
- Pour la capture de photos pendant le vol, vous pouvez utiliser les API de caméra du SDK pour déclencher des prises de vue automatiquement basées sur des minuteries, la distance ou votre propre logique.

Si vous êtes ouvert aux applications tierces (qui utilisent le SDK en arrière-plan) :
- Des applications comme Dronelink ou Litchi peuvent activer un mode "Follow Me" de base sur le Mini 3 en utilisant le GPS de votre téléphone (ou un appareil externe). Pour suivre une voiture spécifiquement, vous devriez l'associer à une balise GPS sur le véhicule (par exemple, via un hotspot smartphone ou un tracker dédié comme une alternative à Tile ou AirTag qui transmet des données à l'application). Cette configuration a fonctionné pour des utilisateurs poursuivant des voitures sur route ou sentier, le drone restant au-dessus ou suivant derrière pour le tournage.

Gardez à l'esprit les notes légales/sécurité : Le suivi de véhicules en mouvement par un drone doit respecter les réglementations locales (par exemple, les règles de la FAA aux États-Unis exigent une visibilité directe, pas d'opérations hors vue). Testez dans des zones dégagées pour éviter les obstacles, et la conception légère du Mini 3 limite sa résistance au vent pendant les poursuites à haute vitesse.

### Références
- [DJI Mini 3 Active Track HACK DJI Mini 3 Follow Me](https://www.youtube.com/watch?v=UYzSdd3iJwA)
- [Does the mini 3 have ai tracking to follow objects like cars](https://www.facebook.com/groups/djimini3ukowners/posts/2726498670890510/)
- [Can someone explain follow me mode? And if it's on mini 3?](https://www.reddit.com/r/dji/comments/13pqbw7/can_someone_explain_follow_me_mode_and_if_its_on/)
- [DJI Mini 3 / Mini 3 Pro - Follow Me Mode With Dronelink](https://www.youtube.com/watch?v=Rhneo8QoXV0)
- [DJI Product SDK Compatibility](https://support.dji.com/help/content?customId=01700000763&spaceId=17&re=US&lang=en&documentType=&paperDocType=ARTICLE)
- [DJI has released MSDK 5.3.0 with support for Mini 3 Pro and Mini 3](https://forum.flylitchi.com/t/dji-has-released-msdk-5-3-0-with-support-for-mini-3-pro-and-mini-3/9512)
- [class ActiveTrackOperator - DJI Mobile SDK Documentation](https://developer.dji.com/api-reference/android-api/Components/Missions/DJIActiveTrackMissionOperator.html)