---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Principe de localisation GPS expliqué simplement
translated: true
type: note
---

### Deuxième tâche de vulgarisation scientifique du jour : Une vidéo expliquant le principe du système de positionnement GPS

Je recommande à tous de regarder cette vidéo qui explique les principes du système de positionnement GPS. Cependant, il y avait un petit problème avec l'une des images, alors j'ai apporté une correction rapide.

Le principe est en fait assez simple—il ne nécessite que des connaissances de base en géométrie dans l'espace pour être compris. On peut le résumer en une phrase : « L'intersection de quatre sphères est un point unique. » Maintenant, je vais détailler exactement comment cela s'applique :

1.  Les satellites GPS (ou les stations de base au sol) transmettent des informations qui incluent leurs « coordonnées » au moment de la transmission et un « horodatage ». (Figure 1)

    - Lorsque le récepteur GPS capte ce signal, il peut calculer la distance \\( r_1 \\) de ce satellite à lui-même en utilisant l'horodatage : \\( r_1 = \\) vitesse de la lumière × temps de transmission.

    - Toutes les positions à une distance \\( r_1 \\) de ce satellite se situent sur une sphère de rayon \\( r_1 \\). Pour simplifier, je l'appellerai la « sphère équidistante ». La géométrie nous dit que l'intersection de deux sphères est un cercle, donc l'intersection de cette « sphère équidistante » avec la Terre est un cercle (Figure 2a—cela demande un peu de visualisation en 3D). Clairement, avec le signal d'un seul satellite, nous ne pouvons pas déterminer notre position exacte ; nous savons seulement que nous sommes quelque part sur ce cercle.

    Si nous recevons les signaux d'un deuxième satellite avec sa position et sa distance, nous pouvons tracer une autre sphère. L'intersection de ces deux sphères équidistantes avec la Terre—trois sphères au total—donne les positions possibles où nous pourrions nous trouver. Cette intersection est très probablement seulement deux points, mais nous ne savons pas lequel est correct. (Figure 2b)

    Avec la position et la distance d'un troisième satellite, sa sphère équidistante passera très probablement par l'un de ces deux points mais pas par l'autre. Cela détermine les coordonnées du récepteur au sol. (Figure 2c)

    Si nous obtenons un signal d'un quatrième satellite, sa sphère équidistante passera également par ce même point. Donc, si nous n'avons besoin que des coordonnées au sol, le quatrième satellite n'est pas strictement nécessaire. (Figure 2d)

Tout cela peut vraiment se résumer à une idée clé : l'intersection de quatre sphères est un point unique. Les trois sphères équidistantes des satellites, plus la Terre elle-même (comme quatrième sphère), s'intersectent en un point unique—une seule localisation.

Notez que ces signaux ne doivent pas nécessairement provenir de satellites. Des stations de base au sol avec des coordonnées connues peuvent transmettre le même type de signal (coordonnées + horodatage), et le récepteur peut calculer sa position exactement de la même manière—c'est simplement un calcul d'intersection géométrique.

**Exercice 1 :** Dans la deuxième étape, parce qu'il y a typiquement une différence de temps entre l'horloge du récepteur et celle du satellite GPS, vous ne pouvez pas obtenir le « temps de transmission » à partir d'un seul signal. Mais si le même satellite envoie deux signaux, vous pouvez éliminer ce décalage et calculer le temps de transmission. Essayez de comprendre pourquoi par vous-même.

**Exercice 2a :** Dans la quatrième étape, j'ai dit que l'intersection des deux sphères équidistantes et de la Terre est « très probablement » seulement deux points. Dans quels cas particuliers cette intersection serait-elle plus de deux points ? Quelle autre forme pourrait-elle prendre ?

**Exercice 2b :** Dans la cinquième étape, j'ai dit que la sphère équidistante du troisième satellite passe « très probablement » par l'un des deux points mais pas par l'autre. Dans quels cas particuliers sa sphère équidistante passerait-elle par les deux points en même temps ?

**Exercice 3 :** Avec les signaux de quatre satellites, vous pouvez non seulement calculer les coordonnées mais aussi l'altitude. Alors, pourquoi le quatrième satellite est-il toujours utile ?

**Exercice 4 :** Si nous comptons entièrement sur des stations de base au sol, nous pouvons calculer les coordonnées en utilisant les signaux de trois stations. Avec le signal d'une quatrième station de base, pouvons-nous calculer l'altitude ? Si oui, quelle condition les positions de ces quatre stations de base doivent-elles satisfaire ?

**Exercice 5 :** Si la configuration de l'Exercice 4 est réalisable, concevez un « système GPS basé au sol » qui n'utilise pas du tout de satellites mais reproduit entièrement les fonctionnalités d'un système GPS satellitaire. Il doit répondre aux besoins de la navigation quotidienne des véhicules et des piétons, de l'aviation, des voyages maritimes, de la randonnée, du hors-piste, et plus encore. Le système doit être rentable, avec des dépenses pas plus élevées que celles d'un système basé sur des satellites.

[Article original : Principes du GPS](https://yinwang1.substack.com/p/gps)