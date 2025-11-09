---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: La Preuve Incertaine de la Science par les Tests
translated: true
type: note
---

### Pourquoi les gens font aveuglément confiance aux expériences scientifiques : une analogie de programmeur

Beaucoup de gens ne parviennent pas à saisir les défauts logiques inhérents aux expériences scientifiques, ce qui les amène à accepter la science "prouvée" pour argent comptant. Ils ne comprennent pas pourquoi une théorie "confirmée" par des expériences peut finalement se révéler fausse. Mais si vous comprenez les principes des tests logiciels, vous verrez la vraie nature des expériences scientifiques — comme les problèmes que j'ai abordés dans mon article *La Logique du Test*.

En bref, une théorie scientifique est comme un morceau de code, et les expériences scientifiques sont comme des tests conçus pour "vérifier" que le code fonctionne correctement. Imaginez que vous écrivez un programme pour calculer une multiplication, mais que vous l'implémentez par erreur comme une addition : `(x, y) => x + y`. Si vous le testez avec les entrées (2, 2) et que vous obtenez 4, vous pourriez penser : "Génial, ça multiplie correctement !" Mais vous auriez tort. Pour confirmer véritablement que c'est une fonction de multiplication, vous devriez tester *toutes les entrées possibles* et vous assurer qu'elle produit le bon résultat à chaque fois. Comme nous ne pouvons pas tester une infinité d'entrées, aucune quantité de tests ne peut *garantir* que le programme est correct. Même si des milliers de tests passent, il pourrait encore échouer spectaculairement sur un cas non testé.

La science fonctionne de la même manière. Une théorie n'est véritablement "prouvée" que si elle résiste à *toutes les conditions concevables* — chaque "entrée" possible de l'univers. Un écueil courant consiste à réaliser une seule expérience dans un cadre étroit et à déclarer la théorie validée. C'est comme se féliciter après le test (2, 2) et considérer que c'est terminé. Parfois, vous exécutez des milliers de tests, et tout fonctionne — jusqu'à ce qu'une nouvelle entrée arrive, et boum, la théorie s'effondre.

C'est l'essence de la "falsifiabilité" de la science. Certaines personnes présentent la falsifiabilité comme la marque de la vraie science, rejetant tout ce qui est non falsifiable comme de la pseudoscience. Mais en utilisant l'analogie de la programmation, nous pouvons voir que ce n'est pas tout à fait juste. La falsifiabilité met en lumière les *limitations* des expériences — elles peuvent réfuter une théorie mais jamais pleinement la prouver. Elle ne devrait pas être la *définition* rigide de ce qui compte comme science.

Plus vous ajoutez de contraintes et de complexité à vos tests (ou expériences), plus il devient difficile d'affirmer avec confiance que votre programme (ou théorie) est correct. En programmation, des configurations de test complexes avec une multitude de cas particuliers rendent la validation plus difficile et moins convaincante. La science n'est pas différente : plus une expérience implique de conditions contrôlées, d'équipements sophistiqués et de variables isolées, plus sa "force de persuasion" pour prouver une théorie générale est faible. Cela pourrait fonctionner dans cette boîte de Pétri, mais est-ce que cela s'applique au monde réel désordonné ?

C'est pourquoi je ne peux pas adhérer à la théorie de la relativité d'Einstein. Les expériences utilisées pour la tester sont rares, confinées à des conditions ultra-spécialisées sans grande universalité. Les expériences classiques de validation de la relativité n'ont lieu qu'une fois par siècle environ, rendant la réplication indépendante presque impossible pour la plupart des chercheurs. Jusqu'à aujourd'hui, il n'y a pas d'application pratique qui *exige* la relativité — l'exemple souvent cité des satellites GPS n'en a pas réellement besoin ; la physique newtonienne de base suffit avec des ajustements mineurs. Même le postulat de base, "la vitesse de la lumière est constante quelle que soit le mouvement de la source", repose sur une seule expérience dans un cadre artificiel avec un équipement hyper-complexe, élevé au rang de vérité éternelle sans examen plus large.

Beaucoup de théories médicales suivent le même schéma : une étude est saluée comme un évangile, citée sans cesse, mais rarement vérifiée de manière indépendante. Les générations suivantes se contentent de la répéter, supposant qu'elle est solide comme le roc.

Cette analogie n'a pas pour but de rejeter la science en bloc — c'est un appel à rester humble sur ce que la "preuve" signifie réellement. Les expériences sont des outils puissants, mais ce sont des projecteurs, pas des phares. Ils éclairent des parcelles de vérité, mais des ombres rôdent partout. Si nous traitions les théories comme du code sous examen constant — ouvert à des tests et des refactorisations sans fin — la science n'en serait que plus forte.