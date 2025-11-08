---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Sous-estimer les experts et la compréhension approfondie
translated: true
type: note
---

### Contexte de l'article
Cet extrait provient d'un article de blog (ou d'une réflexion sur les réseaux sociaux) de Yin Wang, un ingénieur logiciel éminent, un passionné des langages de programmation et un blogueur connu pour ses critiques perspicaces des langages de programmation, des systèmes de types et de la conception de logiciels. Wang a travaillé dans des entreprises comme Google et est l'auteur du blog Yinwang.org, où il se penche souvent en profondeur sur des sujets tels que la programmation fonctionnelle, les dialectes de Lisp et la philosophie de la conception des langages. L'article reflète sa croissance personnelle dans la compréhension des perspectives des experts, en utilisant Dan Friedman comme étude de cas. C'est un humble aveu de biais de confirmation – comment nous (y compris Wang lui-même) pouvons mal juger l'expertise de quelqu'un sur la base de désaccords superficiels.

Le ton est introspectif et philosophique, commençant par une observation générale sur les "schémas de pensée humains" (faisant probablement référence à la façon dont les gens forment rapidement des préjugés) et la reliant à sa propre expérience. Il utilise cette anecdote pour illustrer qu'une critique profonde vient souvent d'une compréhension profonde, et non de l'ignorance.

### L'histoire dans l'anecdote
Yin Wang raconte une époque où il a sous-estimé Dan P. Friedman, un professeur légendaire d'informatique à l'Université de l'Indiana et un pionnier de la programmation fonctionnelle et logique. Friedman est surtout connu pour avoir co-écrit la série emblématique de livres *The Little Schemer* (avec Matthias Felleisen), qui enseigne la programmation à travers un style ludique de questions et réponses en utilisant Scheme, un dialecte minimaliste de Lisp.

- **Son mauvais jugement initial** : Friedman a longtemps été vocal sur sa préférence pour les langages dynamiques comme Scheme, qui n'imposent pas de types à la compilation (permettant plus de flexibilité mais risquant des erreurs à l'exécution). Il critique souvent les systèmes de types statiques dans des langages comme Haskell, arguant qu'ils peuvent être excessivement rigides, verbeux ou limiter l'expressivité sans offrir des bénéfices proportionnels dans les logiciels du monde réel. Wang, qui respectait l'intellect de Friedman (en particulier sa maîtrise de concepts avancés comme les *continuations* – un mécanisme puissant pour manipuler le flux de contrôle, semblable à "capturer" le reste de l'exécution d'un programme comme une fonction), le considérait tout de même comme "biaisé" parce que Friedman "ne connaissait que les langages dynamiques". Wang voyait cela comme un angle mort, un peu comme comment les gens aujourd'hui pourraient stéréotyper des experts en fonction de leurs préférences d'outils.

- **Le point de basculement** : La vision de Wang a changé lorsque Friedman a démontré sa profondeur. Lors d'une session d'enseignement (probablement dans un cours ou un atelier), Friedman a utilisé *miniKanren* – un langage dédié embarqué et léger pour la programmation logique (pensez à des requêtes relationnelles, comme en Prolog, mais intégrées dans Scheme) – pour implémenter le *système de types Hindley-Milner*. C'est l'algorithme d'inférence de types polymorphe qui alimente des langages comme ML et Haskell, qui déduit automatiquement les types sans annotations tout en garantissant la sécurité. L'implémenter dans un langage dynamique comme Scheme via miniKanren montre élégamment comment la programmation logique peut modéliser la vérification de types comme une "recherche" de solutions, créant un pont entre les mondes dynamique et statique.

  Plus tard, Friedman s'est plongé dans les *types dépendants* – une extension avancée des systèmes de types où les types peuvent dépendre de valeurs à l'exécution (par exemple, une fonction qui n'accepte que des listes de longueur exactement 5). Cela permet des garanties encore plus fortes, comme des preuves intégrées au code, comme dans des langages comme Idris ou Agda. Friedman a co-écrit *The Little Typer* (2018, avec David Thrall), un livre pour débutants qui introduit ces idées à travers un langage simple, de type "typer", reprenant le style de ses livres Schemer mais pour la programmation typée.

Wang a réalisé que Friedman n'était pas dismissif par ignorance ; il *comprenait* les types statiques (y compris le système sophistiqué de Haskell, qui combine Hindley-Milner avec des extensions pour la paresse et les monades) mieux que la plupart de ses partisans. Les critiques de Friedman provenaient du fait qu'il voyait leurs limitations – par exemple, comment ils peuvent compliquer des programmes simples ou échouer à capturer des invariants spécifiques à un domaine sans types dépendants. Cette capacité à "voir au-delà" de l'enthousiasme ambiant conduit à une vision plus nuancée, parfois contrariante.

### Pourquoi c'est important
L'article est un méta-commentaire sur l'expertise dans les langages de programmation : La vraie maîtrise ressemble souvent au scepticisme, et non à l'enthousiasme aveugle. Il fait écho aux débats dans la communauté des langages de programmation (par exemple, les guerres entre typage statique et dynamique). Wang l'utilise pour mettre en garde contre les jugements hâtifs, établissant un parallèle avec la façon dont il voit les autres (et lui-même) réagir aux contrariants aujourd'hui.

Pour une lecture complète, l'article original se trouve sur le blog de Yin Wang : [Article de blog de Yin Wang sur Dan Friedman](http://www.yinwang.org/blah?blog=2019/10/01/dan-friedman). Le travail de Friedman est fondamental – consultez *The Little Schemer* pour les bases de Scheme ou *The Little Typer* pour les types dépendants.