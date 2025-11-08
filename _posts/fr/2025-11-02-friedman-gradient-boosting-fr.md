---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Jérôme Friedman et le Gradient Boosting
translated: true
type: note
---

### Introduction à Jerome H. Friedman

Jerome Harold Friedman, né le 29 décembre 1939 dans la petite ville de Yreka, en Californie (près de la frontière de l'Oregon), est un statisticien américain pionnier et l'une des figures les plus influentes dans le développement du machine learning moderne et de l'exploration de données. Avec une formation en physique, il a fait le lien entre les méthodes computationnelles de la physique des hautes énergies et la statistique, créant des algorithmes pratiques pour traiter de grands ensembles de données complexes. Son travail met l'accent sur des modèles interprétables et robustes pour la prédiction et la découverte de motifs, influençant des domaines allant des moteurs de recherche à la bio-informatique. Friedman a publié plus de 70 articles, co-écrit des livres fondamentaux comme *Classification and Regression Trees* (CART, 1984) et *The Elements of Statistical Learning* (2001), et a reçu des distinctions prestigieuses, notamment son élection à la National Academy of Sciences (2010), à l'American Academy of Arts and Sciences (2005), et plusieurs prix pour son innovation dans l'exploration de données et les méthodes statistiques.

### L'article fondateur sur le Gradient Boosting (Friedman, 2001)

L'article marquant de Friedman, *"Greedy Function Approximation: A Gradient Boosting Machine"*, publié dans les *Annals of Statistics* en août 2001, a formalisé le gradient boosting comme une méthode d'ensemble polyvalente pour la régression et la classification. S'appuyant sur des idées antérieures de boosting provenant d'informaticiens comme Yoav Freund et Robert Schapire (qui se concentraient sur l'erreur de classification), Friedman l'a étendu à des fonctions de perte arbitraires en utilisant un cadre de "descente de gradient fonctionnel". L'idée centrale : ajouter itérativement des apprenants faibles (souvent des arbres de décision simples) qui s'ajustent au gradient négatif de la perte sur les résidus actuels, minimisant ainsi efficacement les erreurs étape par étape, comme une descente de gradient stochastique dans l'espace des fonctions.

Les innovations clés comprenaient :
- **Shrinkage (taux d'apprentissage)** : Un paramètre de régularisation pour éviter le surapprentissage en mettant à l'échelle chaque nouvel arbre, réduisant la variance sans augmenter le biais.
- **Flexibilité** : Applicable à toute fonction de perte différentiable (par exemple, l'erreur quadratique pour la régression, la log-vraisemblance pour la classification), en faisant un outil généraliste.
- **Interprétation statistique** : En collaboration avec Trevor Hastie et Robert Tibshirani, il a montré que le boosting réduit la corrélation entre les apprenants faibles, améliorant les performances de l'ensemble.

Cet article (présenté comme sa conférence Rietz en 1999) a déclenché une adoption généralisée — les implémentations comme XGBoost et LightGBM dominent aujourd'hui les compétitions Kaggle et l'industrie. Il compte plus de 20 000 citations et a transformé l'apprentissage par ensemble d'une heuristique en une puissance statistiquement fondée.

### Son histoire : Du bricoleur de petite ville au pionnier du Machine Learning

Le parcours de Friedman ressemble à un récit classique de réinvention guidée par la curiosité. Ayant grandi dans une famille d'immigrants ukrainiens — ses grands-parents ont créé une blanchisserie dans les années 1930, reprise par son père et son oncle — il se décrivait lui-même comme un "sous-performant dramatique" au lycée. Peu intéressé par les livres mais obsédé par l'électronique, il construisait des radios amateur, des postes à galène et des émetteurs haute tension, discutant avec des opérateurs radio du monde entier. Le père d'un ami, passionné de radio, l'a encadré, mais son proviseur l'avait averti qu'il échouerait à l'université. Indomptable, il s'est inscrit à Humboldt State (aujourd'hui Cal Poly Humboldt) pour deux années de fête et de sciences de base, puis a été transféré à UC Berkeley en 1959 après avoir négocié avec son père. Là, un excellent professeur de physique l'a accroché ; il a obtenu un A.B. en Physique en 1962 (moyenne B+/A-, un exploit non négligeable avant l'inflation des notes) tout en travaillant à des petits boulots comme pompier et dans la radio.

Son doctorat en physique des hautes énergies a suivi en 1967, se concentrant sur les réactions des mésons dans les chambres à bulles au sein du groupe légendaire de Luis Alvarez au Lawrence Berkeley Lab. Évitant la conscription grâce à un report d'étudiant pendant la guerre du Vietnam, il s'est plongé dans l'informatique — programmant des diagrammes de dispersion sur d'anciennes machines IBM en langage machine et en Fortran. Cela a déclenché un virage : la reconnaissance manuelle de motifs sur pellicule a conduit à des logiciels comme Kiowa (analyse exploratoire des données) et Sage (simulations de Monte Carlo), mêlant physique et statistiques. Après son doctorat, il est resté comme postdoc (1968–1972), mais un remaniement au laboratoire l'a forcé à bouger.

En 1972, il a atterri à la tête du Computation Research Group au Stanford Linear Accelerator Center (SLAC), faisant la navette depuis Berkeley avec sa femme et sa jeune fille. À la tête d'environ 10 programmeurs, il s'attaquait aux graphiques, aux algorithmes et aux outils pour physiciens sur du matériel de pointe. Des congés sabbatiques — comme au CERN (1976–1977), où il a construit un code Monte Carlo adaptatif — l'ont élargi, mais l'intensité du SLAC correspondait à son style. Les conférences Interface l'ont présenté à des géants de la statistique : John Tukey (projection pursuit, 1974), Leo Breiman (collaboration CART, à partir de 1977) et Werner Stuetzle (extensions de la régression).

En 1982, il a rejoint le département de statistiques de Stanford à mi-temps (professeur titulaire en 1984 ; président 1988–1991 ; émérite en 2007), équilibrant la direction du SLAC jusqu'en 2003. Sa recherche en "marche aléatoire" — résolvant des problèmes épineux par le code et l'empirisme — a produit des avancées :
- **Années 1970** : Les arbres k-d pour les plus proches voisins rapides (1977) et la projection pursuit pour repérer des "amas" en haute dimension.
- **Années 1980** : CART (arbres pour la classification/régression) et ACE (transformations non paramétriques, 1985).
- **Années 1990** : MARS (régression adaptative basée sur les splines, 1991) ; critiques des PLS ; chasse aux bosses (PRIM, 1999).
- **Années 2000** : Gradient boosting (2001) ; RuleFit (règles interprétables à partir d'ensembles) ; glmnet (LASSO/elastic net rapide).

Consultant prolifique (par exemple, Google 2011–2014, Yahoo 2004–2005), il a commercialisé des outils comme le logiciel CART, influençant les moteurs de recherche et au-delà. Influencé par l'orientation opérationnelle de Tukey ("dis-moi les étapes") et le pragmatisme de Breiman, Friedman a délaissé la théorie lourde pour des algorithmes élégants et testables. Il a appris les statistiques sur le tas — sans cours formels — se considérant comme un "opportuniste" s'attaquant au chaos de l'exploration de données. Les collaborations avec des étudiants et des collègues "brillants" l'ont alimenté ; il a pris sa retraite de la direction du SLAC en 2006 mais a continué à consulter et à écrire.

### Où est-il maintenant ?

En 2025, à 85 ans, Friedman reste affilié au département de statistiques de l'université de Stanford en tant que professeur émérite, continuant d'influencer le domaine grâce à son héritage et à son travail occasionnel. Son profil Stanford le liste comme un chercheur actif en machine learning, et des mises à jour récentes (par exemple, American Academy of Arts and Sciences, septembre 2025) soulignent sa reconnaissance continue. Aucune indication d'une retraite complète — il est probable qu'il consulte ou mentorne sporadiquement, étant donné son historique. Il réside dans la région de la Baie, fidèle à ses racines californiennes.

**Références**
- [Jerome H. Friedman - Wikipedia](https://en.wikipedia.org/wiki/Jerome_H._Friedman)
- [Jerome H. Friedman | Department of Statistics, Stanford](https://statistics.stanford.edu/people/jerome-h-friedman)
- [A Conversation with Jerry Friedman (arXiv PDF)](https://arxiv.org/pdf/1507.08502)
- [Vita - Jerome H. Friedman (PDF)](https://jerryfriedman.su.domains/ftp/vita.pdf)
- [Jerome H. Friedman | American Academy of Arts and Sciences](https://www.amacad.org/person/jerome-h-friedman)