---
audio: false
generated: true
lang: fr
layout: post
title: GraalVM
translated: true
type: note
---

GraalVM est un **environnement d'exécution polyglotte et haute performance** qui vous permet d'exécuter des applications écrites dans divers langages de programmation comme Java, JavaScript, Python, Ruby, R et des langages basés sur le framework LLVM (comme C et C++) dans un environnement unique. Il est développé par Oracle et est basé sur la Java HotSpot Virtual Machine.

Voici une présentation de ses principales fonctionnalités et avantages :

**1. Polyglottisme :**

* GraalVM permet une interopérabilité transparente entre différents langages de programmation. Vous pouvez intégrer du code écrit dans un langage dans une application écrite dans un autre. Par exemple, vous pouvez avoir une application Java qui exécute des scripts Python ou des modules Node.js.
* Cela ouvre des possibilités pour tirer parti des forces de différents langages au sein d'une même application.

**2. Génération d'images natives :**

* L'une des fonctionnalités les plus significatives de GraalVM est sa capacité à compiler des applications Java ahead-of-time (AOT) en **exécutables natifs**.
* Ce processus élimine le besoin d'une JVM traditionnelle pour exécuter l'application. L'image native résultante contient tout ce dont l'application a besoin pour s'exécuter, y compris les parties nécessaires du runtime.
* **Avantages des images natives :**
    * **Temps de démarrage plus rapide :** Les exécutables natifs démarrent presque instantanément, ce qui est crucial pour les applications cloud-native et les microservices.
    * **Empreinte mémoire réduite :** Les images natives consomment généralement beaucoup moins de mémoire que l'exécution sur une JVM.
    * **Surface d'attaque réduite :** En excluant le code inutilisé et l'infrastructure de compilation JIT, les images natives peuvent améliorer la sécurité.
    * **Taille de déploiement plus petite :** Les exécutables natifs sont souvent plus petits et plus faciles à empaqueter et à déployer.

**3. Haute performance :**

* GraalVM inclut un compilateur d'optimisation avancé, également nommé Graal, qui peut considérablement améliorer les performances des applications, y compris celles s'exécutant sur la JVM.
* Pour les applications polyglottes, GraalVM vise à fournir des performances comparables ou supérieures à celles des environnements d'exécution spécifiques à un langage.

**4. Capacité d'incorporation :**

* GraalVM peut être intégré dans d'autres applications. Par exemple, vous pouvez intégrer le moteur JavaScript de GraalVM dans une application Java pour fournir des capacités de script.

**5. Cas d'utilisation :**

* **Microservices :** Les images natives sont idéales pour construire des microservices à démarrage rapide et économes en ressources pour les environnements cloud.
* **Fonctions serverless :** Le temps de démarrage rapide fait de GraalVM un excellent choix pour les fonctions serverless où les cold starts peuvent poser problème.
* **Applications polyglottes :** Les applications qui ont besoin de tirer parti de code provenant de multiples langages de programmation.
* **Amélioration des performances des applications Java existantes :** En utilisant le compilateur Graal comme compilateur JIT au sein d'une JVM standard.
* **Création d'environnements d'exécution et d'outils pour langages :** Le framework Truffle au sein de GraalVM permet aux développeurs de construire des interpréteurs haute performance pour de nouveaux langages de programmation ou des langages existants.

**6. Open Source :**

* GraalVM Community Edition est un projet open-source, le rendant accessible à un large éventail d'utilisateurs et de développeurs. Il existe également une Édition Entreprise avec des fonctionnalités supplémentaires et un support.

En résumé, GraalVM est un environnement d'exécution polyvalent et puissant qui offre des avantages significatifs en termes de performance, d'efficacité des ressources et de capacité à travailler avec de multiples langages de programmation. Sa capacité de génération d'images natives est particulièrement convaincante pour le développement cloud-native moderne.