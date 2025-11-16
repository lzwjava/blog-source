---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Histoire sceptique de Rust
translated: true
type: note
---

### Traduction et explication de l'article  
Titre : « L'histoire de Rust telle que je l'ai vécue »

Il s'agit d'une longue réflexion personnelle et assez critique écrite par un programmeur expérimenté (probablement taïwanais, publiant en chinois) sur sa première rencontre avec Rust et sur les raisons pour lesquelles, malgré sa popularité actuelle, il reste profondément sceptique à son égard – à la fois sur les plans technique et culturel.

#### Première rencontre (2009, Université de l'Indiana)
- Alors qu'il étudiait à l'Université de l'Indiana (IU), l'auteur avait deux camarades de classe (non spécialisés en informatique au premier cycle) qui éprouvaient de grandes difficultés dans le cours avancé de langages de programmation de Dan Friedman.
- Ces camarades étaient du genre à « avoir la langue bien pendue » mais sans vraiment comprendre les concepts profonds. Pourtant, ils étaient doués pour le réseautage et l'autopromotion.
- Durant l'été 2009, ces deux camarades ont effectué un stage chez Mozilla Research et ont travaillé sur une version précoce du langage Rust (il s'agissait probablement du projet personnel de Graydon Hoare que Mozilla a adopté par la suite ; les camarades étaient probablement des contributeurs très précoces ou des stagiaires d'été sur le projet).
- À la fin de l'été, ils ont donné une conférence universitaire pour présenter Rust à tous. Ce fut la toute première exposition de l'auteur au langage.

#### La conférence de 2009 (la première impression de l'auteur)
- La conférence était du pur marketing : de grands slogans, presque aucune substance technique.
- Ils ont montré une diapositive avec un triangle présentant « les trois grandes caractéristiques de Rust » – l'une était la « sécurité », l'auteur a oublié les deux autres.
- L'affirmation choc : Rust devait réaliser une gestion de la mémoire entièrement sûre par le biais de la seule analyse statique, sans aucun garbage collection (pas de GC du tout).
- L'auteur est parti en pensant : « C'est juste du battage publicitaire de Mozilla. Ils ne livreront jamais un navigateur avec. Ça mourra comme tous leurs autres projets de recherche. » (Il mentionne spécifiquement DrServ/DrJS comme un autre projet de recherche de Mozilla qui n'a abouti à rien.)

#### Doutes concernant le concepteur et le choix du bootstrap
- L'auteur remet en question la profondeur des connaissances de Graydon Hoare (le créateur original) en théorie des langages de programmation.
- En particulier, il pense que le choix d'OCaml comme premier langage d'implémentation a montré un manque de goût ou de compréhension profonde (une opinion controversée mais pas rare parmi certains vétérans des langages de programmation qui n'aiment pas les particularités d'OCaml).

#### Développements ultérieurs
- L'un de ces camarades a ensuite lancé un projet de doctorat sur un langage GPU « généraliste » qui prétendait permettre de construire des arbres, des graphes, etc. sur les GPU. L'auteur pensait que c'était voué à l'échec car les GPU sont conçus pour des charges de travail à parallélisme de données, et non pour des structures arbitraires avec de nombreux pointeurs. Le projet n'est effectivement jamais devenu pratique, mais le camarade a tout de même obtenu son doctorat et travaille maintenant sur le compilateur Rust dans une grande entreprise technologique.

#### Le parcours personnel de l'auteur avec la gestion de la mémoire
- L'auteur était personnellement fasciné par l'idée d'une sécurité mémoire 100% statique sans GC (exactement le pitch original de Rust).
- Il a passé beaucoup de temps à concevoir des modèles de mémoire et des analyses statiques pour tenter de réaliser ce rêve.
- Un jour, il a parlé de son idée à son directeur de thèse, Kent Dybvig (l'auteur légendaire de Chez Scheme). Kent a calmement répondu :
  « Une gestion de la mémoire entièrement statique – est-ce même possible ? La gestion de la mémoire est intrinsèquement un processus dynamique. »
- Cette seule phrase a brisé les illusions de l'auteur. Il a réalisé qu'un garbage collection précis est indécidable dans le cas général (lié au problème de l'arrêt).
- Lorsqu'il a suggéré le comptage de références à la place, Kent a fait remarquer que le ref-counting a un coût élevé et performe souvent moins bien qu'un bon GC générationnel. Les pauses d'un bon GC ne sont pas un vrai problème si le collecteur est bien conçu (Chez Scheme le prouve).

#### Chez Scheme comme contre-exemple
- L'auteur respecte profondément Kent Dybvig et Chez Scheme :
  - Compilation extrêmement rapide
  - GC hautement réglable et à faibles pauses
  - Philosophie : ne perdez pas de temps à optimiser du code stupide ; supposez que le programmeur est compétent ; choisissez les bonnes abstractions simples.
- En d'autres termes, la sagesse > la sophistication brutale.

#### Ce qu'est réellement devenu Rust
- Le rêve originel d'une « gestion de la mémoire purement statique, jamais de GC » est mort.
- Le Rust moderne comprend :
  - `Rc<T>` / `Arc<T>` (comptage de références avec collecte de cycles via `Weak`)
  - Le code `unsafe` (obligatoire pour de nombreuses bibliothèques du monde réel : piles réseau, navigateurs, noyaux de système d'exploitation, etc.)
  - Des recherches continues pour tenter de sécuriser certaines parties du code `unsafe` (Stacked Borrows, Tree Borrows, etc.), mais chaque nouveau modèle ajoute à nouveau des restrictions.
- Pourtant, le marketing et la communauté répètent toujours le mantra des « fortes garanties statiques » et de la « concurrence sans crainte ».
- Lorsque vous soulignez les lacunes, la réponse officielle devient « c'est juste la philosophie de Rust » ou « vous ne comprenez pas le borrow checker ».

#### La position actuelle de l'auteur
- Il comprend parfaitement les durées de vie, l'emprunt, etc., et a même enseigné des cours avancés sur Rust où les étudiants implémentaient des interpréteurs de langages fonctionnels en Rust.
- Mais plus il enseigne Rust, plus il apprécie le C++ :
  - Les pointeurs intelligents du C++ + RAII sont plus simples et plus expressifs pour de nombreuses tâches.
  - Lorsqu'il a vraiment besoin de performances maximales, il choisira toujours le C/C++ plutôt que Rust.
- Il trouve les messages d'erreur de Rust notoirement difficiles à déchiffrer, et le besoin constant de lutter contre le borrow checker est agaçant.
- La défense par la « philosophie » ressemble à une excuse religieuse pour des compromis de conception.

#### Conclusion
L'auteur considère le succès du Rust moderne comme étant largement un triomphe du marketing et de l'élan de l'écosystème, et non comme une preuve que ses idées fondamentales étaient intrinsèquement plus solides que des décennies d'œuvres antérieures (systèmes de régions, Cyclone, types linéaires, GC haute performance, etc.). Il estime que les affirmations grandioses originales étaient naïves, que les compromis étaient inévitables et que la communauté se cache maintenant derrière la « philosophie » lorsqu'elle est confrontée aux lacunes.

C'est une critique rare, de type initié, de la part de quelqu'un qui :
1. a vu Rust littéralement à sa naissance,
2. a lui-même profondément étudié la sécurité mémoire,
3. a eu Kent Dybvig comme mentor,
4. choisit toujours le C/C++ en 2025 malgré le battage médiatique.

Que vous soyez d'accord ou non, c'est un contre-récit réfléchi face au discours dominant selon lequel « Rust est le futur qui est déjà arrivé ».