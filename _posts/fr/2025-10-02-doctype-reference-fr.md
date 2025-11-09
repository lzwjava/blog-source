---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Référence des déclarations DOCTYPE CodeIgniter
translated: true
type: note
---

### Aperçu
Il s'agit d'un tableau PHP du framework CodeIgniter (un framework d'application web open-source), qui définit les déclarations DOCTYPE pour différents langages de balisage. Un DOCTYPE est une déclaration de type de document qui informe les navigateurs et les validateurs sur la version et la norme du langage de balisage utilisé dans un document HTML. Il assure un rendu et une validation corrects. Ces déclarations sont basées sur les normes officielles du W3C. Ci-dessous, je les expliquerai une par une en les regroupant par thème, y compris leur objectif et leurs cas d'utilisation typiques.

### Doctypes XHTML
XHTML (eXtensible HyperText Markup Language) est HTML reformulé en XML, imposant une syntaxe plus stricte (par exemple, exigeant des balises fermantes et des éléments en minuscules).
- **xhtml11** : Déclare XHTML 1.1, la dernière version de XHTML avec des fonctionnalités modulaires pour les applications web avancées. Strict, conforme au XML ; utilisé pour des pages web modernes et sémantiques sans cadres ni éléments hérités.
- **xhtml1-strict** : XHTML 1.0 Strict ; impose un balisage propre et sémantique sans éléments obsolètes (par exemple, pas de `<font>`). Idéal pour les sites conformes aux normes nécessitant une rétrocompatibilité.
- **xhtml1-trans** : XHTML 1.0 Transitional ; autorise certains éléments HTML hérités pour faciliter la migration depuis HTML 3.2/4.0. Utile pour les sites existants mélangeant ancien et nouveau balisage.
- **xhtml1-frame** : XHTML 1.0 Frameset ; prend en charge les mises en page avec cadres (`<frameset>`). Obsolète dans le web design moderne en raison de problèmes d'utilisabilité et de défauts de référencement (SEO).
- **xhtml-basic11** : XHTML Basic 1.1 ; un profil léger pour les appareils mobiles et les applications simples, excluant les fonctionnalités avancées comme les feuilles de style ou les formulaires.

### Doctypes HTML
HTML est le langage de balisage standard pour les pages web, évoluant de normes laxistes à strictes.
- **html5** : Le DOCTYPE HTML5 moderne ; simple et pérenne, analysé en mode standard par tous les navigateurs. Prend en charge le multimédia, les API et les éléments sémantiques (par exemple, `<article>`, `<header>`). Recommandé pour les nouveaux sites web.
- **html4-strict** : HTML 4.01 Strict ; impose une rigueur sémantique sans éléments obsolètes. Utilisé dans les projets hérités nécessitant une stricte conformité.
- **html4-trans** : HTML 4.01 Transitional ; permissif, autorisant les balises héritées pour des mises à jour progressives. Courant dans les anciens sites en transition vers les standards.
- **html4-frame** : HTML 4.01 Frameset ; pour les pages avec cadres, maintenant obsolète en raison des temps de chargement lents et des problèmes d'accessibilité.

### Doctypes MathML
MathML (Mathematical Markup Language) permet d'afficher des notations mathématiques sur le web.
- **mathml1** : MathML 1.0 ; rendu mathématique de base au format XML. Utilisé dans les outils éducatifs ou les documents avec des équations simples.
- **mathml2** : MathML 2.0 ; prise en charge améliorée pour les mathématiques complexes, mieux intégrée avec d'autres langages de balisage. Fondement pour l'affichage mathématique web moderne.

### Doctypes SVG
SVG (Scalable Vector Graphics) définit des images vectorielles en XML pour les graphiques web.
- **svg10** : SVG 1.0 ; graphiques vectoriels 2D de base. Utilisé pour les illustrations statiques.
- **svg11** : SVG 1.1 ; graphiques 2D complets avec animations et filtres. Standard pour les graphiques web dynamiques.
- **svg11-basic** : SVG 1.1 Basic ; sous-ensemble axé sur le mobile avec moins de fonctionnalités. Pour le SVG léger sur les appareils.
- **svg11-tiny** : SVG 1.1 Tiny ; profil minimal pour les appareils à faible puissance comme les téléphones. Prend en charge les formes de base et les animations.

### Doctypes Composés
Ceux-ci combinent plusieurs normes pour un contenu riche et multimédia.
- **xhtml-math-svg-xh** : XHTML 1.1 avec MathML 2.0 et SVG 1.1 ; pour les documents mélangeant texte, mathématiques et graphiques (par exemple, articles scientifiques).
- **xhtml-math-svg-sh** : Similaire au précédent mais basé sur SVG (`<svg:svg>`), pour les documents à dominance SVG avec XHTML et MathML intégrés.
- **xhtml-rdfa-1** : XHTML avec RDFa 1.0 (Resource Description Framework in attributes) ; améliore l'incorporation de données pour le web sémantique dans les sites riches en métadonnées.
- **xhtml-rdfa-2** : XHTML avec RDFa 1.1 ; RDFa amélioré pour lier les données dans les attributs HTML, utilisé dans les applications du web de données.

### Notes d'utilisation
- Elles sont prédéfinies dans CodeIgniter pour une insertion facile via sa fonction d'aide `doctype()`.
- Le développement web moderne favorise HTML5 (`html5`) pour sa flexibilité et son support par les navigateurs. Les anciens doctypes (par exemple, HTML 4 ou les versions avec cadres) sont largement obsolètes.
- Comme en témoignent les spécifications du W3C (par exemple, w3.org/TR/html5/, w3.org/TR/xhtml11/), elles assurent une analyse cohérente : les navigateurs les utilisent pour déclencher le mode standard ou le mode quirks, affectant la mise en page et les scripts. Choisissez en fonction des besoins de balisage de votre projet pour une meilleure validation (via des outils comme le Validateur W3C). Si vous travaillez dans CodeIgniter, utilisez la clé du tableau dans vos vues pour générer la déclaration.