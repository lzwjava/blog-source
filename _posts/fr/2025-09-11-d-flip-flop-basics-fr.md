---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Fondamentaux et comparaisons de la bascule D
translated: true
type: note
---

Réponse : D flip-flop

Pourquoi c'est le bon choix
- Fonction : Une bascule D (données ou délai) stocke exactement un bit. Sur le front actif de l'horloge (montant ou descendant, selon la conception), elle échantillonne l'entrée D et met à jour la sortie Q avec cette valeur. Entre les fronts d'horloge, Q maintient sa valeur précédente.
- Règle comportementale : Q_suivant = D sur le front d'horloge ; sinon Q reste inchangé. Ce comportement « échantillonner-et-maintenir » est exactement ce que l'on souhaite pour les registres et les pipelines.

En quoi elle diffère des autres
- Bascule RS : Possède des entrées Set et Reset séparées et une condition invalide (S=R=1). Pas idéale pour le stockage de données général dans les conceptions synchrones.
- Bascule JK : Généralise la RS ; J=K=1 provoque une bascule. Plus flexible mais plus complexe et rarement utilisée pour les registres de données standard.
- Bascule T : Bascule lorsque T=1 sur le front d'horloge, maintient l'état lorsque T=0. Excellente pour les compteurs diviseurs par 2, pas pour le stockage de données arbitraires.

Détails clés sur les bascules D
- Sensibilité au front vs verrou : Une bascule D est sensible au front (se met à jour uniquement sur le front d'horloge). Un verrou D est sensible au niveau (transparent tant que l'autorisation est active). Quand on dit « transfère directement l'entrée vers la sortie lors de l'horloge », on fait généralement référence à la bascule D qui capture D sur le front d'horloge.
- Exigences de temporisation : Un fonctionnement correct nécessite de respecter le temps de setup (D stable avant le front) et le temps de hold (D stable après le front). Le non-respect de ces temps peut provoquer une métastabilité.
- Variantes : Incluent souvent des broches de preset (mise à 1) et clear (remise à 0) asynchrones pour initialiser Q.
- Utilisations courantes : Construction de registres n bits (n bascules D en parallèle), étages de pipeline, registres d'état, registres à décalage (souvent avec un MUX pour le chargement série/parallèle), synchroniseurs (en paires) pour les traversées de domaines d'horloge.

Règle générale
- Si vous avez besoin d'un élément de stockage qui « se contente de stocker le bit que vous présentez à l'horloge », utilisez une bascule D.