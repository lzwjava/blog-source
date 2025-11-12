---
audio: false
generated: true
lang: fr
layout: post
title: Formule de capacité de Shannon
translated: true
type: note
---

La formule de capacité de Shannon s'écrit en réalité :

C = B log₂(1 + S/N)

Où :
- C est la capacité du canal en bits par seconde
- B est la bande passante en Hertz
- S/N est le rapport signal sur bruit (rapport de puissance)
- log₂ est le logarithme de base 2

Cette formule représente le débit de données théorique maximum qui peut être transmis de manière fiable sur un canal de communication avec une bande passante B et un rapport signal sur bruit de S/N.

Pour comprendre pourquoi cela est correct :

1. **Facteur de bande passante (B)** : La bande passante influence directement la capacité - doubler la bande passante double la capacité.

2. **Relation logarithmique** : Le log₂ montre que la capacité augmente logarithmiquement avec S/N, et non linéairement. Cela signifie :
   - Doubler S/N ne double pas la capacité
   - Chaque "bit" supplémentaire de capacité nécessite de doubler le S/N

3. **Terme 1 + S/N** : L'addition du 1 garantit que la capacité est toujours positive, même avec des valeurs de S/N très faibles.

Cette formule est fondamentale pour la théorie de l'information car elle établit la limite supérieure théorique de la quantité d'informations pouvant être transmises via un canal bruité, quel que soit le schéma de codage utilisé.

Souhaitez-vous que j'explique un aspect particulier de cette formule plus en détail ?