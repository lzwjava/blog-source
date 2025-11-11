---
audio: false
generated: true
lang: fr
layout: post
title: Chiffres de latence
translated: true
type: note
---

### Points Clés
- Il semble probable que la vidéo aborde les temps de latence standards que les programmeurs devraient connaître, d'après son titre et le contenu en ligne associé.
- Les recherches suggèrent que ces chiffres incluent les durées d'opérations comme l'accès au cache L1 (0,5 ns) et les allers-retours réseau (jusqu'à 150 ms), variant selon le matériel.
- Les éléments indiquent que ces chiffres sont approximatifs, avec des mises à jour reflétant les avancées technologiques, notamment pour les SSD et les réseaux.

### Introduction
La vidéo "Latency Numbers Programmer Should Know: Crash Course System Design #1" couvre probablement les chiffres de latence essentiels pour les opérations informatiques, cruciaux pour la conception de systèmes. Ces nombres aident les programmeurs à comprendre l'impact sur les performances et à optimiser les systèmes.

### Les Chiffres de Latence et Leur Importance
La latence est le délai entre le début et la fin d'une opération, comme l'accès à la mémoire ou l'envoi de données sur un réseau. La vidéo liste probablement les latences typiques, telles que :
- Une référence au cache L1 à 0,5 nanosecondes (ns), l'accès mémoire le plus rapide.
- Un aller-retour dans le même datacenter à 500 microsecondes (us) ou 0,5 millisecondes (ms), affectant les systèmes distribués.

Ces chiffres, bien qu'approximatifs, guident les décisions en conception de système, comme le choix entre le stockage en mémoire et sur disque.

### Contexte en Conception de Système
Comprendre ces latences aide à optimiser le code, à faire des compromis et à améliorer l'expérience utilisateur. Par exemple, savoir qu'une recherche sur disque prend 10 ms peut influencer la conception d'une base de données pour minimiser ce type d'opérations.

### Détail Inattendu
Un aspect intéressant est la façon dont ces chiffres, comme les temps de lecture SSD, se sont améliorés avec la technologie, tandis que les latences CPU fondamentales comme l'accès au cache L1 restent stables, montrant un impact inégal de l'évolution du matériel.

---

### Note d'Enquête : Analyse Détaillée des Chiffres de Latence de la Vidéo

Cette note propose une exploration complète des chiffres de latence probablement abordés dans la vidéo "Latency Numbers Programmer Should Know: Crash Course System Design #1", basée sur le contenu en ligne disponible et les ressources associées. L'analyse vise à synthétiser les informations pour les programmeurs et les concepteurs de systèmes, offrant à la fois un résumé et des insights détaillés sur l'importance de ces nombres.

#### Contexte et Arrière-plan
La vidéo, accessible sur [YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0), fait partie d'une série sur la conception de systèmes, se concentrant sur les chiffres de latence critiques pour les programmeurs. La latence, définie comme le délai entre le début et la fin d'une opération, est essentielle pour comprendre les performances d'un système. Étant donné le titre de la vidéo et les recherches associées, elle semble couvrir les chiffres de latence standard popularisés par des figures comme Jeff Dean de Google, souvent référencés dans les communautés de programmation.

Des recherches en ligne ont révélé plusieurs ressources discutant de ces nombres, notamment un Gist GitHub intitulé "Latency Numbers Every Programmer Should Know" ([GitHub Gist](https://gist.github.com/jboner/2841832)) et un article Medium de 2023 ([Article Medium](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)). Ces sources, ainsi qu'un article de High Scalability de 2013 ([High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)), ont fourni une base pour compiler le contenu probable de la vidéo.

#### Compilation des Chiffres de Latence
Sur la base des informations recueillies, le tableau suivant résume les chiffres de latence standard, probablement discutés dans la vidéo, avec des explications pour chaque opération :

| Opération                                      | Latence (ns) | Latence (us) | Latence (ms) | Explication                                                          |
|------------------------------------------------|--------------|--------------|--------------|----------------------------------------------------------------------|
| Référence cache L1                            | 0,5          | -            | -            | Accès aux données dans le cache de niveau 1, la mémoire la plus rapide près du CPU. |
| Erreur de prédiction de branche                | 5            | -            | -            | Pénalité lorsque le CPU prédit incorrectement une branche conditionnelle. |
| Référence cache L2                            | 7            | -            | -            | Accès aux données dans le cache de niveau 2, plus grand que L1 mais plus lent. |
| Verrouillage/déverrouillage mutex              | 25           | -            | -            | Temps pour acquérir et relâcher un mutex dans les programmes multithreadés. |
| Référence mémoire principale                   | 100          | -            | -            | Accès aux données depuis la mémoire vive principale (RAM). |
| Compresser 1 Ko avec Zippy                     | 10 000       | 10           | -            | Temps pour compresser 1 kilooctet en utilisant l'algorithme Zippy. |
| Envoyer 1 Ko sur un réseau 1 Gbps              | 10 000       | 10           | -            | Temps pour transmettre 1 kilooctet sur un réseau de 1 Gigabit par seconde. |
| Lecture aléatoire de 4 Ko depuis un SSD        | 150 000      | 150          | -            | Lecture aléatoire de 4 kilooctets depuis un disque SSD. |
| Lecture séquentielle de 1 Mo depuis la mémoire | 250 000      | 250          | -            | Lecture séquentielle de 1 mégaoctet depuis la mémoire principale. |
| Aller-retour dans le même datacenter           | 500 000      | 500          | 0,5          | Temps d'aller-retour réseau dans le même datacenter. |
| Lecture séquentielle de 1 Mo depuis un SSD     | 1 000 000    | 1 000        | 1            | Lecture séquentielle de 1 mégaoctet depuis un SSD. |
| Seek HDD                                       | 10 000 000   | 10 000       | 10           | Temps pour qu'un disque dur se positionne sur une nouvelle piste. |
| Lecture séquentielle de 1 Mo depuis le disque  | 20 000 000   | 20 000       | 20           | Lecture séquentielle de 1 mégaoctet depuis un HDD. |
| Envoi paquet CA->Pays-Bas->CA                  | 150 000 000  | 150 000      | 150          | Temps d'aller-retour pour un paquet réseau de Californie aux Pays-Bas. |

Ces chiffres, principalement de 2012 avec quelques mises à jour, reflètent les performances typiques du matériel, avec des variations notées dans les discussions récentes, notamment pour les SSD et les réseaux en raison des avancées technologiques.

#### Analyse et Implications
Les chiffres de latence ne sont pas fixes et peuvent varier selon le matériel et les configurations spécifiques. Par exemple, un article de blog de 2020 par Ivan Pesin ([Espace Pesin](http://pesin.space/posts/2020-09-22-latencies/)) a noté que les latences disque et réseau se sont améliorées grâce aux meilleurs SSD (NVMe) et aux réseaux plus rapides (10/100 Gb), mais les latences CPU fondamentales comme l'accès au cache L1 restent stables. Cette évolution inégale souligne l'importance du contexte en conception de système.

En pratique, ces chiffres guident plusieurs aspects :
- **Optimisation des Performances** : Minimiser les opérations à haute latence, comme les seeks disque (10 ms), peut améliorer significativement la vitesse des applications. Par exemple, mettre en cache les données fréquemment accédées en mémoire (250 us pour une lecture de 1 Mo) plutôt que sur disque peut réduire les temps d'attente.
- **Décisions de Compromis** : Les concepteurs de systèmes font souvent face à des choix, comme utiliser des caches en mémoire plutôt que des bases de données. Savoir qu'une référence mémoire principale (100 ns) est 200 fois plus rapide qu'une référence cache L1 (0,5 ns) peut éclairer de telles décisions.
- **Expérience Utilisateur** : Dans les applications web, les latences réseau, comme un aller-retour dans un datacenter (500 us), peuvent affecter les temps de chargement des pages, impactant la satisfaction utilisateur. Un article de blog Vercel de 2024 ([Blog Vercel](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)) a souligné ce point pour le développement frontend, notant comment les cascades réseau peuvent amplifier la latence.

#### Contexte Historique et Mises à Jour
Les chiffres originaux, attribués à Jeff Dean et popularisés par Peter Norvig, datent d'environ 2010, avec des mises à jour par des chercheurs comme Colin Scott ([Latences Interactives](https://colin-scott.github.io/personal_website/research/interactive_latency.html)). Un article Medium de 2019 par Dan Hon ([Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)) a ajouté des latences humoristiques mais pertinentes, comme le redémarrage d'un MacBook Pro (90 secondes), illustrant des délais plus larges liés à la technologie. Cependant, les chiffres de latence fondamentaux ont connu des changements minimes, le Gist GitHub suggérant qu'ils restent "assez similaires" en 2023, en raison de limitations physiques.

#### Conclusion et Recommandations
Pour les programmeurs et concepteurs de systèmes, mémoriser ces chiffres de latence fournit un modèle mental pour le réglage des performances. Ils doivent être traités comme des lignes directrices, avec des benchmarks réels effectués pour le matériel spécifique. Se tenir informé des mises à jour, surtout dans les technologies émergentes comme l'informatique quantique ou les réseaux 5G, sera crucial. Des ressources comme le Gist GitHub et l'article Medium offrent des points de départ pour une exploration plus poussée.

Cette analyse, fondée sur le contenu probable de la vidéo et complétée par une recherche en ligne extensive, souligne la pertinence durable des chiffres de latence en informatique, avec un appel à s'adapter aux changements technologiques pour une conception de système optimale.

#### Citations Clés
- [Latency Numbers Every Programmer Should Know GitHub Gist](https://gist.github.com/jboner/2841832)
- [Latency Numbers Programmer Should Know YouTube Video](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [Updated Latency Numbers Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [More Numbers Every Awesome Programmer Must Know High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [Latency Numbers Every Web Developer Should Know Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [Latency Numbers Every Engineer Should Know Pesin Space Blog](http://pesin.space/posts/2020-09-22-latencies/)
- [More Latency Numbers Every Programmer Should Know Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [Numbers Every Programmer Should Know By Year Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)