---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Frege sur les fonctions et l'insaturation
translated: true
type: note
---

### Que dit l'essai de 1904 de Frege « Qu'est-ce qu'une fonction ? » ?

Le court essai de Gottlob Frege, initialement intitulé *Was ist eine Funktion?* et publié dans un Festschrift pour le physicien Ludwig Boltzmann, est une clarification concise de la nature logique des fonctions en mathématiques. Écrit tard dans la carrière de Frege (après ses œuvres majeures comme *Grundlagen der Arithmetik* et *Grundgesetze der Arithmetik*), il répond aux confusions persistantes dans la pratique et la pédagogie mathématiques — un peu comme les problèmes que vous avez décrits avec des étudiants confondant les équations graphiques (y = x² + 3x) et la notation fonctionnelle (f(x) = x² + 3x). Frege ne réécrit pas les manuels de mathématiques ici, mais il dissèque pourquoi ces notations induisent en erreur et offre une fondation logique précise de ce que les fonctions *sont réellement*. L'article ne fait qu'environ 8 pages en allemand, et sa traduction anglaise (par Peter Geach) figure dans des recueils comme *Collected Papers on Mathematics, Logic, and Philosophy*.

#### Arguments clés et structure
Frege commence par reconnaître le succès intuitif de la notation fonctionnelle en mathématiques (par exemple, sin x, log x, ou x²) mais soutient qu'une utilisation négligée cache des problèmes logiques plus profonds. Il s'appuie sur ses idées antérieures de « Fonction et concept » (1891), où il a pour la première fois traité les fonctions comme des blocs de construction de la logique, et non pas seulement comme des outils arithmétiques. L'essai comporte trois fils principaux :

1.  **La nature non saturée des fonctions :**
    *   Frege insiste sur le fait qu'une fonction n'est pas une « chose » complète comme un nombre ou un objet — elle est *non saturée* (ou « incomplète »). Considérez-la comme un vide attendant d'être rempli : l'expression ξ² + 3ξ (utilisant ξ comme espace réservé) dénote la fonction elle-même, mais elle ne peut pas exister seule en tant qu'entité significative. Ce n'est que lorsque vous insérez un argument (par exemple, remplacez ξ par 2) qu'elle se « sature » et produit une valeur (comme 2² + 3·2 = 10).
    *   Cela contraste avec l'enseignement courant des mathématiques, où y = x² + 3x est présenté comme « la fonction » équivalente à y (une valeur complète). Frege dit que cela brouille les pistes : le côté gauche (y) est saturé (un objet), mais le côté droit est non saturé tant que x n'est pas spécifié. La notation nous trompe en nous faisant traiter la fonction comme une formule statique, ignorant son rôle logique dynamique.

2.  **Critique de l'usage mathématique traditionnel :**
    *   Frege prend pour cible le changement historique que vous avez mentionné — de la forme graphique y = f(x) à la forme abstraite f(x) — comme symptomatique d'erreurs plus profondes. Les mathématiques anciennes (par exemple, à l'époque d'Euler) voyaient les fonctions comme des courbes ou des règles, mais à l'époque de Frege, la définition de Dirichlet (une fonction comme une correspondance arbitraire entre un domaine et un ensemble d'arrivée) avait pris le dessus. Frege est d'accord avec l'idée extensionnelle (les fonctions définies par leur comportement entrée-sortie) mais reproche la manière dont les variables sont malmenées.
    *   Les variables ne sont pas des « quantités variables » (un mythe pédagogique courant) ; ce sont des espaces réservés dans des expressions. Retirer une variable de 2x³ + x pour « obtenir la fonction » (comme 2( )³ + ( )) échoue dans les cas à plusieurs arguments, où les emplacements pourraient nécessiter le *même* argument (comme dans x³ + x) ou des arguments *différents* (x³ + y). Cela mène à la confusion dans la liaison des variables et la représentation des fonctions complexes.
    *   Il fait également allusion au paradoxe du « concept cheval » (de son essai de 1892) : tout comme on ne peut pas former un nom propre comme « le concept cheval » (traitant un concept prédicatif comme un objet), on ne peut pas nommer directement les fonctions comme des entités complètes. Tenter de le faire effondre la structure logique.

3.  **Implications pour la logique et les mathématiques :**
    *   Les fonctions sont primitives dans le logicisme de Frege (réduire les mathématiques à la logique) : elles sont le ciment pour construire les propositions, les concepts (des fonctions de premier niveau spéciales renvoyant des valeurs de vérité) et même les nombres (comme parcours de valeurs de fonctions). Cela est lié à sa philosophie plus large — les fonctions permettent une inférence précise sans ambiguïté.
    *   Frege termine de manière optimiste : une analyse claire des fonctions affinera les mathématiques, évitant les paradoxes (annonçant par avance la lettre de Russell de 1902 concernant son propre paradoxe, qui a fait dérailler le *Grundgesetze* Vol. 2 à peu près à cette époque).

L'essai n'est pas un pamphlet ; il est diagnostique, comme un logicien-philosophe qui débogue le langage des mathématiques. Il a influencé la philosophie analytique (par exemple, Wittgenstein, Russell) et la théorie des types moderne en logique/informatique, où les fonctions sont en effet des opérations « non saturées ».

#### Qu'est-ce qu'une fonction, selon Frege ?
Selon Frege, une fonction est **une entité (ou expression) logique non saturée qui associe des arguments à des valeurs en complétant sa structure incomplète**. Formellement :
*   Ce n'est pas l'équation (y = f(x)), le graphique, ou même l'ensemble des sorties — ceux-ci sont dérivés.
*   C'est le « vide » dans une expression, comme f(ξ) = ξ² + 3ξ, où ξ signale l'incomplétude.
*   Propriétés : Extensionnelle (les mêmes entrées → les mêmes sorties définissent l'identité) ; hiérarchique (les fonctions de premier niveau prennent des objets comme arguments, renvoient des objets ; les fonctions de second niveau prennent des fonctions) ; et prédicative (les concepts/relations comme cas particuliers).
*   Exemple : Pour f(x) = x² + 3x, la fonction est la règle/l'expression avec un trou ; f(2) = 10 est la valeur saturée.

Cela résout la confusion de vos étudiants : La « fonction » n'est pas l'ensemble y = x² + 3x (qui mélange des parties complètes et incomplètes) ou simplement f(x) = x² + 3x (qui a encore un vide variable). C'est le mécanisme de correspondance pur et non saturé en dessous. L'enseigner de cette manière — à partir de la logique, et pas seulement de l'algèbre — évite l'interférence que vous avez notée.

Si vous le souhaitez, je peux suggérer des moyens d'expliquer cela à une classe de débutants ou approfondir d'autres essais de Frege.

**Références**
*   [Russell and Frege on the Logic of Functions (PDF summary/discussion)](https://newprairiepress.org/cgi/viewcontent.cgi?article=1023&context=biyclc)
*   [The Philosophy of Gottlob Frege (excerpt on functions)](https://assets.cambridge.org/052183/6697/excerpt/0521836697_excerpt.htm)
*   [Stanford Encyclopedia of Philosophy: Gottlob Frege](https://plato.stanford.edu/entries/frege/)
*   [Collected Papers on Mathematics, Logic, and Philosophy (contains English translation)](https://www.oxfordbibliographies.com/display/document/obo-9780195396577/obo-9780195396577-0065.xml)