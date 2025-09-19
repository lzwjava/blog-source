---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Développement logiciel multi-régions
translated: true
---

Pour les entreprises internationales, il existe souvent des projets qui servent les populations de plusieurs régions, comme Singapour, Hong Kong, le Royaume-Uni, les États-Unis et la Chine.

J'ai travaillé sur certains projets qui desservent les utilisateurs de plusieurs régions. Faire les choses correctement dans les projets backend n'est pas facile.

Pour la Standard Chartered Bank, il y a des applications comme SC Mobile India et SC Mobile Hong Kong. Pour McDonald's, il existe des versions comme McDonald's Chine et McDonald's USA. Pour Starbucks, il y a Starbucks USA et Starbucks Chine. Essentiellement, ils fournissent à chaque pays ses propres applications. Souvent, les méthodes de connexion diffèrent pour les utilisateurs chinois et les utilisateurs internationaux. En plus d'utiliser les téléphones mobiles, les utilisateurs chinois ont souvent l'option de se connecter avec WeChat, tandis que les utilisateurs internationaux peuvent se connecter avec Facebook, Google ou Apple.

Ces applications utilisent probablement des serveurs backend différents et ont certaines fonctionnalités différentes, mais elles conservent le même langage de conception. Il est probablement erroné de faire cela. Les premières années, cela semble simple ou réalisable. Mais après une décennie, ils sauront que c'est très douloureux. Le coût de maintenance ou le coût de synchronisation, le coût des tests—il y a des tonnes d'efforts en double.

Cependant, pour Facebook, Google ou Apple Pay, c'est assez simple. Certains pourraient dire qu'ils ne sont pas des applications financières ; ils ont certaines règles de conformité à respecter. Ce n'est pas vrai. La conformité signifie souvent le serveur de base de données, ou la base de données, ou certaines données que les départements gouvernementaux veulent vérifier ou pour que les sociétés d'audit effectuent des audits. Cependant, les autres efforts sont les mêmes. Le logiciel est très flexible. Nous devrions laisser le code être dans le même dépôt, nous devrions utiliser la configuration de la source de données pour héberger les données de différentes régions, et nous devrions partager le même code, la même conception, le même flux de travail et les mêmes tests autant que possible.

Apple Pay est un bon exemple de cela. L'App Store est également un bon exemple de cela. Ils desservent chaque pays aussi.

Il y a probablement certains projets dans les grandes entreprises technologiques qui utilisent les continents pour séparer, comme l'Asie et la région Pacifique, l'Amérique du Nord. Pour ceux-ci aussi.

La première chose à faire lors du développement multi-régions est de savoir ce qui est différent, quelle est la conformité que nous devons suivre, et comment réduire les efforts en double autant que possible.

Pour la synthèse vocale, Google Cloud doit entraîner différentes langues. Ils fournissent différents modèles et différentes langues pour cela. Pour les langues, les différences entre les langues sont leurs sons et leur apparence de caractères. Le premier signifie que lorsque nous utilisons Google Cloud pour la synthèse vocale, nous devons utiliser différents modèles. Pour leur apparence de caractères, cela signifie que lors de la génération de PDF, nous devons être prudents dans le choix de la police.

Pour les projets multi-régions, dans les projets Spring Boot, nous pouvons utiliser ses alias et différentes initialisations d'objets pour cela. Nous pouvons utiliser intelligemment les propriétés ou la configuration YAML. Nous pouvons mettre toute la logique différente basée sur la région dans certains modules ou classes spécifiques.

Et pour l'hébergement de code, différentes branches pour différents pays semblent faciles au début, mais après quelques années, vous saurez à quel point c'est douloureux. Vous devez faire un git cherry-pick pour les autres régions. Et vous devez tester à nouveau dans une autre branche. Chaque fois que vous faites un petit changement, vous devez le synchroniser avec les branches. Et avec le temps, si nous ne mettons pas nos efforts à minimiser le code ou la logique différente, les différences de code entre plusieurs régions ou pays deviennent suffisamment grandes pour être impossibles à corriger.

La bonne nouvelle est qu'aujourd'hui, l'IA peut nous aider à refactoriser ou à écrire un meilleur code, ou à corriger les problèmes de conception de code multi-régions. Peu importe la taille de l'erreur, lorsque nous la corrigeons, c'est une petite erreur.

Non seulement pour le codage, le déploiement et la maintenance des versions, mais aussi pour l'extensibilité. Pensez à ajouter un nouveau pays ou une nouvelle région. Quel effort cela nécessitera-t-il ? Si c'est minimal ou ne nécessite que quelques configurations, alors notre conception est excellente. Si cela prend quelques mois, c'est acceptable aussi. Si cela prend plusieurs années, allons-nous toujours le faire ?

Dans l'essai de Yin Wang, [On Linux, Windows et Mac](https://www.yinwang.org/blog-cn/2013/03/07/linux-windows-mac), il mentionne qu'un designer Adobe lui a dit qu'ils avaient passé deux ans à migrer Photoshop de Windows vers macOS.

Le support d'une nouvelle région nécessitera-t-il deux ans d'adaptation ? Pour certains projets, cela pourrait être le cas. C'est une considération de conception critique.

Le monde devient de plus en plus connecté. Peu importe le pays ou la région que nous ciblons initialement, nous devons aussi considérer les autres régions. Il est préférable de bien faire les choses dès le début. Pour les entreprises internationales établies, il est conseillé de développer des produits logiciels pour au moins deux pays ou régions dès le départ. Maintenez cette mentalité multi-régions dès le début. Si nous avons plus de ressources d'ingénierie, nous pouvons soutenir plus de pays ou de régions.