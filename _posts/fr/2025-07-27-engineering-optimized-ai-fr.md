---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Optimiser l'ingénierie logicielle pour l'IA
translated: true
type: post
---

### Table des matières

1. [Optimisation de l'ingénierie logicielle pour l'IA](#optimizing-software-engineering-for-ai)
    - Architecture plate pour le développement axé sur l'IA
    - Avantages de Python dans les flux de travail pilotés par l'IA
    - Ingénierie de contexte et optimisation des tokens
    - Structuration du code pour l'assistance par l'IA

2. [Prospérer en tant qu'agent manuel d'IA](#thriving-as-a-manual-ai-agent)
    - Travail avec les outils d'IA dans les environnements d'entreprise
    - Sélection d'outils et gestion du contexte
    - Construction de systèmes de prompts réutilisables

3. [Exploiter Python pour le développement Java](#leveraging-python-for-java-development)
    - Scripts Python pour le support des projets Java
    - Stratégies de développement multi-langages
    - Génération de code assistée par l'IA

4. [Les langages de programmation à l'ère de l'IA](#programming-languages-in-the-ai-era)
    - Avenir de Python, Rust et Java
    - Performance vs. simplicité
    - Évolution des langages et intégration de l'IA

### Optimisation de l'ingénierie logicielle pour l'IA

Dans ce blog, j'ai utilisé des centaines de scripts pour aider à la traduction, au playground, à la maintenance des métadonnées et aux bots Telegram. Je pense que cette approche de développement pourrait représenter l'avenir de l'ingénierie logicielle optimisée pour l'IA.

Je ne m'appuie pas beaucoup sur les fonctionnalités des modules Python, ni ne souhaite structurer le code comme un grand projet Java Spring.

J'ai travaillé sur de nombreux projets logiciels tout au long de ma carrière. J'ai observé des architectures bancaires impressionnantes, des microservices, des conceptions multi-pays efficaces qui minimisent la duplication, des frameworks fondamentaux robustes construits sur Spring, et une gouvernance solide avec une configuration centralisée.

Bien que ces architectures bancaires soient impressionnantes, si nous devions commencer aujourd'hui, je considérerais optimiser pour les LLM et l'IA. Cela impliquerait une meilleure ingénierie de contexte, une séparation des préoccupations améliorée, et la priorisation de la pensée axée sur l'IA plutôt que sur la conception centrée sur l'humain. Bien que Spring offre plusieurs couches et une bonne abstraction, il peut être difficile pour les LLM et l'IA de naviguer.

Je pense que nous devrions viser des structures plus plates, similaires à une organisation plate. Cela signifie utiliser seulement deux niveaux : le premier niveau appelle le deuxième niveau. Dans une fonction, il est préférable d'appeler directement 50 autres fonctions plutôt que d'avoir 50 niveaux imbriqués ou des piles. Les IA/LLM ont du mal à juger ou à inférer des structures complexes et imbriquées, mais elles excellent à gérer de petites fonctions de 100 à 200 lignes de code. Python est bien adapté pour appeler et importer d'autres fichiers.

Une raison pour laquelle le code Python est plus facile que Java est que sa gestion des dépendances est simple. Il suffit d'utiliser `pip install` pour ajouter une dépendance. Avec Maven, il faut écrire la dépendance dans un fichier POM XML, puis utiliser `mvn compile` pour que Maven télécharge les dépendances.

Une autre raison de la simplicité de Python est que son code peut être exécuté directement sans problème.

Bien que depuis Java 11, la commande `java` puisse exécuter directement des programmes à source unique sans avoir besoin de les compiler séparément avec `javac`. Cependant, souvent pour les projets Java, ils sont volumineux, donc il faut les exécuter avec `mvn spring-boot:run` ainsi que certaines configurations de propriétés.

Une troisième raison est que la conception des modules Python est simple ; vous pouvez utiliser `from` et `import` pour importer facilement du code d'autres fichiers.

Pour l'instant, de nombreux chatbots IA peuvent exécuter du code Python directement dans la fenêtre du chatbot, comme Grok.

Lors de la comparaison de 100 fichiers Java, chacun contenant environ 1000 lignes de code, avec quelques scripts Python simples, ce n'est pas une comparaison équitable. Pour ce type de projet, je préférerais avoir 1000 fichiers Python, chacun contenant environ 100 lignes de code.

Il est acceptable de sélectionner des lignes de code ou une fonction à modifier. Cependant, il faut savoir où sélectionner. Pourquoi ne pas laisser cette tâche être gérée par l'IA pour faciliter notre vie ? Donc, il suffit d'utiliser "sélectionner tout" pour sélectionner tout le code et dire à l'IA/LLM comment le modifier.

Pour Python, il est plus facile d'utiliser `if __name__ == "__main__":` pour exécuter et tester des fonctions dans un fichier. Il est également plus facile pour d'autres fichiers Python d'appeler les fonctions à l'intérieur de ce fichier sans avoir besoin d'exécuter le test.

C'est l'ingénierie de contexte optimisée pour l'IA. Pourrions-nous l'aborder autrement ? L'IA/LLM est auto-régressive. Cependant, lorsque nous utilisons Copilot ou Claude Code, nous ne savons pas comment l'Agent Logiciel IA nous aide. Ils devraient y penser à notre place.

Pourrions-nous, du côté utilisateur, organiser le code spécifiquement pour réduire l'utilisation des tokens ? Pour ce point, l'approche consistant à avoir 1000 fichiers Python avec chacun 100 lignes de code est bonne à cet effet. Parce que vous pouvez vérifier les fonctions et les fichiers de code facilement avant de laisser d'autres codes Python les appeler.

Mais un problème est que si vous voulez modifier plusieurs fichiers de code ensemble, ce n'est pas facile à faire. Pour une méthode simple, vous pouvez copier le code dans les chatbots IA et les laisser vous dire comment modifier le code dans ces fichiers.

Possiblement, nous n'avons pas besoin d'utiliser le nombre de lignes pour séparer les fonctions ou la logique. Mais nous devrions le faire pour séparer la logique en petites fonctions. Nous pouvons le faire en les séparant naturellement par type de logique, afin qu'elles paraissent plus courtes.

Pourquoi voulons-nous une ingénierie logicielle optimisée pour l'IA ? Parce que l'IA est puissante, nous devrions optimiser tout pour l'IA et ensuite laisser l'IA aider l'ingénierie logicielle autant que possible.

Cela est possible non seulement pour le code, mais aussi pour tout texte. Supposons que nous soyons des éditeurs très pointilleux ; nous ne voulons pas que l'IA édite nos grands textes d'un seul coup. Nous voulons vérifier paragraphe par paragraphe. Pour le code, nous pouvons tolérer de petites erreurs ou bugs. Pour le texte, nous pouvons les tolérer car la plupart des lecteurs ne sont pas si pointilleux.

Mais le code est différent en ce sens que parfois, même une petite erreur peut entraîner le dysfonctionnement complet d'un grand projet.

Pour les fichiers XML ou YAML, nous n'avons probablement pas besoin de les séparer autant car ils sont déjà très structurés.

Et pour les fichiers HTML, nous devrions faire une certaine séparation. Au lieu d'écrire des centaines de fichiers JavaScript avec des centaines de fichiers HTML, ce qui rend facile de dépasser 1000 lignes de code, nous devrions utiliser `import` pour JavaScript pour gérer cela. Pour le code JavaScript, nous pouvons utiliser les méthodes ci-dessus pour séparer.

Nous voulons structurer le code de manière à ce que l'IA puisse facilement nous aider à ajouter, modifier, supprimer et exécuter du code. C'est le début. Imaginez un jour où tout le code peut être généré ou corrigé facilement par l'IA. Le monde sera très numérisé.

Imaginez-moi écrivant 100 grands projets logiciels et fournissant des API pour se connecter avec les autres. Cela inclut mon agenda quotidien ; je suis moi-même comme une entreprise technologique de 1000 employés de nos jours. Ils sont personnalisés pour mes besoins, pour gagner de l'argent ou dépenser de l'argent pour mon bénéfice. C'est vraiment incroyable.

### Prospérer en tant qu'agent manuel d'IA

Les Agents IA doivent être exécutés automatiquement avec du code. Maintenant, le titre de cet essai est "Agent manuel d'IA". Vous pourriez penser que je plaisante, mais ce n'est pas le cas.

La raison pour laquelle je dis "agent manuel d'IA" est que pour les grandes entreprises, l'adoption technologique est lente en raison des préoccupations de sécurité des données et des considérations à long terme.

Il y a beaucoup de nouvelles technologies sur le marché ; qui sait ce qui va durer ou ce qui va disparaître rapidement.

Ils ont également des préoccupations de sécurité des données. Typiquement, ils veulent s'associer avec de grandes marques dont les politiques de données sont strictes et surveillées par le public. C'est pourquoi Microsoft est devenu un partenaire de premier plan parmi les entreprises du Fortune 500. D'autres entreprises utilisent leurs Teams, Microsoft Office 365, Azure et Copilot.

Cependant, que se passe-t-il si les grandes entreprises ne fournissent pas à leurs employés des API LLM à utiliser ? Nous devons réfléchir à la manière de travailler en tant qu'agents manuels d'IA.

Cela signifie que nous utiliserons beaucoup d'outils pour travailler, de manière similaire à l'utilisation d'outils ou à l'appel de fonctions dans ces API. Nous ferons notre propre ingénierie de prompts ou d'ingénierie de contexte.

Au lieu d'utiliser Claude Code ou Manus pour effectuer une tâche complexe, nous pouvons effectuer nous-mêmes les tâches avec un simple chatbot IA.

AspectJ est bon car il utilise la programmation AOP pour intercepter les méthodes. Les filtres dans Spring sont également bons pour capturer les journaux des requêtes HTTP. Le logger dans Log4j est bon pour rediriger des journaux spécifiques vers un fichier. IntelliJ IDEA est bon car il a une fonction pour exporter des objets sous forme de texte.

Les clients SQL sont bons car ils peuvent facilement exporter des fichiers CSV ou Excel de lignes. Git diff est bon car il peut vous donner du texte de comparaison.

Ils vous aident tous à fournir un meilleur contexte pour les chatbots IA. Et les chatbots IA peuvent également aider beaucoup de scripts Python à effectuer des tâches.

Pour être un agent IA efficace, vous devez utiliser de nombreux outils efficaces pour vous aider à effectuer des tâches, qu'elles soient simples ou complexes.

Sans API pour les chatbots LLM/IA, vous devez copier le texte dans les chatbots. C'est un peu plus fastidieux que d'appeler directement l'IA, mais la bonne nouvelle est que vous pouvez sélectionner le contexte ou les prompts plus soigneusement.

Ainsi, vous n'avez pas besoin de demander aux chatbots IA autant de fois que les agents IA automatiques. Vous pouvez soigneusement sélectionner les outils que vous allez utiliser.

Travailler comme un agent manuel d'IA a donc ses avantages. Cependant, la technologie des agents IA évolue rapidement et montre son potentiel au monde.

Si elles sont très utiles, les grandes entreprises les adopteront tout comme les chatbots IA. Sinon, elles ne pourront pas rivaliser avec les entreprises qui les ont adoptées—pas seulement les autres grandes entreprises, mais aussi les petites startups. Parce que l'IA est si puissante maintenant, une startup avec une dizaine d'employés peut battre celles qui en ont 1 000.

Travailler comme des agents manuels d'IA est parfois inévitable. Le travail a d'autres avantages en plus de manquer de technologie IA avancée. Ce n'est pas facile de trouver de bons emplois non plus. Donc, dans ce cas, cela nous donne de l'espace pour utiliser notre sagesse traditionnelle pour tirer le meilleur parti des chatbots IA.

Et cela signifie que nous pouvons organiser et accumuler nos prompts pour créer des prompts système pour les chatbots IA, similaires à ceux utilisés par Claude ou Grok qui ont été exposés. Ainsi, nous n'avons pas besoin d'écrire des prompts à répétition. Nous pouvons utiliser des scripts Python pour nous aider à écrire des prompts. Nous pouvons obtenir les journaux des requêtes HTTP et écrire des prompts pour générer des cas de test d'API.

La magie de la programmation réside dans ses niveaux illimités d'abstraction. C'est similaire aux fonctions où vous pouvez avoir 100 niveaux d'appels de fonctions. Par exemple, WeChat est construit sur iOS, et les Mini Programmes WeChat sont construits sur WeChat. iOS lui-même est construit sur Objective-C ou Swift, qui à leur tour sont construits sur LLVM et le jeu d'instructions des puces ARM d'Apple.

### Exploiter Python pour le développement Java

Comment utiliser Python pour aider au développement Java à l'ère de l'IA ? J'aime Python. J'ai travaillé avec Python le plus au cours des trois dernières années, depuis la sortie de ChatGPT à la fin de novembre 2022.

Une façon d'aider est d'utiliser Python pour écrire des scripts d'aide SQL, des scripts de test et des scripts de recherche de logs pour les projets Java.

Utilisez Python pour analyser les fichiers POM et les dépendances de paquets pour Java. Utilisez Python pour vérifier la cohérence des données dans Java. Il y a beaucoup de choses que nous pouvons faire en Python au lieu de Java.

Mais Java n'a pas PyTorch. Python peut aider à tout en 200 lignes de code qui prendraient 500 lignes en Java. Mais en utilisant les outils d'IA, vous ne pouvez pas facilement obtenir votre propre version de PyTorch non plus. Même quelque chose comme TinyGrad prend du temps à construire.

Pourquoi écrire nos propres scripts en premier ? Une raison est qu'ils sont super personnalisables. Il n'y a pas de logiciels publics ou de projets open source qui peuvent nous aider directement dans nos projets, surtout ceux des grandes entreprises.

Les grands projets des grandes entreprises sont développés sur une décennie ou plus. Ils ont déjà beaucoup de personnalisation.

Donc, à l'avenir, il y aura beaucoup de projets autour des grands projets des grandes entreprises. Il y aura plus de routeurs de code similaires à Claude dans les outils d'agents de codage internes des grandes entreprises. Il y aura plus de Postman, de clients SQL et de compilateurs personnalisés pour les grandes entreprises.

Le code Python peut également se connecter aux agents Java.

Cela signifie que je dois bien apprendre Python et Java, afin de savoir comment utiliser l'un pour aider l'autre.

Et je peux utiliser Python avec l'aide de l'IA pour créer beaucoup de choses pour moi-même et dans les projets d'entreprise également. Java ne semble pas être un obstacle. Java, avec Spring, les bases de données et Angular, Vue ou React servant de frontend, ne devrait pas être un obstacle pour que Python aide beaucoup.

La programmation est une chose si flexible. La limite est notre imagination.

Donc, l'IA se développe rapidement. Nous pouvons mesurer les progrès de l'IA par la quantité et la facilité avec laquelle nous pouvons utiliser le code pour réaliser des choses avec l'aide de l'IA en codage et en apprentissage.

Pourrions-nous un jour écrire certains agents IA, et ensuite ces agents aideraient à créer un entier TikTok, y compris ses nombreux microservices et grands projets iOS ou Android ?

Si l'IA est si puissante, que devons-nous faire aujourd'hui ? Probablement rien, car ce que nous faisons aujourd'hui sera facile à mettre en œuvre avec l'IA. En 2025, notre travail d'un an avec l'aide de l'IA pourra probablement être fait en un mois avec la capacité de l'IA de 2030.

Cela soulève notre question essentielle : Quel est le but de notre vie ? De quoi s'agit-il ? Comment vivre une bonne vie ?

L'IA sort comme d'autres technologies pour nous apporter la liberté. Mais il semble que tout le monde soit occupé comme une machine dans cette société capitaliste.

Revenons au sujet. Donc, Python peut aider à écrire du code Java également. Vous pouvez utiliser Python pour obtenir le contexte pour écrire du code et laisser Copilot l'écrire pour vous afin de le faire du premier coup.

L'IA concerne l'ingénierie des prompts et l'ingénierie du contexte. Les prompts et le contexte aident les réponses des chatbots IA.

Python peut aider avec le contexte ; Python peut aider à générer des prompts.

Donc, cela ne concerne pas seulement Java, mais tous les autres langages de programmation. Python peut les aider en profondeur. Alors, pourquoi avons-nous encore besoin d'utiliser d'autres langages de programmation ?

C'est le design intrinsèque de Python qui le rend moins performant que d'autres langages de programmation, comme C, C++ ou Rust.

### Les langages de programmation à l'ère de l'IA

L'IA est si puissante maintenant que nous devons repenser tout du point de vue de l'IA. Quels langages de programmation seront populaires dans les 10 prochaines années ?

Python le sera sûrement. De nombreux chatbots IA utilisent Python pour exécuter du code dans le navigateur, comme Grok. Python est populaire pour sa simplicité, sa facilité d'apprentissage et ses performances décentes. Il est adopté par de nombreux projets logiciels.

Python est plus lent que C++, Java et Rust. Java a une grande communauté. Rust est construit sur C.

Je me demande si de nombreux projets seront réécrits ou remplacés par Rust. Être réécrit en Rust signifie se référer à un ancien projet et utiliser Rust pour implémenter la même fonctionnalité. Être remplacé signifie que le logiciel écrit dans d'autres langages est maintenant remplacé par un logiciel similaire écrit en Rust.

Rust a une syntaxe relativement complexe. Mais à l'ère de l'IA, ce n'est pas un gros problème, car l'IA aidera à écrire le code. Pour la syntaxe complexe, les humains n'ont pas vraiment de problème non plus.

Je pense que l'hindi ou le tamoul sont assez complexes. Mais pour les Indiens qui vivent dans le Nord, l'hindi n'est pas un problème, et pour ceux du Sud, le tamoul n'est pas un problème non plus.

Mais pour un citoyen chinois comme moi, je pense que c'est un gros problème à apprendre.

À première vue, tous les caractères en hindi me semblent similaires. Je pense que la différence entre l'hindi et l'arabe est comme la différence entre le chinois et le japonais, ou l'anglais et l'espagnol.

Les différences entre les langages de programmation sont moins grandes que celles entre les langues naturelles. Une grande raison est que les langages de programmation ne diffèrent que par l'apparence des caractères, tandis que les langues naturelles diffèrent également par le son. Les langues naturelles diffèrent en deux aspects : le jeu de caractères et la prononciation.

Les langages de programmation n'ont qu'environ un siècle d'histoire, mais les langues naturelles en ont plus de 100 siècles. Plus les gens passent de temps sur quelque chose, plus les différences se développent. Les personnes ayant des opinions légèrement différentes créeront leurs propres versions de choses.

Cela explique l'accent anglais. Dans certaines vidéos TikTok, les gens disent que le pire accent anglais est celui de Birmingham.

Donc, en fait, Rust n'a pas beaucoup de problèmes. Ses performances sont assez bonnes, car il est construit sur C/C++.

Les performances sont critiques pour de nombreuses applications. De nos jours, de nombreuses applications sont utilisées par des milliards de personnes. Pour l'infrastructure informatique en nuage sous-jacente, leurs services sont appelés de nombreuses fois. Donc, même un petit gain de performance peut économiser beaucoup d'argent.

Rust a-t-il beaucoup d'inconvénients ? Une chose dont les gens se plaignent est qu'il est difficile à apprendre. La courbe d'apprentissage est raide. L'IA apporte de bonnes nouvelles, car elle aide beaucoup à l'apprentissage.

Je n'ai pas besoin de connaître beaucoup de choses sur Rust. En tant qu'ingénieur logiciel avec 10 ans d'expérience, je peux utiliser l'IA pour aider à écrire de nombreuses applications Rust simples. Il me suffit de connaître les commandes de compilation de base de Rust comme `cargo` et `cargo build`. Je n'ai même pas besoin de connaître beaucoup la syntaxe de Rust elle-même.

Pour Rust, le modèle de mutabilité ou d'emprunt ne me pose pas de problème. Pour des applications simples de moins de 200 lignes de code, je peux demander à l'IA de corriger directement les erreurs en fournissant les messages d'erreur.

Mais pourquoi les gens utilisent-ils encore beaucoup Python si Rust est si bon ? Parce que Python est bon dans un autre aspect. Il est très facile à utiliser et à apprendre. Il a une grande communauté et de nombreuses bibliothèques.

Python a encore de bonnes performances et peut supporter des produits pour des millions, voire des dizaines de millions, d'utilisateurs. La plupart des produits n'ont pas autant d'utilisateurs. Si vous en avez autant, vous pouvez embaucher des programmeurs Rust ou Java pour optimiser les performances.

Python est bon pour beaucoup de développement : apprentissage automatique, développement web, mathématiques, enseignement et scriptage. Bien que Python ne soit pas bon pour les applications de bureau, MicroPython est utilisé dans Raspberry Pi.

Et Java à l'ère de l'IA ? Ce sera aussi bon, car il a une grande base d'utilisateurs et une communauté. L'IA aide beaucoup à cela. Il est utilisé par de nombreuses grandes entreprises. Elles ont tendance à ne pas changer leurs langages de programmation principaux. Pour certains de leurs grands projets hérités, utiliser un nouveau langage de programmation pour réécrire un projet prendrait une décennie d'effort. L'IA aidera à cela, mais le processus sera toujours lent.

Souvent, les personnes rationnelles dans les grandes entreprises ne considéreront pas changer leur langage de programmation principal. Leur activité principale est dans d'autres secteurs. Ils ne se soucient pas beaucoup de la technologie. Si c'était le cas, ils deviendraient des entreprises logicielles ou Internet et mèneraient dans les communautés open source. Cependant, peu d'entreprises du Fortune 500 se soucient de cela.

Il y aura beaucoup de startups grâce à l'IA. Les startups aiment faire de nouvelles choses, donc elles essayeront de nouveaux langages de programmation. À l'ère de l'IA, les langages de programmation agiles gagneront dans les petites et moyennes entreprises.

Dans les compétitions d'algorithmes, le langage de programmation favori changera-t-il ? C++ a dominé ce secteur depuis des décennies. Dans les compétitions d'algorithmes réelles, vous ne pouvez pas utiliser l'IA. Mais je pense que dans l'ère de l'IA, moins de personnes participeront.

Étant donné que ces personnes sont très douées en programmation, et qu'il y a tant d'opportunités grâce à l'IA, pourquoi ne pas en profiter pour construire des produits réels pour les utilisateurs au lieu de pratiquer des problèmes d'algorithmes ? Même le GOAT des compétitions d'algorithmes, Gennady Korotkevich, a choisi de rejoindre Devin.

Mais les compétitions d'algorithmes peuvent être un passe-temps relaxant ou de retraite pour les programmeurs intelligents. C'est comme les échecs ou le basket. Les gens le font parce qu'ils aiment ça ou en ont besoin, pas pour d'autres raisons. Beaucoup de gens jouent au basket dans la trentaine ou la quarantaine. Ils le font probablement pour des raisons de santé ou pour rendre la vie plus amusante.

Pour iOS et Android, il s'agit de Java, Kotlin, Swift et Objective-C. Il n'y aura pas de changements significatifs dus à l'IA, car il y a peu de choix. Du côté de l'utilisateur final, les exigences de performance ne sont pas si élevées. Google et Apple ont un contrôle très strict sur leurs plateformes. Si Google et Apple ne changent pas, les programmeurs ne changeront pas.

Mais pour les serveurs, il y a beaucoup de choix. Les langages plus amicaux pour l'IA gagneront.

Les langages de programmation procéduraux gagneront plus que les langages orientés objet. Les langages procéduraux sont directs et faciles à générer par l'IA, tandis que les langages OOP ont de nombreux niveaux imbriqués ou motifs de conception.

Y aura-t-il plus de langages de programmation à cause de l'IA ? Je pense que oui. Zed et OCaml auront plus d'utilisateurs. Les LLM/IA sont très bons pour apprendre les motifs, donc il est facile de réécrire des projets dans d'autres langages.

Les langages de programmation feront face à plus de concurrence à l'avenir. Ceux qui sont bons en performance, syntaxe et qualité du compilateur deviendront intrinsèquement plus populaires. La concurrence est similaire à celle des LLM. Ceux qui sont intrinsèquement bons, comme Claude et DeepSeek, deviennent populaires.

Et si l'IA devient si puissante que nous n'avons plus besoin d'apprendre la programmation ? Cela reste encore loin. Supposons que nous ayons un très grand projet avec 1 000 fichiers Java. L'IA aurait probablement besoin de 10 ans pour effectuer facilement des tâches sur celui-ci.