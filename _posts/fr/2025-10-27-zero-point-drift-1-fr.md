---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Causes de la dérive du point zéro de l'amplificateur
translated: true
type: note
---

### Comprendre la phrase : « Bien que des facteurs comme les variations de l'alimentation ou les disparités entre composants y contribuent »

Cette phrase est une transition dans le contexte de l'explication de la **dérive du point zéro** (également appelée dérive de l'offset DC) dans les amplificateurs multi-étages à couplage direct. Elle reconnaît que la température n'est pas la *seule* responsable – d'autres problèmes jouent également un rôle – mais qu'ils sont secondaires. Laissez-moi décomposer cela étape par étape pour plus de clarté, avec quelques bases d'électronique pour rendre cela concret.

#### 1. **Ce que signifie la phrase en termes simples**
   - **« Bien que »** : C'est un mot de concession. C'est comme dire : « Bien sûr, d'autres choses peuvent aussi causer des problèmes, *mais*... » Il met en avant les variations de température comme le principal sujet sans ignorer le reste.
   - **« Des facteurs comme les variations de l'alimentation ou les disparités entre composants y contribuent »** : Ce sont des causes *additionnelles* de la dérive. Elles « contribuent », ce qui signifie qu'elles s'ajoutent au problème, mais elles ne sont pas la cause dominante (c'est la température). Dans les amplis à couplage direct (pas de condensateurs pour bloquer le DC), tout petit décalage DC dans un étage est amplifié dans le suivant, créant un effet boule de neige qui résulte en un offset important et non désiré en sortie – même avec un signal d'entrée nul.

L'idée générale : La dérive provient de multiples sources, mais le texte souligne que la température est la plus difficile à corriger car elle est inévitable et cumulative à travers les étages.

#### 2. **Rappel rapide : Pourquoi la dérive se produit dans les amplis à couplage direct**
   - Ces circuits transmettent *à la fois* le AC (signal) et le DC (polarisation) sans condensateurs, donc toute la chaîne est « liée en DC ».
   - Une petite erreur DC en amont (par exemple, un offset de 1 mV) est multipliée par le gain de chaque étage. Dans un ampli à 3 étages avec un gain de 10x par étage, cela donne un offset de sortie de 1V – problématique pour les applications de précision comme l'audio ou les capteurs.
   - Résultat : Le « point zéro » (la sortie à entrée nulle) dérive, causant une distorsion ou des erreurs.

#### 3. **Explication des facteurs spécifiques mentionnés**
   Voici comment les « variations de l'alimentation » et les « disparités entre composants » conduisent à la dérive, avec des exemples simples :

   - **Variations de l'alimentation** :
     - Votre ampli fonctionne avec une alimentation DC (par exemple, +12V). Si elle fluctue (disons, de 11,9V à 12,1V en raison de changements de charge ou d'une ondulation), cela modifie directement les courants/tensions de polarisation des transistors.
     - Dans une configuration multi-étages, le décalage de polarisation du premier étage se propage : le DC de sortie de l'Étage 1 change → est amplifié dans l'Étage 2 → devient plus important dans l'Étage 3.
     - **Pourquoi cela contribue** : Les alimentations ne sont pas parfaites (par exemple, décharge de batterie ou bruit du régulateur). Même une variation de 0,1 % peut causer des décalages de l'ordre du mV, amplifiés en volts dans les étages suivants.
     - **Exemple** : Dans une conception discrète de type ampli-op, une chute de 50 mV de l'alimentation peut décaler la tension d'émetteur dans un étage à BJT, créant un offset de 5 mV qui est multiplié par 100 sur plusieurs étages.

   - **Disparités entre composants** :
     - Les composants réels ne sont pas identiques : Les transistors peuvent avoir un β (gain en courant) différant de 10 à 20 % entre eux, ou les résistances une tolérance de 1 à 5 %.
     - Dans une paire différentielle (courante pour la stabilité de polarisation), des V_BE (tensions base-émetteur) ou des résistances non appariées créent une tension d'offset inhérente dès le départ.
     - **Pourquoi cela contribue** : Sans condensateurs, cette disparité statique n'est pas bloquée – elle se propage et est amplifiée comme un signal DC.
     - **Exemple** : Deux transistors dans un étage devraient partager le courant de manière égale, mais si l'un a un V_BE = 0,7V et l'autre 0,71V, cela crée un déséquilibre de 10 mV. Amplifié sur 3 étages (gain total de 1000), cela représente une dérive de 10V !

#### 4. **Pourquoi la température reste le problème principal**
   - Ces autres facteurs sont « plus faciles » à atténuer : Utilisez des alimentations régulées ou des composants appariés/sélectionnés.
   - Mais la température ? La V_BE diminue d'environ ~2 mV/°C par transistor, et le β augmente avec la chaleur. Dans un ampli multi-étages, chaque étage ajoute son propre décalage induit par la température, se cumulant comme des intérêts composés. Une augmentation de 10°C pourrait faire dériver la sortie de plusieurs centaines de mV – difficile à compenser complètement sans circuits complexes (par exemple, suivi thermique ou stabilisation par chopper).

#### Conseils pour visualiser ou expérimenter
- **Simulation** : Utilisez LTSpice (gratuit) et construisez un simple ampli BJT à 2 étages (sans condensateurs). Modifiez la tension d'alimentation ou les valeurs des résistances – observez le décalage DC de sortie.
- **Solution pratique** : Pour les conceptions à faible dérive, on ajoute des potentiomètres de réglage d'offset (offset-null) ou on utilise des circuits intégrés comme des ampli-ops avec compensation interne.

Si cela est lié à un circuit spécifique que vous concevez ou étudiez, partagez plus de détails pour des conseils adaptés !